# Obsługa wyjątków w Laravel
Jak obsługiwać wyjątki i błędy w Laravel, zmiana statusu http code z 500 na 422 dla wyjątków z json response.

- https://laravel.com/docs/9.x/errors
- https://laravel.com/docs/9.x/responses#response-macros

## Bezpośrednio w klasie
```php
<?php
namespace App\Exceptions;

use Exception;

class ApiException extends Exception
{
	public function render($request)
	{
		// Show api errors from this exception as json string with code 422
		return response()->json([
			'success' => false,
			'message' => $this->getMessage(),
		], $this->getCode());
	}
  
	public function report()
	{
		// Disable error reporting 
		// return false; 
	}
}
```

### Wywołanie exception
```php
<?php
Route::get('/web/error', function () {
	  throw new ApiException("Invalid api data", 422);
});
```

## Exception handler
Przechwytywanie wyjątków i zmiana http code z 500 na 422 dla json response.

### Dodaj middleware
```php
<?php
namespace App\Http\Middleware;
use Closure;

/**
 *  Force json response
 *
 * Add middleware in App\Http\Kernel.php
 * protected $routeMiddleware = [
 * 	'web-json' => \App\Http\Middleware\WebJsonResponse::class,
 * ]
 */
class WebJsonResponse
{
	public function handle($request, Closure $next)
	{
		$request->headers->set('Accept', 'application/json');
		return $next($request);
	}
}
```

### Użyj aliasu middleware
```php
<?php
Route::get('/web/error', function () {
	  throw new \Exception("Invalid api data", 422);
})->middleware(['web-json']);

Route::prefix('web')->name('web')->middleware(['web', 'web-json'])->group(function () {
	// Routes here
	Route::get('/err', function () {
		throw new \Exception("Invalid api data err", 422);
	});
});
```

### Przechwytuj wyjątki z Handler.php
```php
<?php

namespace App\Exceptions;

use Illuminate\Foundation\Exceptions\Handler as ExceptionHandler;
use Throwable;
use Exception;

class Handler extends ExceptionHandler
{
	public function register()
	{
		$this->reportable(function (Throwable $e) {
			//
		});

		// Return json response with code 422 with WebJsonResponse middleware
		$this->renderable(function (Throwable $e, $request) {      
			// If client accept application/json header
			if ($request->wantsJson() || $request->is('web/api/*')) {
				// return json string
				return response()->json([
					'success' => false,
					'message' => $e->getMessage()
				], 422);
			}
		});
	}
}
```

## Makro dla routes
```php
<?php
namespace App\Providers;
 
use Illuminate\Support\Facades\Response;
use Illuminate\Support\ServiceProvider;
 
class AppServiceProvider extends ServiceProvider
{
	public function boot()
	{
		Response::macro('success', function ($msg, $code = 200) {
			return response()->json([
				'success' => false,
				'message' => $msg
			], $code);
		});

		Response::macro('error', function ($msg, $code = 422) {
			return response()->json([
				'success' => false,
				'message' => $msg
			], $code);
		});
	}
}
```

### Użyj makro
```php
Route::get('/err', function () {
	  return response()->success("Account has been created");
});
```
