<template>
  <div id="detalhesPage" class="page-container">
    <RouterLink to="/listarCredores">
      <p class="back-button">Voltar</p>
    </RouterLink>
    <section class="details-card">
      <header class="details-header">
        <span class="title">{{ credor.nome }}</span>
        <div class="actions">
          <RouterLink :to="`/atualizarCredor/${credor.cnpj}`" class="edit-button">
            Editar
          </RouterLink>
          <button @click="apagarCredor" class="delete-button">
            Apagar
          </button>
        </div>
      </header>
      <main class="details-info">
        <p><strong>CNPJ:</strong> {{ credor.cnpj }}</p>
        <p><strong>E-mail:</strong> {{ credor.email }}</p>
        <p><strong>Endereço:</strong> {{ credor.endereco }}</p>
        <p><strong>Telefone:</strong> {{ credor.telefone }}</p>
      </main>
    </section>
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
.page-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: #f5f7fa;
  min-height: 100vh;
}

.back-button {
  background-color: #3498db;
  color: white;
  padding: 10px 20px;
  border-radius: 12px;
  text-align: center;
  cursor: pointer;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s;
}

.back-button:hover {
  background-color: #2980b9;
}

.details-card {
  width: 80%;
  max-width: 600px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

.details-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #ddd;
  padding-bottom: 10px;
  margin-bottom: 20px;
}

.title {
  font-size: 1.5rem;
  font-weight: bold;
  color: #333;
}

.actions {
  display: flex;
  gap: 10px;
}

.edit-button {
  background-color: #3498db;
  color: white;
  padding: 10px 20px;
  border-radius: 8px;
  text-align: center;
  text-decoration: none;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s;
}

.edit-button:hover {
  background-color: #2980b9;
}

.delete-button {
  background-color: #e74c3c;
  color: white;
  padding: 10px 20px;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s;
}

.delete-button:hover {
  background-color: #c0392b;
}

.details-info p {
  margin: 10px 0;
}
</style>

