<template>
	<div class="checkbox-line">
		<input ref="input" class="checkbox" type="checkbox" :checked="checked" :value="value" :name="name" @change="updateInput" />
		<div class="checkmark">
			<i class="fas fa-check dot"></i>
		</div>
		<label>{{ label }}</label>
	</div>
</template>

<script setup>
import { ref, onMounted, toRefs, computed } from 'vue'

const emit = defineEmits(['update:modelValue', 'change'])
const props = defineProps({
	name: { type: String },
	modelValue: { type: [Array, Boolean] },
	value: { type: String, required: true },
	label: { type: String, required: true },
})
const { value, modelValue } = toRefs(props)
const input = ref(null)

onMounted(() => {
	// input.value.focus()
})

const checked = computed(() => {
	if (modelValue.value instanceof Array) {
		return modelValue.value.includes(value.value)
	}
	return modelValue.value
})

function updateInput(event) {
	let check = event.target.checked
	if (modelValue.value instanceof Array) {
		let newValue = [...modelValue.value]
		if (check) {
			newValue.push(value.value)
		} else {
			newValue.splice(newValue.indexOf(value.value), 1)
		}
		emit('update:modelValue', newValue)
	} else {
		emit('update:modelValue', check)
	}
}
</script>

<style scoped>
/* Vue round checkbox style */
.checkbox-line {
	float: left;
	width: 100%;
	padding: 5px;
	margin-top: 10px;
	display: flex;
	align-items: center;
}
.checkbox-line .checkbox {
	position: absolute;
	height: 30px;
	width: 30px;
	opacity: 0;
	z-index: 9;
	cursor: pointer;
}
.checkbox-line .checkmark {
	box-sizing: border-box;
	position: relative;
	display: inline-block;
	width: 30px;
	height: 30px;
	margin-right: 15px;
	border: 1px solid var(--color);
	box-shadow: var(--inp-shadow-focus);
	border-radius: 50%;
	z-index: 3;
}
.checkbox-line .checkmark .dot {
	box-sizing: border-box;
	opacity: 0;
	color: #fff;
	width: 30px;
	height: 30px;
	padding: 5px;
	border-radius: 50%;
	background: var(--color);
	border: 1px solid var(--color);
	text-align: center;
	z-index: 1;
}
.checkbox-line .checkbox:checked + .checkmark {
	border: transparent;
	box-shadow: var(--inp-shadow-focus);
}
.checkbox-line .checkbox:checked + .checkmark .dot {
	opacity: 1;
	border: 1px solid var(--color);
}
</style>
