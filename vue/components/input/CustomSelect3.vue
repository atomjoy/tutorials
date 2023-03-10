<!--
<script setup>
	import CustomSelect from '@/components/input/CustomSelect3.vue'

	const selected1 = ref('go')
	const selected2 = ref(3)

	function onSubmit(e) {
		let data = new FormData(e.target);
		for (var pair of data.entries()) {
      			console.log("Key:", pair[0], "Value:", pair[1]);
		}
    		// axios request here
	}
</sctipt>
<template>
	<form @submit.prevent="onSubmit">
		<CustomSelect
			:name="'language1'"
			:options="['go', 'python', 'rust', 'javascript']"
			v-model="selected1"
			:class="'second-class'"
		/>
		<CustomSelect
			class="select"
			:name="'language2'"
			:options="[{id: 1, value: 'go'}, {id: 2, value: 'python'}, {id: 3, value: 'rust'}, {id: 4, value: 'javascript'}]"
			v-model="selected2"
		/>
		<button> Send </button>
	</form>
</template>
-->

<template>
	<div class="custom-select" @blur="open = false" :tabindex="tabindex">
		<div class="selected" :class="{ open: open }" @click="open = !open">{{ selected }} <i class="fas fa-caret-down selected-icon"></i></div>

		<div ref="items" class="items" :class="{ selectHide: !open }">
			<div v-for="(option, i) of options" :key="i" @click="updateClick(option)">
				{{ option.value ?? option }}
			</div>
		</div>
		<!-- @change="emit('update:modelValue', selected)" -->
		<input ref="input" type="hidden" :name="name" v-model="modelValue" />
	</div>
</template>

<script setup>
import { ref, onMounted, toRefs } from 'vue'

const emit = defineEmits(['update:modelValue', 'change', 'click', 'blur'])
const props = defineProps({ name: { type: String }, options: { type: Array }, modelValue: { type: String } })
const { name, options, modelValue } = toRefs(props)
const input = ref(null)
const open = ref(false)
const selected = ref(null)
const tabindex = ref(0)

onMounted(() => {
	// input.value.focus()
	selected.value = options?.value?.find((o) => o.id === modelValue.value)?.value ?? modelValue.value
})

function updateClick(option) {
	modelValue.value = option.id ?? option
	selected.value = option.value ?? option
	open.value = false
	emit('update:modelValue', modelValue.value)
}
</script>

<style scoped>
.custom-select {
	position: relative;
	float: left;
	width: 100%;
	outline: none;
}
.custom-select .selected {
	background-color: transparent;
	border-radius: 6px;
	border: 1px solid #eee;
	cursor: pointer;
	user-select: none;
	padding: 1rem 1.5rem;
}
.custom-select .selected.open {
	border: 1px solid #07f;
	border-radius: 6px 6px 0px 0px;
}
.custom-select .selected .selected-icon {
	color: #eee;
	position: absolute;
	top: calc(50% - (1rem / 2));
	right: 1.5em;
	transition: all 0.6s;
}
.custom-select .selected.open .selected-icon {
	color: #07f;
	transform: rotate(180deg);
}
.custom-select .items {
	scrollbar-width: thin;
	scrollbar-color: #07f #eee;
	color: #fff;
	border-radius: 0px 0px 6px 6px;
	overflow: hidden;
	border-right: 1px solid #07f;
	border-left: 1px solid #07f;
	border-bottom: 1px solid #07f;
	position: absolute;
	background-color: #fff;
	left: 0;
	right: 0;
	z-index: 1;
	max-height: 300px;
	overflow-y: auto;
}
.custom-select .items::-webkit-scrollbar {
	width: 6px;
	background-color: #07f;
}
.custom-select .items::-webkit-scrollbar-thumb {
	background: #07f;
}
.custom-select .items div {
	color: #111;
	padding-left: 1em;
	cursor: pointer;
	user-select: none;
	padding: 1rem 1.5rem;
}
.custom-select .items div:hover {
	color: #fff;
	background-color: #07f;
}
.custom-select .items .selected-option {
	color: #fff;
	background-color: #07f;
}
.selectHide {
	display: none;
}
</style>
