<template>
    <div id="editPage">
      <header id="headerPage" class="mb-7">
        <h1 class="font-bold text-3xl">Editar Conta</h1>
        <nav class="text-xl">
          <RouterLink to="/listarContas">Voltar</RouterLink>
        </nav>
      </header>
  
      <form @submit.prevent="editarConta" id="editForm">
        <div class="form-group">
          <label for="descricao">Descrição:</label>
          <input type="text" id="descricao" v-model="conta.descricao" required />
        </div>
  
        <div class="form-group">
          <label for="valor">Valor:</label>
          <input type="number" id="valor" v-model="conta.valor" step="0.01" required />
        </div>
        <div class="form-group">
          <label for="data_vencimento">Data de Vencimento:</label>
          <input type="date" id="data_vencimento" v-model="conta.data_vencimento" required />
        </div>
  
        <div class="form-group">
          <label for="multa">Multa:</label>
          <input type="number" id="multa" v-model="conta.multa" step="0.01" />
        </div>
  
        <div class="form-group">
          <label for="juros">Juros:</label>
          <input type="number" id="juros" v-model="conta.juros" step="0.01" />
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
    name: 'EditarConta',
    data(){
      return{
         route : useRoute(),
         router : useRouter(),
         conta : {
          descricao: '',
          valor: 0,
          data_vencimento: '',
          multa: 0,
          juros: 0,
          credor: {
                nome: '',
                cnpj:'',
            }
        }

      }
    } ,
  methods:{

    async fetchConta()  {
      try {
        const response = await fetch(`http://127.0.0.1:5000/contas/${this.route.params.id}`);
        const data = await response.json();
        if (data) {
          this.conta = {
            ...data,
            data_vencimento: this.formatDate(data.data_vencimento), // Converte a data para o formato YYYY-MM-DD
          };
        }
      } catch (error:any) {
        alert('Erro ao buscar conta: ' + error.message);
      }
    },

    async editarConta (){
      try {
        const response = await fetch(`http://127.0.0.1:5000/contas/atualizar/${this.route.params.id}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({...this.conta,credor:{nome:this.conta.credor.nome,cnpj:this.conta.credor.cnpj}}),
        });
        const result = await response.json();
        if (response.ok) {
          alert('Conta atualizada com sucesso!');
          this.router.push('/listarContas');
        } else {
          alert('Erro ao atualizar conta: ' + result.mensagem);
        }
      } catch (error:any) {
        alert('Erro ao atualizar conta: ' + error.message);
      }
    },
    formatDate(dateString: string): string {
      // Assume que dateString está no formato YYYY-MM-DD
      const date = new Date(dateString);
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0'); // Meses começam do 0
      const day = String(date.getDate()).padStart(2, '0');
      return `${year}-${month}-${day}`;
    },
  },
  computed:{
   
  },
  mounted() {
      this.fetchConta()
  },}
  
  
    
  
  </script>
  
  <style scoped>
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
  
  #editForm {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f4f4f4;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  .form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }
  
  .form-group input {
    width: 100%;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .form-actions {
    text-align: center;
  }
  
  .form-actions button {
    padding: 10px 20px;
    font-size: 16px;
    background-color: #4caf50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .form-actions button:hover {
    background-color: #388e3c;
  }
  </style>
