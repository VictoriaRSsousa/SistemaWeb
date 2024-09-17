<template>
  <div class="page-container">
    <header class="page-header">
      <h1>Editar Dados do Credor</h1>
      <nav>
        <RouterLink :to="`/detalhesCredor/${route.params.cnpj}`" class="back-link">
          <i class="fas fa-arrow-left"></i> Voltar
        </RouterLink>
      </nav>
    </header>
    <div class="form-container">
      <form @submit.prevent="atualizarCredor">
        <div class="form-group">
          <label for="cnpj">CNPJ:</label>
          <input type="text" id="cnpj" v-model="credor.cnpj" required />
        </div>
        <div class="form-group">
          <label for="nome">Nome:</label>
          <input type="text" id="nome" v-model="credor.nome" required />
        </div>
        <div class="form-group">
          <label for="endereco">Endereço:</label>
          <input type="text" id="endereco" v-model="credor.endereco" required />
        </div>
        <div class="form-group">
          <label for="telefone">Telefone:</label>
          <input type="text" id="telefone" v-model="credor.telefone" required />
        </div>
        <div class="form-group">
          <label for="email">E-mail:</label>
          <input type="email" id="email" v-model="credor.email" required />
        </div>
        <button type="submit" class="submit-button">
          <i class="fas fa-save"></i> Salvar Alterações
        </button>
      </form>
    </div>
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
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(this.credor),
        });
        const result = await response.json();
        if (response.ok) {
          alert('Credor atualizado com sucesso!');
          this.router.push(`/detalhesCredor/${this.credor.cnpj}`);
        } else {
          alert('Erro ao atualizar conta: ' + result.mensagem);
        }


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