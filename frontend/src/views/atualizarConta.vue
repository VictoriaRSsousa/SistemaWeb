<template>
    <div id="editPage">
      <header id="headerPage">
        <h1>Editar Conta</h1>
        <nav>
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
  import { defineComponent, ref } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  
  export default defineComponent({
    name: 'EditarConta',
    setup() {
      const route = useRoute();
      const router = useRouter();
      const conta = ref({
        descricao: '',
        valor: 0,
        data_vencimento: '',
        multa: 0,
        juros: 0,
      });
  
      const fetchConta = async () => {
        try {
          const response = await fetch(`http://127.0.0.1:5000/conta/${route.params.id}`);
          const data = await response.json();
          if (data.Conta) {
            conta.value = data.Conta;
          }
        } catch (error) {
          alert('Erro ao buscar conta: ' + error.message);
        }
      };
  
      const editarConta = async () => {
        try {
          const response = await fetch(`http://127.0.0.1:5000/atualizarConta/${route.params.id}`, {
            method: 'PATCH',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(conta.value),
          });
          const result = await response.json();
          if (response.ok) {
            alert('Conta atualizada com sucesso!');
            router.push('/listarContas');
          } else {
            alert('Erro ao atualizar conta: ' + result.mensagem);
          }
        } catch (error) {
          alert('Erro ao atualizar conta: ' + error.message);
        }
      };
  
      fetchConta();
  
      return {
        conta,
        editarConta,
      };
    },
  });
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
