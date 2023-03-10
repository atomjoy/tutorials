<!--
  <script setup>
    const selected1 = ref('go')
    const selected2 = ref(3)
  </sctipt>

  <CustomSelectKeys
    :name="'language'"
    :options="['go', 'python', 'rust', 'javascript']"
    v-model="selected1"
    :class="'second-class'"
  />

  <CustomSelectKeys
    class="select"
    :name="'language'"
    :options="[{key: 1, value: 'go'}, {key: 2, value: 'python'}, {key: 3, value: 'rust'}, {key: 4, value: 'javascript'}]"
    v-model="selected2"
  />
-->

<template>
	<div class="custom-select" @blur="open = false">
		<div class="selected" :class="{ open: open }" @click="open = !open">{{ selected }} <i class="fas fa-caret-down selected-icon"></i></div>

		<div class="items" :class="{ selectHide: !open }">
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

onMounted(() => {
	// input.value.focus()
	selected.value = options?.value?.find((o) => o.key === modelValue.value)?.value ?? modelValue.value
})

function updateClick(option) {
	modelValue.value = option.key ?? option
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
	border: 1px solid var(--inp-border);
	cursor: pointer;
	user-select: none;
	padding: 1rem 1.5rem;
}
.custom-select .selected.open {
	border: 1px solid var(--color);
	border-radius: var(--radius) var(--radius) 0px 0px;
}
.custom-select .selected .selected-icon {
	color: var(--inp-border);
	position: absolute;
	top: calc(50% - (1rem / 2));
	right: 1.5em;
	transition: all 0.6s;
}
.custom-select .selected.open .selected-icon {
	color: var(--color);
	transform: rotate(180deg);
}
.custom-select .items {
	color: var(--btn-color);
	border-radius: 0px 0px 6px 6px;
	overflow: hidden;
	border-right: 1px solid var(--color);
	border-left: 1px solid var(--color);
	border-bottom: 1px solid var(--color);
	position: absolute;
	background-color: var(--bg);
	left: 0;
	right: 0;
	z-index: 1;
}
.custom-select .items div {
	color: var(--color-text);
	padding-left: 1em;
	cursor: pointer;
	user-select: none;
	padding: 1rem 1.5rem;
}
.custom-select .items div:hover {
	color: var(--btn-color);
	background-color: var(--btn-bg);
}
.selectHide {
	display: none;
}
</style>
