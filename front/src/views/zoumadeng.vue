<template>
  <div style="padding: 50px">
    <a-badge count="5">
      <a href="#" class="head-example" />
    </a-badge>
    <a-badge count="0" show-zero>
      <a href="#" class="head-example" />
    </a-badge>
    <a-badge>
      <template #count>
        <clock-circle-outlined style="color: #f5222d" />
      </template>
      <a href="#" class="head-example"></a>
    </a-badge>
  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import { ClockCircleOutlined } from '@ant-design/icons-vue';
export default defineComponent({
  components: {
    ClockCircleOutlined,
  },
});
</script>
