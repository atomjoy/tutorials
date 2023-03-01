### Checkbox
```vue
import Checkbox3 from './Checkbox3.vue'
const confirm_services = ref(false)

<Checkbox3 :label="$t('register.Confirm_services')" value="1" v-model="confirm_services" name="confirm_services" />
```
