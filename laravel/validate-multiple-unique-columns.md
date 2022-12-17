# Walidacja unikalnych kolumn/wierszy w Laravel
Jak działa walidacja unikalnych wierszy/kolumn w tabeli z Laravel.

### Utwórz klasy dla modelu Day (około 10 sztuk)
```sh
php artisan make:model Day -a
php artisan make:resource DayResource
php artisan make:resource DayCollection
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
