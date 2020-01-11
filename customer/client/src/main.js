/*
 * @Description:
 * @Author: superz
 * @Date: 2020-01-11 14:56:35
 * @LastEditTime : 2020-01-11 21:06:35
 */
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
// 插入Bootstrap样式
import 'bootstrap/dist/css/bootstrap.css'
import BootstrapVue from 'bootstrap-vue'
import Vue from 'vue'
import App from './App'
import router from './router'

Vue.config.productionTip = false

Vue.use(BootstrapVue)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
