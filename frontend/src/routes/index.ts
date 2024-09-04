import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/home.vue';
import sobre from '../views/sobre.vue';
import adicionarConta from '../views/adicionarConta.vue';
import atualizarConta from '../views/atualizarConta.vue';
import listarContas from '../views/listarContas.vue';
import listarCredores from '../views/listarCredores.vue';
import adicionarCredor from '../views/adicionarCredor.vue';
import atualizarCredor from '../views/atualizarCredor.vue';
//Rotas ...
const routes = [
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
    name: 'adicionarConta',
  },
  {
    path: '/atualizarConta',
    component: atualizarConta,
    name: 'atualizarConta'
  },
  {
    path: '/listarCredores',
    component: listarCredores,
    name: 'listarCredores'
  },
  {
    path: '/adicionarCredor',
    component: adicionarCredor,
    name: 'adicionarCredor'
  },
  {
    path: '/atualizarCredor',
    component: atualizarCredor,
    name: 'atualizarCredor'
  }
];

// Adicionar rota credor
 
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
