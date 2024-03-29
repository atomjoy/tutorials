<!--
    <div class="cursor-change">Change cursor style to white</div>
 -->
<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue'

const updateCursor = (event) => {
	document.querySelectorAll('.cursor').forEach(async (el) => {
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
:root {
  --cursor-b: #222
  --cursor-w: #fff
}
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
	background: var(--cursor-b);
	transform: translate(-50%, -50%);
	pointer-events: none;
	backface-visibility: hidden;
	/* transition: all 0.05s ease-out; */
}
.cursor-border {
	padding: 10px;
	border: 2px solid var(--cursor-b);
	background: transparent;
	box-sizing: border-box;
	transition: all 0.11s;
}
.cursor-mix-change {
	border-width: 2px;
	background: var(--cursor-w);
	transform: translate(-50%, -50%) scale(1.3);
	filter: blur(0px);
}
.cursor-mix-change-border {
	border-color: var(--cursor-w);
	transform: translate(-50%, -50%) scale(1.3);
	filter: blur(0px);
}
</style>
