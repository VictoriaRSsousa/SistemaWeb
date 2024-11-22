<template>
  <div class="page-container max-w-2xl mx-auto p-6 font-roboto">
    <header
      class="flex justify-between items-center mb-8 pb-3 border-b-2 border-blue-600"
    >
      <nav>
        <RouterLink
          to="/"
          class="text-blue-600 font-medium no-underline hover:underline"
        >
          <i class="fas fa-arrow-left"></i> Voltar
        </RouterLink>
      </nav>
      <h1 class="text-2xl text-blue-600">
        {{
          isRegisterForm() ? "Cadastrar novo credor" : "Editar dados do credor"
        }}
      </h1>
    </header>

    <div class="bg-gray-100 p-6 rounded-lg shadow-md">
      <form @submit.prevent="validateFields">
        <div class="mb-5">
          <label for="cnpj" class="block mb-1 font-medium text-gray-800"
            >CNPJ:</label
          >
          <input
            v-model="creditor.cnpj"
            type="text"
            id="cnpj"
            class="input-field"
            :class="v$.creditor.cnpj.$error ? 'border-red-600' : ''"
          />
          <p
            class="text-xs text-red-600 transition-all"
            :class="
              v$.creditor.cnpj.$error
                ? 'opacity-100'
                : '-translate-y-6 opacity-0 invisible'
            "
          >
            Cnpj inválido.
          </p>
        </div>

        <div class="mb-5">
          <label for="nome" class="block mb-1 font-medium text-gray-800"
            >Nome:</label
          >
          <input
            v-model="creditor.nome"
            type="text"
            id="nome"
            class="input-field"
            :class="v$.creditor.nome.$error ? 'border-red-600' : ''"
          />
          <p
            :class="
              v$.creditor.nome.$error
                ? 'opacity-100'
                : '-translate-y-6 opacity-0 invisible'
            "
            class="text-xs text-red-600 transition-all"
          >
            Nome inválido. Somente letras.
          </p>
        </div>

        <div class="mb-5">
          <label for="endereco" class="block mb-1 font-medium text-gray-800"
            >Endereço:</label
          >
          <input
            v-model="creditor.endereco"
            type="text"
            id="endereco"
            class="input-field"
            :class="v$.creditor.endereco.$error ? 'border-red-600' : ''"
          />
          <p
            :class="
              v$.creditor.endereco.$error
                ? 'opacity-100'
                : '-translate-y-6 opacity-0 invisible'
            "
            class="text-xs text-red-600 transition-all"
          >
            Endereço inválido.
          </p>
        </div>

        <div class="mb-5 relative">
          <label for="telefone" class="block mb-1 font-medium text-gray-800"
            >Telefone:</label
          >
          <input
            v-model="creditor.telefone"
            type="text"
            id="telefone"
            class="input-field"
            :class="v$.creditor.telefone.$error ? 'border-red-600' : ''"
          />
          <p
            :class="[
              'text-xs text-red-600 absolute left-0 transition-all duration-300 ease-in-out',
              v$.creditor.telefone.$error
                ? 'opacity-100 translate-y-0 visible'
                : 'opacity-0 -translate-y-2 invisible',
            ]"
          >
            Telefone inválido. Formato: (xx)xxxxx-xxxx
          </p>
        </div>

        <div class="mb-5">
          <label for="email" class="block mb-1 font-medium text-gray-800"
            >E-mail:</label
          >
          <input
            v-model="creditor.email"
            type="email"
            id="email"
            class="input-field"
            :class="v$.creditor.email.$error ? 'border-red-600' : ''"
          />
          <p
            :class="
              v$.creditor.email.$error
                ? 'opacity-100'
                : '-translate-y-6 opacity-0 invisible'
            "
            class="text-xs text-red-600 transition-all"
          >
            Email inválido.
          </p>
        </div>

        <button
          type="submit"
          class="flex items-center gap-2 bg-blue-600 text-white px-5 py-3 rounded-md hover:bg-blue-700 transition duration-300"
        >
          <i class="fas fa-user-plus"></i>
          <p>
            {{ isRegisterForm() ? "Adicionar credor" : "Atualizar credor" }}
          </p>
        </button>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import Creditor from "../../models/creditor.model";
import { CreditorService } from "./creditor.service";
import { take } from "rxjs";
import { useVuelidate } from "@vuelidate/core";
import { email, minLength, required } from "@vuelidate/validators";
import {
  validateName,
  validatePhone,
  validateCnpj,
} from "../../utils/validator.util";
import { defineComponent } from "vue";
import { Toasts } from "../../utils/toasts.util";

export default defineComponent({
  setup() {
    return { v$: useVuelidate() };
  },
  name: "form-creditor",
  validations() {
    return {
      creditor: {
        cnpj: { required, validateCnpj },
        email: { required, email },
        endereco: { required, minLength: minLength(5) },
        nome: { required, validateName },
        telefone: { required, validatePhone },
      },
    };
  },
  data() {
    return {
      creditor: new Creditor(),
      showToast: new Toasts(),
    };
  },
  methods: {
    validateFields() {
      this.v$.$validate();
      if (!this.v$.$error) {
        if (this.isRegisterForm()) {
          this.registerCreditor();
        } else {
          this.updateCreditor();
        }
      }
    },

    registerCreditor() {
      this.service.creditor.pipe(take(1)).subscribe({
        next: (response) => {
          console.log(response);
          this.showToast.showSuccess("Cadastro realizado!", response.Mensagem);
        },
        error: () => {
          this.showToast.showError();
        },
      });
      this.service.register(this.creditor);
    },
    updateCreditor() {
      this.service.creditor.pipe(take(1)).subscribe({
        next: (response) => {
          console.log(response);
          this.showToast.showSuccess("Cadastro atualizado!", response.Mensagem);
        },
        error: () => {
          this.showToast.showError();
        },
      });
      this.service.update(this.creditor, this.cnpj);
    },
    isRegisterForm(): boolean {
      return this.$route.path === "/adicionarCredor";
    },
    getCreditorByCnpj() {
      this.service.creditor.pipe(take(1)).subscribe({
        next: (response) => {
          this.creditor = response;
        },
      });
      this.service.getByCnpj(this.cnpj);
    },
    verifyRequestForm(): void {
      if (!this.isRegisterForm()) {
        this.getCreditorByCnpj();
      }
    },
  },

  mounted() {
    this.verifyRequestForm();
  },
  computed: {
    service(): CreditorService {
      return new CreditorService();
    },
    cnpj(): string {
      return this.$route.params.cnpj as string;
    },
  },
});
</script>
