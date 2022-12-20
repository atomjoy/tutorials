# Niestandardowe linki w kolekcjach laravela

### Product Kontroler
```php
class ProductController extends Controller
{
  // trait
  use HasJsonresponse;

  function perpage()
  {
    return request()->input('perpage') ?? config('app.perpage', 12);
  }

  public function index()
  {
    $search = "" . app()->request->input('search');

    $a = Product::where(DB::raw("CONCAT_WS(' ','name','slug','about')"), 'regexp', str_replace(" ", "|", $search))
      ->orderBy("id", 'desc')
      ->paginate($this->perpage())
      ->withQueryString();

    return $this->jsonResponse("Products", new ProductCollection($a));
  }
}
```

### Klasa kolekcji dla modelu Product
```php
<?php
namespace App\Http\Resources;
use Illuminate\Http\Resources\Json\ResourceCollection;

class ProductCollection extends ResourceCollection
{
	public function toArray($request)
	{
		return [
			'data' => ProductResource::collection($this->collection),
			'links' => $this->resource->withQueryString()->linkCollection(),
			'meta' => [
				'count' => $this->collection->count()
			]
		];
	}
}
```

### Klasa resource modelu Product
```php
<?php
namespace Cartelo\Http\Resources;
use Illuminate\Http\Resources\Json\JsonResource;

class ProductResource extends JsonResource
{
	public function toArray($request)
	{
		return parent::toArray($request);
	}
}
```

### Response trait
```php
<?php

namespace Webi\Traits\Http;

trait HasJsonResponse
{
	function jsonResponse($message, $data = null, $code = 200, $alert_type = 'success')
	{
		if (config('app.translate_response', false) == true) {
			$message = trans($message);
		}

		return response()->json([
			'alert' => [
				'message' => $message,
				'type' => $alert_type,
			],
			'bag' => $data,
		], $code, [], JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
	}
}
```
