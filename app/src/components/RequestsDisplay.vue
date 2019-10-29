<template>
  <div id="request-display" class="card">
    <div class="card-body">
      <h4 class="card-title">Feature Requests</h4>
      <div class="row">
        <RequestList/>
        <RequestDetail/>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import RequestList from '@/components/RequestList.vue';
import RequestDetail from '@/components/RequestDetail.vue';

export default Vue.extend({
  name: 'RequestsDisplay',
  components: {
    RequestList,
    RequestDetail,
  },
});
</script>

<style lang="scss">
</style>
