<template>
  <div id="aboutPage" class="flex flex-col items-center">
    <header id="headerPage" class="w-full flex justify-between items-center p-5 bg-[#2980b9] text-white">
      <nav>
        <RouterLink to="/" class="text-white font-bold hover:underline">
          <i class="fas fa-home text-2xl mr-2"></i>
          </RouterLink>
      </nav>
      <h1 class="text-3xl font-bold mx-auto">Sobre</h1>
    </header>

    <main id="mainContent" class="max-w-2xl w-full mt-5 p-5 bg-[#f4f4f4] rounded-lg shadow-lg">
      <h2 class="text-center mb-4 text-2xl font-bold uppercase text-black">Equipe de Desenvolvimento</h2>

      <ul class="list-none p-0">
        <li class="mb-4 text-lg">
          <strong class="text-[#2980b9]">Samuel Bastos da Silva</strong><br>
          <a href="mailto:samuel.bastos.silva02@aluno.ifce.edu.br" class="text-[#333] hover:underline">samuel.bastos.silva02@aluno.ifce.edu.br</a>
        </li>
        <li class="mb-4 text-lg">
          <strong class="text-[#2980b9]">Luiz Kayo Souza Soares</strong><br>
          <a href="mailto:luiz.kayo.souza02@aluno.ifce.edu.br" class="text-[#333] hover:underline">luiz.kayo.souza02@aluno.ifce.edu.br</a>
        </li>
        <li class="mb-4 text-lg">
          <strong class="text-[#2980b9]">Victoria Regia Sales Sousa</strong><br>
          <a href="mailto:victoria.regia08@aluno.ifce.edu.br" class="text-[#333] hover:underline">victoria.regia08@aluno.ifce.edu.br</a>
        </li>
      </ul>

      <div id="content" class="mt-5 text-base leading-6 text-black">
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
