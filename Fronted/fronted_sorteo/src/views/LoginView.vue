<template>
<div class="container login-container">
  <div class="col-md-6 login-form-1">
    <div class="icon d-flex justify-content-center mb-3">
    <img src="@/assets/icons8-hotel-64.png" id="icon" alt="User Icon" />
    </div>

    <h3>Bienvenido</h3>

    <!--Login form-->
    <form v-on:submit.prevent="login">
        <div class="form-group">
            <input type="email" class="form-control" placeholder="Email " v-model="email" value="" required/>
        </div>
        <div class="form-group">
            <input type="password" class="form-control" placeholder="Contraseña " v-model="password" value="" required />
        </div>
        <div class="form-group">
            <input type="submit" class="btnSubmit" value="Login" />
        </div>
        <div class="alert alert-danger" role="alert" v-if="error">
            {{ error_msg }}
        </div>
    </form>
  </div>
</div>
</template>

<script>
import {useRouter} from 'vue-router';
import api from '@/axios';

export default {
    name: 'LoginView',
    data(){
    return{
        email: "",
        password: "",
        error:false,
        error_msg:""
    };
    },
    setup(){
        const router = useRouter();
        return { router};
    },
    methods: { 
        async login() {
            try {

                let json ={
                    email: this.email,
                    password: this.password
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

<style scoped >

.login-container{
    margin-top: 5%;
    margin-bottom: 5%;
    display: flex;
    justify-content: center;
}
.login-form-1{
    padding: 5%;
    box-shadow: 0 5px 8px 0 rgba(0, 0, 0, 0.2), 0 9px 26px 0 rgba(0, 0, 0, 0.19);
}
.login-form-1 h3{
    text-align: center;
    color: #333;
}

.login-container form{
    padding: 10%;
    margin: 20px;
}
.form-group{
    margin-bottom: 10px;
}
.btnSubmit{
    width: 50%;
    border-radius: 0.5rem;
    padding: 1.5%;
    border: none;
    cursor: pointer;
    margin-top: 4%;
    transition: all 0.3s ease-in-out;
    box-shadow: #0062cc;
}

.btnSubmit:hover{
    background-color: #3b83cf;
    color: white;
    transition: all 0.2s ease;
}
.btnSubmit:active{
    transform: scale(0.98);
    box-shadow: #0062cc;
    transition: all 0.2s ease;
}

.login-form-1 .btnSubmit{
    font-weight: 600;
    color: #fff;
    background-color: #1a6dc5;
}

.login-form-1 .ForgetPwd{
    color: #0062cc;
    font-weight: 600;
    text-decoration: none;
    margin:20px;
}
</style>
