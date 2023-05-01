# Dev

## DNS

Usuwaj nie używane wpisy subdomen i przekierowania na wygasłe VPS-y.

### SPF ograniczenie wysyłania

Dodać rekord SPF dla każdej subdomeny i domeny z której nie można wysyłać wiadomości email.

```sh
v=spf1 -all
```

### SPF wysyłanie email

Dodać rekord SPF dla każdej subdomeny i domeny z której chcesz wysyłać wiadomości email (a mx ptr ip: include: -all).

```sh
v=spf1 a mx ip:1.2.3.4 include:mx.ovh.com -all
```

## Cache

Kaszuj dużo prosty cache na nginx czyni cuda. Statyczny kontent puszczaj zawsze z subdomeny lub z cdn.

## Ciasteczka

Usuwaj ciasteczka z kontentu statycznego na serwerze. Nie zabieraj mocy/transferu serwera na wysyłanie obrazków z ciasteczkami.

## Upload

Zmieniaj nazwy wysyłanych plików. Pliki trzymaj na jakimś cdn i puszczaj z subdomeny.

## DNS Przykład strefy dns ovh

```sh
$TTL 3600
@	IN SOA dns112.ovh.net. tech.ovh.net. (2023043000 86400 3600 3600000 300)
                          IN NS     ns112.ovh.net.
                          IN NS     dns112.ovh.net.
                          IN MX     1 mx1.mail.ovh.net.
                          IN MX     5 mx2.mail.ovh.net.
                          IN MX     100 mx3.mail.ovh.net.
                          IN A      11.22.33.44
                      600 IN TXT    "v=spf1 a mx include:mx.ovh.com -all"
www                       IN A      11.22.33.44
www                   600 IN TXT    "v=spf1 a mx include:mx.ovh.com -all"

### Poniżej do usunięcia tylko zaśmieca 
_autodiscover._tcp        IN SRV    0 0 443 mailconfig.ovh.net.
_imaps._tcp               IN SRV    0 0 993 ssl0.ovh.net.
_submission._tcp          IN SRV    0 0 465 ssl0.ovh.net.
autoconfig                IN CNAME  mailconfig.ovh.net.
autodiscover              IN CNAME  mailconfig.ovh.net.
ftp                       IN CNAME  example.com.
imap                      IN CNAME  ssl0.ovh.net.
mail                      IN CNAME  ssl0.ovh.net.
pop3                      IN CNAME  ssl0.ovh.net.
smtp                      IN CNAME  ssl0.ovh.net.
```
