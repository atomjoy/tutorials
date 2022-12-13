# Uuid zamiast auto-increment id w Laravelu

### Utwórz trait
Automatyczne tworzyenie uuid klucza.
```php
<?php

namespace App\Models\Traits;

use Illuminate\Support\Str;

/**
 * Change key name in model (optional)
 *
 * protected $primaryKey = 'id';
 */
trait Uuids
{
	protected static function boot()
	{
		parent::boot();

		static::creating(function ($model) {
			if (empty($model->{$model->getKeyName()})) {
				$model->{$model->getKeyName()} = (string) Str::uuid();
			}
		});
	}

	public function getIncrementing(): bool
	{
		return false;
	}

	public function getKeyType(): string
	{
		return 'string';
	}
}
```


### Dodaj w modelu
Dodaj trait w modelu i/lub zmień nazwę klucza $primaryKey.
```php
<?php

namespace Payu\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;
use Payu\Models\Traits\Uuids;
use App\Models\Order;

class Payments extends Model
{
	use HasFactory, SoftDeletes, Uuids;

	protected $primaryKey = 'id';
  
  protected $guarded = [];

	protected $casts = [
		'created_at'  => 'date:Y-m-d H:i:s',
	];
  
  // ...
}
```

### Tabela w bazie danych

```php
<?php

Schema::create('payments', function (Blueprint $table) {
  $table->string('id', 191)->primary();  
  
  $table->timestamps();
  $table->softDeletes();
  
  // Opcjonalnie dodaj referencje
  $table->unsignedBigInteger('order_id')->nullable(true);
  $table->foreign('order_id')->references('id')->on('orders')->onDelete('cascade')->onUpdate('cascade');
});
```
