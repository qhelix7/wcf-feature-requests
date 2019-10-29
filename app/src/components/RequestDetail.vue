<template>
  <div class="request-detail card col-8">
    <div class="card-body">
      <div class="d-flex justify-content-between">
        <h4 class="card-title">Some cool new feature too long title</h4>
      </div>
      <h6 class="card-subtitle text-muted">From Client A on 2019-04-01</h6>
      <div class="request-priority mb-4">
        <div class="badge badge-pill badge-primary">Critical</div>
        <div>Target Date: 2019-11-30</div>
      </div>

      <p class="card-text">
          Detailed description of all the stuff the client would like
          implemented in the product.
      </p>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'RequestDetail',
  props: {
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
