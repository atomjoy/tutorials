<!--
  <PrefixSelect label="Prefix" :selected="48" name="prefix" />
-->

<script setup>
import prefix from './json/country.json' // array with object [{prefix: "48"}, {prefix: "47"}]

const props = defineProps({
	label: { type: String, default: 'Prefix code' },
	name: { type: String, default: 'prefix', required: true },
	selected: { type: Number, default: 48 },
	class: String,
})

function check(i) {
	if (parseInt(i.prefix) == props.selected) {
		return true
	}
	return false
}

// Sort array of objects
function compare(a, b) {
	if (parseInt(a.prefix) < parseInt(b.prefix)) {
		return -1
	}
	if (parseInt(a.prefix) > parseInt(b.prefix)) {
		return 1
	}
	return 0
}
// Sort objects by prefix
// prefix.sort(compare)
// Get prefix codes array (numbers)
// const unique = [...new Set(prefix.map((item) => item.prefix))]
// Sort prefix codes array
// const codes = unique.sort((a, b) => parseInt(a) - parseInt(b))
</script>

<template>
	<label>{{ props.label }}</label>
	<select :name="props.name" class="remove-arrow" :class="class">
		<option v-for="i of prefix" value="i" :selected="check(i)">{{ i.name }} {{ i.emoji }} +{{ i.prefix }}</option>
	</select>
</template>

<style scoped>
option {
	font-size: 14px;
	font-weight: 400;
}
.remove-arrow {
	appearance: none;
	-moz-appearance: none;
	-webkit-appearance: none;
}

.remove-arrow::-ms-expand {
	display: none;
}
</style>
