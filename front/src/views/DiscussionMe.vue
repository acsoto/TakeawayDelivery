<template>
  <div>
    <a-layout-header style="background: #fff; padding: 0">
    </a-layout-header>
    <a-layout-content style="margin: 0 16px">
      <a-breadcrumb style="margin: 16px 0">
        <a-breadcrumb-item>讨论区</a-breadcrumb-item>
        <a-breadcrumb-item>与我有关的</a-breadcrumb-item>
      </a-breadcrumb>
      <div :style="{ padding: '24px', background: '#fff', minHeight: '550px' }">
<a-comment
                :author="item.author"
                :avatar="item.avatar"
              >
                <template #actions>
                  <a-popconfirm
                    title="您确认要删除自己的评论吗？删除了之后您还可以重新发评论"
                    ok-text="确认"
                    cancel-text="取消"
                    @confirm="handleDelete"
                  >
                    <span>删除</span>
                  </a-popconfirm>
                </template>
                <template #content>
                  <p>
                    {{ item.content }}
                  </p>
                </template>
                <template #datetime>
                  <div>
                    <a-rate
                      style="margin-right:10px;font-size:15px;"
                      :default-value="3"
                      disabled
                    />
                    <a-tooltip :title="item.datetime.format('YYYY-MM-DD HH:mm:ss')">
                      <span>{{ item.datetime.fromNow() }}</span>
                    </a-tooltip>
                  </div>
                </template>
              </a-comment>
        <a-list
          class="comment-list"
          :header="`${data.length} replies`"
          item-layout="horizontal"
          :data-source="data"
        >
          <template #renderItem="{ item }">
            <a-list-item>
              <a-comment
                :author="item.author"
                :avatar="item.avatar"
              >
                <template #actions>
                  <a-popconfirm
                    title="您确认要删除自己的评论吗？删除了之后您还可以重新发评论"
                    ok-text="确认"
                    cancel-text="取消"
                    @confirm="handleDelete"
                  >
                    <span>删除</span>
                  </a-popconfirm>
                </template>
                <template #content>
                  <p>
                    {{ item.content }}
                  </p>
                </template>
                <template #datetime>
                  <div>
                    <a-rate
                      style="margin-right:10px;font-size:15px;"
                      :default-value="3"
                      disabled
                    />
                    <a-tooltip :title="item.datetime.format('YYYY-MM-DD HH:mm:ss')">
                      <span>{{ item.datetime.fromNow() }}</span>
                    </a-tooltip>
                  </div>
                </template>
              </a-comment>
            </a-list-item>
          </template>
        </a-list>
      </div>
    </a-layout-content>
    <a-layout-footer style="text-align: center">
      <!--        Ant Design ©2018 Created by Ant UED-->
      ©For the King of Alxa
    </a-layout-footer>
  </div>
</template>
<script>
import dayjs from 'dayjs';
import { defineComponent } from 'vue';
import relativeTime from 'dayjs/plugin/relativeTime';
dayjs.extend(relativeTime);
export default defineComponent({
  data() {
    return {
      collapsed: true,
item:{ actions: ['Reply to'],
        author: 'Han Solo',
        avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
        content: 'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
        datetime: dayjs().subtract(1, 'days'),}
    };
  },
  methods: {
  },
  setup() {
    return {
      data: [{
        actions: ['Reply to'],
        author: 'Han Solo',
        avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
        content: 'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
        datetime: dayjs().subtract(1, 'days'),
      }, {
        actions: ['Reply to'],
        author: 'Han Solo',
        avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
        content: 'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
        datetime: dayjs().subtract(2, 'days'),
      }, {
        actions: ['Reply to'],
        author: 'Han Solo',
        avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
        content: 'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
        datetime: dayjs().subtract(2, 'days'),
      }
      ],
      dayjs,
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
