<script setup lang="ts">
   import { useChatsStore } from '@/stores/chat';
   import { computed } from 'vue';
   import router from '@/router/route';

   const goChat = (question: string, id: string) => {
      router.push({ name: 'chat', params: { question, id } });
   };

   const store = useChatsStore();

   const chats = computed(() => store.chatHistory);

   defineProps<{
      isSidebarOpen: boolean;
      toggleSidebar: () => void;
   }>();
</script>

<template>
   <aside
      v-if="isSidebarOpen"
      class="fixed top-0 left-0 h-full w-full xl:w-2/5 bg-font-600"
      aria-label="Sidebar de historial de chats"
   >
      <header class="p-4 flex justify-between items-center border-b border-background-default">
         <h2 class="header-3 text-background-default">Historial de Chats</h2>
         <button
            @click="toggleSidebar"
            class="text-background-default header-3 font-bold cursor-pointer py-1.5 px-3 rounded-4xl hover:bg-primary-400 active:bg-primary-400"
            aria-label="Cerrar sidebar"
         >
            ✕
         </button>
      </header>
      <nav class="size-full">
         <ul
            class="size-full flex flex-col gap-3 p-4 body-1 text-background-default overflow-y-auto"
         >
            <li
               v-for="(chat, id) in chats"
               :key="id"
               class="flex flex-row p-2 items-center border-[1.5px] border-background-default bg-font-400 rounded-lg overflow-hidden"
            >
               <img
                  class="size-7"
                  src="@/assets/icon/history-rounded.png"
                  alt="history icon"
               />
               <button
                  class="w-full text-left px-2 p-2 mr-2 cursor-pointer"
                  :aria-label="'Abrir ' + chat.title"
                  @click="goChat(chat.title, chat.id.toString())"
               >
                  {{ chat.title }}
               </button>
               <button
                  class="bg-red-500 active:bg-red-300 rounded-md w-fit text-left px-2 p-2 cursor-pointer"
                  :aria-label="'Abrir ' + chat.title"
                  @click="useChatsStore().deleteChatById(chat.id)"
               >
                  Borrar
               </button>
            </li>
         </ul>
      </nav>
   </aside>
</template>
