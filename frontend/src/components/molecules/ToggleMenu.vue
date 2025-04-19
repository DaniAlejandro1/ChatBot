<script setup lang="ts">
   const props = defineProps<{
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
      v-if="props.isSidebarOpen"
      class="fixed top-0 left-0 h-full w-full bg-font-600"
      aria-label="Sidebar de historial de chats"
   >
      <header
         class="p-4 flex justify-between items-center border-b border-background-default"
      >
         <h2 class="header-3 text-background-default">Historial de Chats</h2>
         <button
            @click="toggleSidebar"
            class="text-background-default header-3 font-bold cursor-pointer py-1.5 px-3 rounded-4xl hover:bg-primary-400 active:bg-primary-400"
            aria-label="Cerrar sidebar"
         >
            ✕
         </button>
      </header>
      <nav>
         <ul
            class="flex flex-col gap-3 p-4 body-1 text-background-default hover:bg-primary-300 hover:text-font-500 cursor-pointer overflow-y-scroll"
         >
            <li
               v-for="(chat, index) in chats"
               :key="index"
               class="flex flex-row p-2 items-center border-[1.5px] border-background-default bg-font-400 rounded-lg overflow-hidden active:bg-primary-300"
            >
               <img
                  class="size-7"
                  src="@/assets/icon/history-rounded.png"
                  alt="history icon"
               />
               <button
                  class="block w-full text-left px-2 p-2"
                  :aria-label="'Abrir ' + chat"
               >
                  {{ chat }}
               </button>
            </li>
         </ul>
      </nav>
   </aside>
</template>
