# Walidacja unikalnych kolumn/wierszy w Laravel
Jak działa walidacja unikalnych wierszy/kolumn w tabeli z Laravel.

### Utwórz klasy dla modelu Day (około 10 sztuk)
```sh
php artisan make:model Day -a
php artisan make:resource DayResource
php artisan make:resource DayCollection
```

### Route resource
```php
Route::prefix('food')->name('food')->middleware(['web'])->group(function () {
  // Path: /food/day/{day}
  Route::resource('day', DayController::class);
  
  // Path: /food/day/{cool_day}
  Route::resource('day', DayController::class)->parameters(['day' => 'cool_day']);
  
  // Ignore routes with ->except() lub ->only()
  Route::resource('day', DayController::class)->except(['create', 'edit']);
});
```

### Reguły w FormRequest
Sprawdzaj wszystkie wiersze tabeli (defaultowo).
```php
// Aktualny model z route
$day = $this->route('day');

// Pojedyńczy unikalny klucz $table->unique('number')
'number' => Rule::unique('days');

// Z inna nazwą kolumny niż ta w request
'number' => Rule::unique('days', 'number_column');

// StoreDayRequest - Sprawdzaj wiersze tabeli bez tych usunietych z softDelete
'number' => Rule::unique('days', 'number_column')->withoutTrashed();
'number' => Rule::unique('days', 'number_column')->whereNull('deleted_at');

// UpdateDayRequest - Ignorowanie sprawdzania istniejącego modelu w tabeli podczas aktualizacji
'number' => Rule::unique('days', 'number_column')->ignore($this->route('day'))->withoutTrashed();
'number' => Rule::unique('days', 'number_column')->ignore($this->route('day'))->whereNull('deleted_at');

// UpdateDayRequest - Ignorowanie sprawdzania istniejących modeli w tabeli podczas aktualizacji
'number' => Rule::unique('days', 'number_column')->whereNull('deleted_at')->orWhereNotNull('deleted_at');

// Password validation
'password_current' => 'required',
'password' => [
  'required',
  Password::min(11)->letters()->mixedCase()->numbers()->symbols(),
  'confirmed',
  'max:50',
],
'password_confirmation' => 'required',
```

### Inne metody
https://laravel.com/api/8.x/Illuminate/Validation/Rules/Unique.html
```php
->withoutTrashed() - Ignore rows where deleted_at != null
->whereNull('deleted_at') - Ignore rows where deleted_at != null
->orWhereNotNull('deleted_at'); - Ignore rows where deleted_at == null
```

### Walidacja podwójnych unikalnych kluczy w laravel
Podwójny unikalny klucz $table->unique(['size', 'product_id']) z referencją tabela variants
```php
// Unique columns: size, restaurant_id, product_id
public function rules()
{
  $rid = request('restaurant_id');
  $pid = request('product_id');
  $variant = $this->route('variant');

  return [     
	'price' => 'required|numeric|gte:0|regex:/^-?[0-9]+(?:.[0-9]{1,2})?$/',
	'name' => 'required',
	'about' => 'required',

	'restaurant_id' => 'required',
	'product_id' => 'required',

	// StoreRequest
	'size' => [
		'required',
		Rule::unique('variants')->where(function ($query) use ($rid, $pid) {
			return $query->where('product_id', $pid);
			// return $query->where('product_id', $pid)->where('restaurant_id', $rid);        
		})->whereNull('deleted_at'); // Without trashed rows
	],

	// UpdateRequest
	'size' => [
		'required',
		Rule::unique('variants')->where(function ($query) use ($rid, $pid, $variant) {
			return $query->where('product_id', $pid);
			// return $query->where('product_id', $pid)->where('restaurant_id', $rid);              
		})->ignore($variant)->whereNull('deleted_at'); // Without trashed rows
	],
  ];
}

<!--
function prepareForValidation()
{
	$this->merge(
		$this->stripTags(
			collect(request()->json()->all())->only([
				'restaurant_id', 'product_id', 'name', 'about', 'visible', 'sorting'
			])->toArray()
		)
	);
}
 
public function messages()
{
	return [
		'size.unique' => 'Couple size and product_id has to be unique.',
	];
}

public function failedValidation(Validator $validator)
{
	throw new \Exception($validator->errors()->first(), 422);
} 
-->
```

### Kontroler resource
```php
public function index()
{
  $search = "" . app()->request->input('search');

  $a = Day::where(
    DB::raw("CONCAT_WS(' ','number', 'closed')"), 'regexp', str_replace(" ", "|", $search)
  )->orderBy("id", 'desc')->simplePaginate($this->perpage())->withQueryString();

  return $this->jsonResponse("Days", [
    'days' => $a
  ]);
}
  
public function store(StoreDayRequest $request)
{
  $v = $request->validated();
  $v['deleted_at'] = NULL;
  Day::withTrashed()->updateOrCreate([
    'number' => $v['number']
  ], $v);

  return $this->jsonResponse("The day has been created");
}

public function update(UpdateDayRequest $request, Day $day)
{
  $v = $request->validated();
  $day->fill($v);
  $day->save();

  return $this->jsonResponse("The day has been updated");
}

public function show(Day $day)
{
  return $this->jsonResponse("Day", [
    'day' => new DayResource($day)
  ]);
}
  
public function destroy(Day $day)
{
  $day->delete(); // Or permanently ->forceDelete();

  return $this->jsonResponse("The day has been deleted");
}
```

### Przykład Request form validation
```php
<?php

namespace Webi\Http\Requests;

use Exception;
use Illuminate\Contracts\Validation\Validator;
use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Validation\Rules\Password;
use Illuminate\Http\Exceptions\HttpResponseException;

class WebiRegisterRequest extends FormRequest
{
	// To nie działa jak powinno i wyświetla wszystkie wyjątki zamiast pierwszego 
	// i tak message z ilością błędów i psuje test, trzeba użyć faliedValidation() z własnym exception.
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
			'name' => 'required|min:3|max:50',
			'email' => [
				'required', $email, 'max:191',
				Rule::unique('users')->whereNull('deleted_at')
			],
			'password' => [
				'required',
				Password::min(11)->letters()->mixedCase()->numbers()->symbols(),
				'confirmed',
				'max:50',
			],
			'password_confirmation' => 'required'
		];
	}

	public function failedValidation(Validator $validator)
	{
		// throw new Exception($validator->errors()->first(), 422);
		
		// get only first error (stopOnFirstfailure does not work)
		throw new HttpResponseException(response()->json([
			'message' => $validator->errors()->first()
		], 422));
	}

	function prepareForValidation()
	{
		$this->merge(
			collect(request()->json()->all())->only(['name', 'email', 'password', 'password_confirmation'])->toArray()
		);
	}
}
```

### Walidacja wielu kolumn z query
```php
// Enums php 8.1
namespace App\Enums;

enum ExamName: string {
    case EXAM1 = 'exam1';
    case EXAM2 = 'exam2';
}

// Validate
use App\Enums\ExamName;
use Illuminate\Validation\Rules\Enum;

public function rules()
{
	return [
		'exam_name' => [new Enum(ExamName::class)],
		'student_id' => 'required|numeric',
		'exam_year' => 'required|numeric',
		'exam_category_id' => [
			'required',
			Rule::unique('exams')->where(function ($query) use ($request) {
		   		return $query->where('exam_name', $request->exam_name)->where('exam_year', $request->exam_year)->where('student_id', $request->student_id);
			}),
		],
		// 'type' => ['required', Rule::in(MyClass::$typesArray)],
		// 'letter' => ['required', Rule::in(['a', 'b','c'])],
	];
}
```
