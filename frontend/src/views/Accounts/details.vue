<template>
      <ConfirmDialog></ConfirmDialog>

  <div class="max-w-2xl mx-auto p-5">
    <header
      class="flex justify-between items-center mb-8 pb-4 border-b-2 border-blue-500"
    >
      <RouterLink
        to="/listarContas"
        class="text-blue-500 font-medium hover:underline flex items-center gap-2"
      >
        <i class="fas fa-arrow-left"></i> Voltar para Lista
      </RouterLink>

      <h1 class="text-2xl font-semibold text-blue-500">Detalhes da Conta</h1>
    </header>

    <div class="bg-gray-100 p-6 rounded-lg shadow-lg">
      <div class="flex justify-between items-center mb-5">
        <h2 class="text-xl font-medium text-gray-800">
          {{ account?.credor?.nome }} - Conta #{{ account?.id }}
        </h2>
        <div class="flex gap-3">
          <RouterLink
            :to="`/atualizarConta/${account.id}`"
            class="bg-blue-500 text-white px-4 py-2 rounded-lg font-medium transition hover:bg-blue-600 flex items-center gap-2"
          >
            <i class="fas fa-edit"></i> Editar
          </RouterLink>
          <button
            @click="confirmDelete"
            class="bg-red-500 text-white px-4 py-2 rounded-lg font-medium transition hover:bg-red-600 flex items-center gap-2"
          >
            <i class="fas fa-trash-alt"></i> Apagar
          </button>
        </div>
      </div>

      <div class="space-y-2">
        <p><strong>Descrição:</strong> {{ account.descricao }}</p>
        <p><strong>Valor:</strong> R$ {{ account?.valor }}</p>
        <span class="flex">
          <p><strong>Juros de atraso:</strong> {{ account?.juros }}%</p>
          <p>X {{ daysLate }} dias.</p>
        </span>
        <p><strong>Multa de atraso:</strong> R$ {{ account?.multa }}</p>
        <p v-if="!account.data_pagamento" class="font-bold">
          <strong>Total a pagar:</strong> R$ {{ totalToPay }}
        </p>
      </div>

      <div v-if="account.data_pagamento" class="mt-4">
        <p><strong>Data de pagamento:</strong></p>
        <input
          type="date"
          readonly
          :value="formateDate(account.data_pagamento)"
          class="mt-1 px-4 py-2 border rounded-md w-full"
        />
      </div>

      <footer v-else class="mt-6">
        <button
          @click="confirmPayment"
          class="flex items-center gap-2 px-5 py-3 bg-red-500 text-white rounded-lg font-bold text-lg transition hover:bg-red-600 active:scale-95 focus:outline-none focus:ring-2 focus:ring-pink-500"
        >
          <i class="fas fa-money-bill-wave"></i> Pagar Conta
        </button>
      </footer>
    </div>
  </div>
</template>

<script lang="ts">
import { useConfirm } from "primevue/useconfirm";
import { take } from "rxjs";
import Account from "../../models/account.model";
import { AccountService } from "./account.service";
import { Toasts } from "../../utils/toasts.util";

export default {
  name: "detalhesConta",
  data() {
    return {
      totalToPay: 0,
      showToasts: new Toasts(),
      account: new Account(""),
      daysLate: 0,
      confirm: useConfirm()
    };
  },
  methods: {
    getAccountById() {
      this.service.account.pipe(take(1)).subscribe({
        next: (response) => {
          this.account = response;
          this.calcularTotal();
          if (this.account.data_pagamento) {
            this.formateDate(this.account.data_pagamento as string);
          }
        },
      });
      this.service.getById(this.accountId);
    },
    formateDate(date: string) {
      const data = new Date(date);
      const ano = data.getFullYear();
      const dia = (data.getDate() + 1).toString().padStart(2, "0");
      const mes = (data.getMonth() + 1).toString().padStart(2, "0");
      return `${ano}-${mes}-${dia}`;
    },
    confirmPayment(){
      this.confirm.require({
                message: 'Você tem certeza que quer continuar?',
                header: 'Confirmação de pagamento',
              //  icon: 'pi pi-bell',
                rejectProps: {
                    label: 'Cancelar',
                    severity: 'secondary',
                    outlined: true
                },
                acceptProps: {
                    label: 'Pagar'
                },
                accept: () => {
                  this.payAccount()
                    //this.$toast.add({ severity: 'info', summary: 'Confirmed', detail: 'You have accepted', life: 3000 });
                },
                reject: () => {
                    //this.$toast.add({ severity: 'error', summary: 'Rejected', detail: 'You have rejected', life: 3000 });
                }
            });
    },
    payAccount() {
      this.account.data_vencimento = this.formateDate(
        this.account.data_vencimento
      );
      (this.account.data_pagamento = new Date().toISOString().split("T")[0]),
        (this.account.valor = this.totalToPay);
      this.account.cnpj = this.account.credor.cnpj;
      this.account.status = "PAGA";

      this.service.account.pipe(take(1)).subscribe({
        next: (response) => {
          this.getAccountById();
          this.showToasts.showSuccess("Pagamento efetuado!", response.Mensagem);
        },
      });
      this.service.update(this.account, this.accountId);
    },
    confirmDelete(){
      this.confirm.require({
        message: 'Você tem certeza que quer continuar?',
                header: 'Confirmação de exclusão',
               // icon: 'pi pi-exclamation-triangle',
                rejectProps: {
                    label: 'Cancelar',
                    severity: 'secondary',
                    outlined: true
                },
                acceptProps: {
                    label: 'Deletar'
                  },
                accept: () => {
                  this.deleteAccount()
                    //this.$toast.add({ severity: 'info', summary: 'Confirmed', detail: 'You have accepted', life: 3000 });
                },
                reject: () => {
                    //this.$toast.add({ severity: 'error', summary: 'Rejected', detail: 'You have rejected', life: 3000 });
                }
            });
    },

    deleteAccount() {
      this.service.account.pipe(take(1)).subscribe({
        next: () => {
          this.$router.push("/listarContas");
        },
      });
      this.service.delete(this.accountId);
    },
    calcularTotal() {
      this.totalToPay = this.account.valor;

      const vencimento = new Date(this.account.data_vencimento);
      const today = new Date();

      const porcentagem = this.totalToPay * (this.account.juros / 100);

      if (this.account.status === "ABERTA") {
        this.totalToPay = Number(this.account.valor) as number;
      } else {
        this.totalToPay += Number(this.account.multa) as number;
        const oneDay = (24 * 60 * 60 * 1000) as number;
        this.daysLate = Math.floor(
          (today.getTime() - vencimento.getTime()) / oneDay
        ) as number;
        this.totalToPay = this.totalToPay + porcentagem * this.daysLate;
      }
    },
  },
  mounted() {
    this.getAccountById();
  },
  computed: {
    service(): AccountService {
      return new AccountService();
    },
    accountId(): number {
      return Number(this.$route.params.id);
    },
  },
};
</script>

<style scoped>
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css");
</style>
