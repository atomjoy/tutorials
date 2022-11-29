<script setup>
const props = defineProps({
	msg: {
		type: String,
		required: true,
		default: 'Your account has been created.',
	},
	type: {
		type: String,
		required: true,
		default: 'info',
		validator(value) {
			return ['info', 'success', 'warning', 'danger', 'error'].includes(value)
		},
	},
})
</script>

<template>
	<div ref="div" class="animate__animated animate__flipInX" :class="'alert-' + type">{{ msg }}</div>
</template>

<style lang="css" scoped>
.alert-info {
	font-size: 0.8rem;
	display: block;
	padding: 10px 20px;
	margin: 10px 0px;
	color: #6f6af8;
	background: #dddcfa;
	border: 1px solid #6f6af8;
	border-radius: var(--radius);
}
.alert-success {
	font-size: 0.8rem;
	display: block;
	padding: 10px 20px;
	margin: 10px 0px;
	color: #5c5;
	background: #dffbdb;
	border: 1px solid #5c5;
	border-radius: var(--radius);
}
.alert-warning {
	font-size: 0.8rem;
	display: block;
	padding: 10px 20px;
	margin: 10px 0px;
	color: #f7d169;
	background: #fdf8ec;
	border: 1px solid #f7d169;
	border-radius: var(--radius);
}
.alert-danger {
	font-size: 0.8rem;
	display: block;
	padding: 10px 20px;
	margin: 10px 0px;
	color: #f23;
	background: #fddbe9;
	border: 1px solid #f23;
	border-radius: var(--radius);
}
.alert-error {
	font-size: 0.8rem;
	display: block;
	padding: 10px 20px;
	margin: 10px 0px;
	color: #fff;
	background: #f00;
	border: 1px solid #f00;
	box-shadow: 0px 0px 0px 3px rgba(255, 0, 0, 0.15);
	border-radius: var(--radius);
}
</style>
