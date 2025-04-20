<script setup lang="ts">
   import MainLayout from '@/page/layout/MainLayout.vue';
   import AppFooter from '@/components/organisms/AppFooter.vue';
   import AppHeader from '@/components/organisms/AppHeader.vue';
   import { useTopicQuestion } from '@/composables/useChatBot';

   const props = defineProps<{ question: string }>();
   const primaryQuestion = useTopicQuestion(props.question);
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
