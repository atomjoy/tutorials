# Obrazki w wiadomościach email (laravel, blade)
Jak dodać w Laravelu obrazki w wiadomościach email. Jak wysłać wiadomość email z osadzonymi obrazkami w Laravelu.

## Utwórz link symboliczny public/storage odnoszący sie do storage/app/public
```sh
php artisan storage:link
```

# Jak dodać obrazki do wiadomości emaill

## Url do obrazka z public/storage lub url z aws s3
```blade
<img src="{{ Storage::url('images/image.jpg') }}" alt="">
```

## Obraz osadzony w wiadomości e-mail
```blade
<img src="{{ $message->embed(public_path() . '/images/image.jpg') }}" alt="" />

<img src="{{ $message->embed(storage_path() . 'app/public/images/image.jpg') }}" alt="" />

<img src="data:image/png;base64,{{base64_encode(file_get_contents(storage_path('app/public/images/image.png')))}}" alt="Seo description">
```

# Jak wysłać wiadomość email
```sh
php artisan make:mail RegisterMail
```

## Edytuj klasę
app/Mail/RegisterMail.php
```php
<?php

namespace App\Mail;

use Illuminate\Bus\Queueable;
use Illuminate\Mail\Mailable;
use Illuminate\Queue\SerializesModels;
use App\Models\User;

class RegisterMail extends Mailable
{
	use Queueable, SerializesModels;

	public $user;
	public $params;

	public function __construct(User $user, $params = null)
	{
		$this->user = $user;
		$this->params = $params;
	}

	public function build()
	{
		// Z aplikacji 
		$email = $this->subject(trans('Hello there'))->view('emails.register');
				
		// Parametry wiadomości: ->cc(), ->bcc(), ->replyTo()
		// $email->from('noreply@' . request()->getHttpHost(), 'Rejestracja');
		// $email->attach(storage_path('pdf/fra-123.pdf'), ['as' => 'invoice-123.pdf', 'mime' => 'application/pdf']);
		
		return $email;

		// Z pakietu
		// return $this->subject(trans('webi::webi.subject.register'))->view('webi::emails.register');
	}
}
```

## Szablon blade wiadomości email
resources/views/emails/register.blade.php
```blade
<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8" />
	<meta http-equiv="X-UA-Compatible" content="IE=edge" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>@lang('Welcome') {{ $user->name }}</title>

	<style>
		@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;500;600;700;800&display=swap');
		@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;500;600;700;800&display=swap');

		.email-body,
		.email-bg {
			margin: 0px;
			padding: 0px;
			background-color: rgb(243, 246, 248);
			font-size: 16px;
			font-family: 'Baloo 2', cursive, 'Open Sans', Helvetica, Arial, monospace, sans-serif;
			box-sizing: border-box;
			height: auto;
		}

		.email-bg {
			margin: 50px auto;
			width: 90%;
			max-width: 600px;
		}

		.email-box {
			position: relative;
			float: left;
			width: 100%;
			min-height: 200px;
			margin-bottom: 100px;
			background-color: #fff;
			box-shadow: 1px 5px 20px rgb(104, 150, 181, 0.05);
		}

		.email-box-top {
			padding: 50px 0px;
			overflow: hidden;
			text-align: center;
			background: #ffc900;
		}

		.email-box-mid {
			padding: 30px 0px;
			text-align: center;
		}

		.email-box-bot {
			overflow: hidden;
			background: #fefefe;
		}

		.email-text {
			padding: 10px 25px;
			text-align: center;
			font-size: 17px;
			font-weight: 400;
		}

		.email-regards {
			padding: 30px;
			text-align: center;
			font-size: 20px;
			font-weight: 900;
			background-color: #efefef;
		}

		.email-button {
			padding: 15px 25px;
			margin: 20px auto;
			min-width: 200px;
			color: #ffc900;
			background-color: #000;
			display: inline-block;
			text-decoration: none;
			text-align: center;
			font-weight: 900;
			box-shadow: 0px 5px 10px rgb(0, 0, 0, 0.1);
			transition: all .6s ease-in-out;
		}

		.email-button:hover {
			color: #000;
			background-color: #ffcc00;
			box-shadow: 0px 5px 20px #ffcc0088;
		}

		.email-logo {
			margin: 10px auto;
		}
	</style>
</head>

<body class="email-body">
	<div class="email-bg">
		<div class="email-box">
			<div class="email-box-top">
				@if (file_exists(public_path() . '/logo/logo.png'))
				<img class="email-logo" src="{{ $message->embed(public_path() . '/logo/logo.png') }}" />
				@endif
				<h1>@lang('Welcome')!</h1>
				<h3>{{ $user->name }}</h3>
			</div>

			<div class="email-box-mid">
				<p class="email-text">
					@lang('Email-Activation-Message')
				</p>
				<a class="email-button"
					href="{{ request()->getSchemeAndHttpHost() }}/activate/{{ $user->id }}/{{ $user->code }}?locale={{ app()->getLocale() }}"
					target="_blank">
					@lang('Confirm email')
				</a>
			</div>

			<div class="email-box-bot">
				<div class="email-regards">@lang('Have a nice day!')</div>
			</div>
		</div>
	</div>
</body>

</html>
```

## Wyślij wiadomość
routes/web.php
```php
<?php

Route::get('/send', function () {

	$user = User::create(['email => 'email@example.com', 'name' => 'Alexia', 'code' => '1234asdf']);

	Mail::to($user)->locale('pl')->send(new RegisterMail($user));

	// Mail::to($user->email)->locale('en')->send(new RegisterMail($user));	
	
	// Mail::mailer('mailgun')->to($user->email)->queue(new RegisterMail($user));
	
	// Mail::mailer('mailgun')->to($user->email)->later(now()->addMinutes(5), new RegisterMail($user));

	// Zobacz wiadomość w przeglądarce
	return new RegisterMail($user);  
}
```

## Parametry wiadomości
```php
<?php

Route::get('/send', function () {

	$user = User::factory()->make(['email => 'email@example.com', 'name' => 'Alexia']);

	Mail::send('email.test', ['param' => '123456'], function ($message) use ($user) {
	  $message->subject('Test mail');
	  $message->from('noreply@local.host', 'Promocje');  
	  $message->to('user@localhost'); 
	  $message->cc('worker@localhost')->bcc('admin@localhost');

	  // $message->from('noreply@' . request()->getHttpHost(), 'MailBot')
	  // $message->replyTo($user->email, $user->name);
	  // $message->to($user->email, $user->name);
	  // $message->attach(storage_path('pdf/user/123/fra-123.pdf'), ['as' => 'invoice-123.pdf', 'mime' => 'application/pdf']);
	  
	  return $message;
	});

});
```
