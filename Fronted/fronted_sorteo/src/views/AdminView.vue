<template>
    <div>
        <h1>Panel de Administración</h1>
        <SideBar/>
        <Tables/>
    </div>

</template>

<script>
import Tables from '@/components/Tables.vue';
import SideBar from '@/components/SideBar.vue';

export default {
  name: 'AdminView',
  components:{
    SideBar,
    Tables

  }
  }

</script>