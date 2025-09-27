<template>
    <div>
        <h1>Verificación de cuenta</h1>
        <form @submit.prevent="verifyPassword">
            <div >
                <label for="password">Nueva Contraseña:</label>
                <input type="newPassword" id="newPassword" v-model="newpassword" required />
            </div>
            <div >
                <label for="confirmPassword">Confirmar Contraseña:</label>
                <input type="confirmPassword" id="confirmPassword" v-model="confirmpassword" required />
            </div>
            <button type="submit">Verificar</button>
        </form>
        <div class="alert alert-danger" role="alert" v-if="error">
            {{ error_msg }}
        </div>

    </div>

</template>

<script>
import {useRouter} from 'vue-router';
import api from '@/axios';

export default {
    name: 'AdminView',
    data(){
    return{
        newpassword: "",
        confirmpassword: "",
        error:false,
        error_msg:""
    };
    },
    setup(){
        const router = useRouter();
        return { router};
    },
    methods: { 
        async verifyPassword() {
            try {

                let json ={
                    newpassword: this.newpassword,
                    confirmpassword: this.confirmpassword
                };

                await api.post('/login', json)
                .then(res=>{
                    if (res.data.status === 'success') {
                        localStorage.setItem('token', res.data.token);
                        this.router.push('/admin');
                    }
                    else {
                        this.error = true;
                        this.error_msg = res.data.message;
                    }
                })
            } catch (error) {
                console.error('Error during login:', error);
                alert('An error occurred. Please try again.');
            }
    }
    },
    }

</script>