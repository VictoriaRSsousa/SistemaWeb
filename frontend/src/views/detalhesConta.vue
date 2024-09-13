
<script lang="ts">
import { useRoute, useRouter } from 'vue-router';

export default {
  name: "detalhesConta",
  data() {
    return {
      route : useRoute(),
      router : useRouter(),
      conta: {} as any,
      totalAPagar: 0,
      formattedDate: '',
    };
  },
  methods: {
    async getContaPoRiD() {
      try {
        const response = await fetch(
          `http://127.0.0.1:5000/contas/${this.route.params.id}`,
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
            },
          }
        );
        const data = await response.json();
        this.conta = data
        if (this.conta.data_pagamento) {
          const data = new Date(this.conta.data_pagamento)
          const ano = data.getFullYear()
          const dia = (data.getDate()+1).toString().padStart(2, '0')
          const mes = (data.getMonth() + 1).toString().padStart(2, '0')
          this.formattedDate = `${ano}-${mes}-${dia}`  
          console.log(data);

          
          console.log(this.formattedDate);
          
          
        }

      } catch (error: any) {
        console.error(`Erro ao buscar a conta: ${error.message}`);
      }
    },
    async pagarConta() {
      try {
        const response = await fetch(
          `http://127.0.0.1:5000/contas/pagar/${this.route.params.id}`,
          {
            method: "PATCH",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ data_pagamento: new Date().toISOString().split('T')[0], valor: this.totalAPagar }), // Formata a data para ISO 8601
          }
        );

       
        if (!response.ok) {
          throw new Error(`Erro ao pagar a conta: ${response.statusText}`);
        }

        const data = await response.json();
        this.conta = data; 
        alert("Pagamento efetuado com sucesso!");
        window.location.reload()
      } catch (error: any) {
        console.error(`Erro ao pagar a conta: ${error.message}`);
      }
    },
    async apagarConta() {
      try {
        const response = await fetch(
          `http://127.0.0.1:5000/contas/remover/ ${this.route.params.id}`,
          {
            method: "DELETE",
            headers: {
              "Content-Type": "application/json",
            },
          }
        );
        const data = await response.json();

        this.conta = data;
      } catch (error: any) {
        console.error(`Erro ao buscar a conta: ${error.message}`);
      }
    },
    calcularTotal() {
      const vencimento = new Date(this.conta.data_vencimento);
      let pagamento = new Date(this.conta.data_pagamento);

      if (!this.conta.data_pagamento) {
        pagamento = new Date();
      }
      this.totalAPagar = Number(this.conta.valor) || 0;

      if (pagamento > vencimento) {
        this.totalAPagar += Number(this.conta.multa) || 0;

        const um_dia = 24 * 60 * 60 * 1000;
        const dias_atraso = Math.ceil(
          (pagamento.getTime() - vencimento.getTime()) / um_dia
        );

        this.totalAPagar += (Number(this.conta.juros) || 0) * dias_atraso;
      }

      return this.totalAPagar;
    },
    dateToString() {
    return this.conta.data_pagamento.toString().substr(0,10)
  }
  },
  mounted() {
    this.getContaPoRiD();
  },
  computed:{
  }
};
</script>
<template>
  <div class="w-full h-screen flex flex-col gap-4 items-center py-32 justify-center bg-gray-100">
    <RouterLink to="/listarContas">
      <p class="bg-green-500 absolute top-4 left-4 text-center md:w-[8vw] w-[20vw] m-10  text-white mr-8 px-4 py-2 font-semibold rounded-md shadow hover:bg-green-600 transition">
        Voltar
      </p>
    </RouterLink>
    <section
      class="w-[50vw]  h-[400px] bg-white shadow-lg p-6 rounded-md border border-gray-200"
    >
      <header class="flex justify-between items-center mb-4 border-b pb-3">
        <span class="flex gap-4 text-2xl font-extrabold text-gray-700">
          <h3>{{ conta?.id }}</h3>
          <p>{{ conta?.credor?.nome }}</p>
        </span>
        <div class="flex gap-3">
          <RouterLink :to="`/atualizarConta/${conta.id}`" class="link-conta">
            <button
              class="w-[10vw] h-10 bg-blue-500 text-white font-bold rounded-md shadow hover:bg-blue-600 transition"
            >
              Editar
            </button>
          </RouterLink>
          <button
            class="w-[10vw] h-10 bg-red-500 text-white font-bold rounded-md shadow hover:bg-red-600 transition"
            @click="apagarConta"
          >
            Apagar
          </button>
        </div>
      </header>
      <main class="font-medium text-gray-600">
        <p class="text-lg text-center mb-4">{{ conta.descricao }}</p>
        <div class="flex flex-col gap-2 items-start">
          <p><strong>Valor:</strong> R$ {{ conta?.valor }}</p>
          <p><strong>Juros de atraso:</strong> {{ conta?.juros }}%</p>
          <p><strong>Multa de atraso:</strong> R$ {{ conta?.multa }}</p>
          <p
            v-if="!conta.data_pagamento"
            class="w-full flex items-end justify-end text-xl font-semibold text-red-600"
          >
            Total a pagar: R$ {{ calcularTotal() }}
          </p>
        </div>
      </main>
      <div v-if="conta.data_pagamento" class="mt-6 w-full flex justify-center flex flex-col gap-2 items-center">
        <label for="" class="font-bold">Data de pagamento:</label>
        <input type="date" readonly :value="formattedDate"  class="border px-3 py-2 rounded border-black"/>
      </div>
      <footer v-else class="mt-6 flex justify-end">
        <button
          class="bg-red-500 text-white w-[10vw] h-10 font-bold rounded-md shadow hover:bg-red-600 transition"
          @click="pagarConta"
        >
          Pagar Conta
        </button>
      </footer>
    </section>
  </div>
</template>


