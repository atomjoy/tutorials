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
