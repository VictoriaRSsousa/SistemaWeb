
<script lang="ts">
import { useRoute, useRouter } from 'vue-router';

export default {
  name: "detalhesCredor",
  data() {
    return {
      route : useRoute(),
      router : useRouter(),
      credor: {} as any,
      totalAPagar: 0,
    };
  },
  methods: {
    async getCredorPorId() {
      try {
        console.log(this.route.params.cnpj);
        
        const response = await fetch(
          `http://127.0.0.1:5000/credores/${this.route.params.cnpj}`,
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
            },
          }
        );
        const data = await response.json();

        this.credor = data;
      } catch (error: any) {
        console.error(`Erro ao buscar a conta: ${error.message}`);
      }
    },

    async apagarCredor() {
      try {
        const response = await fetch(
          `http://127.0.0.1:5000/credores/remover/${this.route.params.cnpj}`,
          {
            method: "DELETE",
            headers: {
              "Content-Type": "application/json",
            },
          }
        );
        const data = await response.json();

        this.credor = data;
      } catch (error: any) {
        console.error(`Erro ao buscar a conta: ${error.message}`);
      }
    },

  },
  mounted() {
    this.getCredorPorId();
  },
};
</script>
<template>
  <div class="w-full h-screen flex flex-col gap-4 items-center py-32 justify-center bg-gray-100">
    <RouterLink to="/listarCredores">
      <p class="bg-green-500 absolute top-4 left-4 text-center md:w-[8vw] w-[20vw] m-10  text-white mr-8 px-4 py-2 font-semibold rounded-md shadow hover:bg-green-600 transition">
        Voltar
      </p>
    </RouterLink>
    <section
      class="w-[50vw]  h-[400px] bg-white shadow-lg p-6 rounded-md border border-gray-200"
    >
      <header class="flex justify-between items-center mb-4 border-b pb-3">
        <span class="flex gap-4 text-2xl font-extrabold text-gray-700">
          <p>{{credor.nome  }}</p>
        </span>
        <div class="flex gap-3">
          <RouterLink :to="`/atualizarCredor/${credor.cnpj}`" class="link-conta">
            <button
              class="w-[10vw] h-10 bg-blue-500 text-white font-bold rounded-md shadow hover:bg-blue-600 transition"
            >
              Editar
            </button>
          </RouterLink>
          <button
            class="w-[10vw] h-10 bg-red-500 text-white font-bold rounded-md shadow hover:bg-red-600 transition"
          >
            Apagar
          </button>
        </div>
      </header>
      <main class="font-medium text-gray-600">
        <div class="flex flex-col gap-3 items-start mt-10 ">
          <p ><strong>Cnpj: </strong>{{ credor.cnpj }}</p>
          <p><strong>E-mail:</strong>  {{ credor.email }}</p>
          <p><strong>Endereço:</strong> {{ credor.endereco}}</p>
          <p><strong>Telefone:</strong> {{credor.telefone }}</p>
         
        </div>
      </main>
    </section>
  </div>
</template>


