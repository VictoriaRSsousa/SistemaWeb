import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config';
import ToastService from 'primevue/toastservice';
import 'primeicons/primeicons.css'
import setPrimeComponent from './modules/prime.module';
import Aura from '@primevue/themes/aura';
import ConfirmationService from 'primevue/confirmationservice';




const app = createApp(App)
app.use(ConfirmationService);

app.use(router ); 
app.use(ToastService );
app.use(PrimeVue, {
    theme: {
        preset: Aura,
        options: {
            darkModeSelector: false || 'none'
        }
    }
});
setPrimeComponent(app)
app.mount('#app');

 export default app