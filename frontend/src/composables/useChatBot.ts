import { TOPIC, TOPIC_DESCRIPTION } from '@/utils/enums';
import { computed, shallowRef, ShallowRef } from 'vue';

export const useTopicQuestion = (question: string) => {
   const response: ShallowRef<string> = shallowRef<string>('Soy un robot');
   const primaryQuestion = computed(() => {
      if (question === TOPIC.CLIMA) {
         return TOPIC_DESCRIPTION.CLIMA;
      } else if (question === TOPIC.DOLAR) {
         return TOPIC_DESCRIPTION.DOLAR;
      } else if (question === TOPIC.UF) {
         return TOPIC_DESCRIPTION.UF;
      } else if (question === TOPIC.NOTICIAS) {
         return TOPIC_DESCRIPTION.NOTICIAS;
      } else {
         return question;
      }
   });

   return { primaryQuestion, response };
}