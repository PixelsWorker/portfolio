// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../page/HomePage.vue' // Create this new component
import About from '../page/AboutPage.vue'


const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/about', name: 'About', component: About },
  // Redirect any unmatched routes to home
  { path: '/:pathMatch(.*)*', redirect: '/' }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router