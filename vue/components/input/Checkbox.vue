<template>
  <div class="checkbox-line">
    <input class="checkbox" type="checkbox" :checked="isChecked" :value="value" :name="name" @change="updateInput"/>
    <div class="checkmark">
      <i class="fas fa-check dot"></i>
    </div>
    <label>{{label}}</label>
  </div>
</template>

<script>
export default {
  props: {
    value: { type: String },
    name: { type: String },
    modelValue: {type: [Array, Boolean]},
    label: { type: String, required: true},
  },
  computed: {
    isChecked() {
      if (this.modelValue instanceof Array) {
        return this.modelValue.includes(this.value)
      }
      return this.modelValue == true
    }
  },
  methods: {
    updateInput(event) {
      let isChecked = event.target.checked
      if (this.modelValue instanceof Array) {
        let newValue = [...this.modelValue]
        if (isChecked) {
          newValue.push(this.value)
        } else {
          newValue.splice(newValue.indexOf(this.value), 1)
        }
        this.$emit('update:modelValue', newValue)
      } else {
        this.$emit('update:modelValue', isChecked ? true : false)
      }
    }
  }
}
</script>

<style scoped>
/* Vue round checkbox style */
.checkbox-line {
  float: left;
  width: 100%;
  margin-top: 10px;
  display: flex;
  align-items: center;
}
.checkbox-line .checkbox {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 30px;
  width: 30px;
  z-index: 9;
}
.checkbox-line .checkmark {
  position: relative;
  display: inline-block;
  width: 30px;
  height: 30px;
  margin-right: 15px;
  border: 2px solid #07f;
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
  background: #07f;
  border-radius: 50%;
  border: 2px solid #07f;
  text-align: center;
  z-index: 1;
}
.checkbox-line .checkbox:checked + .checkmark {
  border: transparent;
  box-shadow: 0px 0px 0px 5px #0077ff33;
}
.checkbox-line .checkbox:checked + .checkmark .dot {
  opacity: 1;
}
</style>

<!-- 
// Import fontawesome icon v5.10 in html head tag
<link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.10.0/css/all.css" integrity="sha384-AYmEC3Yw5cVb3ZcuHtOA93w35dYTsvhLPVnYs9eStHfGJvOvKxVfELGroGkvsg+p" crossorigin="anonymous" referrerpolicy="no-referrer" />

// Variable setup
const remember_me = ref(false)
const list = ref([])

// v-model => remember_me = true
<Checkbox :label="$t('login.Remember_me')" value="1" v-model="remember_me" name="remember_me" />

// v-model => list = ['baz1', 'baz2']
<Checkbox label="Baz1" value="baz1" v-model="list" />
<Checkbox label="Baz2" value="baz2" v-model="list" />
<Checkbox label="Baz3" value="baz3" v-model="list" /> 

// Show with
<p>Checked: {{ list }}</p>
-->
