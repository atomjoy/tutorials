# Hosting ovh Laravel 11
Jak dodać aplikację laravel na hostingu w ovh.

## Linki symboliczne w laravel
php artisan storage:link

## Hosting php w dashboard
Zmień PHP na wersję 8.3

## Dodaj domenę do hostingu multiviews 
Ścieżka do katalogu www/project-name/public

## Zmiany w DNS u dostawcy domeny
Konieczne będzie ustawienie rekordu TXT i przekierować na DNS jeżeli domena parokwana gdzie indziej

## Upload plików laravela na server do katalogu
www/project-name

## Po 2h od ustawieniu przekierowania
Wygeneruj certufikaty ssl dla domeny w panelu (czasami domena nie dodaje się odrazu do certfikatu)

## Pamiętaj o utworzeniu baz danych mysql
Jeżeli sa dodane w pliku .env, .env.production

## Zmień w .env, .env.production ustawienia sesji gdy nie ma bazy danych
SESSION_DRIVER=file
