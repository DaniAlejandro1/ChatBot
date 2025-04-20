<script setup lang="ts">
   import type { Topic } from '@/utils/types';
   import { useImagePath } from '@/composables/useImg';

   const props = defineProps<Topic>();
</script>

<template>
   <article
      class="flex flex-row items-center justify-evenly p-2.5 xl:h-24 border-button interaction-button"
   >
      <img class="size-8 mx-2" :src="useImagePath(props.img).value" :alt="props.title" />

      <div class="w-full pl-4">
         <h2 class="header-3">{{ props.title }}</h2>
         <p class="body-1">
            {{ props.description }}
         </p>
      </div>
   </article>
</template>
