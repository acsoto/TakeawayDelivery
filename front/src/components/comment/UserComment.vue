<template>
  <div>
    <a-comment
      :author="thisComment.userNickName"
      :avatar="thisComment.userIconUrl"
    >
      <template #actions>
        <a-popconfirm
          title="您确认要删除自己的评论吗？删除了之后您还可以重新发评论"
          ok-text="确认"
          cancel-text="取消"
          @confirm="handleDelete"
          v-if="thisComment.userID==this.$store.state.userID"
        >
          <span>删除</span>
        </a-popconfirm>
      </template>
      <template #content>
        <p v-if="commented==true">
          {{ thisComment.evaluateText }}
        </p>
        <p v-else>
          该用户未留下评价
        </p>
      </template>
      <template #datetime>
        <div>
          <a-rate
            style="margin-right:10px;font-size:15px;"
            v-model:value=" thisComment.evaluateScore"
            disabled
          />
          <span>{{ thisComment.evaluateDate }}</span>
        </div>
      </template>
    </a-comment>
  </div>
</template>
<script>
import dayjs from 'dayjs';
import relativeTime from 'dayjs/plugin/relativeTime';
dayjs.extend(relativeTime);
export default {
  props: ['comment'],
  data() {
    return {
      collapsed: true,
      thisComment: this.comment,
      commented: this.comment.evaluateText.trim().length > 0,
    };
  },
  methods: {
    handleDelete() {
      this.$emit('handleDelete', this.thisComment);
    },
  },
};
</script>

<style>
</style>
