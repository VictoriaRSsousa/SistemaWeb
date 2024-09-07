<template>
    <div id="adicionarConta">
      <h2>Cadastro de Nova Conta</h2>
      <form @submit.prevent="adicionarConta">
        <div>
          <label for="cnpj">CNPJ:</label>
          <input v-model="novaConta.cnpj" type="text" id="cnpj" required />
        </div>
        <div>
          <label for="valor">Valor:</label>
          <input v-model="novaConta.valor" type="number" id="valor" required />
        </div>
        <div>
          <label for="descricao">Descrição:</label>
          <input v-model="novaConta.descricao" type="text" id="descricao" required />
        </div>
        <div>
          <label for="data_vencimento">Data de Vencimento:</label>
          <input v-model="novaConta.data_vencimento" type="date" id="data_vencimento" required />
        </div>
        <div>
          <label for="multa">Multa:</label>
          <input v-model="novaConta.multa" type="number" id="multa" required />
        </div>
        <div>
          <label for="juros">Juros:</label>
          <input v-model="novaConta.juros" type="number" id="juros" required />
        </div>
        <div>
          <label for="data_pagamento">Data de Pagamento (Opcional):</label>
          <input v-model="novaConta.data_pagamento" type="date" id="data_pagamento" />
        </div>
        <button type="submit">Adicionar Conta</button>
      </form>
    </div>
  </template>
  
  <script lang="ts">
  export default {
    data() {
      return {
        novaConta: {
          cnpj: '',
          valor: 0,
          descricao: '',
          data_vencimento: '',
          multa: 0,
          juros: 0,
          data_pagamento: '',
        },
      };
    },
    methods: {
      async adicionarConta() {
        try {
          const response = await fetch('http://127.0.0.1:5000/adicionarConta', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(this.novaConta),
          });
          const result = await response.json();
          alert(result.mensagem);
          // Limpar o formulário após o sucesso
          this.novaConta = {
            cnpj: '',
            valor: 0,
            descricao: '',
            data_vencimento: '',
            multa: 0,
            juros: 0,
            data_pagamento: '',
          };
        } catch (error:any) {
          alert('Erro ao adicionar conta: ' + error.message);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  #adicionarConta {
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
  