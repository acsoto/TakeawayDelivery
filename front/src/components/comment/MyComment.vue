<template>
  <div class="background">
    <a-comment
      :author="thisComment.userNickName"
      :avatar="thisComment.userIconUrl"
    >
      <template #actions>
        <a-popconfirm
          title="您确认要发布评论嘛"
          ok-text="确认"
          cancel-text="取消"
          @confirm="handleEvaluate"
        >
          <a-button type="primary">
            发布评论
          </a-button>
        </a-popconfirm>
      </template>
      <template #content>
        <a-textarea
          v-model:value="thisComment.evaluateText "
          placeholder="请输入您的评价"
          :rows="4"
          :cols="160"
          allow-clear
        />
      </template>
      <template #datetime>
        <div style="margin-top:-4px;">您的评分：
          <a-rate
            style="margin-right:10px;"
            v-model:value="thisComment.evaluateScore"
          />
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
    };
  },
  methods: {
    handleEvaluate() {
      if (!this.thisComment.evaluateScore) return this.$message.error("请选择分数");
      this.$emit('handleEvaluate', this.thisComment);
    },
  },
  watch: {
    comment() {
      this.thisComment = this.comment;
    }
  },
};
</script>

<style>
@media screen and (min-width: 1201px) {
  .background {
    margin: 20px auto;
    background: rgb(255, 255, 255, 0.9);
    box-shadow: 1px 1px 7px #adadad, -1px -1px 7px #ffffff;
    border-radius: 10px;
    padding: 20px;
    width: 80%;
    overflow: auto;
  }
}

@media screen and (max-width: 1200px) {
  .background {
    margin: 20px auto;
    background: rgb(255, 255, 255, 0.9);
    box-shadow: 1px 1px 7px #adadad, -1px -1px 7px #ffffff;
    border-radius: 10px;
    padding: 20px;
    width: 99%;
    overflow: auto;
  }
}
</style>
