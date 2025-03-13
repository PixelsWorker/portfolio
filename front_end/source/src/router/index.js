import { createRouter, createWebHistory } from 'vue-router';
import Home from '../page/HomePage.vue';
import About from '../page/AboutPage.vue';
import Projects from '../page/ProjectsPage.vue';
import Contact from '../page/ContactPage.vue';

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/about', name: 'About', component: About },
  { path: '/projects', name: 'Projects', component: Projects },
  { path: '/contact', name: 'Contact', component: Contact },
  { path: '/:pathMatch(.*)*', redirect: '/' }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
