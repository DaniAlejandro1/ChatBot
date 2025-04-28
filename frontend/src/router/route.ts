import { createWebHistory, createRouter } from 'vue-router';

import ChatView from '@/page/ChatView.vue';
import HomeView from '@/page/HomeView.vue';

const routes = [
   { path: '/', redirect: '/home' },
   { path: '/home', name: 'home', component: HomeView },
   { path: '/chat/:index', name: 'chat', component: ChatView},
];

const router = createRouter({
   history: createWebHistory(),
   routes,
});

export default router;
