<template>
    <div id="sobre">
      <header id="sobre">
        <h1>Sobre... aqui um pagina de dedicação de autoria desse Sistema  </h1>
      </header>
  
      <div id="homeContent">
        <RouterLink to="/">
          <button id="homeButton">Menu Principal</button>
        </RouterLink>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  export default {
    name: 'sobre',
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
    height: 60vh;
  }
  
  #contasButton {
    padding: 15px 30px;
    font-size: 18px;
    background-color: #4caf50;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
  }
  
  #contasButton:hover {
    background-color: #388e3c;
  }
  </style>
  