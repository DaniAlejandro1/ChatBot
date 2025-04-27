<script setup lang="ts">
   import MainLayout from '@/page/layout/MainLayout.vue';
   import AppFooter from '@/components/organisms/AppFooter.vue';
   import AppHeader from '@/components/organisms/AppHeader.vue';
   import { useTopicQuestion } from '@/composables/useChatBot';
   import { useChatsStore } from '@/stores/chat';
   import { ref, watch, nextTick } from 'vue';

   const store = useChatsStore();
   const props = defineProps<{
      question: string;
      id: string;
   }>();

   const state = ref('LOADING');
   const { primaryQuestion, response } = await useTopicQuestion(props.question);
   setTimeout(() => {
      state.value = 'SUCCESS';
   }, 500);

   const chatContainer = ref<HTMLElement | null>(null);

   // Se valida que la ID no exista previamente antes de crear el chat
   if (!store.isPresentChat(Number.parseInt(props.id))) {
      store.addChat({
         id: Number(props.id),
         title: primaryQuestion.value,
         message: [],
      });

      store.addMessageToChat(Number(props.id), primaryQuestion.value, response);
   }

   const addMessage = (id: number, message: string, response: string): void => {
      store.addMessageToChat(id, message, response);
   };

   const chats = store.getChatMessages(Number(props.id));

   watch(
      chats,
      async () => {
         await nextTick();
         if (chatContainer.value) {
            chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
         }
      },
      { deep: true }
   );
</script>

<template>
   <MainLayout>
      <template #header>
         <AppHeader />
      </template>

      <template #main>
         <article
            ref="chatContainer"
            class="size-full flex flex-col py-2 bg-gray-50 gap-2 overflow-y-auto box-border h-full"
         >
            <!-- Skeleton Loader -->
            <div v-if="state === 'LOADING'" class="flex flex-col gap-3 p-4">
               <div class="w-full h-fit flex justify-end items-center">
                  <div
                     class="w-2/3 h-6 bg-gray-300 rounded-t-2xl rounded-bl-2xl animate-pulse"
                  ></div>
               </div>
               <div class="w-full h-fit flex justify-start items-center">
                  <div
                     class="w-1/2 h-6 bg-gray-300 rounded-t-2xl rounded-br-2xl animate-pulse"
                  ></div>
               </div>
            </div>

            <!-- Chat Messages -->
            <div v-else v-for="chat in chats" :key="chat.id" class="flex flex-col gap-3 p-4">
               <div class="w-full h-fit flex justify-end items-center">
                  <p
                     class="body-1 font-semibold text-right p-3 bg-primary-200 rounded-t-2xl rounded-bl-2xl"
                  >
                     {{ chat.question }}
                  </p>
               </div>
               <div class="w-full h-fit flex justify-start items-center">
                  <p
                     class="body-1 font-semibold text-left p-3 bg-gray-300 rounded-t-2xl rounded-br-2xl"
                  >
                     {{ chat.response }}
                  </p>
               </div>
            </div>
         </article>
      </template>

      <template #footer>
         <AppFooter :is-first-question="false" :id="id" :addMessage="addMessage" />
      </template>
   </MainLayout>
</template>
