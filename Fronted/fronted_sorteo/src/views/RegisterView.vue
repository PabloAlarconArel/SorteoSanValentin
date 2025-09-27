<template>
    <div class="container">
        <div class="text-center mb-4 py-1 text-white">
            <img src="@/assets/icons8-hotel-64.png" alt="San Valentín" class="img-fluid mb-4" style="max-width: 100px; background-color:bisque; border-radius: 30%; padding: 15px; ">
            <h1 class="display-4 text-white">¡Participa, Registrate y Gana en este san Valentín!</h1>
            <p class="lead">El premio es una estadía de 2 noches todo pagado para una pareja en el hotel "H".</p>
        </div>
    
    <div class="text-center mb-4 py-4">
        <form @submit.prevent="register" class="bg-light p-3 rounded shadow-sm">
        <div class="row d-flex justify-content-center mx-auto mt-3">
            <div class="col-md-3 mb-3">
                <label for="email" class="form-label">Nombre Completo</label>
                <input v-model="name" type="text" id="name" class="form-control"  required />
            </div>
            <div class="col-md-3 mb-3">
                <label for="Correo" class="form-label">Correo electrónico</label>
                <input v-model="email" type="email" id="email" class="form-control"  required />
            </div>
            <div class="col-md-2 mb-3">
                <label for="teléfono" class="form-label">Teléfono</label>
                <input v-model="phone" type="tel" id="phone" class="form-control" placeholder="" required />
            </div>
        </div>
        <div class="col-2 d-flex justify-content-center mx-auto mt-3">
            <button type="submit" class="btn btn-success btn-lg w-100">Registrarse</button>
        </div>        
        </form>
    </div>
    <div v-if="is_message">
        <div  class = box>
            <div class="message" >
                {{ message }}
            </div>
            <button onclick="ConfirmMessage()" :class="confirm_button">Aceptar</button>"
        </div>   
    </div>
    <router-link to="/login">Entrar como administrador</router-link> 
    </div>


</template>

<script>
import api from '@/axios'
export default {
    name: 'RegistView',
    data(){
        return{
            name: "",
            email: "",
            phone: "",
            is_message: false,
            message: "",
        };
    },
    methods:{
        async register(){
            try{
                let json ={
                    email: this.email,
                    full_name: this.name,
                    phone: this.phone
                };

                await api.post('/register/', json)
                .then(res=>{
                    if (res.data.status === 'success') {
                        this.name = "";
                        this.email = "";
                        this.phone = "";
                        this.is_message = true;
                        this.message = res.data.message;

                    } else {
                        alert('Error en el registro: ' + res.data.message);
                    }
                });
            }catch(error){
                console.error('Error en la solicitud:', error);
                alert('Ocurrió un error durante el registro. Por favor, inténtalo de nuevo.');
            }
        },
        ConfirmMessage(){
            this.is_message = false;
            this.message = "";
        },
    }    
};
</script>

<style scoped >
.container{
    background: linear-gradient(90deg,#d6336c,#a61e4d);
    padding:40px 20px;
    text-align: center;
    border-radius: 12px;
    box-shadow: 0 6px 15px rgba(0,0,0,0.2);
    background-image: url('https://images.vexels.com/content/103742/preview/love-vector-background-677802.png');
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    align-content: center; 
    margin-top: 20px; 
    height:auto;
    width:70%;
}
.banner h1{
    font-size: 2rem;
    font-weight: bold;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
    margin-bottom: 10px;
}
.form-label {
  display: flex;
  font-weight: bold;
  text-align:left;

}

img {
  filter: hue-rotate(120deg);
}

.box{
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  display: none; /* oculto por defecto */
  align-items: center;
  justify-content: center;
  z-index: 1000;

}

.box p {
  margin-bottom: 15px;
  font-size: 18px;
}

.confirm_button {
  background-color: #28a745;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}
</style>