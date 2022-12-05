# Vue slots

## Jak pobrać dane przekazane do slotu

### Create Select.vue
```vue
<template>
  <select>
    <slot />
  </select>
</template>

<script>
export default {
  mounted() {
    // Multiple slots this.$slots.slotProps
    const options = this.$slots.default.filter((node) => node.tag === "option");

    for (const opt of options) {
      const innerText = opt.children.map((c) => c.text).join();
      const value = opt.data.attrs.value;
      console.log({ innerText, value });
    }
  },
};
</script>
```

### Utwórz App.vue
```vue
<template>
  <div id="app">
    <custom-select>
      <option value="value 1">Option 1</option>
      <option value="value 2">Option 2</option>
      <option value="value 3">Option 3</option>
      <option value="value 4">Option 4</option>
    </custom-select>
  </div>
</template>

<script>
import CustomSelect from "./components/CustomSelect";

export default {
  name: "App",
  components: {
    CustomSelect,
  },
};
</script>

<style>
#app {
  font-size: 16px;
  padding: 20px
}
</style>
```

## Named Scoped Slots 

### Przykład listy z komponentu
ListView.vue
```vue
<FancyList :api-url="url" :per-page="10">
  <template #item="{ body, username, likes }">
    <div class="item">
      <p>{{ body }}</p>
      <p>by {{ username }} | {{ likes }} likes</p>
    </div>
  </template>
</FancyList>
```

### Fancy list komponent
FancyList.vue
```vue
//...
<template>
  <h1>List</h1>
  <ul>
    <li v-for="item in items">
      <slot name="item" v-bind="item"></slot>
      <!-- 
        <slot v-slot:name="item"></slot>
        <slot #item="item"></slot> 
      -->
    </li>
  </ul>
</template>
//...
```
