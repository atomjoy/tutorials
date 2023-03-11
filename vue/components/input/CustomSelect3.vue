<!--
<script setup>
  import CustomSelect from '@/components/input/CustomSelect3.vue'

  const selected1 = ref(null)
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
    <CustomSelect v-model="selected1" :placeholder="'Wybierz'" :label="'Language1'" :name="'language1'" :options="['Go', 'Python', 'Rust', 'Javascript', 'Php', 'Html', 'Vue', 'React', 'Css']" :class="'custom-class'" />

    <CustomSelect
      v-model="selected2"
      :placeholder="'Wybierz'"
      :label="'Language2'"
      :name="'language2'"
      :options="[
        { key: 1, value: 'Php' },
        { key: 2, value: 'Css' },
        { key: 3, value: 'Html' },
        { key: 4, value: 'JavaScript' },
      ]"
      :class="'custom-class'"
    />

    <button> Send </button>
  </form>
</template>
-->

<template>
	<label v-if="label" :for="name">{{ label }}</label>
	<div class="custom-select" @blur="open = false" :tabindex="tabindex">
		<div class="selected" :class="{ open: open, inactive: inactive }" @click="open = !open">{{ selected }} <i class="fas fa-caret-down selected-icon"></i></div>

		<div ref="items" class="items" :class="{ selectHide: !open }">		
			<div :key="0" @click="updateClick(null)">{{ placeholder }}</div>			
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
const props = defineProps({
	label: { type: String },
	name: { type: String },
	options: { type: Array },
	modelValue: { type: String },
	tabindex: { type: Number, default: 0 },
	placeholder: { type: String, default: 'Choose something' },
})
const { label, name, options, modelValue, tabindex, placeholder } = toRefs(props)
const input = ref(null)
const open = ref(false)
const inactive = ref(false)
const selected = ref(null)

onMounted(() => {
	if (modelValue.value !== null) {
		selected.value = options?.value?.find((option) => option.key === modelValue.value)?.value ?? modelValue.value
	} else {
		selected.value = placeholder.value
		inactive.value = true
		modelValue.value = null
	}
})

function updateClick(option = null) {
	if (option == null) {
		// placeholder
		modelValue.value = null
		selected.value = placeholder.value
		inactive.value = true
		open.value = false
	} else {
		// Options
		modelValue.value = option.key ?? option
		selected.value = option.value ?? option
		inactive.value = false
		open.value = false
	}

	emit('update:modelValue', modelValue.value)
}

function renameKeys(obj = { id: '1', name: 'Alex' }, newKeys = { id: 'key', name: 'value' }) {
	const keyValues = Object.keys(obj).map((key) => {
		const newKey = newKeys[key] || key
		return { [newKey]: obj[key] }
	})
	return Object.assign({}, ...keyValues)
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
.custom-select .selected.inactive {
	color: #999;
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
