<!--
    <div class="cursor-change">Change cursor style to white</div>
 -->
<script setup>
import { onMounted, nextTick } from 'vue'

const updateCursor = (event) => {
	document.querySelectorAll('.cursor-small').forEach(async (el) => {
		el.style.top = event.pageY + 'px'
		el.style.left = event.pageX + 'px'
	})

	document.querySelectorAll('.cursor-border').forEach(async (el) => {
		await new Promise((r) => setTimeout(r, 50))
		await nextTick(() => {
			el.style.top = event.pageY + 'px'
			el.style.left = event.pageX + 'px'
		})
	})
}

onMounted(() => {
	let cursor = document.querySelector('.cursor-small')
	let cursorBorder = document.querySelector('.cursor-border')

	window.addEventListener('mousemove', updateCursor)

	document.querySelectorAll('.cursor-change').forEach((el) => {
		el.addEventListener(
			'mouseleave',
			(e) => {
				cursor.classList.remove('cursor-mix-change')
				cursorBorder.classList.remove('cursor-mix-change-border')
			},
			true
		)
		el.addEventListener(
			'mousemove',
			(e) => {
				cursor.classList.add('cursor-mix-change')
				cursorBorder.classList.add('cursor-mix-change-border')
			},
			true
		)
	})
})
</script>

<template>
	<div class="cursor cursor-small"></div>
	<div class="cursor cursor-border"></div>
</template>

<style>
.cursor {
	z-index: 100;
	box-sizing: border-box;
	position: absolute;
	top: 0px;
	left: 0px;
	border-radius: 50%;
	width: 10px;
	height: 10px;
	padding: 5px;
	background: var(--c3);
	transform: translate(-50%, -50%);
	pointer-events: none;
	backface-visibility: hidden;
	/* transition: all 0.05s ease-out; */
}
.cursor-border {
	padding: 10px;
	border: 2px solid var(--c3);
	background: transparent;
	box-sizing: border-box;
	/* transition: all 0.11s; */
}
.cursor-mix-change {
	border-width: 2px;
	background: #fff;
	transform: translate(-50%, -50%) scale(1.3);
	filter: blur(0px);
}
.cursor-mix-change-border {
	border-color: #fff;
	transform: translate(-50%, -50%) scale(1.3);
	filter: blur(0px);
}
</style>
