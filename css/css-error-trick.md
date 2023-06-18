# Css

### Root parametry

```css
:root {
	--select-border: #f5f5f5;
	--divider-primary: #e1e1e1;
	--accent-primary: #09f;
}
```

## Wpychanie padingu do elementu

```css
* {
	box-sizing: border-box;	
	text-decoration: none;
	outline: 0px none transparent;
}

*::before,
*::after {
	content: none;
	/* Error in flex justify-content: space-between; if set to content: ''; */
}
```

## Flex justify divs

```css
.widget {
	display: flex;
	flex-flow: row wrap;
	justify-content: space-between;
}

.widget::before,
.widget::after {
	content: none;		
}

.widget .box {
	width: 25%;
	align-items: center;
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
a {
	text-decoration: none;
}

a:hover,
a:focus,
a:active {
	color: red;
}
```

## Select arrow

```css
select {
	outline: none;
	appearance: none;
	background-color: transparent;
	border: 1px solid var(--select-border);
	line-height: 1.1;
	background-color: #fff;
	background-image: linear-gradient(to top, #f9f9f9, #fff 33%);
}

select[multiple] option {
  white-space: normal;
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

## Code pre

```css
pre {
	white-space: pre-wrap; 
	word-break: keep-all;
	/* word-wrap: break-word; */	
}
```
