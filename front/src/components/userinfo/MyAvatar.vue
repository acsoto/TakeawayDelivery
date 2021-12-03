<template>
  <div>
    <a-avatar
      style="color: #f56a00; backgroundColor: #fde3cf"
      :size="size"
      v-if="user.userIconUrl==''"
    >
      {{$store.state.username}}
    </a-avatar>
    <a-avatar
      :size="size"
      :src="user.userIconUrl"
      v-else
      alt="无法加载"
    />
  </div>
</template>

<script>

export default {
  name: "NewLogin",
  props: ['user'],
  data() {
    return {
      size: 200,
    };
  },
}
</script>

<style scoped>
</style>
