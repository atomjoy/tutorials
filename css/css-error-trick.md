# Css

## Wpychanie padingu do elementu

```css
*,
*::before,
*::after {
	box-sizing: border-box;
	outline: 0px none transparent;
	text-decoration: none;
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

## Scrollbar

```css
.scrollbar {
  scrollbar-width: thin;
}
