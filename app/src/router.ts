import Vue from 'vue';
import Router from 'vue-router';
import FeatureRequests from './views/FeatureRequests.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'feature-requests',
      component: FeatureRequests,
    },
  ],
});
