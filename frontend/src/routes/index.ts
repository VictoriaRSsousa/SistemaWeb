import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/home.vue';
import sobre from '../views/sobre.vue';
import adicionarConta from '../views/adicionarConta.vue';
import atualizarConta from '../views/atualizarConta.vue';
import listarContas from '../views/listarContas.vue';
import detalharConta from '../views/detalharConta.vue';


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
    path: '/atualizarConta/:id',
    component: atualizarConta,
    name: 'atualizarConta',
  },
  {
    path: '/detalhesConta/:id',
    component: detalharConta,
    name: 'detalharConta',
  }
];

// Adicionar rota credor
 
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
