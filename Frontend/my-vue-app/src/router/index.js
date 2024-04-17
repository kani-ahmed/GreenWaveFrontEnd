// router/index.js

import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '../components/Loginpage.vue';
import RegisterPage from '../components/RegisterPage.vue';
import ImpactCalculator from '../components/ImpactCalculator.vue';
import ChallengeCenter from '../components/ChallengeCenter.vue';
import store from '../store';
import UserProfile from "../components/UserProfile.vue";
import SendChallenge from "../components/SendChallenge.vue";
//import ChallengeInbox from "../components/ChallengeInbox.vue";
//import UserProfile from "../components/UserProfile.vue";
import SocialMedia from "../components/SocialMedia.vue";
//import EcoPoints from "../components/EcoPoints.vue";

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', name: 'LoginPage', component: LoginPage },
  { path: '/register', name: 'RegisterPage', component: RegisterPage },
  {
    path: '/calculator',
    name: 'ImpactCalculator',
    component: ImpactCalculator,
    meta: { requiresAuth: true }
  },
  {
    path: '/sendchallenge',
    name: 'SendChallenge',
    component: SendChallenge,
    meta: { requiresAuth: true }
  },
  {
    path: '/gamification',
    name: 'ChallengeCenter',
    component: ChallengeCenter,
    meta: { requiresAuth: true }
  },
    {
        path: '/profile',
        name: 'UserProfile',
        component: UserProfile,
        meta: { requiresAuth: true }
  },
  {
    path: '/socialmedia',
    name: 'SocialMedia',
    component: SocialMedia,
    meta: { requiresAuth: true }
  }, 
    
  
    
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  const currentUser = store.getters.currentUser;

  if (requiresAuth && !currentUser) {
    next('/login');
  } else {
    next();
  }
});

export default router;