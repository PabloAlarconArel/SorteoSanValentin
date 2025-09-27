import { createApp } from 'vue';
import App from './App.vue';
import vueGoodTableNext from 'vue-good-table-next';
import router from './router';
//import BootstrapVueNext from 'bootstrap-vue-next';
import 'vue-good-table-next/dist/vue-good-table-next.css';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css';
import axios from 'axios';
import VueAxios from 'vue-axios';


const app = createApp(App);

app.use(router);
app.use(vueGoodTableNext);
//app.use(BootstrapVueNext);
app.use(VueAxios, axios)

app.mount('#app')
