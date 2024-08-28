<template>
    <div id="homePage">
      <header id="headerPage">
        <h1>Bem-vindo ao Sistema de Contas a Pagar</h1>
      </header>
  
      <div id="homeContent">
        <RouterLink to="/listarContas">
          <button id="contasButton">Contas</button>
        </RouterLink>
        <RouterLink to="/sobre">
          <button id="sobreButton">Sobre</button>
        </RouterLink>
        <RouterLink to="/adicionarConta">
        <button id="adicionarButton">Adicionar Conta</button>
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
  #headerPage {
    padding: 20px;
    background-color: #4caf50;
    color: white;
    text-align: center;
  }
  
  #homeContent {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    height: 60vh;
  }
  
  button {
    padding: 15px 30px;
    font-size: 18px;
    background-color: #4caf50;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #388e3c;
  }
  </style>
  