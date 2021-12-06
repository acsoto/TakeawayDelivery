<template>
  <div>
    <div :style="{ padding: '24px', background: '#fff', minHeight: '550px' }">
      <a-list
        v-if="comments.length"
        :data-source="comments"
        :header="`${comments.length} ${comments.length > 1 ? 'replies' : 'reply'}`"
        item-layout="horizontal"
      >
        <template #renderItem="{ item }">
          <a-list-item>
            <a-comment
              :author="item.author"
              :avatar="item.avatar"
              :content="item.content"
              :datetime="item.datetime"
            />
          </a-list-item>
        </template>
      </a-list>
      <a-comment>
        <template #avatar>
          <a-avatar
            src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
            alt="Han Solo"
          />
        </template>
        <template #content>
          <a-form-item>
            <a-textarea
              v-model:value="value"
              placeholder="Your Comment"
              :rows="4"
              :cols="160"
              allow-clear
            />
          </a-form-item>
          <a-form-item>
            <a-button
              html-type="submit"
              :loading="submitting"
              type="primary"
              @click="handleSubmit"
            >
              Add Comment
            </a-button>
          </a-form-item>
        </template>
      </a-comment>
    </div>
  </div>
</template>
<script>
import { defineComponent, ref } from 'vue';
import dayjs from 'dayjs';
import relativeTime from 'dayjs/plugin/relativeTime';
dayjs.extend(relativeTime);
export default defineComponent({
  setup() {
    const comments = ref([]);
    const submitting = ref(false);
    const value = ref('');

    const handleSubmit = () => {
      if (!value.value) {
        return;
      }

      submitting.value = true;
      setTimeout(() => {
        submitting.value = false;
        comments.value = [{
          author: 'Han Solo',
          avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
          content: value.value,
          datetime: dayjs().fromNow(),
        }, ...comments.value];
        value.value = '';
      }, 1000);
    };

    return {
      comments,
      submitting,
      value,
      handleSubmit,
    };
  },
  data() {
    return {
      collapsed: true,
    };
  },
  methods: {
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

.comments {
  width: 100%; /*自动适应父布局宽度*/
  overflow: auto;
  word-break: break-all;
  /*在ie中解决断行问题(防止自动变为在一行显示，主要解决ie兼容问题，ie8中当设宽度为100%时，文本域类容超过一行时，
  当我们双击文本内容就会自动变为一行显示，所以只能用ie的专有断行属性“word-break或word-wrap”控制其断行)*/
}
</style>
