<template>
    <div>
    <header class="flex w-full justify-between p-5 bg-[#4caf50] text-white items-center">
    <h1 class="font-bold text-3xl">Listar Credores</h1>
    <nav class="text-xl">
      <RouterLink to="/">Voltar</RouterLink>
    </nav>
  </header>

    <div v-for="(credor, index) in credores" :key="index" class="conta-grupo">
      <header class="grupo-header">
        <h2>{{ credor.nome }}</h2>
      </header>

        <RouterLink :to="`/detalhesCredor/${credor.cnpj}`" class="link-conta">
          <div class="conta-info">
            <p><strong>CNPJ:</strong> {{ credor.cnpj }}</p>
            <p><strong>Nome:</strong> {{ credor.nome }}</p>
            <p><strong>Endereço:</strong> {{ credor.endereco }}</p>
            <p><strong>Telefone:</strong> {{ credor.telefone }}</p>
            <p><strong>E-mail:</strong> {{ credor.email }}</p>
          </div>
        </RouterLink>
      </div>
    </div>

  </template>
  
  <script lang="ts">
  import { useRoute, useRouter } from 'vue-router';
  export default {
    data(){
      return{
        route : useRoute(),
         router : useRouter(),
         credores : [] as any
    //      {
    //       cnpj: '',
    //       nome: '',
    //       endereco: '',
    //       telefone: '',
    //       email: '',

      
    // }
    ,}},
    methods:{
      async listarCredores(){
        const response = await fetch('http://127.0.0.1:5000/credores/listar')
        const result =await  response.json()
        this.credores = result


      }

    },
    mounted(){
      this.listarCredores()

    },
    name: 'listarCredores',
  };
  </script>

<style scoped>
/* Header e Navbar */
#headerPage {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background-color: #4caf50;
  color: white;
}

#headerPage nav a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

#headerPage nav a:hover {
  text-decoration: underline;
}

/* Estilizando o grupo de contas */
.conta-grupo {
  margin: 20px 0;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 10px;
  background-color: #f9f9f9;
}

/* Estilizando o box de cada conta */
.conta-box {
  padding: 15px;
  margin-bottom: 10px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Status das contas */
.status-paga {
  background-color: #c8e6c9;
}

.status-atrasada {
  background-color: #fff9c4;
}

.status-pendente {
  background-color: #ffcdd2;
}

.status-cancelada {
  background-color: #e0e0e0;
}

/* Informações da conta */
.conta-info p {
  margin: 5px 0;
}

.link-conta {
  text-decoration: none;
  color: inherit;
  flex: 1;
}

/* Ações da conta */
.conta-actions {
  display: flex;
  gap: 10px;
}

.action-button {
  padding: 8px 15px;
  font-size: 14px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.edit-button {
  background-color: #1976d2;
  color: white;
}

.edit-button:hover {
  background-color: #1565c0;
}

.delete-button {
  background-color: #e53935;
  color: white;
}

.delete-button:hover {
  background-color: #d32f2f;
}
</style>