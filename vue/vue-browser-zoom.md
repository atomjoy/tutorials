# Vue 3 zoom w przeglądarce z javascript 
Jak pobrać zoom, wysokość i szerokość strony www przy zmianie rozmiaru okna przeglądarki.

### Komponent
```vue
<script setup>
import { ref, reactive, toRefs, onMounted, onUnmounted, watch, created } from 'vue'

let h = ref(0)
let w = ref(0)
let z = ref(0)

function update() {
	h.value = window.innerHeight ?? document.documentElement.clientHeight
	w.value = window.innerWidth ?? document.documentElement.clientWidth
	z.value = Math.round(window.devicePixelRatio * 100)
}

function onResize() {
	update()
	console.log('Resize', h, w, z)
}

onMounted(() => {
	window.addEventListener('resize', onResize)
	update()
})

onUnmounted(() => {
	document.removeEventListener('resize', onResize)
})
</script>

<template>
	<div class="device-width">
		<div>
			<div>Device width:</div>
			<div>{{ w }} px</div>
		</div>
		<div>
			<div>Device height:</div>
			<div>{{ h }} px</div>
		</div>
		<div>
			<div>System zoom + Browser zoom:</div>
			<div>{{ z }} %</div>
		</div>
	</div>
</template>

<style lang="css" scoped>
.device-width {
	float: left;
	width: 100%;
	padding: 20px;
	display: flex;
	gap: 2%;
	justify-content: space-between;
}
.device-width div {
	width: 50%;
	font-size: 21px;
	font-weight: 700;
	color: #07f;
	background: #0077ff22;
	border: 2px solid #07f;
	padding: 10px;
	display: flex;
	flex-direction: column;
	align-items: stretch;
	justify-content: space-evenly;
	gap: 20px;
}
.device-width div > div {
	float: left;
	width: 100%;
	padding: 10px;
	box-sizing: border-box;
	vertical-align: middle;
	text-align: center;
}
.device-width div > div:first-child {
	height: 100%;
}
</style>
```

### Link do komponentu Vue
https://github.com/atomjoy/tutorials/blob/main/vue/components/ResizeEvent.vue
