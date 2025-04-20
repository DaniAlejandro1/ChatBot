<script setup lang="ts">
   import { computed, ComputedRef } from 'vue';
   import cloudIcon from '@/assets/icon/cloud.png';
   import moneyCalcIcon from '@/assets/icon/money-calculator.png';
   import moneyIcon from '@/assets/icon/money-alt.png';
   import newsIcon from '@/assets/icon/news.png';
   import type { Topic } from '@/utils/types';

   const props = defineProps<Topic>();

   const imageMap: Record<string, string> = {
      'cloud.png': cloudIcon,
      'money-calculator.png': moneyCalcIcon,
      'money-alt.png': moneyIcon,
      'news.png': newsIcon,
   };

   const imagePath: ComputedRef<string> = computed(() => {
      return imageMap[props.img] || '';
   });
</script>

<template>
   <article
      class="flex flex-row items-center justify-evenly p-2.5 xl:h-24 box-border border-[1.5px] border-font-500 rounded-2xl active:bg-primary-200 hover:bg-primary-200 cursor-pointer"
   >
      <img class="size-8 mx-2" :src="imagePath" :alt="props.title" />

      <div class="w-full pl-4">
         <h2 class="header-3">{{ props.title }}</h2>
         <p class="body-1">
            {{ props.description }}
         </p>
      </div>
   </article>
</template>
