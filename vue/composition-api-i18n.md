# Vue3 Composition api i18n
Tłumaczenia w composition api vue3 komponent ze **<script setup\>**.

## Vue3 i18n watch w komponencie

### Konfiguracja vue3 i18n composition api
./lang/index.js
```js
import en from './lang_en.json' // { "error404" : { "title" : "Error page title here"}}
import pl from './lang_pl.json' // { "error404" : { "title" : "Tytuł strony tutaj"}}

const lang = {
	// Allow compositions api in components
	allowComposition: true, 
	globalInjection: true,
	legacy: false,
	// Locales
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
components/PageTitleComposition.vue
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

## Zmiana języka, tłumaczenia strony w Vue3 i18n

### Komponent do zmiany języka strony
```vue
<template>
	<div class="locale-changer">
		<select v-model="$i18n.locale" class="locale-changer-select">
			<option v-for="locale in $i18n.availableLocales" :key="`locale-${locale}`" :value="locale">{{ locale }}</option>
		</select>
	</div>
</template>

<script>
export default {
	name: 'ChangeLocale',
	data() {
		return {}
	},
	watch: {
		// Change server locale
		'$i18n.locale': function (newVal, oldVal) {
			console.log('From ', oldVal, 'to', newVal, 'curr', this.$i18n.locale)
			
			// Change locale function here
			// this.changeLocale(newVal)
		},
	},
}
</script>

<style scoped>
.locale-changer {
	float: right;
	width: auto;
	height: auto;
	padding: 15px;
}
.locale-changer-select {
	float: right;
	width: 50px;
	padding: 10px;
	text-align: center;
	border: 0px;
	background: transparent;
}
.locale-changer-select:focus {
	border: none;
	box-shadow: none;
}
</style>
```

## Linki
```sh
https://vue-i18n.intlify.dev/guide/migration/vue3.html#migration-in-vue-3
https://vue-i18n.intlify.dev/guide/advanced/composition.html#message-translation
```
