<!--测试文件，无用-->
<template>
  <div class="icons-list">
    <HomeOutlined />
    <SettingFilled />
    <SmileOutlined />
    <SyncOutlined spin />
    <SmileOutlined :rotate="180" />
    <LoadingOutlined />
  </div>
</template>
<script>
import { defineComponent } from 'vue';
import { HomeOutlined, SettingFilled, SmileOutlined, SyncOutlined, LoadingOutlined } from '@ant-design/icons-vue';
export default defineComponent({
  components: {
    HomeOutlined,
    SettingFilled,
    SmileOutlined,
    SyncOutlined,
    LoadingOutlined,
  },
});
</script>
<style scoped>
.icons-list :deep(.anticon) {
  margin-right: 6px;
  font-size: 24px;
}
</style>
