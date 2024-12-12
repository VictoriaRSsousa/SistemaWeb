<template>
  <div id="listarCredoresPage" >
    <header class="w-full p-5 bg-[#3498db] flex  text-white text-center shadow-md">
      <RouterLink
        to="/"
        class=" flex  items-center justify-center h-10  transition transform hover:-translate-y-1  active:translate-y-0"
      >
        <i class="fas fa-home text-2xl mr-2"></i>
      </RouterLink>
      <h1 class="text-2xl font-semibold mx-auto">Listar Credores</h1>
    </header>

    <div id="listarCredoresContent" class="px-3">
      <div class="filter-group ">
        <div class="filter-item w-[20vw]">
          <label for="cnpjCredor" class="text-black">CNPJ:</label>
          <input v-model="query.cnpj" @keyup.enter="getAllCreditors" type="text" class="input-field " id="cnpjCredor">
        </div>
        <!-- <button @click="listarCredores()" class="search-button">Pesquisar</button> -->
      </div>

      <div v-for="(credor, index) in credores" :key="index" class="credor-box">
        <RouterLink :to="`/detalhesCredor/${credor.cnpj}`" class="link-credor">
          <div class="credor-info">
            <p><strong>CNPJ:</strong> {{ credor.cnpj }}</p>
            <p><strong>Nome:</strong> {{ credor.nome }}</p>
            <p><strong>Endereço:</strong> {{ credor.endereco }}</p>
            <p><strong>Telefone:</strong> {{ credor.telefone }}</p>
            <p><strong>E-mail:</strong> {{ credor.email }}</p>
          </div>
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { useRoute, useRouter } from "vue-router";
import { CreditorService } from "./creditor.service";
import QueryParams from "../../models/queryParams.model";
export default {
  data() {
    return {
      route: useRoute(),
      router: useRouter(),
      credores: [] as any,
      cnpjCredor: "",
      query: new QueryParams()
    };
  },
  methods: {

    getAllCreditors(){
      this.service.creditors.pipe().subscribe({
        next:(response)=>{
          this.credores = response
        }
      })
      this.service.getAll(this.query)
    },
  },
  mounted() {
    this.getAllCreditors()
  },
  computed:{
    service(): CreditorService{
      return new CreditorService()
    }
  },
  name: "listarCredores",
};
</script>

<style scoped>
body {
  font-family: 'Poppins', sans-serif;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  min-height: 100vh;
  margin: 0;
}

/* Cabeçalho */
.header {
  width: 100%;
  padding: 20px;
  background-color: #3498db;
  color: white;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.header h1 {
  font-size: 2rem;
  margin: 0;
  font-weight: 600;
}

/* Botões de Navegação */
.navButton {
  display: inline-flex;
  padding: 10px 20px;
  font-size: 16px;
  min-width: 120px;
  background-color: #ffffff;
  color: #333;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  text-decoration: none;
  align-items: center; /* Alinhar ícone e texto verticalmente */
  justify-content: center; /* Centraliza o texto e ícone */
}

.navButton i {
  font-size: 24px;
  margin-right: 8px;
}

.navButton:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
}

.navButton:active {
  transform: translateY(0);
}


.filter-group {
  display: flex;
  justify-content: flex-end;
  align-items: center; 
  gap: 10px;
  margin-bottom: 20px;
  margin-top: 20px;
}

.filter-item {
  display: flex;
  flex-direction: column;

  padding: 10px; 
  background-color: #ffffff; 
  border-radius: 8px; 
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); 
  margin-right: 10px; 
}

.filter-item label {
  margin-bottom: 5px; /* Espaçamento abaixo do label */
}

.filter-item input {
  padding: 5px;
  border: 1px solid #ccc; /* Bordas do input */
  border-radius: 4px; /* Bordas arredondadas para o input */
  font-size: 16px;
}

.search-button {
  border: none;
  padding: 10px 20px;
  background-color: #3498db;
  color: white;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.search-button:hover {
  background-color: #2980b9; /* Cor de fundo ao passar o mouse */
}

.search-button:active {
  background-color: #1f6d8f; /* Cor de fundo ao clicar */
}

/* Contas e Credores */
.credor-box {
  background-color: #bedfe4;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin-bottom: 20px;
}

.credor-info p {
  margin: 5px 0;
}

/* Links */
.link-credor {
  text-decoration: none;
  color: inherit;
}

</style>
