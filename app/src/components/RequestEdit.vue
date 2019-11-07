<template>
  <div class="request-edit card col-8">
    <div v-if="internalRequest" class="card-body">
      <div class="form-group">
        <label for="requestTitle">Title</label>
        <input
          id="requestTitle"
          type="text"
          class="form-control"
          placeholder="Title"
          v-model="internalRequest.title"
        >
      </div>

      <div class="form-group" v-if="clients">
        <label for="requestClient">Client</label>
        <select id="requestClient" class="form-control" v-model="internalRequest.client">
          <option disabled value="">Select a client</option>
          <option v-for="client in clients" :value="client">{{ client.name }}</option>
        </select>
      </div>

      <div class="form-group">
        <label for="requestCreatedAt">Request Date</label>
        <input
          id="requestCreatedAt"
          type="text"
          class="form-control"
          placeholder="year-month-day"
          v-model="internalRequest.created_at"
        >
      </div>

      <div class="form-group">
        <label for="requestPriority">Priority</label>
        <select id="requestPriority" class="form-control" v-model="internalRequest.priority">
          <option>Undetermined</option>
          <option>Critical</option>
          <option>High</option>
          <option>Medium</option>
          <option>Low</option>
        </select>
      </div>

      <div class="form-group">
        <label for="requestTargetDate">Target Date</label>
        <input
          id="requestTargetDate"
          type="text"
          class="form-control"
          placeholder="year-month-day"
          v-model="internalRequest.target_date"
        >
      </div>

      <div class="form-group">
        <label for="requestDescription">Description</label>
        <textarea class="form-control" id="requestDescription" rows="5"></textarea>
      </div>

      <button type="button" class="btn btn-primary" @click="save">Save</button>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import FeatureRequest from '@/types/index';
import { Client } from '@/types/index';
import { Priority } from '@/types/index';

function blankRequest() {
    const req: FeatureRequest = {
        title: '',
        description: '',
        client: {id: -1, name: ''},
        priority: Priority.Low,
        target_date: '',
    };
    return req;
}

export default Vue.extend({
  name: 'RequestEdit',
  data() {
      return {
        internalRequest: blankRequest(),
      };
  },
  props: {
    // The original request
    request: {
      type: Object as () => FeatureRequest,
      default: blankRequest,
    },
    clients: {
      type: Array as () => Client[],
      default: [],
    },
  },
  watch: {
    request() {
      // copy original request to internalRequest
      if (!this.request) {
        this.internalRequest = blankRequest();
      } else {
        this.internalRequest = Object.assign({}, this.request);
      }
    },
  },
  methods: {
    save(): any {
      this.$emit('postRequest', this.internalRequest);
    },
  },
});
</script>

<style lang="scss">
.request-edit {
  background: linear-gradient(180deg, rgba(226,255,266,1) 0%, rgba(255,255,255,1) 100%);
}
</style>
