import { createRouter, createWebHistory } from 'vue-router'
import listarContas from '../views/listarContas.vue'


const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/listarContas', component: listarContas, name: 'listarContas'
        },
    
    ]
})



export default router