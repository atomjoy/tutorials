# Dark mode css

### Style
```css
@import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

:root {
	--font-family: 'Poppins', sans-serif;
	--section-gap: 160px;
	--radius: 10px;
	--font-size: 16px;
}

:root {
  --bg: #fff;
}

/* browser setting */
@media (prefers-color-scheme: dark) {
	:root {
		--bg: #222;
	}
}

/* js change mode html tag */
[color-scheme="light"] {
  color-scheme: light;
  --bg: #fff;
  --bg-light: #dfe7ee;
}

[color-scheme="dark"] {
  color-scheme: dark;
  --bg: #22223d;
  --bg-light: #292a40;
}

html {
  background-color: var(--bg);
}
```

### Script
```js
var theme = null;

window.onload = () => {
  initTheme()
  document.querySelector('#theme-toggle')?.addEventListener('click', changeTheme)
}

function initTheme() {
  // Get
  if(localStorage.getItem('color-scheme') == null) {
    theme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
  } else {
    theme = localStorage.getItem('color-scheme')
  }
  // Update
  document.firstElementChild.setAttribute('color-scheme', theme)
  localStorage.setItem('color-scheme', theme)
}

function changeTheme() {
  // Change
  theme = theme === 'light' ? 'dark' : 'light'
  // Update html tag class
  document.firstElementChild.setAttribute('color-scheme', theme)
  localStorage.setItem('color-scheme', theme)
  console.log("Changed", theme)
}
```
