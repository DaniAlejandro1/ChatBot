<script setup lang="ts">
   import router from '@/router/route';

   const goToHome = (): void => {
      router.push({ name: 'home' });
   };
</script>

<template>
   <button class="body-1 px-4 py-1 border-button interaction-button" @click="goToHome">
      + Nuevo Chat
   </button>
</template>
