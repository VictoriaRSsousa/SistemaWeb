<template>
  <header id="headerPage">
    <h1>Contas a pagar</h1>
  </header>

  <div v-for="(contaGrupo, index) in resultado" :key="index">
    <header>
      <h1>{{ contaGrupo.empresa.nome }}</h1>
    </header>

    <div v-for="(conta, i) in contaGrupo.contas" :key="i" id="box-conta">
        <RouterLink :to="`/conta/${conta.id}`" class="link-conta">
        <p>Descrição: {{ conta.descricao }}</p>
        <footer id="footer">
          <p>Valor: {{ conta.valor }}</p>
          <p>
            {{
              verificarPagamento(conta.data_pagamento, conta.data_vencimento)
            }}
          </p>
        </footer>
    </RouterLink>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      resultado: [] as any,
    };
  },
  methods: {
    async listarContas() {
      try {
        const response = await fetch("http://127.0.0.1:5000/listarConta");
        const result = await response.json();
        this.resultado = result;
      } catch (error) {
        alert(error);
      }
    },
    verificarPagamento(dataPagamento: any, dataVencimento: any) {
      const vencimento = new Date(dataVencimento);
      const hoje = new Date();

      if (dataPagamento) {
        const pagamento = new Date(dataPagamento);

        if (pagamento > vencimento) {
          return "Paga com atraso";
        } else if (pagamento <= vencimento) {
          return "Paga";
        }
      } else {
        if (vencimento > hoje) {
          return "Em aberto";
        } else if (hoje > vencimento) {
          return "Pagamento pendente";
        }
      }
    },
  },
  mounted() {
    this.listarContas();
  },
};
</script>
<style>
#headerPage {
  display: flex;
  width: 100vw;
  justify-content: center;
  align-items: center;
}
#descricao {
  background-color: aquamarine;
  width: 60vw;
}
#box-conta {
  background-color: #e0ffff;
  padding: 5px 20px;
  margin-bottom: 8px;
  width: 60vw;
}
.link-conta{
    text-decoration: none;
    color: inherit;
}
#footer {
  display: flex;
  justify-content: space-between;
}
</style>
