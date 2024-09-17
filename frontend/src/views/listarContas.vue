<template>
  <div id="listarContasPage">
    <header class="header">
      <h1>Listar Contas</h1>
      <RouterLink to="/" class="navButton">
        <i class="fas fa-home"></i>
        <span>Voltar</span>
      </RouterLink>
    </header>

    <div id="listarContasContent" class="m-4 ">
      <div class="filter-group ">
        <div class="filter-item">
          <label for="dataPagamento" class="font-bold">Data de pagamento:</label>
          <input @change="listarContas" type="date" v-model="dataPagamento" id="dataPagamento" class="p-1">
        </div>
        <div class="filter-item">
          <label for="dataVencimento" class="font-bold">Data de vencimento:</label>
          <input @change="listarContas" v-model="dataVencimento" type="date" id="dataVencimento"  class="p-1">
        </div>
        <button @click="limparFiltro" class="navButton mt-4 font-bold">Limpar filtro</button>
      </div>

      <div v-for="(contaGrupo, index) in resultado" :key="index" class="conta-grupo">
        <h2>{{ contaGrupo.empresa.nome }}</h2>
        <div v-for="(conta, i) in contaGrupo.contas" :key="i" :class="['conta-box', getStatusClass(conta)]">
          <RouterLink :to="`/detalhesConta/${conta.id}`" class="link-conta">
            <div class="conta-info">
              <p><strong>CNPJ:</strong> {{ conta.cnpj }}</p>
              <p><strong>Descrição:</strong> {{ conta.descricao }}</p>
              <p><strong>Valor:</strong> R$ {{ formatValor(conta.valor) }}</p>
              <p><strong>Vencimento:</strong> {{ formatDate(conta.data_vencimento) }}</p>
              <p><strong>Status:</strong> {{ verificarPagamento(conta.data_pagamento, conta.data_vencimento) }}</p>
            </div>
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      resultado: [] as any[],
      dataPagamento: '',
      dataVencimento: ''
    };
  },
  methods: {
    async listarContas() {
      try {
        const url = new URL("http://127.0.0.1:5000/contas/");
      if (this.dataPagamento) {
        url.searchParams.append("data_pagamento", this.dataPagamento);
      }
      if (this.dataVencimento) {
        url.searchParams.append("data_vencimento", this.dataVencimento);
      }
      const response = await fetch(url.toString());
        const result = await response.json();
        this.resultado = result;
      } catch (error: any) {
        alert("Erro ao listar contas: " + error.Mensagem);
      }
    },
    async limparFiltro(){
      this.dataPagamento = ''
      this.dataVencimento = ''
      try {
        const url = new URL("http://127.0.0.1:5000/contas/");
        url.searchParams.delete('data_pagamento');
        url.searchParams.delete('data_vencimento');
      const response = await fetch(url.toString());
        const result = await response.json();
        this.resultado = result;
      } catch (error: any) {
        alert("Erro ao listar contas: " + error.Mensagem);
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
      const status = this.verificarPagamento(
        conta.data_pagamento,
        conta.data_vencimento
      );
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
    formatDate(dateString: string): string {
      if (!dateString) return "";
      const date = new Date(dateString);
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, "0"); // Meses começam do 0
      const day = String(date.getDate() + 1).padStart(2, "0");
      return `${day}/${month}/${year}`;
    },
    formatValor(valor: any) {
      const number = parseFloat(valor);
      return isNaN(number) ? "N/A" : number.toFixed(2);
    },
    async deletarConta(id: number) {
      try {
        const response = await fetch(
          `http://127.0.0.1:5000/removerConta/${id}`,
          {
            method: "DELETE",
          }
        );
        if (response.ok) {
          this.resultado = this.resultado.map((grupo) => ({
            ...grupo,
            contas: grupo.contas.filter((conta: any) => conta.id !== id),
          }));
        } else {
          alert("Erro ao deletar conta");
        }
      } catch (error: any) {
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
.filter-group {
  display: flex;
  justify-content: flex-end;
  gap: 20px;
  margin-bottom: 20px;
}

.filter-item {
  display: flex;
  flex-direction: column;
}

.conta-grupo {
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin-bottom: 20px;
}

.conta-box {
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 10px;
}

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

#listarContasPage {
  font-family: 'Poppins', sans-serif;
  min-height: 100vh;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.navButton {
  height: 40px;
  display: inline-flex; 
  padding: 4px 20px;
  font-size: 16px; 
  min-width: 120px; 
  background-color: #ffffff;
  color: #333;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  text-decoration: none;
  align-items: center;
  justify-content: center;
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

.conta-info p {
  margin: 5px 0;
}

.link-conta {
  text-decoration: none;
  color: inherit;
}
</style>
