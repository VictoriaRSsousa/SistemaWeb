<template>
  <div id="listarContasPage">
    <header class="w-full p-5 bg-[#3498db] text-white text-center shadow-md">
      <h1 class="text-2xl font-semibold">Listar Contas</h1>
      <RouterLink
        to="/"
        class="w-[15vw] flex items-center justify-center h-10 px-5 bg-white text-gray-800 rounded-md transition transform hover:-translate-y-1 shadow-md hover:shadow-lg active:translate-y-0"
      >
        <i class="fas fa-home text-2xl mr-2"></i>
        <span>Voltar</span>
      </RouterLink>
    </header>

    <div id="listarContasContent" class="m-4">
      <div class="filters-container">
        <div class="filter-group flex flex-wrap justify-end gap-5 mb-5">
          <div
            class="filter-item flex flex-col w-[20vw] min-w-[200px] p-2 bg-white rounded-md shadow-md"
          >
            <label for="cnpjCredor" class="font-bold mb-1">CNPJ:</label>
            <input
              v-model="query.cnpj"
              type="text"
              id="cnpjCredor"
              class="filter-input p-2 border border-gray-300 rounded-md text-base"
            />
          </div>
          <div
            class="filter-item flex flex-col w-[20vw] min-w-[200px] p-2 bg-white rounded-md shadow-md"
          >
            <label for="status" class="font-bold mb-1">Status:</label>
            <select
              v-model="query.status"
              id="status"
              class="filter-input p-2 border border-gray-300 rounded-md text-base"
            >
              <option value="">Todos</option>
              <option value="PAGA">Paga</option>
              <option value="ATRASADA">Atrasada</option>
              <option value="ABERTA">Aberta</option>
            </select>
          </div>
          <div
            class="filter-item flex flex-col w-[20vw] min-w-[200px] p-2 bg-white rounded-md shadow-md"
          >
            <label for="dataPagamento" class="font-bold mb-1"
              >Data de pagamento:</label
            >
            <input
              @change="getAllAccounts()"
              type="date"
              v-model="query.data_pagamento"
              id="dataPagamento"
              class="filter-input p-2 border border-gray-300 rounded-md text-base"
            />
          </div>
          <div
            class="filter-item flex flex-col w-[20vw] min-w-[200px] p-2 bg-white rounded-md shadow-md"
          >
            <label for="dataVencimento" class="font-bold mb-1"
              >Data de vencimento:</label
            >
            <input
              @change="getAllAccounts()"
              v-model="query.data_vencimento"
              type="date"
              id="dataVencimento"
              class="filter-input p-2 border border-gray-300 rounded-md text-base"
            />
          </div>
          <button
            @click="getAllAccounts()"
            class="rounded-md my-auto bg-[#2980b9] text-white px-3 h-12"
          >
            Pesquisar
          </button>
          <button
            @click="cleanFilter()"
            class="rounded-md my-auto border border-[#2980b9] text-[#2980b9] px-2 h-12"
          >
            Limpar filtro
          </button>
        </div>
      </div>

      <div v-for="(account, i) in accounts" :key="i" class="">
        <!-- <RouterLink :to="`/detalhesConta/${account.id}`" class="link-conta">
          <div class="conta-info p-4 mb-2 rounded-md shadow-md">
            <p class="my-1"><strong>CNPJ:</strong> {{ account.cnpj }}</p>
            <p class="my-1"><strong>Descrição:</strong> {{ account.descricao }}</p>
            <p class="my-1"><strong>Valor:</strong> R$ {{ formatValor(account.valor) }}</p>
            <p class="my-1"><strong>Vencimento:</strong> {{ formatDate(String(account.data_vencimento)) }}</p>
            <p class="my-1"><strong>Status:</strong> {{ account.status }}</p>
          </div>
        </RouterLink> -->
        <RouterLink
          :to="`/detalhesConta/${account.id}`"
          class="link-conta"
        >
        <div
          class="w-[70vw] mx-auto bg-white border border-gray-300 rounded-lg shadow-lg p-6 space-y-4 mb-3"
        >
          <div class="flex justify-between items-center">
            <h3 class="text-lg font-semibold text-gray-700">
              Detalhes da Conta
            </h3>
            <span
              class="px-3 py-1 w-[10vw] text-center text-xs font-bold rounded-full"
              :class="getStatusClass(account.status)"
            >
              {{ account.status }}
            </span>
          </div>
          <div class="text-sm text-gray-600">
            <p><strong>CNPJ:</strong> {{ account.cnpj }}</p>
            <p><strong>Descrição:</strong> {{ account.descricao }}</p>
            <p><strong>Valor: </strong> R${{ formatValor(account.valor) }}</p>
            <p>
              <strong>Vencimento:</strong>
              {{ formatDate(account.data_vencimento) }}
            </p>
          </div>
        </div>
      </RouterLink>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import Account from "../../models/account.model";
import QueryParams from "../../models/queryParams.model";
import { AccountService } from "./account.service";

export default {
  data() {
    return {
      resultado: [] as any[],
      dataPagamento: "",
      dataVencimento: "",
      credores: [] as any,
      cnpjCredor: "",
      statusFiltro: "",
      accounts: [] as Array<Account>,
      query: new QueryParams(),
    };
  },
  methods: {
    getAllAccounts() {
      this.service.accounts.pipe().subscribe({
        next: (response) => {
          this.accounts = response;
        },
      });
      this.service.getAll(this.query);
    },
    cleanFilter() {
      this.query = new QueryParams();
      this.getAllAccounts();
    },

    getStatusClass(status: string) {
      switch (status) {
        case "PAGA":
          return "text-green-700 bg-green-100";
        case "ATRASADA":
          return "text-red-700 bg-red-100";
        case "ABERTA":
          return "text-blue-700 bg-blue-100";
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
  },
  mounted() {
    this.getAllAccounts();
  },
  computed: {
    service(): AccountService {
      return new AccountService();
    },
  },
};
</script>
