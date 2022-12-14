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

// Podwójny unikalny klucz $table->unique(['number', 'restaurant_id']) z referencją
'number' => Rule::unique('days', 'restaurant_id');

// StoreDayRequest - Sprawdzaj wiersze tabeli bez tych usunietych z softDelete
'number' => Rule::unique('days', 'restaurant_id')->withoutTrashed();
'number' => Rule::unique('days', 'restaurant_id')->whereNull('deleted_at');

// UpdateDayRequest - Ignorowanie sprawdzania istniejącego modelu w tabeli podczas aktualizacji
'number' => Rule::unique('days', 'restaurant_id')->ignore($this->route('day'))->withoutTrashed();
'number' => Rule::unique('days', 'restaurant_id')->ignore($this->route('day'))->whereNull('deleted_at');

// UpdateDayRequest - Ignorowanie sprawdzania istniejących modeli w tabeli podczas aktualizacji
'number' => Rule::unique('days', 'restaurant_id')->whereNull('deleted_at')->orWhereNotNull('deleted_at');
```

### Inne metody
https://laravel.com/api/8.x/Illuminate/Validation/Rules/Unique.html
```php
->withoutTrashed() - Ignore rows where deleted_at != null
->whereNull('deleted_at') - Ignore rows where deleted_at != null
->orWhereNotNull('deleted_at'); - Ignore rows where deleted_at == null
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

### Przykład walidacji z query
```php
public function rules()
{
  $rid = request('restaurant_id');
  $pid = request('product_id');

  return [
    // uniques
    'restaurant_id' => 'required',
    'product_id' => 'required', 
    'size' => 'required',
    
    // columns
    'price' => 'required|numeric|gte:0|regex:/^-?[0-9]+(?:.[0-9]{1,2})?$/',
    
    // StoreRequest
    'size' => [
      'required',
      Rule::unique('variants')->where(function ($query) use ($rid, $pid) {
        return $query->where('restaurant_id', $rid)
          ->where('restaurant_id', $rid)
          ->where('product_id', $pid)
          ->whereNull('deleted_at'); // Without trashed rows
      })
    ],
    
    // UpdateRequest
    'size' => [
      'required',
      Rule::unique('variants')->ignore($this->route('variant'))->where(function ($query) use ($rid, $pid) {
        return $query->where('restaurant_id', $rid)
          ->where('restaurant_id', $rid)
          ->where('product_id', $pid)
          ->whereNull('deleted_at'); // Without trashed rows
      })
    ],
  ];
}
```
