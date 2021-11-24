<template>
  <a-list item-layout="horizontal" :data-source="planList">
    <template v-slot:renderItem="{ item }">
      <a-list-item>
        <a-list-item-meta :description="`耗时${item.time}h`">
          <template v-slot:title>
            <div>{{ item.content }}</div>
            <span>{{ formatDate(item.date) }}</span>
          </template>
        </a-list-item-meta>
        <template v-slot:actions>
          <a @click="deletePlan(item)">完成</a>
        </template>
      </a-list-item>
    </template>
  </a-list>
</template>
<script>
import { reactive, toRefs, ref, onMounted } from 'vue'
import moment from 'moment'
import { useStore } from 'vuex'
export default {
  setup(props, context) {
    console.log('setup', props, context)
    const store = useStore()
    const state = reactive({
      planList: store.state.planList // planList 取的是store中默认值
    })
    onMounted(() => {
      console.log('onMounted')
    })
    const formatDate = date => {
      return moment(date).format('YYYY-MM-DD HH:mm:ss')
    }
    const deletePlan = item => {
      console.log('删除', item)
    }
    return {
      ...toRefs(store.state),
      formatDate,
      deletePlan
    }
  },
  created() {
    console.log('create')
  },
  mounted() {
    console.log('mounted')
  }
}
</script>
