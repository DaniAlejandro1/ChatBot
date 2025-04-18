import { createApp } from 'vue';
import { createPinia } from 'pinia';
import router from './router/route.ts';
import App from './App.vue';
import '@/assets/index.css';

createApp(App).use(router).use(createPinia()).mount('#root');
