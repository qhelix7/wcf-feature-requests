<template>
  <div id="request-list" class="col-4 card px-0">
    <div class="card-body p-2">
      <ul class="list-group">
        <li v-for="request in requests" v-bind:key="request.id"
          class="list-group-item"
        >
          {{ request.title }}
        </li>
      </ul>
      <div class="d-flex justify-content-end mt-4">
        <button
          id="add-request-button"
          type="button"
          class="btn btn-success rounded-circle align-middle p-0"
        >
          +
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'RequestList',
  data() {
    return {
      yo: 'YO!',
      requests: [
        {id: 1, title: 'Feature 1'},
        {id: 2, title: 'Feature 2'},
        {id: 3, title: 'Feature 3'},
        {id: 4, title: 'Feature 4'},
      ],
    };
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
