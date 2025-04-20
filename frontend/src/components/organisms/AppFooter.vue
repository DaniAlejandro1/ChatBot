<script setup lang="ts"></script>

<template>
   <input
      type="text"
      placeholder="Escribe un mensaje..."
      class="w-full h-2/3 xl:h-4/5 px-3 border-[1.5px] body-1 placeholder:body-1 border-font-500 rounded-2xl box-border"
   />
   <button
      class="flex items-center justify-center h-2/3 w-24 xl:h-4/5 bg-primary-500 rounded-2xl cursor-pointer hover:bg-primary-300 active:bg-primary-300 active:scale-95"
   >
      <img class="w-10 xl:w-8" src="@/assets/icon/send-solid.png" alt="send solid" />
   </button>
</template>
