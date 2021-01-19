<template>
  <div class="dashboard-container">
    <station-table />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import StationTable from '@/components/StationTable'
export default {
  name: 'Dashboard',
  components: { StationTable },
  computed: {
    ...mapGetters([
      'name'
    ])
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    padding: 10px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
