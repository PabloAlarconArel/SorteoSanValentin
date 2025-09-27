<template>
    <div>
        <h1>Panel de Administración</h1>
        <SideBar/>
        <button @click="generateWinner">Generar Ganador</button>
        <div v-if="winner" class="winner-info">
            <h2>Ganador:</h2>
            <p class="winner-p">{{ winner }}</p>
        </div>

    </div>

</template>

<script>
import SideBar from '@/components/SideBar.vue';
import api from '@/axios';

export default {
    name: 'AdminView',
    components:{
        SideBar,
    },
    data() {
        return {
        password: "",
        isAuthenticated: false, 
        winner: null, 
        email: "",
        };
    },
    methods: {
        async generateWinner() {
            try{
                await api.get("/select-winner/")
                .then(response => {
                    this.winner = response.data.full_name + " - " + response.data.email ;
                })
            }catch(error){
                console.error("Error generating winner:", error);
                alert("Ocurrió un error al generar el ganador. Por favor, inténtalo de nuevo.");
            }

        }
    }

}

</script>

<style scoped >
.winner-info {
    margin-top: 20px;
    padding: 10px;
    border: 2px solid #4CAF50;
    border-radius: 5px;
    background-color: #f9f9f9;
}

.winner-p {
    font-size: 1.2em;
    color: #333;
}

button {
    padding: 10px 20px;
    font-size: 16px;
    color: #fff;
    background-color: #4CAF50;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
button:hover {
    background-color: #45a049;
}
</style>