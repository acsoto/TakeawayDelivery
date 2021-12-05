 <template>
  <a-card
    hoverable
    style="width:154px;height:250px;margin:10px;text-align:center;align:center;border-radius: 10px;"
    @click="$router.push({ path: '/home/food',
            query: {
              foodID: food.foodID,
            },});"
  >
    <template
      #cover
      style="width:150px;height:150px;"
    >
      <img
        alt="example"
        :src="food.foodUrl"
        style="width:150px;height:150px;margin:0px;border-radius: 10px;"
      />
    </template>
    <a-card-meta :title="food.foodName">
      <template #description>{{food.foodPrice}}</template>
    </a-card-meta>
  </a-card>
</template>


<script>
export default {
  props: ['food'],
  data() {
    return {
    };
  },
  created() {

  },
  methods: {},
  watch: {

  },
}
</script>

<style scoped>
</style>