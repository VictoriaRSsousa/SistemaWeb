<template>
  <header class=" mb-7 flex w-full justify-between p-5 bg-[#4caf50] text-white items-center">
    <h1 class="font-bold text-3xl">Cadastrar Novo Credor</h1>
    <nav class="text-xl">
      <RouterLink to="/">Voltar</RouterLink>
    </nav>
  </header>
  <div id="adicionarCredor">
    <h2>Cadastro de novo Credor</h2>
    <form @submit.prevent="adicionarCredor">
      <div>
        <label for="cnpj">CNPJ:</label>
        <input v-model="novoCredor.cnpj" type="text" id="cnpj" required />
      </div>
      <div>
        <label for="nome">Nome:</label>
        <input v-model="novoCredor.nome" type="text" id="nome" required />
      </div>
      <div>
        <label for="endereco">Endereço:</label>
        <input v-model="novoCredor.endereco" type="text" id="endereco" required />
      </div>
      <div>
        <label for="telefone">Telefone:</label>
        <input v-model="novoCredor.telefone" type="text" id="telefone" required />
      </div>
      <div>
        <label for="email">E-mail:</label>
        <input v-model="novoCredor.email" type="text" id="email" required />
      </div>
      <button type="submit">Adicionar Credor</button>
    </form>
  </div>
</template>
  
  <script lang="ts">
  import { useRoute, useRouter } from 'vue-router';

  export default {
    name: 'adicionarCredor',
    data(){

      return{
        route: useRoute(),
        router: useRouter(),
        novoCredor:{
          cnpj:"",
          nome:"",
          endereco:"",
          telefone:"", 
          email:"" 
        }
      }
    },
    methods:{
      async adicionarCredor() {
        try {
          const response = await fetch("http://127.0.0.1:5000/credores/adicionar", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(this.novoCredor),
        });
        const result = await response.json();
        alert (result.mensagem);
        this.novoCredor = {

          cnpj:"",
          nome:"",
          endereco:"",
          telefone:"", 
          email:"" 

        };
        this.router.push("/listarCredores");


        }catch (error: any) {
        alert("Erro ao adicionar credor: " + error.message);
      }
        
        
      }
    }

  };
  </script>

<style scoped>
#adicionarCredor {
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