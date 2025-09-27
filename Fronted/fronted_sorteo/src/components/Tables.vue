<template>
    <div class="container-table">
        <VueGoodTable
          :columns="columns"
          :rows="rows"
          :search-options="{ enabled: true, placeholder: 'Buscar...' }"
          :pagination-options="{ 
          enabled: true, 
          perPage: 15,
          perPageDropdown: [10, 20, 50],
          dropdownAllowAll: false,
          nextLabel: 'Siguiente',
          prevLabel: 'Anterior',
          rowsPerPageLabel: 'Filas por página',
          ofLabel: 'de',
          pageLabel: 'Página', 
          allLabel:'Todos' 
          }"
        />
    </div>
</template>

<script>
import api from '@/axios';
import { VueGoodTable } from 'vue-good-table-next'
import 'vue-good-table-next/dist/vue-good-table-next.css'

export default {
  name: 'TablesComponent',
  components: {
    VueGoodTable
  },
  data() {
    return {
      columns: [
        { label: 'Nombre', field: 'name' ,width: '40%'},
        { label: 'Correo', field: 'email' ,width: '40%'},
        { label: 'Estado de Verificación', field: 'state',width:'20%'},
      ],
      rows: []
    }
  },
  async mounted() {
      await api.get('/participants/')
      .then(response => {
        this.rows = response.data  
      })
      .catch(error => {
        console.error("Error al obtener usuarios:", error)
      })
  }
}
</script>

<style scoped >
.container-table{
    width: 60%;
    max-width: 1200px;
    margin: 0 auto;
}
.vue-good-table .vgt-table {
  border-collapse: separate;
  border-spacing: 0 8px; 
}

</style>

