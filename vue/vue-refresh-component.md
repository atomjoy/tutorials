# Vue3 Odświeżanie komponentu, css style
Dodaj do komponentu dodatkowy parametr :key="counter" z incrementowaną wartością onclick, onsubmit, onchange

```vue
<script setup>
import { ref, reactive, toRefs, computed, onMounted } from 'vue'
import Alert from '@/components/Alert.vue'
import { useAuthStore } from '@/stores/auth.js'

// Store
const auth = useAuthStore()
const message = ref('')
const type = ref('success')

// Refresh key
const refresh = ref(1)

async function onSubmit(e) {
	await auth.loginUser(new FormData(e.target))
  
	message.value = auth.alert.message	
	type.value = auth.alert.type
  
	// Refresh alert component css animation
	refresh.value++
}
</script>

<template>
  <form method="post" class="form" @submit.prevent="onSubmit">
    <h2>Sign In</h2>
    
    <!-- Refresh :key on action -->
    <Alert v-if="message" :msg="message" :type="type" :key="refresh" />

    <input type="submit" value="Login" />
  </form>
</template>
```
