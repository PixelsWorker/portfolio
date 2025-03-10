import { createRouter, createWebHistory } from 'vue-router'
import Home from '../App.vue'
import About from '../About.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/about', name: 'About', component: About }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
