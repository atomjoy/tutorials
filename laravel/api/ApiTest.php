<?php

namespace Tests\Feature;

// use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class ApiTest extends TestCase
{
	/**
	 * A basic test example.
	 *
	 * @return void
	 */
	public function test_login_invalid_pass_response()
	{
		$response = $this->postJson('api/v1/login', [
			'email' => 'email@gmail.com',
			'password' => 'www'
		]);

		$response->assertStatus(422);

		$response->assertJson([
			// 'message' => "The email field is required."
			'message' => "The password must be at least 11 characters."
		]);
	}

	public function test_show_http_404_response()
	{
		$response = $this->getJson('api/v1/error');

		$response->assertStatus(404);

		$response->assertJson([
			'message' => "The route api/v1/error could not be found."
		]);
	}

	public function test_show_http_500_db_response()
	{
		$response = $this->getJson('api/v1/error/db');

		$response->assertStatus(500);

		$response->assertJson([
			'message' => "Server Error"
		]);
	}
}
