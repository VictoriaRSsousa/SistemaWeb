import { createRouter, createWebHistory } from 'vue-router';
import listarContas from '../views/listarContas.vue';
import adicionarConta from '../views/adicionarconta.vue';
import Home from '../views/home.vue';
import sobre from '../views/sobre.vue';
const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: Home,  
      name: 'Home',
    },
    {
      path: '/listarContas',
      component: listarContas,
      name: 'listarContas',
    },
    {
      path: '/sobre',
      component: sobre,
      name: 'sobre',
    },
    {
      path: '/adicionarConta',
      component: adicionarConta,
      name: adicionarConta,
    }
  ],
});

export default router;