# Db Translate Laravel
Tłumaczenia z bazy danych.

## Utwórz
```sh
php artisan make:model Translate -m
```

## Model
```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Translate extends Model
{
	use HasFactory;

	protected $guarded = [];

	// Translate from database translations (e.g. products, categories)
	public static function trans($str)
	{
		$locale = app()->getLocale();
		return self::text($str)->locale($locale)->first()->value ?? trans($str);
	}

	// Get translated text
	public function scopeText($query, $key)
	{
		$query->where('key', $key);
	}

	// Scope translated locale
	public function scopeLocale($query, $locale = 'pl')
	{
		$query->where('locale', $locale);
	}
}
```

## Tabelka
```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
	public function up()
	{
		Schema::create('translates', function (Blueprint $table) {
			$table->id();
			$table->string('locale')->nullable()->default('en');
			$table->string('key');
			$table->string('value');
			$table->timestamps();

			$table->unique(['locale', 'key']);
		});
	}

	public function down()
	{
		Schema::dropIfExists('translates');
	}
};
```

## Przykład
```php
<?php
use App\Models\Translate;

Route::get('/trans', function () {

	try {
		if (Translate::all()->count() == 0) {
			Translate::create(['locale' => 'pl', 'key' => 'Hello', 'value' => 'Witaj']);
		}
		echo "<br> EN " . Translate::trans('Hello');

		app()->setLocale('pl');
    
		// If exists in db
		echo "<br> PL " . Translate::trans('Hello');
    
		// If not exists in db from trans() helper
		echo "<br> PL " . Translate::trans('Error key in db');
    
	} catch (Exception $e) {
		return $e;
	}

	return '';
})->name('trans.test');
```
