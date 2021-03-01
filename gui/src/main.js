// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
//import router from './router'
import jQuery from 'jquery'
import echarts from 'echarts'
import VueSession from 'vue-session' 
 import ViewUI from 'view-design'

 Vue.use(VueSession);
Vue.use(ViewUI);

Vue.config.productionTip = false

import router from './router/router.js'
Vue.prototype.$=jQuery;
Vue.prototype.$echarts=echarts;
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
