<script setup lang="ts">
   import MainLayout from '@/page/layout/MainLayout.vue';
   import AppFooter from '@/components/organisms/AppFooter.vue';
   import AppHeader from '@/components/organisms/AppHeader.vue';
</script>

<template>
   <MainLayout>
      <template #header>
         <AppHeader />
      </template>

      <template #main>
         <h2>main</h2>
      </template>

      <template #footer>
         <AppFooter />
      </template>
   </MainLayout>
</template>
