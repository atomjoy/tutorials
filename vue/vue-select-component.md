# Select component
Vue select komponent z input dla FormData z formularza form.

## Vue 3 with setup
- <https://github.com/atomjoy/tutorials/blob/main/vue/components/input/CustomSelect3.vue>
- <https://github.com/atomjoy/tutorials/blob/main/vue/components/input/CustomSelectKeys3.vue>

## Sandbox Vue 2
- <https://codesandbox.io/s/custom-vue-js-select-component-forked-yx77kh>
- <https://codesandbox.io/s/custom-vue-js-select-component-forked-byricm>

### App Vue 2
```vue
<template>
  <div id="app">
    <h1>Custom Vue Select Component formdata</h1>
    
    <form @submit.prevent="onSubmit">
      <CustomSelect
        :name="'language'"
        :options="['go', 'python', 'rust', 'javascript']"
        :default="'go'"
        class="select"
        @input="alert($event)"
      />

      <button>Submit</button>
    </form>
  </div>
</template>

<script>
import CustomSelect from "./components/CustomSelect.vue";

export default {
  components: {
    CustomSelect,
  },
  methods: {
    onSubmit: (e) => {
      let data = new FormData(e.target);
      for (var pair of data.entries()) {
        console.log("Key", pair[0], "Value",  pair[1]);
      }
    },
    alert: (e) => {
      console.log(e);
    },
  },
};
</script>

<style lang="scss">
*,
*::before,
*::after {
  box-sizing: border-box;
}

#app {
  max-width: 400px;
  margin: 0 auto;
  line-height: 1.4;
  font-family: Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

h1 {
  text-align: center;
}
</style>
```

### CustomSelect.vue
```
<template>
  <div class="custom-select" :tabindex="tabindex" @blur="open = false">
    <div class="selected" :class="{ open: open }" @click="open = !open">
      {{ selected }}
    </div>
    <div class="items" :class="{ selectHide: !open }">
      <div
        v-for="(option, i) of options"
        :key="i"
        @click="
          selected = option;
          open = false;
          $emit('input', option);
        "
      >
        {{ option }}
      </div>
    </div>

    <input type="hidden" :name="name" v-model="selected" />
  </div>
</template>

<script>
export default {
  props: {
    options: {
      type: Array,
      required: true,
    },
    default: {
      type: String,
      required: false,
      default: null,
    },
    tabindex: {
      type: Number,
      required: false,
      default: 0,
    },
    name: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      selected: this.default
        ? this.default
        : this.options.length > 0
        ? this.options[0]
        : null,
      open: false,
    };
  },
  mounted() {
    this.$emit("input", this.selected);
  },
};
</script>

<style scoped>
.custom-select {
  position: relative;
  width: 100%;
  text-align: left;
  outline: none;
  height: 50px;
  line-height: 50px;
}

.custom-select .selected {
  background-color: #ffffff;
  border-radius: 6px;
  border: 1px solid #666666;
  color: #111;
  padding-left: 1em;
  cursor: pointer;
  user-select: none;
}

.custom-select .selected.open {
  border: 1px solid #0075ff;
  border-radius: 6px 6px 0px 0px;
}

.custom-select .selected:after {
  position: absolute;
  content: "";
  top: 22px;
  right: 1em;
  width: 0;
  height: 0;
  border: 5px solid transparent;
  border-color: #fff transparent transparent transparent;
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
}

.custom-select .items div:hover {
  color: #fff;
  background-color: #0075ff;
}

.selectHide {
  display: none;
}
</style>
```
