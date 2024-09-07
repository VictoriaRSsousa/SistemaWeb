<template>
  <div id="homePage">
    <header class="flex w-full justify-center font-bold text-xl p-5 bg-[#4caf50] text-white items-center">
      <h1 class="text-3xl">Bem-vindo ao Sistema de Contas a Pagar</h1>
  </header>

    <div id="homeContent">
      <RouterLink to="/listarContas">
        <button class="navButton">Contas</button>
      </RouterLink>
      <RouterLink to="/adicionarConta">
        <button class="navButton">Adicionar Conta</button>
      </RouterLink>
      <RouterLink to="/adicionarCredor">
        <button class="navButton">Adicionar Credor</button>
      </RouterLink>
      <RouterLink to="/sobre">
        <button class="navButton">Sobre</button>
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
#homePage {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: 'Roboto', sans-serif;
  min-height: 100vh;
  background-color: #f5f5f5;
}

#headerPage {
  width: 100%;
  padding: 20px;
  background-color: #4caf50;
  color: white;
  text-align: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

#homeContent {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  margin-top: 50px;
}

.navButton {
  padding: 15px 40px;
  font-size: 20px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.navButton:hover {
  background-color: #388e3c;
  transform: translateY(-2px);
}

.navButton:active {
  background-color: #2e7d32;
  transform: translateY(0);
}
</style>
