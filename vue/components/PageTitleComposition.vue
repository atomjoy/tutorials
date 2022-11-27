
<!-- 
// Add this to i18n config in ./lang/index.js
// Allow i18n in compositions api
const lang = {  
	allowComposition: true, 
}
-->

<template></template>
<script setup>
import { watch, onMounted } from 'vue'
import { useI18n } from 'vue-i18n'

const { t, locale } = useI18n({ useScope: 'global' })

const props = defineProps({
	title: {
		type: String,
		default: 'error404.title',
	},
})

const title = props.title

onMounted(() => {
	console.log('Tiyle', title, locale.value)
	document.title = t(title)
})

watch(
	() => locale.value,
	(lang) => {
		document.title = t(title)
		console.log('Title, locale', t(title), lang)
	}
)
</script>
