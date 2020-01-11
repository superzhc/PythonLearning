/*
 * @Description:
 * @Author: superz
 * @Date: 2020-01-11 14:56:35
 * @LastEditTime : 2020-01-11 20:39:30
 */
import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Ping from '@/components/Ping'
import Book from '@/components/Book'

Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // }
    {
      path: '/',
      name: 'Book',
      component: Book
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping
    }
  ],
  mode: 'hash'
})
