# Typescript

Na początek instalujemy nodejs (będzie wtedy można używać npm)

## Instalacja typescript

Uruchom z konsoli jako administrator i zainstaluj globalnie

```sh
npm i -g typescript
```

### Tworzenie projektu

Utwórz katalog dla projektu i uruchom polecenie które utworzy plik package.json

```sh
npm init
```

### Aktualizacja projektu

Zmień w pliku **package.json** linijkę, pozwoli to na kompilację typescript z konsoli vscode

```json
{
    "scripts": {
        "compile" : "tsc"
    },
}
```

### Kompilacja projektu

```sh
tsc
# lub gdy tsc nie działa
npm run compile
```

## Konfiguracja aplikacji ts

Dodaj w pliku **tsconfig.json**

```json
{
    "compilerOptions": {
        "rootDir": "./src",
        "outDir": "./dist",
        "target": "ES2015",
    }
}
```

### Plik aplikacji typescript

Utwórz katalog **src** i dodaj w nim plik **app.ts** dla aplikacji

```ts
console.log('Hello from ts app!');
```

### Plik aplikacji html

Dodaj w pliku **index.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TypeScript</title>
</head>
<body>
    <h1>Hello</h1>
    <script src="./dist/app.js"></script>
</body>
</html>
```
