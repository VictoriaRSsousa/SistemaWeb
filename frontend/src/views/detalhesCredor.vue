<template>
  <div class="page-container">
    <header class="page-header">
      <h1>Detalhes do Credor</h1>
      <nav>
        <RouterLink to="/listarCredores" class="back-link">
          <i class="fas fa-arrow-left"></i> Voltar para Lista
        </RouterLink>
      </nav>
    </header>
    <div class="conta-details">
      <div class="conta-header">
        <h2>{{ credor.nome }}</h2>
        <div class="action-buttons">
          <RouterLink :to="`/atualizarCredor/${credor.cnpj}`" class="edit-button">
            <i class="fas fa-edit"></i> Editar
          </RouterLink>
          <button @click="apagarCredor" class="delete-button">
            <i class="fas fa-trash-alt"></i> Apagar
          </button>
        </div>
      </div>
      <div class="conta-info">
        <p><strong>CNPJ:</strong> {{ credor.cnpj }}</p>
        <p><strong>E-mail:</strong> {{ credor.email }}</p>
        <p><strong>Endereço:</strong> {{ credor.endereco }}</p>
        <p><strong>Telefone:</strong> {{ credor.telefone }}</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { useRoute,useRouter } from 'vue-router';

export default {
  name: 'detalhesCredor',
  data() {
    return {
      route: useRoute(),
      router: useRouter(),
      credor: {} as any,
    };
  },
  methods: {
    async getCredorPorId() {
      try {
        const response = await fetch(`http://127.0.0.1:5000/credores/${this.route.params.cnpj}`);
        const data = await response.json();
        this.credor = data;
      } catch (error:any) {
        console.error(`Erro ao buscar o credor: ${error.Mensagem}`);
      }
    },
    async apagarCredor() {
      try {
        await fetch(`http://127.0.0.1:5000/credores/remover/${this.route.params.cnpj}`, { method: 'DELETE' });
        this.router.push('/listarCredores');
      } catch (error:any) {
        console.error(`Erro ao apagar o credor: ${error.Mensagem}`);
      }
    },
  },
  mounted() {
    this.getCredorPorId();
  },
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

.delete-button:hover {
  background-color: #c0392b;
}

.conta-info p {
  margin: 10px 0;
}
</style>