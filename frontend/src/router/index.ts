import { createRouter, createWebHistory } from 'vue-router';

//Rotas ...
const routes = [
  {
    path: '/',
    component: ()=> import('../views/Home/home.vue'),
    name: 'Home',
  },
  {
    path: '/listarContas',
    component: ()=> import('../views/Accounts/list.vue'),
    name: 'listarContas',
  },
  {
    path: '/sobre',
    component: ()=> import('../views/About/about.vue'),
    name: 'sobre',
  },
  {
    path: '/adicionarConta',
    component: ()=> import('../views/Accounts/form.vue'),
    name: 'adicionarConta',
  },
  {
    path: '/atualizarConta/:id',
    component: ()=> import('../views/Accounts/form.vue'),
    name: 'atualizarConta'
  },
  {
    path: '/listarCredores',
    component: ()=> import('../views/Creditor/list.vue'),
    name: 'listarCredores'
  },
  {
    path: '/adicionarCredor',
    component: ()=> import('../views/Creditor/form.vue'),
    name: 'adicionarCredor'
  },
  {
    path: '/atualizarCredor/:cnpj',
    component: ()=> import('../views/Creditor/form.vue'),
    name: 'atualizarCredor'
  },
  {
    path: '/detalhesConta/:id',
    component: ()=> import('../views/Accounts/details.vue'),
    name: 'detalhesConta'
  },
  {
    path: '/detalhesCredor/:cnpj',
    component: ()=> import('../views/Creditor/details.vue'),
    name: 'detalhesCredor'
  },

];

// Adicionar rota credor
 
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
