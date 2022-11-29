<!-- 
  First add in i18n lang.js config param: 
  allowComposition: true 
 -->
 
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
