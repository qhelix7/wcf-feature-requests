<template>
  <div id="request-list" class="col-4 card px-0">
    <div class="card-body p-2">
      <template v-if="requests.length > 0">
        <ul class="list-group">
          <li
            v-for="request in requests"
            v-bind:key="request.id"
            class="list-group-item"
            v-bind:class="{ 'active' : isSelected(request) }"
            @click="selectRequest(request)"
          >
            {{ request.title }}
          </li>
        </ul>
      </template>
      <template v-else>
        <p class="text-center">No feature requests!</p>
      </template>
      <div class="d-flex justify-content-end mt-4">
        <button
          id="add-request-button"
          type="button"
          class="btn btn-success rounded-circle align-middle p-0"
          @click="requestFeature"
        >
          +
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import FeatureRequest from '@/types/index';

export default Vue.extend({
  name: 'RequestList',
  props: {
    requests: {
      type: Array as () => FeatureRequest[],
      default: () => [],
    },
    selected: {
      type: Object as () => FeatureRequest,
      default: () => undefined as undefined | FeatureRequest,
    },
  },
  methods: {
    isSelected(request: FeatureRequest) {
      if (this.selected) {
        return request.id === this.selected.id;
      } else {
        return false;
      }
    },
    selectRequest(request: FeatureRequest) {
      this.$emit('selectRequest', request);
    },
    requestFeature(event: Event) {
      this.$emit('newFeatureRequest', null);
    },
  },
});
</script>

<style lang="scss">
#request-list {
    background-color: #fffff4;
}
#add-request-button {
    font-size: 1.7rem;
    width: 2.5rem;
    height: 2.5rem;
    text-align: center;
    position: relative;
    bottom: 0.2rem;
}
</style>
