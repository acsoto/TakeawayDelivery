<template>
  <div style="cursor:pointer;" @click="changeWord">{{ world }}</div>
</template>

<script>
import { reactive, toRefs } from 'vue'
export default {
  setup() {
    const data = reactive({
      world: 'Hellow world'
    })
    let changeWord = () => {
      data.world == 'Hellow world'
        ? (data.world = 'get out of the world')
        : (data.world = 'Hellow world111')
    }
    return {
      changeWord,
      ...toRefs(data)
    }
  },
  components: {}
}
</script>

<style></style>
