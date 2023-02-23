# Vue 3 Composition Api change locales
Vue 3 Composition Api change locales with <script setup>.

## main.js
```js
import { createI18n } from 'vue-i18n'

const lang = {
  // Allow compositions api (required) !!!
  allowComposition: true,
  globalInjection: true,
  legacy: false,
  
  // Locales
  locale: 'en',
  fallbackLocale: 'en',
  availableLocales: ['en', 'pl'],
  
  // Example messages
  messages: {
    en: { en: "English", pl: "Polish" },
    pl: { en: "Angielski", pl: "Polski" },
  },
}

const i18n = createI18n(lang)
app.use(i18n)
```

### ChangeLocale.vue
```vue
<template>
	<div class="locale-changer">
		<select v-model="locale" class="locale-changer-select">
			<option v-for="lang in availableLocales" 
				:key="`locale-${lang}`" 
				:value="lang">{{ t(lang) }}</option>
		</select>
	</div>
</template>

<script setup>
import { watch, computed, onMounted } from 'vue'
import { useI18n } from 'vue-i18n'

const { t, locale, availableLocales } = useI18n({ useScope: 'global' })

onMounted(() => {
	console.log('Current locale', locale.value, availableLocales)
})

watch(
	() => locale.value,
	(lang) => {
		console.log('Changed locale', lang)
		// Do something on change here ...
		// store.changeServerLang()
	}
)

const msg = computed(() => t('example.msg'))
</script>
```

# Links
<https://vue-i18n.intlify.dev/guide/advanced/composition.html#global-scope>
