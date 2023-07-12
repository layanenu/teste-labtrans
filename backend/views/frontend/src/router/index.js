import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Upload from '../views/Upload.vue';
import Download from '../views/Download.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/upload',
    name: 'Upload',
    component: Upload,
  },
  {
    path: '/download',
    name: 'Download',
    component: Download,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
