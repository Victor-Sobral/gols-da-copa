import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../pages/HomePage.vue'),
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../pages/AboutView.vue'),
    },
    {
      path: '/sixteenFinal',
      name: 'sixteenFinal',
      component: () => import('../pages/SixteenFinal.vue'),
    },
    {
      path: '/eightFinal',
      name: 'eightFinal',
      component: () => import('../pages/EightFinal.vue'),
    },
    {
      path: '/fourFinal',
      name: 'fourFinal',
      component: () => import('../pages/FourFinal.vue'),
    },
    {
      path: '/semiFinal',
      name: 'semiFinal',
      component: () => import('../pages/SemiFinal.vue'),
    },
    {
      path: '/final',
      name: 'final',
      component: () => import('../pages/Final.vue'),
    },
  ],
})

export default router
