<template>
 <div class="sidebar-layout">

    <aside class="sidebar bg-primary text-white">
        <div class="icon d-flex justify-content-center mb-4">
        <img src="@/assets/icons8-hotel-64.png" id="icon" alt="User Icon" />
        </div>
      <h4 class="p-3">Menú Principal</h4>
      <ul class="nav flex-column p-3">
        <li class="nav-item mb-2">
            <a
            href="#opcion1"
            :class="['nav-link', { active: activo === 'opcion1' }]"
            @click.prevent="setActivo('opcion1')"
            >Participantes</a>
        </li>
        <li class="nav-item mb-2">
            <a
            href="#opcion2"
            :class="['nav-link', { active: activo === 'opcion2' }]"
            @click.prevent="setActivo('opcion2')"
            >Concurso</a>
        </li>
        <hr class="bg-light"/>
        <li class="nav-item">
            <button class="btn btn-danger w-100" @click="cerrarSesion">Cerrar sesión</button>
        </li>
    </ul>
    </aside>

    <main class="content p-3">
    </main>
  </div>
</template>

<script>

export default {
  name: 'SideBar',
  data() {
    return {
    activo: 'opcion1'}
    },
  methods: {
    cerrarSesion() {
    },
    setActivo(opcion) {
      this.activo = opcion
    }
  }
  }

</script>

<style scoped>
.sidebar-layout {
  display: flex;
}


.sidebar {
  width: 220px;        
  min-height: 100vh;  
  position: fixed;     
  top: 0;
  left: 0;
  overflow-y: auto;    
}


.content {
  margin-left: 220px;  
}


.bg-primary {
  background-color: #1e3a8a !important; 
}

.text-white {
  color: #fff !important;
}

.nav-link {
  margin-bottom: 10px; 
}

.b-nav, .b-nav.flex-column {
  display: flex !important;
  flex-direction: column !important;
}
</style>