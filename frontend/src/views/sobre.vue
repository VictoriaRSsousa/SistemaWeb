<template>
  <div id="aboutPage">
    <header id="headerPage" class="text-xl">
      <h1 class="text-3xl font-bold">Sobre</h1>
      <nav>
        <RouterLink to="/" >Voltar</RouterLink>
      </nav>
    </header>

    <main id="mainContent">
      <h2>Equipe de Desenvolvimento</h2>

      <ul class="team-list">
        <li>
          <strong>Samuel Bastos da Silva</strong><br>
          <a href="mailto:samuel.bastos.silva02@aluno.ifce.edu.br">samuel.bastos.silva02@aluno.ifce.edu.br</a>
        </li>
        <li>
          <strong>Luiz Kayo Souza Soares</strong><br>
          <a href="mailto:luiz.kayo.souza02@aluno.ifce.edu.br">luiz.kayo.souza02@aluno.ifce.edu.br</a>
        </li>
        <li>
          <strong>Victoria Regia Sales Sousa</strong><br>
          <a href="mailto:victoria.regia08@aluno.ifce.edu.br">victoria.regia08@aluno.ifce.edu.br</a>
        </li>
      </ul>

      <div id="content">
        Software desenvolvido durante aulas de "SISTEMAS WEB" da cadeira de Telemática do 5º semestre do Instituto Federal do Ceará. Criado com auxílio dos professores Antonio de Barros Serra e Rondinelli Moura. Foi desenvolvido utilizando Python com Flask e, para o front-end, Vue.js.
      </div>
    </main>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'Sobre',

});
</script>

<style scoped>
#headerPage {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background-color: #4caf50;
  color: white;
}

#headerPage nav a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

#headerPage nav a:hover {
  text-decoration: underline;
}

#mainContent {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  background-color: #f4f4f4;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  margin-bottom: 20px;
  color: #333;
}

.team-list {
  list-style-type: none;
  padding: 0;
}

.team-list li {
  margin-bottom: 15px;
  font-size: 18px;
}

.team-list li strong {
  color: #4caf50;
}

.team-list li a {
  color: #333;
  text-decoration: none;
}

.team-list li a:hover {
  text-decoration: underline;
}

#content {
  margin-top: 20px;
  font-size: 16px;
  line-height: 1.6;
  color: #000000;
}
</style>
