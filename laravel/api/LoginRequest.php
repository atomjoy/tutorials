<?php

namespace App\Http\Requests;

use Illuminate\Contracts\Validation\Validator;
use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Validation\ValidationException;
use Illuminate\Validation\Rule;
use Illuminate\Validation\Rules\Password;

class LoginRequest extends FormRequest
{
	protected $stopOnFirstFailure = true;

	public function authorize()
	{
		return true;
	}

	public function rules()
	{
		$email = 'email:rfc,dns';
		if (env('APP_DEBUG') == true) {
			$email = 'email';
		}

		return [
			// Login rules
			'email' => ['required', $email, 'max:191'],
			'password' => [
				'required',
				Password::min(11)->letters()->mixedCase()->numbers()->symbols(),
				'confirmed',
				'max:50',
			],
			'remember_me' => 'sometimes|boolean',
			// Register user rules
			// 'name' => 'required|min:3|max:50',
			// 'email' => [
			// 	'required', $email, 'max:191',
			// 	Rule::unique('users')->whereNull('deleted_at')
			// ],
			// 'password' => [
			// 	'required',
			// 	Password::min(11)->letters()->mixedCase()->numbers()->symbols(),
			// 	'confirmed',
			// 	'max:50',
			// ],
			// 'password_confirmation' => 'required'
		];
	}

	function prepareForValidation()
	{
		$this->merge(
			collect(request()->json()->all())->only(['email', 'password', 'remember_me'])->toArray()
		);
	}

	public function failedValidation(Validator $validator)
	{
		throw (new ValidationException($validator, response()->json([
			'message' => $validator->errors()->first()
		], 422)));
	}
}
