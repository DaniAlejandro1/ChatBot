<script setup lang="ts">
   import { useChatsStore } from '@/stores/chat';
   import { computed } from 'vue';
   import router from '@/router/route';

   const goChat = (index: number) => {
      router.push({ name: 'chat', params: { index: index } });
   };

   const store = useChatsStore();

   const chats = computed(() => store.getAllConversations());

   defineProps<{
      isSidebarOpen: boolean;
      toggleSidebar: () => void;
   }>();
</script>

<template>
   <Transition name="fade-slide">
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
                  v-for="(chat, index) in chats"
                  :key="index"
                  class="flex flex-row p-2 items-center border-[1.5px] border-background-default bg-font-400 rounded-lg overflow-hidden"
               >
                  <img
                     class="size-7"
                     src="@/assets/icon/history-rounded.png"
                     alt="history icon"
                  />
                  <button
                     class="w-full text-left px-2 p-2 mr-2 cursor-pointer"
                     :aria-label="'Abrir ' + chat[0].question"
                     @click="goChat(index)"
                  >
                     {{ chat[0].question }}
                  </button>
                  <button
                     class="bg-red-500 active:bg-red-300 rounded-md w-fit text-left px-2 p-2 cursor-pointer"
                     :aria-label="'Abrir ' + chat[0].question"
                     @click="useChatsStore().removeConversation(index)"
                  >
                     Borrar
                  </button>
               </li>
            </ul>
         </nav>
      </aside>
   </Transition>
</template>

<style scoped>
.fade-slide-enter-active, .fade-slide-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}
.fade-slide-enter-from, .fade-slide-leave-to {
  opacity: 0;
  transform: translateX(-100%);
}
.fade-slide-enter-to, .fade-slide-leave-from {
  opacity: 1;
  transform: translateX(0);
}
</style>
