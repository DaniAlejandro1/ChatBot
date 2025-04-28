<script setup lang="ts">
   import MainLayout from '@/page/layout/MainLayout.vue';
   import AppFooter from '@/components/organisms/AppFooter.vue';
   import AppHeader from '@/components/organisms/AppHeader.vue';
   import { useChatsStore } from '@/stores/chat';
   import { ref, watch } from 'vue';
   import { useRoute } from 'vue-router';



   import type { Conversation } from '@/utils/types';

   const route = useRoute();
   const store = useChatsStore();
   

   const id = Number(route.params.index)
   
   const conversationList = ref<Conversation[]>(store.getConversation(id));

   console.log('index', id);
   console.log("conversaciones, ",conversationList.value)
   console.log("all", useChatsStore().getAllConversations());


   const response = async (message: string): Promise<string> => {
   const res = await fetch(
      `http://localhost:8000/chat?topico=${encodeURIComponent(message)}`
   );
   const data = await res.json();

   return data;
};

   response(conversationList.value[0].question).then((res) => {
      store.setResponse(id, res); 
   }).catch((error) => {
      console.error('Error fetching response:', error);
   });
   


   

   
   
   
   watch(

      () => conversationList.value,
      () => 
      async () => {
        try {

            
          //store.setResponse(id, 'respuesta llegada');
        } catch (error) {
          console.error('Error al obtener la respuesta:', error);
        }
      }

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
            

            <!-- Chat Messages -->
            <div v-for="(chat, index) in conversationList" :key="index" class="flex flex-col gap-3 p-2">
                  <div class="w-full h-fit flex justify-end items-center">
                     <p
                        class="body-1 font-semibold text-right p-4 bg-primary-200 rounded-t-2xl rounded-bl-2xl max-w-[90%]"
                     >
                        {{ chat.question }}
                     </p>
                  </div>

                  <!-- Skeleton Loader -->
                  <div v-if="chat.response === ''" class="flex flex-col gap-3 p-2">
                     <div class="w-full h-fit flex justify-start items-center">
                        <div
                           class="h-10 bg-gray-300 rounded-t-2xl rounded-br-2xl animate-pulse max-w-[90%] w-full"
                        ></div>
                     </div>
                  </div>

                  <!-- Mensaje de respuesta -->
                  <div v-else class="w-full h-fit flex justify-start items-center">
                     <p
                        class="body-1 font-semibold text-left p-4 bg-gray-300 rounded-t-2xl rounded-br-2xl max-w-[80%]"
                     >
                        {{ chat.response }}
                     </p>
                  </div>
            </div>

            
         </article>
      </template>

      <template #footer>
         <AppFooter :index="id "  />
      </template>
   </MainLayout>
</template>
