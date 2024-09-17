<template>
  <div id="listarContasPage">
    <header class="header">
      <h1>Listar Contas</h1>
      <RouterLink to="/" class="navButton">
        <i class="fas fa-home"></i>
        <span>Voltar</span>
      </RouterLink>
    </header>

    <div id="listarContasContent" class="m-4">
      <div class="filters-container">
        <div class="filter-group">
          <div class="filter-item w-[20vw]">
            <label for="cnpjCredor" class="font-bold">CNPJ:</label>
            <input
              v-model="cnpjCredor"
              type="text"
              id="cnpjCredor"
              class="filter-input"
            />
          </div>
          <div class="filter-item w-[20vw]">
            <label for="status" class="font-bold">Status:</label>
            <select v-model="statusFiltro" id="status" class="filter-input">
              <option value="">Todos</option>
              <option value="PAGA">Paga</option>
              <option value="ATRASADA">Atrasada</option>
              <option value="ABERTA">Aberta</option>
            </select>
          </div>
          <div class="filter-item w-[20vw]">
            <label for="dataPagamento" class="font-bold">Data de pagamento:</label>
            <input
              @change="listarContas"
              type="date"
              v-model="dataPagamento"
              id="dataPagamento"
              class="filter-input"
            />
          </div>
          <div class="filter-item w-[20vw]">
            <label for="dataVencimento" class="font-bold">Data de vencimento:</label>
            <input
              @change="listarContas"
              v-model="dataVencimento"
              type="date"
              id="dataVencimento"
              class="filter-input"
            />
          </div>
          <button @click="listarContas()" class=" rounded-md my-auto  bg-[#2980b9] text-white px-3 h-12">Pesquisar</button>
          <button @click="limparFiltro" class=" rounded-md  my-auto border border-[#2980b9] text-[#2980b9]  px-2 h-12">Limpar filtro</button>
        </div>
      </div>

      <div
        v-for="(conta, i) in resultado"
        :key="i"
        :class="['conta-box', getStatusClass(conta)]"
      >
        <RouterLink :to="`/detalhesConta/${conta.id}`" class="link-conta">
          <div class="conta-info">
            <p><strong>CNPJ:</strong> {{ conta.cnpj }}</p>
            <p><strong>Descrição:</strong> {{ conta.descricao }}</p>
            <p><strong>Valor:</strong> R$ {{ formatValor(conta.valor) }}</p>
            <p>
              <strong>Vencimento:</strong>
              {{ formatDate(conta.data_vencimento) }}
            </p>
            <p>
              <strong>Status:</strong>
              {{ verificarPagamento(conta.data_pagamento, conta.data_vencimento) }}
            </p>
          </div>
        </RouterLink>
      </div>
    </div>
  </div>
</template>


<script lang="ts">
export default {
  data() {
    return {
      resultado: [] as any[],
      dataPagamento: "",
      dataVencimento: "",
      credores: [] as any,
      cnpjCredor: "",
      statusFiltro: "",
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
        if (this.cnpjCredor){
          url.searchParams.append('cnpj',this.cnpjCredor)
        }
        if(this.statusFiltro){
          url.searchParams.append('status',this.statusFiltro)
        }
        const response = await fetch(url.toString());
        const result = await response.json();
        this.resultado = result;
      } catch (error: any) {
        alert("Erro ao listar contas: " + error.Mensagem);
      }
    },
    limparFiltro() {
      this.cnpjCredor = "";
      this.dataPagamento = "";
      this.dataVencimento = "";
      this.statusFiltro = "";

      this.listarContas();
    },
    async atualizarStatusConta(
      id: number,
      dataPagamento: string,
      dataVencimento: string
    ) {
      const status = this.verificarPagamento(dataPagamento, dataVencimento);
      try {
        const url = new URL(
          `http://127.0.0.1:5000/contas/atualizarStatus/${id}`
        );

        const response = await fetch(url.toString(), {
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ status }),
        });

        if (!response.ok) {
          throw new Error("Erro ao atualizar o status da conta.");
        }
      } catch (error: any) {
        alert("Erro ao atualizar o status da conta: " + error.message);
      }
    },

    verificarPagamento(dataPagamento: string, dataVencimento: string) {
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

    getStatusClass(conta: any) {
      const status = this.verificarPagamento(
        conta.data_pagamento,
        conta.data_vencimento
      );
      switch (status) {
        case "PAGA":
          return "status-paga";
        case "ATRASADA":
          return "status-pendente";
        default:
          return "status-cancelada";
      }
    },
    formatDate(dateString: string): string {
      if (!dateString) return "";
      const date = new Date(dateString);
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, "0"); 
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
.filter-group {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin-bottom: 20px;
}

.filter-item {
  display: flex;
  flex-direction: column;
  flex: 1;
  min-width: 200px;
  padding: 10px;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.filter-item label {
  margin-bottom: 5px;
}

.filter-input {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
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
  background-color: #2980b9;
}

.search-button:active {
  background-color: #1f6d8f;
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
