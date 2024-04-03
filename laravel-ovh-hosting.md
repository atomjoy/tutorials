# Hosting ovh Laravel 11
Jak dodać aplikację laravel na hostingu w ovh.

### Pamiętaj
- Na hostingu gdy przy pakiecie Starter nie dodasz domeny to licza po 111.94 za hosting z jedną domeną i nie można dodawać więcej subdomen poza tą z www. 
- Jak już to zamówić ten droższy pakiet Perso z 5 domenami (129,74).
- Czasami oszukuja na terminach za domeny pod koniec okresu i kasuja podwójnie udając że nie zaksięgowali wpłaty na czas (Każa dopłacać jak wpłata już poszła że niby zwrócą a poźniej doliczają opłate za wznowienie).
- Jak już wpłacisz kasę to nie sposób nic od nich odzyskać w ramach zwrotu czy rezygnacji.
- Suport nie najlepszy zwłaszcza ten francuski.
- Coś pogmatwali z jakimiś kodami recovery (nie używać) jak zgubisz to się z suportem nie dogadasz bo będą głupczyć.
- No i ten zamulony panel administracyjny.
- Na plus klucze ssh do vps w panelu podczas reinstalacji oraz SSL lets encrypt za free w hostingu i niedroge odnowienia domen.
- W sumie to nazwa jest nie taka zła na hosting tylko trzeba ręcznie Letsencrypt instalować a vps się dziwacznie instaluje i nie można w panelu dodać klucza ssh do vps.
- No i te upierdliwe telefony z promocjami co chwila w nazwa (Hosting dość drogi w drugim roku i za domeny kasują strasznie dużo w drugim roku) domeny lepiej kupić w ovh.

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
