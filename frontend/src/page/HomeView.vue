<script setup lang="ts">
   import MainLayout from '@/page/layout/MainLayout.vue';
   import AppFooter from '@/components/organisms/AppFooter.vue';
   import AppHeader from '@/components/organisms/AppHeader.vue';
   import TopicButton from '@/components/atoms/TopicButton.vue';
   import { topyc } from '@/utils/constants';
</script>

<template>
   <MainLayout>
      <template #header>
         <AppHeader />
      </template>

      <template #main>
         <section class="w-full h-fit flex flex-col items-center gap-2">
            <header class="flex flex-col gap-3">
               <h1 class="header-1 text-left">
                  <strong class="text-primary-500">
                     Estoy aquí para ayudarte.
                  </strong>
                  Dime en qué puedo ayudarte.
               </h1>
               <p class="header-2 italic xl:text-center">
                  ¡Cuéntame tu duda y con gusto <br />te asistiré!
               </p>
            </header>
         </section>

         <section class="w-full h-fit grid grid-cols-1 gap-4 xl:grid-cols-2">
            <TopicButton
               v-for="(item, index) in topyc"
               :key="index"
               :title="item.title"
               :description="item.description"
               :img="item.img"
            />
         </section>
      </template>

      <template #footer>
         <AppFooter />
      </template>
   </MainLayout>
</template>
