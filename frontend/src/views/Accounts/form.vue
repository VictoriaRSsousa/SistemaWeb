<template>
  <div class="max-w-2xl mx-auto p-6">
    <header
      class="flex justify-between items-center mb-8 pb-4 border-b-2 border-blue-500"
    >
      <nav>
        <RouterLink to="/" class="text-blue-500 font-medium">
          <i class="fas fa-arrow-left"></i> Voltar
        </RouterLink>
      </nav>
      <span class="text-2xl text-blue-500 font-medium">
        <p v-if="isRegisterForm()">Cadastrar Nova Conta</p>
        <p v-else>Atualizar conta</p>
      </span>
    </header>
    <div class="bg-gray-100 p-8 rounded-lg shadow-md">
      <form @submit.prevent="validateFields">
        <div class="mb-6">
          <label for="cnpj" class="block mb-2 font-medium text-gray-700"
            >CNPJ:</label
          >
          <input
            v-model="account.credor.cnpj"
            type="text"
            id="cnpj"
            class="w-full p-2 border border-gray-300 rounded-md"
          />
        </div>
        <div class="mb-6">
          <label for="valor" class="block mb-2 font-medium text-gray-700"
            >Valor:</label
          >
          <input
            v-model="account.valor"
            type="number"
            step="0.01"
            class="w-full p-2 border border-gray-300 rounded-md"
          />
        </div>
        <div class="mb-6">
          <label for="descricao" class="block mb-2 font-medium text-gray-700"
            >Descrição:</label
          >
          <input
            v-model="account.descricao"
            type="text"
            id="descricao"
            class="w-full p-2 border border-gray-300 rounded-md"
          />
        </div>
        <div class="mb-6">
          <label
            for="data_vencimento"
            class="block mb-2 font-medium text-gray-700"
            >Data de Vencimento:</label
          >
          <input
            v-model="account.data_vencimento"
            type="date"
            id="data_vencimento"
            class="w-full p-2 border border-gray-300 rounded-md"
          />
        </div>
        <div class="mb-6">
          <label for="multa" class="block mb-2 font-medium text-gray-700"
            >Multa:</label
          >
          <input
            v-model="account.multa"
            type="number"
            id="multa"
            step="0.01"
            class="w-full p-2 border border-gray-300 rounded-md"
          />
        </div>
        <div class="mb-6">
          <label for="juros" class="block mb-2 font-medium text-gray-700"
            >Juros:</label
          >
          <input
            v-model="account.juros"
            type="number"
            id="juros"
            step="0.01"
            class="w-full p-2 border border-gray-300 rounded-md"
          />
        </div>
        <div class="mb-6">
          <label
            for="data_pagamento"
            class="block mb-2 font-medium text-gray-700"
            >Data de Pagamento (Opcional):</label
          >
          <input
            v-model="account.data_pagamento"
            type="date"
            id="data_pagamento"
            class="w-full p-2 border border-gray-300 rounded-md"
          />
        </div>
        <button
          type="submit"
          class="bg-blue-500 text-white flex gap-2 items-center px-4 py-3 rounded-md font-medium hover:bg-blue-600 transition-colors"
        >
          <i class="fas fa-plus-circle"></i>
          <p v-if="isRegisterForm()">Adicionar Conta</p>
          <p v-else>Atualizar conta</p>
        </button>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import Account from "../../models/account.model";
import useVuelidate from "@vuelidate/core";
import { minLength, minValue, required } from "@vuelidate/validators";
import { validateCnpj } from "../../utils/validator.util";
import { AccountService } from "./account.service";
import { take } from "rxjs";
import { Toasts } from "../../utils/toasts.util";

export default {
  setup() {
    return { v$: useVuelidate() };
  },
  validations() {
    return {
      account: {
        credor: {
          cnpj: { required, validateCnpj },
        },
        valor: { required, minValue: minValue(1) },
        descricao: { required, minLength: minLength(5) },
        data_vencimento: { required },
        multa: { required },
        juros: { required },
      },
    };
  },
  data() {
    return {
      account: new Account(""),
      showToast: new Toasts(),
    };
  },
  methods: {
    validateFields() {
      this.v$.$validate();
      if (this.account.data_pagamento === "") {
        this.account.data_pagamento = undefined;
      }
      if (!this.v$.$error && this.isRegisterForm()) {
        this.registerAccount();
      } else if (!this.v$.$error && !this.isRegisterForm()) {
        this.updateAccount();
      }
    },
    registerAccount() {
      this.account.cnpj = this.account.credor.cnpj;
      this.account.status = this.verifyStatusAccount(
        this.account.data_vencimento,
        this.account.data_pagamento as string
      );
      this.service.account.pipe(take(1)).subscribe({
        next: (response) => {
          this.showToast.showSuccess("Conta cadastrada!", response.Mensagem);
          this.clearForm()
        },
        error: () => {
          this.showToast.showError();
        },
      });
      this.service.register(this.account);
    },
    updateAccount() {
      this.account.status = this.verifyStatusAccount(
        this.account.data_vencimento,
        this.account.data_pagamento as string
      );
      this.account.cnpj = this.account.credor.cnpj
      // // if (this.account.data_pagamento === "") {
      // //   this.account.data_pagamento = undefined;
      // // }
      //  console.log(this.account);
      

      this.service.account.pipe(take(1)).subscribe({
        next: (response) => {  
          this.showToast.showSuccess("Conta atualizada!", response.Mensagem);
        },
        error: () => {
          this.showToast.showError();
        },
      });
      this.service.update(this.account, this.accountId);
    },
    clearForm(){
      this.account = new Account("");
    },
    getAccountByCnpj() {
      this.service.account.pipe(take(1)).subscribe({
        next: (response) => {
          this.account = response;
          this.account.data_pagamento = this.formatDate(
            this.account.data_pagamento as string
          );
          this.account.data_vencimento = this.formatDate(
            this.account.data_vencimento
          );
        },
      });
      this.service.getById(this.accountId);
    },
    verifyStatusAccount(dataVencimento: string, dataPagamento: string) {
      const due = new Date(`${dataVencimento}T00:00:00`);
      const today = new Date();

      const normalizeDate = (date: Date) =>
        new Date(date.getFullYear(), date.getMonth(), date.getDate());
      const dueDateNormalized = normalizeDate(due);
      const todayDateNormalized = normalizeDate(today);

      if (dataPagamento) {
        return "PAGA";
      } else {
        return dueDateNormalized >= todayDateNormalized ? "ABERTA" : "ATRASADA";
      }
    },

    isRegisterForm(): boolean {
      return this.$route.path === "/adicionarConta";
    },
    verifyRequestForm(): void {
      if (!this.isRegisterForm()) {
        this.getAccountByCnpj();
      }
    },
    formatDate(dateString: string): string {
      if (!dateString) return "";
      const date = new Date(dateString);
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, "0");
      const day = String(date.getDate() + 1).padStart(2, "0");
      return `${year}-${month}-${day}`;
    },
  },
  computed: {
    service(): AccountService {
      return new AccountService();
    },
    accountId(): number {
      return Number(this.$route.params.id);
    },
  },
  mounted() {
    this.verifyRequestForm();
  },
};
</script>
