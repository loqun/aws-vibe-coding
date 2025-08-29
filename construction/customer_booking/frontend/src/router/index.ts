import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/book',
      name: 'booking-flow',
      component: () => import('../views/BookingFlowView.vue'),
      children: [
        {
          path: 'franchise',
          name: 'select-franchise',
          component: () => import('../views/FranchiseSelectionView.vue')
        },
        {
          path: 'datetime',
          name: 'select-datetime',
          component: () => import('../views/DateTimeSelectionView.vue')
        },
        {
          path: 'information',
          name: 'customer-information',
          component: () => import('../views/InformationView.vue')
        },
        {
          path: 'summary',
          name: 'booking-summary',
          component: () => import('../views/BookingSummaryView.vue')
        },
        {
          path: 'confirmation',
          name: 'booking-confirmation',
          component: () => import('../views/BookingConfirmationView.vue')
        }
      ]
    },
    {
      path: '/booking/:id',
      name: 'booking-details',
      component: () => import('../views/BookingDetailsView.vue')
    },
    {
      path: '/lookup',
      name: 'booking-lookup',
      component: () => import('../views/BookingLookupView.vue')
    }
  ]
})

export default router
