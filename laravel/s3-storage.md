# Laravel s3

## Create disks

```php
<?php

return [

	/*
    |--------------------------------------------------------------------------
    | Default Filesystem Disk
    |--------------------------------------------------------------------------
    |
    | Here you may specify the default filesystem disk that should be used
    | by the framework. The "local" disk, as well as a variety of cloud
    | based disks are available to your application for file storage.
    |
    */

	'default' => env('FILESYSTEM_DISK', 'local'),

	/*
    |--------------------------------------------------------------------------
    | Filesystem Disks
    |--------------------------------------------------------------------------
    |
    | Below you may configure as many filesystem disks as necessary, and you
    | may even configure multiple disks for the same driver. Examples for
    | most supported storage drivers are configured here for reference.
    |
    | Supported Drivers: "local", "ftp", "sftp", "s3"
    |
    */

	'disks' => [

		'local' => [
			'driver' => 'local',
			'root' => storage_path('app'),
			'throw' => false,
		],

		'public' => [
			'driver' => 'local',
			'root' => storage_path('app/public'),
			'url' => env('APP_URL') . '/storage',
			'visibility' => 'public',
			'throw' => false,
		],

		's3' => [
			'driver' => 's3',
			'key' => env('AWS_ACCESS_KEY_ID'),
			'secret' => env('AWS_SECRET_ACCESS_KEY'),
			'region' => env('AWS_DEFAULT_REGION'),
			'bucket' => env('AWS_BUCKET'),
			'url' => env('AWS_URL'),
			'endpoint' => env('AWS_ENDPOINT'),
			'use_path_style_endpoint' => env('AWS_USE_PATH_STYLE_ENDPOINT', false),
			'throw' => false,
		],
		
		'invoices' => [
			'driver' => 's3',
			'key' => env('AWS_ACCESS_KEY_ID'),
			'secret' => env('AWS_SECRET_ACCESS_KEY'),
			'region' => env('AWS_DEFAULT_REGION'),
			'bucket' => env('AWS_BUCKET'),
			'url' => env('AWS_URL'),
			'endpoint' => env('AWS_ENDPOINT'),
			'use_path_style_endpoint' => env('AWS_USE_PATH_STYLE_ENDPOINT', false),
			'visibility' => 'public',
			'root' => 'invoices'
		],
		
		'profile-photos' => [
			'driver' => 's3',
			'key' => env('AWS_ACCESS_KEY_ID'),
			'secret' => env('AWS_SECRET_ACCESS_KEY'),
			'region' => env('AWS_DEFAULT_REGION'),
			'bucket' => env('AWS_BUCKET'),
			'url' => env('AWS_URL'),
			'endpoint' => env('AWS_ENDPOINT'),
			'use_path_style_endpoint' => env('AWS_USE_PATH_STYLE_ENDPOINT', false),
			'visibility' => 'public',
			'root' => 'profile-photos'
		],
	],

	/*
    |--------------------------------------------------------------------------
    | Symbolic Links
    |--------------------------------------------------------------------------
    |
    | Here you may configure the symbolic links that will be created when the
    | `storage:link` Artisan command is executed. The array keys should be
    | the locations of the links and the values should be their targets.
    |
    */

	'links' => [
		public_path('storage') => storage_path('app/public'),
	],

];
```

## Upload images

Get url https://your-bucket-name.s3.amazonaws.com/profile-photos/hero.png

```php
<?php

Route::get('profile-photos', function($path){
    $disk = 'profile-photos';

    if (Storage::disk('s3')->exists($path)) {
        # Image url
        return Storage::disk($disk)->url($path);
  
        # Image response
        return Storage::disk('s3')->response($path);
        return Storage::disk('s3')->response('images/avatars/' . basename($path));
    }
});

Route::post('profile-photos', function(){
    $disk = 'profile-photos';
    $heroImage = Storage::get('hero.png');
    $uploadedPath = Storage::disk($disk)->put('hero.png', $heroImage);
    return Storage::disk($disk)->url($uploadedPath);

    # From request
    $path = request()->file('image')->store('images/invoices', 's3');
    $path = request()->file('avatar')->store('images/avatars', 's3');
    return Storage::disk($disk)->url($path);

    # From request
    $path = Storage::putFile('avatars', request()->file('avatar'));
    $path = Storage::putFileAs('avatars', $request->file('avatar'), request()->user()->id . '.webp');
    return Storage::disk($disk)->url($path);
});

Route::post('files', function(){
    # If you do not have S3 as your default:
    $contents = Storage::disk('s3')->get('path/to/file.ext');
    Storage::disk('s3')->put('path/to/file.ext', 'some-content');

    # If you set S3 as your default .env:
    # FILESYSTEM_DISK=s3
    $contents = Storage::get('path/to/file.ext');
    Storage::put('path/to/file.ext', 'some-content');    
});
```

## Copy images from local to s3

```php
<?php

$path = storage_path() . '/books/images/' . '21.png'
$contents = Storage::get($path);
Storage::disk('s3')->put('books/21.png', $contents);
```
