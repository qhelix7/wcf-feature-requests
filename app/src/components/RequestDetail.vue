<template>
  <div class="request-detail card col-8">
    <div class="card-body" v-if="request">
      <div class="d-flex justify-content-between">
        <h4 class="card-title">{{ request.title }}</h4>
      </div>
      <h6 class="card-subtitle text-muted">From {{ request.client }} {{ request.created_at }}</h6>
      <div class="request-priority mb-4">
        <div class="badge badge-pill badge-primary">{{ request.priority }}</div>
        <div>Target Date: {{ request.target_date }}</div>
      </div>

      <p class="card-text">{{ request.description }}</p>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import FeatureRequest from '@/types/index';

export default Vue.extend({
  name: 'RequestDetail',
  props: {
    request: {
      type: Object as () => FeatureRequest,
      default: () => null,
    },
  },
});
</script>

<style lang="scss">
.request-detail {
  background: linear-gradient(180deg, rgba(226,248,255,1) 0%, rgba(255,255,255,1) 100%);
}
.request-due {
  white-space: nowrap;
  color: #06a;
}
.request-detail .card-subtitle {
  font-size: 0.9rem;
}
.request-priority {
  text-align: right;
}
</style>
