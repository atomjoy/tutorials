# Obsługa wyjątków w Laravel gdy żądanie chce JSON
Przechwytywanie wyjątków, błędów w Laravel z json response w web api z walidacją w Requests (Exception Handler).


## Utwórz klasę exception
Błędy wyrzucane z tą klasą będą miały kod status http 200, co pozwala na wyświetlanie gdy debug ustawiony jest na false w .env (debug=false).
```php
<?php

namespace App\Exceptions;

use Exception;

class WebException extends Exception
{
}
```

## Dodaj w pliku app/Exceptions/Handler.php
```php
<?php

namespace App\Exceptions;

use Throwable;
use PDOException;
use Illuminate\Foundation\Exceptions\Handler as ExceptionHandler;
use Illuminate\Support\Arr;
use Illuminate\Database\QueryException;
use Illuminate\Auth\AuthenticationException;
use Illuminate\Validation\ValidationException;
use Symfony\Component\HttpKernel\Exception\NotFoundHttpException;
use App\Exceptions\WebException;

class Handler extends ExceptionHandler
{
	/**
	 * A list of exception types with their corresponding custom log levels.
	 *
	 * @var array<class-string<\Throwable>, \Psr\Log\LogLevel::*>
	 */
	protected $levels = [
		//
	];

	/**
	 * A list of the exception types that are not reported.
	 *
	 * @var array<int, class-string<\Throwable>>
	 */
	protected $dontReport = [
		//
	];

	/**
	 * A list of the inputs that are never flashed to the session on validation exceptions.
	 *
	 * @var array<int, string>
	 */
	protected $dontFlash = [
		'current_password',
		'password',
		'password_confirmation',
		'remember_token',
		'code',
	];

	/**
	 * Register the exception handling callbacks for the application.
	 *
	 * @return void
	 */
	public function register()
	{
		$this->renderable(function (Throwable $e, $request) {
			// Można dodać: || $request->wantsJson()
			// Tylko dla routes /web/api/*			
			if ($request->is('web/api/*') ) {
				$alert = 'error';
				$message = $e->getMessage();
				
				// Wszystkie exceptions
				$message = empty($message) ? 'Unknown Exception.' : $message;
				$status = $this->validCode($e) ? $e->getCode() : 422;
				
				// Błędy mysql w logach
				if ($e instanceof QueryException || $e instanceof PDOException) {
					$status = 500;
					$alert = 'error';
					$message = 'Database error.';
				}
				
				// Powiadomienia aplikacji, walidacja formularzy, wszystko to co musi zobaczyć użytkownik api ze statusem http 200
				if ($e instanceof WebException) {
					$status = 200;
					$alert = 'danger';
				}

				if ($e instanceof AuthenticationException) {
					$status = 200;
					$alert = 'danger';
				}

				if ($e instanceof ValidationException) {
					$status = 200;
					$alert = 'danger';
				}

				if ($e instanceof NotFoundHttpException) {
					$status = 200;
					$alert = 'danger';
					$message = 'Not Found.';
				}

				if (config('webi.settings.translate_response') == true) {
					$this->updateLocale($request);
					$message = trans($message);
				}

				$data['alert'] = ['message' => $message, 'type' => $alert,];
				$data['bag'] = null;

				if (config('app.debug')) {
					$data['debug'] = [
						'exception' => get_class($e),
						'file' => $e->getFile(),
						'line' => $e->getLine(),
						'trace' => collect($e->getTrace())->map(fn ($trace) => Arr::except($trace, ['args']))->all(),
					];
				}

				return response()->json($data, $status, [], JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
			}
		});
	}

	/**
	 * Refresh session locale.
	 *
	 * @return void
	 */
	public function updateLocale($request)
	{
		$lang =  session('locale', config('app.locale'));
		app()->setLocale($lang);
		if ($request->has('locale')) {
			app()->setLocale($request->query('locale'));
		}
	}

	/**
	 * Http codes validation.
	 *
	 * @return bool
	 */
	public function validCode($e)
	{
		return ($e->getCode() >= 100 && $e->getCode() <= 599) ? true : false;
	}
}
```

## Alerty
Handler zwraca alerty (success, danger, error)
- **success** - Potwierdzenie działania ... http code 200, 201
- **danger** - Niepoprawne dane np. logowania z formularza ... http code 200
- **error** - Błąd serwera aplikacji database error, php error ... http code 500, 400, 401, 422 z throw new Exceptions()

### Błąd z kontrolera
```php
throw new WebException('Invalid credentials', 422);
```

### Wyświetli json response http status 200
```json
{
	"alert": [
		"message": "Invalid credentials",
		"type": 'danger'
	],
	"bag": null
}
```

## Przykład klasy walidacji form request
```php
<?php

namespace App\Http\Requests;

use Illuminate\Contracts\Validation\Validator;
use Illuminate\Foundation\Http\FormRequest;
use App\Exceptions\WebException;

class WebLoginRequest extends FormRequest
{
	protected $stopOnFirstFailure = true;

	public function authorize()
	{
		return true; // Allow all
	}

	public function rules()
	{
		$email = 'email:rfc,dns';
		if (env('APP_DEBUG') == true) {
			$email = 'email';
		}

		return [
			'email' => ['required', $email, 'max:191'],
			'password' => 'required|min:11',
			'remember_me' => 'sometimes|boolean'
		];
	}
	
	public function failedValidation(Validator $validator)
	{
		throw new WebException($validator->errors()->first()); // To jest istotne !!!
	}

	function prepareForValidation()
	{
		$this->merge(
			collect(request()->json()->all())->only(['email', 'password', 'remember_me'])->toArray()
		);
	}
}
```
