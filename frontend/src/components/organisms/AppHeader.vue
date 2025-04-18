<script setup lang="ts">
   import NewChatButton from '@/components/atoms/NewChatButton.vue';
   import ToggleMenu from '@/components/molecules/ToggleMenu.vue';
   import { ShallowRef, shallowRef } from 'vue';

   const isSidebarOpen: ShallowRef<boolean> = shallowRef(false);

   const toggleSidebar = (): void => {
      isSidebarOpen.value = !isSidebarOpen.value;
   };
</script>

<template>
   <button
      class="text-xl font-bold p-1 rounded-2xl active:bg-primary-200"
      @click="toggleSidebar"
   >
      <img class="size-12" src="@/assets/icon/menu-rounded.png" alt="menu icon" />
   </button>
   <ToggleMenu :is-sidebar-open="isSidebarOpen" :toggle-sidebar="toggleSidebar" />

   <NewChatButton />
</template>
