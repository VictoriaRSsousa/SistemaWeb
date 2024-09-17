 <template>
  <div class="page-container">
    <header class="page-header">
      <h1>Detalhes da Conta</h1>
      <nav>
        <RouterLink to="/listarContas" class="back-link">
          <i class="fas fa-arrow-left"></i> Voltar para Lista
        </RouterLink>
      </nav>
    </header>
    <div class="conta-details">
      <div class="conta-header">
        <h2>{{ conta?.credor?.nome }} - Conta #{{ conta?.id }}</h2>
        <div class="action-buttons">
          <RouterLink :to="`/atualizarConta/${conta.id}`" class="edit-button">
            <i class="fas fa-edit"></i> Editar
          </RouterLink>
          <button @click="apagarConta" class="delete-button">
            <i class="fas fa-trash-alt"></i> Apagar
          </button>
        </div>
      </div>
      <div class="conta-info">
        <p><strong>Descrição:</strong> {{ conta.descricao }}</p>
        <p><strong>Valor:</strong> R$ {{ conta?.valor }}</p>
        <p><strong>Juros de atraso:</strong> {{ conta?.juros }}%</p>
        <p><strong>Multa de atraso:</strong> R$ {{ conta?.multa }}</p>
        <p v-if="!conta.data_pagamento" class="total-a-pagar">
          <strong>Total a pagar:</strong> R$ {{ calcularTotal() }}
        </p>
      </div>
      <div v-if="conta.data_pagamento" class="pagamento-info">
        <p><strong>Data de pagamento:</strong></p>
        <input type="date" readonly :value="formattedDate" class="date-input" />
      </div>
      <footer v-else class="footer-actions">
        <button @click="pagarConta" class="pay-button">
          <i class="fas fa-money-bill-wave"></i> Pagar Conta
        </button>
      </footer>
    </div>
  </div>
</template>

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

          
        }

      } catch (error: any) {
        console.error(`Erro ao buscar a conta: ${error.Mensagem}`);
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
            body: JSON.stringify({ data_pagamento: new Date().toISOString().split('T')[0], valor: this.totalAPagar }), 
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
        console.error(`Erro ao pagar a conta: ${error.Mensagem}`);
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
        console.error(`Erro ao buscar a conta: ${error.Mensagem}`);
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

.conta-details {
  background-color: #f8f9fa;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.conta-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.conta-header h2 {
  font-size: 20px;
  color: #333;
}

.action-buttons {
  display: flex;
  gap: 10px;
}

.edit-button, .delete-button {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  transition: background-color 0.3s;
}

.edit-button {
  background-color: #3498db;
  color: white;
}

.delete-button {
  background-color: #e74c3c; 
  color: white;
}
</style>