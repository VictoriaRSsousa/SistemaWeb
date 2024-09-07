<template>
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
  export default {
    name: 'adicionarCredor',
    data(){

      return{
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
      adicionarCredor(){
        alert("olá mundo")
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