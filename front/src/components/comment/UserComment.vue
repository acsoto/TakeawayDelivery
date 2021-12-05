<template>
  <div class="background">
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
        <p>
          {{ thisComment.evaluateText }}
        </p>
      </template>
      <template #datetime>
        <div>
          <a-rate
            style="margin-right:10px;font-size:15px;"
            :default-value=" thisComment.evaluateScore"
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
import { defineComponent } from 'vue';
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
    handleDelete() {

    },
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
  }
}

@media screen and (max-width: 1200px) {
  .background {
    margin: 20px auto;
    background: rgb(255, 255, 255, 0.9);
    box-shadow: 1px 1px 7px #adadad, -1px -1px 7px #ffffff;
    border-radius: 10px;
    padding: 20px;
    width: 100%;
  }
}
</style>
