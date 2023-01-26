# Errors

## Environment

Zmienne środowiskowe ustawiamy w pliku .env lub w plikach .env.testing dla testów i .env.production dla produkcji.
Gdy w pliku .env parametr APP_ENV zmienimy z **local** na **production** Laravel wczyta plik konfiguracyjny z pliku .env.production. Wartość tego parametru ustawiona na **local** określa bieżący plik ustawień. Nie zapomnij wyczyścić cache pliku konfiguracyjnego **php artisan config:clear** z terminala.

## Debug

Zmieniając APP_DEBUG z **true** na **false** wyłączyasz debugowanie błędów w Laravelu. 
Gdy użyjesz teraz **throw new Exception('Empty email', 422)** w kontrolerach to otrzymasz błąd serwera o kodzie 500
**500 "Server Error"**. 

## Exception

Jeżeli chcesz przechwycić ten wyjątek to musisz użyć **try{ }catch(Exception $e){ }**. Dla odpowiedzi w formacie json użyj **return response()->json([], 200)** z kodem http **200** lub kodem błędu **422**, aby zapisać błąd do logów użyj **report($e)** i następnie zwróć **response()->json()** z kodem błędu lub sukcesu.

## Handler

Błędy można przechwycić w **Exceptions\Handler.php** w metodzie **register()** używając **$this->renderable()** bez potrzeby używania try...catch() w kontrolerach.
```php
public function register()
{
    $this->renderable(function (Throwable $e, $request) {			
        // Change "ServerError" Exception when app_debug=false to a json response
        if ($request->is('web/api/*') || $request->wantsJson()) {

            $msg = $e->getMessage() ?? 'Error';
            $code = $e->getCode();

            if($e instanceof Error) {
                $msg = 'Php Error.';
                $code = 500;
            }

            if($e instanceof PDOException) {
                $msg = 'Database Error.';
                $code = 500;
            }
            
            if($e instanceof NotFoundHttpException) {
                $msg = 'Not Found.';
                $code = 404;
            }

            if($e instanceof AuthenticationException) {
                $code = 401;
            }

            if($e instanceof ValidationException) {
                $code = 422;
            }

            return response()->json([
                'message' => trans($msg),
            ], $code);
        }
    });
}
```

## Headers

Gdy chcesz otrzymać odpowiedż w formacie json do zapytania musisz dodać nagłówek **Accept: application/json** wtedy serwer zwróci json string.

## Policy

W Policy trzeba dodać **index(?User $user)** w metodach bez użytkownika inaczej będzie wyświetlał się błąd uwierzytelnienia.
