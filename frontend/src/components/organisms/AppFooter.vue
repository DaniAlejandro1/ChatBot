<script setup lang="ts">
   import router from '@/router/route';
   import { watch, ShallowRef, shallowRef } from 'vue';

   const question: ShallowRef<string> = shallowRef<string>('');
   const props = defineProps<{ isFirstQuestion: boolean }>();
   const errorMessage: ShallowRef<string> = shallowRef<string>('');

   const goToChat = (question: string): void => {
      if (props.isFirstQuestion && question.length > 0) {
         router.push({ name: 'chat', params: { question } });
      } else {
         errorMessage.value = 'Por favor, escribe un mensaje.';
      }
   };

   watch(question, () => {
      if (question.value.length > 0) {
         errorMessage.value = '';
      }
   });
</script>

<template>
   <input
      v-model="question"
      required
      type="text"
      placeholder="Escribe un mensaje..."
      :class="[
         'w-full h-2/3 xl:h-4/5 px-3 border-[1.5px] body-1 placeholder:body-1 rounded-2xl box-border',
         errorMessage.length > 0 ? 'border-red-600' : 'border-font-500',
      ]"
   />
   <button
      class="flex items-center justify-center h-2/3 w-24 xl:h-4/5 bg-primary-500 rounded-2xl cursor-pointer hover:bg-primary-300 active:bg-primary-300 active:scale-95"
      @click="goToChat(question)"
   >
      <img class="w-10 xl:w-8" src="@/assets/icon/send-solid.png" alt="send solid" />
   </button>
   <p class="absolute text-red-600 -top-4 left-4">{{ errorMessage }}</p>
</template>
