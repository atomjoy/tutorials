<!--
// Add in main i18n options https://vue-i18n.intlify.dev/guide/advanced/composition.html#global-scope
import { createI18n } from 'vue-i18n'

const lang = {
  // Allow compositions api (required)
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
-->

<template>
	<div class="locale-changer">
		<select v-model="locale" class="locale-changer-select">
			<option v-for="lang in availableLocales" :key="`locale-${lang}`" :value="lang">{{ t(lang) }}</option>
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
	}
)

const msg = computed(() => t('example.msg'))
</script>

<style scoped>
.locale-changer {
	float: right;
	width: auto;
	height: auto;
	padding: 5px;
}
.locale-changer-select {
	float: right;
	width: 50px;
	padding: 2px;
	text-align: center;
	border: 0px;
	background: transparent;
	font-size: 15px;
}
.locale-changer-select:focus {
	border: none;
	box-shadow: none;
}
</style>
