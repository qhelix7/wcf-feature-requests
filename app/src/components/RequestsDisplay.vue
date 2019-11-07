<template>
  <div id="request-display" class="card">
    <div class="card-body">
      <h4 class="card-title">Feature Requests</h4>
      <div class="row">
        <RequestList 
          v-bind:requests="requests"
          v-bind:selected="selected"
          v-on:selectRequest="selectRequest"
          v-on:newFeatureRequest="newFeatureRequest"
        />
        <RequestEdit
          v-if="editing"
          v-bind:request="selected"
          v-bind:clients="clients"
          v-on:postRequest="postRequest"
        />
        <RequestDetail v-else v-bind:request="selected"/>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import axios from 'axios';
import RequestList from '@/components/RequestList.vue';
import RequestDetail from '@/components/RequestDetail.vue';
import RequestEdit from '@/components/RequestEdit.vue';
import FeatureRequest from '@/types/index';
import { Client } from '@/types/index';
import { Priority } from '@/types/index';


export default Vue.extend({
  name: 'RequestsDisplay',
  components: {
    RequestList,
    RequestDetail,
    RequestEdit,
  },
  data() {
    return {
      editing: false,
      requests: [] as FeatureRequest[],
      selected: null as FeatureRequest | null | undefined,
      clients: [] as Client[],
    };
  },
  created() {
    this.refreshClients();
    this.refreshFeatureRequests();
  },
  methods: {
    refreshClients() {
      axios.get('api/client')
      .then((response) => {
        this.clients = response.data.clients;
      })
      .catch((e) => {
        this.clients = [];
      });
    },
    refreshFeatureRequests() {
      axios.get('api/feature-request')
      .then((response) => {
        this.requests = response.data.feature_requests;
      })
      .catch((e) => {
        this.requests = [];
      });
    },
    selectRequest(request?: FeatureRequest) {
      this.editing = false;
      this.selected = request;
    },
    newFeatureRequest() {
      this.selected = null;
      this.editing = true;
    },
    postRequest(request: FeatureRequest) {
      const data: any = Object.assign({}, request);
      data.client_id = data!.client!.id;
      delete data!.client;

      axios.post('api/feature-request', data)
      .then((response) => {
        this.editing = false;
        this.refreshFeatureRequests();
        // TODO: set selected from list instead
        this.selected = response.data;
      })
      .catch((e) => {
        alert('error' + e);
      });
    },
  },
});
</script>

<style lang="scss">
</style>
