<template>
  <div class="feature-requests">
    <RequestsDisplay/>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import RequestsDisplay from '@/components/RequestsDisplay.vue';

export default Vue.extend({
  name: 'FeatureRequests',
  components: {
    RequestsDisplay,
  },
});
</script>
