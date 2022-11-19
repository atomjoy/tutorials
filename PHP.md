# Php
Proste przykłady w php

## Php zamiana złotych na grosze w payu
```php
<?php
function toCents(float $decimal): int
{
	if ($decimal < 0.01) {
		throw new Exception("Minimal decimal value: 0.01", 422);
	}

	if (!preg_match('/^\d+(\.\d{1,2})?$/', $decimal)) {
		throw new Exception("Invalid decimal value", 422);
	}
	
	return number_format($decimal * 100, 2, '.', '');
}
```

## Ignore ErrorException

### Ignore undefined key
```php
<?php
$a = [];
// Error
echo $a[0];
// No error with @ or ??
echo @$a[0];
echo $a[0] ?? null;
```

### Ignore undefined property
```php
<?php
$o = (object) [];
// Error undefined property
echo $o->b; 
// No error with @ or ??
echo @$o->a; 
echo @$o->a->b;
echo $o->a ?? null;
echo $o->a->b ?? null;
```

## Exceptions
Zaimportuj klasy Exception, PDOException, ... jeżeli potrzeba.

### Multiple Exception
```php
use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Log;
use App\Models\User;

Route::get('/ex', function () {
	try {
		// Invalid column
		User::create(['xxx' => 123]);
	} catch (OpenPayU_Exception $e | SmsApi_Exception $e) {
		Log::error($e->getMessage());
		throw new Exception($e->getMessage(), 422);
	} catch (PDOException $e) {
  		report($e);
		throw new Exception('Databse error', 422);
	} catch (Exception $e) {
		report($e);
		throw new Exception('Regular error', 422);
	}
});
```

### Mysql Exception with instanceof
```php
use Illuminate\Support\Facades\Route;
use App\Models\User;

Route::get('/ex', function () {
	try {
		// Invalid column
		User::create(['xxx' => 123]);
	} catch (Exception $e) {
		report($e);

		if ($e instanceof \PDOException) {
			throw new Exception('Databse error', 422);
		}

		throw new Exception('Regular error', 422);
	} finally {
		// And do this if the catch has no throws
	}
});
```

