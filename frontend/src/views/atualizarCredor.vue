<template>
    <div id="editPage">
      <header id="headerPage" class="mb-7">
        <h1 class="font-bold text-3xl">Editar Dados Credor</h1>
        <nav class="text-xl">
          <RouterLink to="/listarCredores">Voltar</RouterLink>
        </nav>
      </header>

     <form @submit.prevent="atualizarCredor" id="editForm">
        <div class="form-group">
          <label for="cnpj">CNPJ:</label>
          <input type="text" id="cnpj" v-model="credor.cnpj" required />
        </div>
  
        <div class="form-group">
          <label for="nome">Nome:</label>
          <input type="text" id="nome" v-model="credor.nome" step="0.01" required />
        </div>
        <div class="form-group">
          <label for="endereco">Endereço:</label>
          <input type="text" id="endereco" v-model="credor.endereco" required />
        </div>
  
        <div class="form-group">
          <label for="telefone">Telefone:</label>
          <input type="text" id="telefone" v-model="credor.telefone" step="0.01" />
        </div>
  
        <div class="form-group">
          <label for="email">E-mail:</label>
          <input type="text" id="email" v-model="credor.email" step="0.01" />
        </div>
  
        <div class="form-actions">
          <button type="submit">Salvar</button>
        </div>
      </form>
    </div>

  </template>
  
  <script lang="ts">
  import { useRoute, useRouter } from 'vue-router';

  export default{
    name: 'AtualizarCredor',
    data(){
      return{
         route : useRoute(),
         router : useRouter(),
         credor : {
          cnpj: '',
          nome: '',
          endereco: '',
          telefone: '',
          email: '',
          
        }

      }
    } ,
  methods: {
    async atualizarCredor(){
      try{
        const response = await fetch(`http://127.0.0.1:5000/credores/atualizar/${this.route.params.cnpj}`, {
          method: "PATCH",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(this.credor),
        });
        const result = await response.json();
        alert(result)


      }catch(error){
        alert(error)

      }
      

    },
    async buscarCredor(){
      try{
        const response = await fetch(`http://127.0.0.1:5000/credores/${this.route.params.cnpj}`)
        const result = await response.json(); 
        this.credor = result  


      }catch(error){
        alert(error)
      }
    }

    
  },
  mounted(){
    this.buscarCredor()
  }
}
  </script>

<style scoped>
#editForm {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f9f9f9;
}

form > div {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  padding: 10px 20px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #388e3c;
}
</style>
