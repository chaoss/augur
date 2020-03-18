import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../layouts/Login/Login.vue';
import Dashboard from '../layouts/Dashboard/Dashboard.vue';
import ManageRepos from '../layouts/ManageRepos/ManageRepos.vue';
// import AnalyzeRepos from '../components/Dashboard/AnalyzeRepos/AnalyzeRepos.vue';
import AboutAugur from '../layouts/AboutAugur/AboutAugur.vue';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'login',
    component: Login
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: Dashboard, 
    children: [
      {
        path: 'manage', 
        component: ManageRepos
      }, 
      // {
      //   path: 'analyze', 
      //   component: AnalyzeRepos
      // }, 
      {
        path: 'about', 
        component: AboutAugur
      }
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
