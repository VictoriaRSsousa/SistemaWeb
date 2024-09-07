<template>
    <h1>detalhes</h1>
    <p>{{conta.credor.cnpj}}</p>
    <p>{{conta}}</p>
    <p>{{conta.descricao}}</p>
</template>
<script lang="ts">

export default{
data(){
    return{
        conta:{} as any
    }
},
methods:{
    async getContaPorId(){
        try {
            const response = await fetch(`http://127.0.0.1:5000/conta/${this.$route.params.id}`)
            console.log(response);
            
        const result = await response.json();
        console.log(result);
        
        this.conta = result;
      } catch (error:any) {
        alert("Erro ao listar contas: " + error.message);
      }
    }
},
mounted() {
    this.getContaPorId()
}
}
</script>