# Css

## Wpychanie padingu do elementu

```css
* {
	box-sizing: border-box;	
	text-decoration: none;
	outline: 0px none transparent;
}

*::before,
*::after {
	content: '';
}
```

## Google przycisk logowania błąd białego tła w trybie ciemnym

```css
iframe {
	color-scheme: light !important;
}
```

## Błąd image/svg niewidoczny margines pod zdjęciem lub ikoną

```css
img, svg {
  display: block;
  max-width: 100%;
}
```

## Zaznaczanie tekstu

```css
::placeholder {
	color: var(--divider-primary);
	font-size: 1rem;
	font-weight: 500;
}

::selection {
	background: var(--accent-primary);
	color: #fff;
}
```

## Linki

```css
a:hover,
a:focus,
a:active {
	color: red;
}
```

## Scrollbar

```css
.scrollbar {
  scrollbar-width: thin;
}
```


## Formularz z marginesem górnym umieść w div

```css
.form-wrapper {
	float: left;
	width: 100%;
	margin: 0px;
	padding: 0px;
	overflow: hidden;
	position: relative;
}

form {
	width: 90%;
	max-width: 640px;
	margin: 50px auto;
	padding: 0px 30px;
}
```
