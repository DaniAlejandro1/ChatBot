<script setup lang="ts">
   import MainLayout from '@/page/layout/MainLayout.vue';
   import AppFooter from '@/components/organisms/AppFooter.vue';
   import AppHeader from '@/components/organisms/AppHeader.vue';
   import { TOPIC, TOPIC_DESCRIPTION } from '@/utils/enums';
   import { computed } from 'vue';

   const props = defineProps<{
      question: string;
   }>();

   const primaryQuestion = computed(() => {
      if (props.question === TOPIC.CLIMA) {
         return TOPIC_DESCRIPTION.CLIMA;
      } else if (props.question === TOPIC.DOLAR) {
         return TOPIC_DESCRIPTION.DOLAR;
      } else if (props.question === TOPIC.UF) {
         return TOPIC_DESCRIPTION.UF;
      } else if (props.question === TOPIC.NOTICIAS) {
         return TOPIC_DESCRIPTION.NOTICIAS;
      } else {
         return props.question;
      }
   });
</script>

<template>
   <MainLayout>
      <template #header>
         <AppHeader />
      </template>

      <template #main>
         <article class="size-full flex flex-col gap-2 bg-amber-200">
            <p>{{ primaryQuestion }}</p>
         </article>
      </template>

      <template #footer>
         <AppFooter />
      </template>
   </MainLayout>
</template>
