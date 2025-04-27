import { ComputedRef, computed } from 'vue';
import { IMAGE_MAP } from '@/utils/enums';

export const useImagePath = (imageKey: string): ComputedRef<string> => {
   const computedImagePath: ComputedRef<string> = computed(() => {
      return IMAGE_MAP[imageKey] || '';
   });

   return computedImagePath;
};
