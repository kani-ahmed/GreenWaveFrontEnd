import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '../components/Loginpage.vue';
import RegisterPage from '../components/RegisterPage.vue';
import ImpactCalculator from '../components/ImpactCalculator.vue';

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: LoginPage },
  { path: '/register', component: RegisterPage },
  { path: '/calculator', component: ImpactCalculator },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
