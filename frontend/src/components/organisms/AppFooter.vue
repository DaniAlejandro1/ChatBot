<script setup lang="ts">
   import router from '@/router/route';
   import { useChatsStore } from '@/stores/chat';
   import { ref } from 'vue';
   
   
   
   const props = defineProps<{
      index: number;
   }>();

   const store = useChatsStore();
   const inputValue = ref<string>('');
   const showError = ref<boolean>(false);

   const response = async (message: string): Promise<string> => {
   const res = await fetch(
      `http://localhost:8000/chat?topico=${encodeURIComponent(message)}`
   );
   const data = await res.json();

   return data;
};




   async function setInputValue(index: number): Promise<void> {
      if (inputValue.value.trim() === '') {
         showError.value = true;
         return; // No envía si el input está vacío
      }

      store.setConversation(index, {
         question: inputValue.value,
         response: '',
      });
      store.setResponse(index, await response(inputValue.value)); // Limpiar la respuesta anterior
      inputValue.value = ''; 
      router.push({ name: 'chat', params: { index: index } });
   }

</script>

<template>
   <input
      v-model="inputValue"
      required
      type="text"
      placeholder="Escribe un mensaje..."
      :class="[
         'w-full h-[50%] xl:h-4/5 px-3 border-[1.5px] body-1 placeholder:body-1 rounded-2xl box-border',
         showError ? 'border-red-600' : 'border-font-500',
      ]"
      @input="showError = false"
   />
   <button
      class="flex items-center justify-center h-[50%] w-24 xl:h-4/5 bg-primary-500 rounded-2xl cursor-pointer hover:bg-primary-300 active:bg-primary-300 active:scale-95"
      @click="setInputValue(props.index)"
   >
      <img class="w-8 xl:w-8" src="@/assets/icon/send-solid.png" alt="send solid" />
   </button>
   <p v-if="showError" class="absolute text-red-600 -top-4 left-4">Escribe un mensaje</p>
</template>
