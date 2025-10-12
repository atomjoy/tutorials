# Php curl, http laravel

If self-signed certs error in php curl download https://curl.se/ca/cacert.pem and place to **C:/php** directory and add path to this file in **php.ini** 
**curl.cainfo** and **opessl.cafile** for Http client in php, laravel.

```sh
[PHP]

# Php extension directory
extension_dir="./ext"

# Settings
post_max_size = 500M
upload_max_filesize = 100M

# Unhash extensions
extension=bz2
extension=curl
extension=ftp
extension=fileinfo
extension=gd
extension=gettext
extension=intl
extension=mbstring
extension=exif
extension=openssl
extension=pdo_mysql
extension=pdo_sqlite
extension=sockets
extension=sqlite3
extension=zip
zend_extension=opcache

[Session]
session.cookie_secure = Off
session.cookie_httponly = On
session.cookie_lifetime = 86400
session.gc_maxlifetime = 1440

[curl]
curl.cainfo = "C:\php\cacert.pem"

[openssl]
openssl.cafile="C:\php\cacert.pem"
```
