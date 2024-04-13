import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '../components/LoginPage.vue';
import RegisterPage from '../components/RegisterPage.vue';
import ImpactCalculator from '../components/ImpactCalculator.vue';
import ChallengeCenter from '../components/ChallengeCenter.vue';



const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', name: 'LoginPage',component: LoginPage },
  { path: '/register', name: 'RegisterPage', component: RegisterPage },
  { path: '/calculator', name: 'ImpactCalculator', component: ImpactCalculator },
  { path: '/gamification', name: 'ChallengeCenter', component: ChallengeCenter },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
