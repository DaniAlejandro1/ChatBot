<script setup lang="ts">
   import { RouterView } from 'vue-router';
</script>

<template>
   <Suspense>
      <RouterView :key="String($route.params.index)" />
   </Suspense>
</template>
