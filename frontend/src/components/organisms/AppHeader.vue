<script setup lang="ts">
   import NewChatButton from '@/components/atoms/NewChatButton.vue';
   import ToggleMenu from '@/components/molecules/ToggleMenu.vue';
   import { useToggleMenu } from '@/composable/useToggleMenu';

   const { isSidebarOpen, toggleSidebar } = useToggleMenu();
</script>

<template>
   <button
      class="text-xl font-bold p-1 rounded-2xl active:bg-primary-200"
      @click="toggleSidebar"
   >
      <img class="size-12" src="@/assets/icon/menu-rounded.png" alt="menu icon" />
   </button>
   <ToggleMenu :isSidebarOpen="isSidebarOpen" :toggleSidebar="toggleSidebar" />
   <NewChatButton />
</template>
