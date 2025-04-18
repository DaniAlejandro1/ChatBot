<script setup lang="ts">
   const props = defineProps<{
      isSidebarOpen: boolean;
      toggleSidebar: () => void;
   }>();
</script>

<template>
   <div>
      <div
         v-if="props.isSidebarOpen"
         class="fixed top-0 left-0 h-full w-64 bg-white shadow-lg border-r border-gray-300 z-50"
      >
         <div class="p-4 flex justify-between items-center border-b border-gray-300">
            <h2 class="text-lg font-bold">Sidebar</h2>
            <button @click="toggleSidebar" class="text-gray-500 hover:text-gray-700">
               ✕
            </button>
         </div>
         <ul class="py-4">
            <li>
               <button class="block w-full text-left px-4 py-2 hover:bg-gray-100">
                  Opción 1
               </button>
            </li>
            <li>
               <button class="block w-full text-left px-4 py-2 hover:bg-gray-100">
                  Opción 2
               </button>
            </li>
            <li>
               <button class="block w-full text-left px-4 py-2 hover:bg-gray-100">
                  Opción 3
               </button>
            </li>
         </ul>
      </div>
   </div>
</template>
