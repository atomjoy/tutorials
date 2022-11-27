# Vue3 Composition api i18n
Tłumaczenia w composition api vue3 komponent ze **<script setup\>**.

### Konfiguracja vue3 i18n composition api
./lang/index.js
```js
import en from './lang_en.json' // { "error404" : { "title" : "Error page title here"}}
import pl from './lang_pl.json' // { "error404" : { "title" : "Tytuł strony tutaj"}}

const lang = {
	allowComposition: true, // Allow compositions api
	locale: 'en', // set locale
	fallbackLocale: 'en', // set fallback locale
	availableLocales: ['en', 'pl'], // available locales
	messages: {
    en: en,
    pl: pl,
  },
}

export default lang
```

### Dodaj tłumaczenia i18n do Vue3
main.js
```js
import { createI18n } from 'vue-i18n'
import lang from './lang'

// ...

const i18n = createI18n(lang)
const app = createApp(App)
app.use(i18n)

// ...
```

### Zmiana tytułu strony www w Vue3 composition api setup
components/PageTitle.vue
```vue
<template></template>
<script setup>
import { watch, onMounted } from 'vue'
import { useI18n } from 'vue-i18n'

const { t, locale } = useI18n({ useScope: 'global' })

const props = defineProps({
	title: {
		type: String,
		default: 'error404.title', // Translation key from lang_en.json translation messages
	},
})

const title = props.title

onMounted(() => {
	document.title = t(title)
  // console.log('Title', title, locale.value)
})

watch(
	() => locale.value,
	(lang) => {
		document.title = t(title)
		// console.log('Title, locale', t(title), lang)
	}
)
</script>
```

### Dodaj komponent w szablonie strony
views/HomePageView.vue
```vue
<script setup>
import Title from '@/components/PageTitle.vue'
</script>

<template>
	<Title title="error404.title" />
  
	<p>{{ $t('error404.message') }}</p>
</template>
```
