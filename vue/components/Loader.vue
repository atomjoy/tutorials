<template>
	<div class="loader">
		<div class="loader-circle"></div>
	</div>
</template>

<style scoped>
.full-width {
	overflow: hidden;
	width: 100%;
}
.loader {
	position: fixed;
	top: 20%;
	left: calc(50% - 40px);
	width: 80px;
	height: 80px;
	padding: 5px;
	background: #fff;
	box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.2);
	box-sizing: border-box;
	border-radius: 100%;
	z-index: 99999999;
}
.loader-circle {
	padding: 5px;
	width: 70px;
	height: 70px;
	border-radius: 100%;
	background: transparent;
	border: 6px solid transparent;
	border-left: 6px solid #09f;
	border-right: 6px solid #09f;
	animation: rotate 0.5s linear infinite;
	box-sizing: border-box;
}
@keyframes rotate {
	100% {
		transform: rotate(360deg);
	}
}
</style>
