import { ToggleMenu } from '@/utils/types';
import { ShallowRef, shallowRef } from 'vue';


export const useToggleMenu = (): ToggleMenu => {
   const isSidebarOpen: ShallowRef<boolean> = shallowRef(false);

   const toggleSidebar = (): void => {
      isSidebarOpen.value = !isSidebarOpen.value;
   };

   return {
      isSidebarOpen,
      toggleSidebar,
   }
}
