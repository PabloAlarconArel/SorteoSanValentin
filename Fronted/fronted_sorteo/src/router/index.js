import {createRouter, createWebHistory} from 'vue-router'
import LoginView from '@/views/LoginView.vue'
import AdminView from '@/views/AdminView.vue'
import WinnerView from '@/views/WinnerView.vue' 
import RegisterView from '@/views/RegisterView.vue'

const routes = [
    {path:'/', name:'Register', component: RegisterView},
    {path:'/login', name:'Login', component: LoginView},
    {path:'/admin', name:'Admin', component: AdminView},
    {path:'/concurso', name:'Concurso', component: WinnerView},
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;