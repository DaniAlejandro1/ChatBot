<script setup lang="ts">
   import MainLayout from '@/page/layout/MainLayout.vue';
   import AppFooter from '@/components/organisms/AppFooter.vue';
   import AppHeader from '@/components/organisms/AppHeader.vue';
   import { useTopicQuestion } from '@/composables/useChatBot';
   import { useChatsStore } from '@/stores/chat';

   const store = useChatsStore();
   const props = defineProps<{ question: string }>();

   const { primaryQuestion, response } = useTopicQuestion(props.question);

   store.addChat({
      id: store.lengthChats + 1,
      title: primaryQuestion.value,
      message: [
         {
            question: primaryQuestion.value,
            response: response.value,
         },
      ],
   });

   console.log('Cantidad de chats', store.lengthChats);
   console.log('Chats', store.chats);
</script>

<template>
   <MainLayout>
      <template #header>
         <AppHeader />
      </template>

      <template #main>
         <article class="size-full flex flex-col gap-2 bg-amber-200">
            <p>{{ primaryQuestion }}</p>
            <p>{{ response }}</p>
         </article>
      </template>

      <template #footer>
         <AppFooter :is-first-question="false" />
      </template>
   </MainLayout>
</template>
