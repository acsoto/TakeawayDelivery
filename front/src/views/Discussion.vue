<template>
  <div>
    <a-breadcrumb style="margin: 16px 0">
      <a-breadcrumb-item>讨论区</a-breadcrumb-item>
      <a-breadcrumb-item>菜品贴</a-breadcrumb-item>
    </a-breadcrumb>
    <div :style="{ padding: '24px', background: '#fff', minHeight: '550px' }">
      <template>
        <a-list
          item-layout="horizontal"
          :data-source="data"
        >
          <template #renderItem="{ item }">
            <a-list-item>
              <a-list-item-meta description="Ant Design, a design language for background applications, is refined by Ant UED Team">
                <template #title>
                  <a href="https://www.antdv.com/">{{ item.title }}</a>
                </template>
                <template #avatar>
                  <a-avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" />
                </template>
              </a-list-item-meta>
            </a-list-item>
          </template>
        </a-list>
      </template>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
const data = [{
  title: 'Ant Design Title 1',
}, {
  title: 'Ant Design Title 2',
}, {
  title: 'Ant Design Title 3',
}, {
  title: 'Ant Design Title 4',
}];
export default defineComponent({
  setup() {
    return {
      data,
      collapsed: true,
    };
  },

});
</script>

<style>
#components-layout-demo-side .logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px;
}
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}
</style>
