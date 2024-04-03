# Hosting ovh Laravel 11
Jak dodać aplikację laravel na hostingu w ovh.

### Hmmm
- Oszukują na hostingu gdy przy pakiecie Starter nie dodasz domeny to licza po 111.94 za hosting z jedną domeną i nie można dodawać więcej subdomen poza tą z www!!! 
- Lepiej zamówić ten droższy pakiet Perso z 5 domenami (jak już).
- Suport nie najlepszy zwłaszcza ten francuski.
- Czasami oszukuja na terminach za domeny pod koniec okresu i kasuja podwójnie udając że nie zaksięgowali wpłaty na czas (Każa dopłacać jak wpłata już poszła).

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
Jeżeli sa dodane w pliku .env, .env.production lub zmień na DB_CONNECTION=sqlite

## Zmień w .env, .env.production ustawienia sesji gdy nie ma bazy danych
SESSION_DRIVER=file

## Dodaj .htaccess w laravel root dir

Zabezpiecz pliki .env i blokuj wyświetlanie w przeglądarce katalogu głownego (nie twórz pliku error.php)

```htaccess
SetEnv PHP_VER 8_2
SetEnv REGISTER_GLOBALS 0

DirectoryIndex index.php
Options -Indexes -MultiViews +FollowSymlinks +SymLinksIfOwnerMatch

# Disable directory browsing
RewriteEngine on
RewriteCond %{REQUEST_URI} !^public
RewriteRule ^(.*)$ error.php [L]
# RewriteRule ^(.*)$ public/$1 [L]

<FilesMatch "^\.">
    Order allow,deny
    Deny from all
</FilesMatch>

# RewriteEngine On
# RewriteCond %{HTTP_HOST} ^domain.com$ [NC,OR]
# RewriteCond %{HTTP_HOST} ^www.domain.com$
# RewriteCond %{REQUEST_URI} !public/
# RewriteRule (.*) /public/$1 [L]
```
