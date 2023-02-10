# Własny Query Builder w Laravel
Filtrowanie danych z model query buider.

## Model
```php
namespace App\Models;

use App\Builders\BookBuilder;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Book extends Model
{
  use HasFactory;

  public function author(): BelongsTo
  {
    return $this->belongsTo(User::class);
  }

  public function ratings(): HasMany
  {
    return $this->hasMany(Rating::class);
  }

  public function newEloquentBuilder($query): BookBuilder
  {
    return new BookBuilder($query);
  }
  
  public function publish(Book $book)
  {
    $book->publish();
  }

}
```

## Builder
```php
namespace App\Builders;

use App\Models\User;
use Illuminate\Database\Eloquent\Builder;

class BookBuilder extends Builder
{
  public function wherePublished(): self
  {
      return $this->where('publish_at', '<=', now());
  }

  public function whereAuthor(User $user): self
  {
      return $this->where('author_id', $user->id);
  }

  public function wherePriceBetween(float $from, float $to): self
  {
      return $this->whereBetween('price', [$from, $to]);
  }

  public function whereContains(string $searchTerm): self
  {
      return $this->where(function ($query) use ($searchTerm) {
          $query->where('title', 'LIKE', "%$searchTerm%")->orWhere('description', 'LIKE', "%$searchTerm%");
      });
  }
  
  public function orderByRatings(): self
  {
    return $this->withAvg('ratings as average_rating', 'rating')->orderByDesc('average_rating');
  }
  
  public function mostPopular(int $count): self
  {
    return $this->orderByRatings()
        ->take($count);
  }
  
  public function publishAll(): self
  {
    // $this->whereNotPublished()->get()->each->publish();
    $this->whereNotPublished()->update(['publish_at' => now()]);
    
    return $this;
  }

  public function publish(): self
  {
    $this->model->publish_at = now();
    $this->model->save();

    return $this;
  }
}
```

## Controller
```php
class BookController extends Controller
{
  public function index(Request $request)
  {
    return Book::query()
      ->wherePublished()
      ->when($request->authorId, fn ($query) => $query->whereAuthor(User::find($request->authorId)))
      ->when($request->fromPrice, fn ($query) => $query->wherePriceBetween($request->fromPrice, $request->toPrice))
      ->orderByRatings()
      ->get();
  }

  public function popular()
  {
    return Book::mostPopular(5)->get();
  }
  
  public function publish(Book $book)
  {
    $book->publish();
  }
  
  public function publishAll()
  {
    Book::whereNotPublished()->get()->each->publish();
  }

}
```

### Links
<https://martinjoo.dev/build-your-own-laravel-query-builders>
