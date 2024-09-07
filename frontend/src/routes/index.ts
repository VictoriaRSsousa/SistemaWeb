import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/home.vue';
import sobre from '../views/sobre.vue';
import adicionarConta from '../views/adicionarConta.vue';
import atualizarConta from '../views/atualizarConta.vue';
import listarContas from '../views/listarContas.vue';
<<<<<<< HEAD
import detalharConta from '../views/detalharConta.vue';

=======
import listarCredores from '../views/listarCredores.vue';
import adicionarCredor from '../views/adicionarCredor.vue';
import atualizarCredor from '../views/atualizarCredor.vue';
import detalhesConta from '../views/detalhesConta.vue';
import teste from '../views/teste.vue';
>>>>>>> af560d077d6415f0865ad7bcb88838fc92d45d06

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
<<<<<<< HEAD
    name: 'atualizarConta',
  },
  {
    path: '/detalhesConta/:id',
    component: detalharConta,
    name: 'detalharConta',
=======
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
  },
  {
    path: '/detalhesConta/:id',
    component: detalhesConta,
    name: 'detalhesConta'
  },
  {
    path: '/teste',
    component: teste,
    name: 'teste'
>>>>>>> af560d077d6415f0865ad7bcb88838fc92d45d06
  }
];

// Adicionar rota credor
 
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
