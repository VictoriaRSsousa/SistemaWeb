import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath } from 'node:url'

// https://vitejs.dev/config/
export default defineConfig(({mode})=>{
  const env = loadEnv(mode, process.cwd(),"");
  const _VITE_BASE_URL = env.VITE_BASE_URL ?? "" 
  
  return{

    
    plugins: [vue()],
    resolve:{
      alias:{
        "@": fileURLToPath(new URL("./src",import.meta.url))
      }
    },
    server:{
      proxy:{
        "^/api":{
          target: _VITE_BASE_URL,
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\/api/, "")
        },
      }
  
    }
  }
})
