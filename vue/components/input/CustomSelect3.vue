<template>
	<div class="custom-select" @blur="open = false">
		<div class="selected" :class="{ open: open }" @click="open = !open">{{ modelValue }} <i class="fas fa-caret-down selected-icon"></i></div>

		<div class="items" :class="{ selectHide: !open }">
			<div v-for="(option, i) of options" :key="i" @click="updateClick(option)">
				{{ option }}
			</div>
		</div>

		<input ref="input" type="hidden" :name="name" v-model="modelValue" @change="emit('update:modelValue', modelValue)" />
	</div>
</template>

<script setup>
import { ref, onMounted, toRefs, computed } from 'vue'

const emit = defineEmits(['update:modelValue', 'change', 'click', 'blur'])

const props = defineProps({ name: { type: String }, options: { type: Array }, modelValue: { type: String } })
const { name, options, modelValue } = toRefs(props)
const input = ref(null)
const open = ref(false)

onMounted(() => {
	// input.value.focus()
	console.log('Selected', modelValue.value)
})

const selected = computed(() => {
	return modelValue.value
})

function updateClick(option) {
	modelValue.value = option
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
	background-color: #ffffff;
	border-radius: 6px;
	border: 1px solid #666666;
	cursor: pointer;
	user-select: none;
	padding: 1rem 1.5rem;
}
.custom-select .selected.open {
	border: 1px solid #0075ff;
	border-radius: 6px 6px 0px 0px;
}
.custom-select .selected .selected-icon {
	position: absolute;
	top: calc(50% - (1rem / 2));
	right: 1.5em;
	transition: all 0.6s;
}
.custom-select .selected.open .selected-icon {
	color: #0075ff;
	transform: rotate(180deg);
}
.custom-select .items {
	color: #fff;
	border-radius: 0px 0px 6px 6px;
	overflow: hidden;
	border-right: 1px solid #0075ff;
	border-left: 1px solid #0075ff;
	border-bottom: 1px solid #0075ff;
	position: absolute;
	background-color: #fff;
	left: 0;
	right: 0;
	z-index: 1;
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
	background-color: #0075ff;
}
.selectHide {
	display: none;
}
</style>

<!--
  <script setup>
    const selected = ref('go')
  </sctipt>

  <Select
    :name="'language'"
    :options="['go', 'python', 'rust', 'javascript']"
    class="select"
    v-model="selected"
  />
-->
