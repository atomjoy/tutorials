# Vue3 pinis store
```js
// Vite .env variables
const app_debug = import.meta.env.VITE_APP_DEBUG
if (app_debug == true) {
	console.log('Debug enabled', app_debug)
}

// Store with setup(), <template setup>
export const useMaxStore = defineStore('max', () => {
	// States ref()s become state properties
	const count = ref(0)
	const name = ref('Maximo')
	const alert = ref({ message: '', type: 'danger' })
	const debug = app_debug // Check with: if(debug == true) {}

	// Getters computed()s become getters
	const doubleCount = computed(() => count.value * 2)
	const getAlert = computed(() => alert.value.toLowerCase())

	// Actions function()s become actions
	function increment() {
		count.value++
	}

	return { count, name, alert, doubleCount, getAlert, increment }
})

// Get store details
// const auth = useMaxStore()

// Reactivr
// const alert = reactive(auth.alert)
// console.log('onSubmit torefs', alert.message)

// Ref
// const alert = ref(auth.alert)
// console.log('onSubmit torefs', alert.value.message)

// toRefs
// const { alert } = toRefs(auth)
// console.log('onSubmit torefs', alert.value.message)
```
