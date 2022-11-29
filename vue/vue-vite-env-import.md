# Vue3 Vite import .env 

### .env 
```sh
# Variables only with VITE_

VITE_APP_DEBUG=true
```

### Vue, js
```js
// Vite .env variables
const app_debug = import.meta.env.VITE_APP_DEBUG

if (app_debug == true) {
	console.log('Debug enabled', app_debug)
}
```
