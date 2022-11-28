# Laravel remember me cookie

### Dodaj ciasteczko
Tworzenie bezbiecznego ciasteczka remember_me
```php
<?php

if(Auth::atempt(['email' => $email, 'password' => $pass], false) {

  $remember = (request()->input('remember_me') == 1) ? true : false;

  // Only if https
  if ($remember == true && request()->secure()) {

    // Create token
    if (empty($user->remember_token)) {
      $user->remember_token = uniqid() . md5(microtime());
      $user->save();
    }

  if (!empty($user->remember_token)) {
      // Set cookie
      // $name, $val, $minutes, $path,
      // $domain, $secure, $httpOnly = true,
      // $raw = false, $sameSite = 'strict'
      Cookie::queue(
        '_remember_token',
        $user->remember_token,
        env('APP_REMEBER_ME_MINUTES', 3456789),
        '/',
        '.' . request()->getHost(),
        request()->secure(), // or true for https only 
        true,
        false,
        'strict'
      );
    }
  }
}
```

### Pobieranie ciasteczka i logowanie
Url do sprawdzania czy ciastko remember_me istnieje (/web/api/logged)
```php
<?php

$token = cookie('_remember_token');

$user = User::where('remember_token', $token)->first();

if($user instanceof User) {
 // Lub true na logowanie z remember_me laravela
  Auth::login($user, false);
  
  return response()->json('Authenticated.');
} else {
  throw new \Exception('Not authenticated.', 401);
}
```
