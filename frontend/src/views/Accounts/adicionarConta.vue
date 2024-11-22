<template>
  <div class="page-container">
    <header class="page-header">
      <h1>Cadastrar Nova Conta</h1>
      <nav>
        <RouterLink to="/" class="back-link">
          <i class="fas fa-arrow-left"></i> Voltar
        </RouterLink>
      </nav>
    </header>
    <div class="form-container">
      <form @submit.prevent="adicionarConta">
        <div class="form-group">
          <label for="cnpj">CNPJ:</label>
          <input v-model="novaConta.cnpj" type="text" id="cnpj" required />
        </div>
        <div class="form-group">
          <label for="valor">Valor:</label>
          <input v-model="novaConta.valor" type="number" id="valor" required />
        </div>
        <div class="form-group">
          <label for="descricao">Descrição:</label>
          <input v-model="novaConta.descricao" type="text" id="descricao" required />
        </div>
        <div class="form-group">
          <label for="data_vencimento">Data de Vencimento:</label>
          <input v-model="novaConta.data_vencimento" type="date" id="data_vencimento" required />
        </div>
        <div class="form-group">
          <label for="multa">Multa:</label>
          <input v-model="novaConta.multa" type="number" id="multa" required />
        </div>
        <div class="form-group">
          <label for="juros">Juros:</label>
          <input v-model="novaConta.juros" type="number" id="juros" required />
        </div>
        <div class="form-group">
          <label for="data_pagamento">Data de Pagamento (Opcional):</label>
          <input v-model="novaConta.data_pagamento" type="date" id="data_pagamento" />
        </div>
        <button type="submit" class="submit-button">
          <i class="fas fa-plus-circle"></i> Adicionar Conta
        </button>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import { useRoute, useRouter } from 'vue-router';

export default {
  data() {
    return {
      route : useRoute(),
      router : useRouter(),
      novaConta: {
        cnpj: "",
        valor: 0,
        descricao: "",
        data_vencimento: null,
        multa: 0,
        juros: 0,
        data_pagamento: null,
        status: ''
      },
    };
  },
  methods: {
    async adicionarConta() {
      try {
        const status = this.verificarPagamento(this.novaConta.data_pagamento,this.novaConta.data_vencimento)
        console.log(status);
        if(!this.novaConta.data_pagamento){
          this.novaConta.data_pagamento = null
        }
        const response = await fetch("http://127.0.0.1:5000/contas/adicionar", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({...this.novaConta, status: status}),
        });
        const result = await response.json();
        alert(result.Mensagem);
        this.novaConta = {
          cnpj: "",
          valor: 0,
          descricao: "",
          data_vencimento: null,
          multa: 0,
          juros: 0,
          data_pagamento: null,
          status: status,
        };
        this.router.push("/listarContas");
      } catch (error: any) {
        alert("Erro ao adicionar conta: " + error.message);
      }
    },

    verificarPagamento(dataPagamento: any, dataVencimento: any) {
      const vencimento = new Date(dataVencimento);
      const hoje = new Date();

      if (dataPagamento) {
        const pagamento = new Date(dataPagamento);
        if (pagamento > vencimento) {
          return "PAGA";
        }
        return "PAGA"; 
      } else {
        return vencimento > hoje ? "ABERTA" : "ATRASADA";
      }
    },

    
  },
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
