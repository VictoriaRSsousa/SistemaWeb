s<template>
  <div id="homePage">
    <header class="header">
      <h1>Sistema de Gestão Financeira</h1>
      <p>Controle suas contas com facilidade</p>
    </header>

    <div id="homeContent">
      <div class="button-group">
        <RouterLink to="/listarContas" class="navButton">
          <i class="fas fa-list-ul"></i>
          <span>Contas</span>
        </RouterLink>
        <RouterLink to="/listarCredores" class="navButton">
          <i class="fas fa-users"></i>
          <span>Credores</span>
        </RouterLink>
      </div>
      <div class="button-group">
        <RouterLink to="/adicionarConta" class="navButton">
          <i class="fas fa-plus-circle"></i>
          <span>Nova Conta</span>
        </RouterLink>
        <RouterLink to="/adicionarCredor" class="navButton">
          <i class="fas fa-user-plus"></i>
          <span>Novo Credor</span>
        </RouterLink>
      </div>
      <RouterLink to="/sobre" class="navButton about-button">
        <i class="fas fa-info-circle"></i>
        <span>Sobre</span>
      </RouterLink>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  name: 'Home',
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css');

#homePage {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: 'Poppins', sans-serif;
  min-height: 100vh;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.header {
  width: 100%;
  padding: 40px 20px;
  background-color: #3498db;
  color: white;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.header h1 {
  font-size: 2.5rem;
  margin: 0;
  font-weight: 600;
}

.header p {
  font-size: 1.2rem;
  margin-top: 10px;
  font-weight: 300;
}

#homeContent {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 30px;
  margin-top: 50px;
  width: 80%;
  max-width: 600px;
}

.button-group {
  display: flex;
  gap: 20px;
  width: 100%;
}

.navButton {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
  font-size: 18px;
  background-color: #ffffff;
  color: #333;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-decoration: none;
}

.navButton i {
  font-size: 24px;
  margin-bottom: 10px;
}

.navButton:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
}

.navButton:active {
  transform: translateY(0);
}

.about-button {
  background-color: #f39c12;
  color: white;
}

.about-button:hover {
  background-color: #e67e22;
}

@media (max-width: 768px) {
  .button-group {
    flex-direction: column;
  }
  
  #homeContent {
    width: 90%;
  }
}
</style>
