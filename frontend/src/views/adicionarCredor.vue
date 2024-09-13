<template>
  <div class="page-container">
    <header class="page-header">
      <h1>Cadastrar Novo Credor</h1>
      <nav>
        <RouterLink to="/" class="back-link">
          <i class="fas fa-arrow-left"></i> Voltar
        </RouterLink>
      </nav>
    </header>
    <div class="form-container">
      <form @submit.prevent="adicionarCredor">
        <div class="form-group">
          <label for="cnpj">CNPJ:</label>
          <input v-model="novoCredor.cnpj" type="text" id="cnpj" required />
        </div>
        <div class="form-group">
          <label for="nome">Nome:</label>
          <input v-model="novoCredor.nome" type="text" id="nome" required />
        </div>
        <div class="form-group">
          <label for="endereco">Endereço:</label>
          <input v-model="novoCredor.endereco" type="text" id="endereco" required />
        </div>
        <div class="form-group">
          <label for="telefone">Telefone:</label>
          <input v-model="novoCredor.telefone" type="text" id="telefone" required />
        </div>
        <div class="form-group">
          <label for="email">E-mail:</label>
          <input v-model="novoCredor.email" type="email" id="email" required />
        </div>
        <button type="submit" class="submit-button">
          <i class="fas fa-user-plus"></i> Adicionar Credor
        </button>
      </form>
    </div>
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
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css');

.page-container {
  font-family: 'Roboto', sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  padding-bottom: 10px;
  border-bottom: 2px solid #3498db;
}

.page-header h1 {
  font-size: 24px;
  color: #3498db;
}

.back-link {
  color: #3498db;
  text-decoration: none;
  font-weight: 500;
}

.form-container {
  background-color: #f8f9fa;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: 500;
  color: #333;
}

input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ced4da;
  border-radius: 4px;
  font-size: 16px;
}

.submit-button {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 500;
  transition: background-color 0.3s;
}

.submit-button:hover {
  background-color: #2980b9;
}
</style>
