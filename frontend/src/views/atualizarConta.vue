  <template>
    <div class="page-container">
      <header class="page-header">
        <h1>Editar Conta</h1>
        <nav>
          <RouterLink :to="`/detalhesConta/${route.params.id}`" class="back-link">
            <i class="fas fa-arrow-left"></i> Voltar
          </RouterLink>
        </nav>
      </header>
      <div class="form-container">
        <form @submit.prevent="editarConta">
          <div class="form-group">
            <label for="descricao">Descrição:</label>
            <input type="text" id="descricao" v-model="conta.descricao" required />
          </div>
          <div class="form-group">
            <label for="valor">Valor:</label>
            <input type="number" id="valor" v-model="conta.valor" step="0.01" required />
          </div>
          <div class="form-group">
            <label for="data_vencimento">Data de Vencimento:</label>
            <input type="date" id="data_vencimento" v-model="conta.data_vencimento" required />
          </div>
          <div class="form-group" v-if="conta.data_pagamento">
            <label for="data_pagamento">Data de Pagamento:</label>
            <input type="date" id="data_pagamento" v-model="conta.data_pagamento" required />
          </div>
          <div class="form-group">
            <label for="multa">Multa:</label>
            <input type="number" id="multa" v-model="conta.multa" step="0.01" required />
          </div>
          <div class="form-group">
            <label for="juros">Juros:</label>
            <input type="number" id="juros" v-model="conta.juros" step="0.01" required />
          </div>
          <button type="submit" class="submit-button">
            <i class="fas fa-save"></i> Salvar Alterações
          </button>
        </form>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { useRoute, useRouter } from 'vue-router';
  
  export default{
    name: 'EditarConta',
    data(){
      return{
         route : useRoute(),
         router : useRouter(),
         conta : {
          descricao: '',
          valor: 0,
          data_vencimento: '',
          data_pagamento: null,
          multa: 0,
          juros: 0,
          status: '',
          credor: {
                nome: '',
                cnpj:'',
            }
        }

      }
    } ,
  methods:{

    async fetchConta()  {
      try {

        const response = await fetch(`http://127.0.0.1:5000/contas/${this.route.params.id}`);
        const data = await response.json();
        if (data) {
          this.conta = {
            ...data,
            data_vencimento: this.formatDate(data.data_vencimento),
            data_pagamento : this.formatDate(data.data_pagamento) 
          };
        }
      } catch (error:any) {
        alert('Erro ao buscar conta: ' + error.Mensagem);
      }
    },

    async editarConta (){
      if(!this.conta.data_pagamento){
          this.conta.data_pagamento = null
        }
      this.conta. status = this.verificarPagamento(this.conta.data_pagamento,this.conta.data_vencimento)
      try {

        const response = await fetch(`http://127.0.0.1:5000/contas/atualizar/${this.route.params.id}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({...this.conta,credor:{nome:this.conta.credor.nome,cnpj:this.conta.credor.cnpj}}),
        });
        const result = await response.json();
        if (response.ok) {
          alert('Conta atualizada com sucesso!');
          this.router.push(`/detalhesConta/${this.route.params.id}`);
        } else {
          alert('Erro ao atualizar conta: ' + result.Mensagem);
        }
      } catch (error:any) {
        alert('Erro ao atualizar conta: ' + error.Mensagem);
      }
    },
    formatDate(dateString: string): string {
      if (!dateString) return '';
      const date = new Date(dateString);
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0'); 
      const day = String(date.getDate()+1).padStart(2, '0');
      return `${year}-${month}-${day}`;
    },
    verificarPagamento(dataPagamento: any, dataVencimento: any) {
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
  },
  mounted() {
      this.fetchConta()
  },}
  
  </script>
  
  
  <style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css');

.page-container {
  font-family: 'Roboto', sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  padding-bottom: 10px;
  border-bottom: 2px solid #3498db;
}

.page-header h1 {
  font-size: 24px;
  color: #3498db;
}

.back-link {
  color: #3498db;
  text-decoration: none;
  font-weight: 500;
}

.form-container {
  background-color: #f8f9fa;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: 500;
  color: #333;
}

input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ced4da;
  border-radius: 4px;
  font-size: 16px;
}

.submit-button {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 500;
  transition: background-color 0.3s;
}

.submit-button:hover {
  background-color: #2980b9;
}
</style>