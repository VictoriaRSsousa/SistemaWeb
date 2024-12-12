<template>
  <ConfirmDialog></ConfirmDialog>
  <div class="max-w-3xl mx-auto p-5 font-roboto">
    <header class="flex justify-between items-center mb-8 pb-2 border-b-2 border-blue-600">
      <h1 class="text-2xl text-blue-600">Detalhes do Credor</h1>
      <nav>
        <RouterLink to="/listarCredores" class="text-blue-600 font-medium">
          <i class="fas fa-arrow-left"></i> Voltar para Lista
        </RouterLink>
      </nav>
    </header>
    <div class="bg-gray-100 p-8 rounded-lg shadow-md">
      <div class="flex justify-between items-center mb-5">
        <h2 class="text-xl text-gray-800">{{ creditor.nome }}</h2>
        <div class="flex gap-2">
          <RouterLink :to="`/atualizarCredor/${creditor.cnpj}`" class="bg-blue-600 text-white px-4 py-2 rounded transition hover:bg-blue-700">
            <i class="fas fa-edit"></i> Editar
          </RouterLink>
          <button @click="confirmDelete" class="bg-red-600 text-white px-4 py-2 rounded transition hover:bg-red-700">
            <i class="fas fa-trash-alt"></i> Apagar
          </button>
        </div>
      </div>
      <div>
        <p class="mb-2"><strong>CNPJ:</strong> {{ creditor.cnpj }}</p>
        <p class="mb-2"><strong>E-mail:</strong> {{ creditor.email }}</p>
        <p class="mb-2"><strong>Endereço:</strong> {{ creditor.endereco }}</p>
        <p class="mb-2"><strong>Telefone:</strong> {{ creditor.telefone }}</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { CreditorService } from './creditor.service';
import { take } from 'rxjs';
import Creditor from '../../models/creditor.model';
import { useConfirm } from 'primevue';

export default {
  name: 'deatails-creditor',
  data() {
    return {
      creditor: {} as Creditor,
      confirm:useConfirm()
      
    };
  },
  methods: {
    getCreditorByCnpj(){
      this.service.creditor.pipe(take(1)).subscribe({
        next:(response)=>{
          this.creditor = response
        }
      })
      this.service.getByCnpj(this.cnpj)
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
                  this.deleteCreditor()
                    //this.$toast.add({ severity: 'info', summary: 'Confirmed', detail: 'You have accepted', life: 3000 });
                },
                reject: () => {
                    //this.$toast.add({ severity: 'error', summary: 'Rejected', detail: 'You have rejected', life: 3000 });
                }
            });
    },
    deleteCreditor(){
      this.service.creditor.pipe(take(1)).subscribe({
        next:()=>{
          this.$router.push('/listarCredores')
        },
        error:(error)=>{
          console.log(error);
          
        }
      })
      this.service.delete(this.cnpj)
    }
  },
  computed:{
    service(): CreditorService{
      return new CreditorService()
    },
    cnpj():string{
      return this.$route.params.cnpj as string
    }
  },
  mounted() {
    this.getCreditorByCnpj();
  },
};
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css');
