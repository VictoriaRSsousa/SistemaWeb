<template>
  <div>
    <header class="flex w-full justify-between p-5 bg-[#4caf50] text-white items-center">
    <h1 class="font-bold text-3xl">Listar Conta</h1>
    <nav class="text-xl">
      <RouterLink to="/">Voltar</RouterLink>
    </nav>
  </header>

    <div v-for="(contaGrupo, index) in resultado" :key="index" class="conta-grupo">
      <header class="grupo-header">
        <h2>{{ contaGrupo.empresa.nome }}</h2>
      </header>

      <div
        v-for="(conta, i) in contaGrupo.contas"
        :key="i"
        :class="['conta-box', getStatusClass(conta)]"
      >
        <RouterLink :to="`/detalhesConta/${conta.id}`" class="link-conta">
          <div class="conta-info">
            <p><strong>CNPJ:</strong> {{ conta.cnpj }}</p>
            <p><strong>Descrição:</strong> {{ conta.descricao }}</p>
            <p><strong>Valor:</strong> R$ {{ formatValor(conta.valor) }}</p>
            <p><strong>Vencimento:</strong> {{ formatDate(conta.data_vencimento) }}</p>
            <!-- <p><strong>Multa:</strong> R$ {{ formatValor(conta.multa) }}</p>
            <p><strong>Juros:</strong> R$ {{ formatValor(conta.juros) }}</p> -->
            <p><strong>Status:</strong> {{ verificarPagamento(conta.data_pagamento, conta.data_vencimento) }}</p>
          </div>
        </RouterLink>
        <!-- <div class="conta-actions">
          <RouterLink :to="`/atualizarConta/${conta.id}`">
            <button class="action-button edit-button">Editar</button>
          </RouterLink>
          <button class="action-button delete-button" @click="deletarConta(conta.id)">Excluir</button>
        </div> -->
      </div>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      resultado: [] as any[],
    };
  },
  methods: {
    async listarContas() {
      try {
        const response = await fetch("http://127.0.0.1:5000/contas/listar");
        const result = await response.json();
        this.resultado = result;
      } catch (error:any) {
        alert("Erro ao listar contas: " + error.message);
      }
    },
    verificarPagamento(dataPagamento: string, dataVencimento: string) {
      const vencimento = new Date(dataVencimento);
      const hoje = new Date();

      if (dataPagamento) {
        const pagamento = new Date(dataPagamento);
        return pagamento > vencimento ? "Paga com atraso" : "Paga";
      } else {
        return vencimento > hoje ? "Em aberto" : "Pagamento pendente";
      }
    },
    getStatusClass(conta: any) {
      const status = this.verificarPagamento(conta.data_pagamento, conta.data_vencimento);
      switch (status) {
        case "Paga":
          return "status-paga";
        case "Paga com atraso":
          return "status-atrasada";
        case "Pagamento pendente":
          return "status-pendente";
        default:
          return "status-cancelada";
      }
    },
    formatDate(dateString: string) {
      const options: Intl.DateTimeFormatOptions = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(dateString).toLocaleDateString('pt-BR', options);
    },
    formatValor(valor: any) {
      const number = parseFloat(valor);
      return isNaN(number) ? "N/A" : number.toFixed(2);
    },
    async deletarConta(id: number) {
      try {
        const response = await fetch(`http://127.0.0.1:5000/removerConta/${id}`, {
          method: 'DELETE',
        });
        if (response.ok) {
          this.resultado = this.resultado.map(grupo => ({
            ...grupo,
            contas: grupo.contas.filter((conta:any) => conta.id !== id)
          }));
        } else {
          alert("Erro ao deletar conta");
        }
      } catch (error:any) {
        alert("Erro ao deletar conta: " + error.message);
      }
    },
  },
  mounted() {
    this.listarContas();
  },
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

