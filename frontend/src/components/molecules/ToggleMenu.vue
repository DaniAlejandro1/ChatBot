<script setup lang="ts">
   defineProps<{
      isSidebarOpen: boolean;
      toggleSidebar: () => void;
   }>();

   const chats: string[] = [
      'Chat 1, no ando creativo',
      'Chat 2, no ando creativo',
      'Chat 3, no ando creativo',
   ];
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
               v-for="(chat, index) in chats"
               :key="index"
               class="flex flex-row p-2 items-center border-[1.5px] border-background-default bg-font-400 rounded-lg overflow-hidden hover:bg-primary-300 active:bg-primary-300"
            >
               <img
                  class="size-7"
                  src="@/assets/icon/history-rounded.png"
                  alt="history icon"
               />
               <button
                  class="block w-full text-left px-2 p-2 cursor-pointer"
                  :aria-label="'Abrir ' + chat"
               >
                  {{ chat }}
               </button>
            </li>
         </ul>
      </nav>
   </aside>
</template>
