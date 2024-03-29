<script>
// import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

function scrollToTop() {
	window.scrollTo({ top: 0, behavior: 'smooth' })
	// window.scrollTo(0,0);
	// window.scrollIntoView({ behavior: 'smooth' })
}
</script>
<template>
	<a href="#" @click="scrollToTop">
		<div class="scrolltop">
			UP <!-- <font-awesome-icon :icon="['fas', 'chevron-up']" /> -->            
		</div>
	</a>
</template>

<style>
html {
	scroll-behavior: smooth;
}

.scrolltop {
	color: #fff;
	background: var(--c3);
	border-radius: 50%;
	position: fixed;
	bottom: 10px;
	right: 10px;
	padding: 10px;
	width: 40px;
	height: 40px;
	text-align: center;
}
</style>
