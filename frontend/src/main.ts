import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './routes'

createApp(App)
  .use(router as any)
  .mount('#app')
