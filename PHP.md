# Php
Proste przykłady w php

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
  		report($e);
		Log::error($e->getMessage());
		throw new Exception($e->getMessage(), 422);
	} catch (PDOException $e) {
  		report($e);
		Log::error($e->getMessage());
		throw new Exception('Databse error', 422);
	} catch (Exception $e) {
		report($e);
		Log::error($e->getMessage());
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

