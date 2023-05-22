<?php

use App\Models\User;
use Illuminate\Support\Facades\Route;
use App\Http\Requests\LoginRequest;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
	// Debug false (Server Error)
	throw new Exception("Error Processing Request", 422);

	return view('welcome');
});

Route::prefix('api/v1')->name('api.v1.')->middleware(['web'])->group(function () {

	Route::post('login', function (LoginRequest $request) {
		$data = $request->validated();

		return response()->json([
			'message' => $data
		], 200);
	})->name('login');

	// Errors
	Route::get('error/db', function () {
		User::create([
			'invalid_column' => 'Db error test'
		]);
	})->name('db');
});
