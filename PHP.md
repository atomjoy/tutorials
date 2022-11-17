# Php

## Exceptions

### Multiple catch
```php
Route::get('/', function () {
	try {
		// Invalid column
		PayuLog::create(['xxx' => 123]);
	} catch (PDOException $e) {
  	report($e);
		throw new Exception('Databse error', 422);
	} catch (Exception $e) {
		report($e);
		throw new Exception('Regular error', 422);
	} finally {
    // Do this
  }
});
```

### InstanceOf
```php
Route::get('/', function () {
	try {
		// Invalid column
		PayuLog::create(['xxx' => 123]);
	} catch (Exception $e) {
		report($e);

		if ($e instanceof \PDOException) {
			throw new Exception('Databse error', 422);
		}

		throw new Exception('Regular error', 422);
	}
});
```

