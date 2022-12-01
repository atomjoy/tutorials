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
	<div ref="div" class="animate__animated animate__flipInX" :class="'alert-default alert-' + type">{{ msg }}</div>
</template>

<style lang="css" scoped>
.alert-default {
	font-size: 0.8rem;
	display: block;
	padding: 10px 20px;
	margin: 10px 0px;
	border-radius: 10px;
	font-weight: 700;
}
.alert-info {
	color: #6f6af8;
	background: #dddcfa;
	border: 1px solid #6f6af8;
}
.alert-success {
	color: #5c5;
	background: #dffbdb;
	border: 1px solid #5c5;
}
.alert-warning {
	color: #f7d169;
	background: #fdf8ec;
	border: 1px solid #f7d169;
}
.alert-danger {
	color: #f23;
	background: #fddbe9;
	border: 1px solid #f23;
}
.alert-error {
	color: #fff;
	background: #f00;
	border: 1px solid #f00;
	box-shadow: 0px 0px 0px 5px rgba(247, 56, 56, 0.3);
}

@media (prefers-color-scheme: dark) {
	.alert-default {
		background: transparent !important;
	}
}
</style>
