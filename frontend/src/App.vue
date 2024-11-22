<template>
  <main>
    <Toast/>
    <RouterView />
  </main>
</template>
<script lang="ts">

import { RouterView } from 'vue-router';

export default {
    components: {
        RouterView

}
}
</script>
