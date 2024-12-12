<template>
  <div id="listarContasPage">
    <header class="w-full p-5 bg-[#3498db] flex  text-white text-center shadow-md">
      <RouterLink
        to="/"
        class=" flex  items-center justify-center h-10  transition transform hover:-translate-y-1  active:translate-y-0"
      >
        <i class="fas fa-home text-2xl mr-2"></i>
      </RouterLink>
      <h1 class="text-2xl font-semibold mx-auto">Listar Contas</h1>
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
              @keyup.enter="getAllAccounts"
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
              @change="getAllAccounts"
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
          <div class="flex gap-2">

            <!-- <button
              @click="getAllAccounts()"
              class="rounded-md my-auto bg-[#2980b9] text-white px-2 h-10"
            >
              Pesquisar
            </button> -->
            <button
              @click="cleanFilter()"
              class="rounded-md my-auto border border-[#2980b9] text-[#2980b9] px-2 h-10"
            >
              Limpar filtro
            </button>
          </div>
        </div>
      </div>

      <div v-for="(account, i) in accounts" :key="i" class="">
        <div
          class="w-[70vw] mx-auto bg-white border border-gray-300 rounded-lg shadow-lg p-6 space-y-4 mb-3"
        >
        <RouterLink
          :to="`/detalhesConta/${account.id}`"
          class="link-conta"
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
      </RouterLink>
        </div>
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
