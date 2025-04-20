import { TOPIC, TOPIC_DESCRIPTION } from '@/utils/enums';
import { AddMessageFunction } from '@/utils/types';
import { computed, shallowRef, ShallowRef } from 'vue';
import { Router } from 'vue-router';

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



export const useChatBot = (router: Router, isFirstQuestion: boolean, addMessage: AddMessageFunction) => {
   const question: ShallowRef<string> = shallowRef<string>('');
   const errorMessage: ShallowRef<string> = shallowRef<string>('');

   const goToChat = (question: string, id: string): void => {
      if (isFirstQuestion && question.length > 0) {
         router.push({ name: 'chat', params: { question, id } });
      } else if (question.length > 0) {
         const response = 'Soy un robot 2';
         console.log(Number(id), question, response)
         addMessage(Number(id), question, response);
      } else {
         errorMessage.value = 'Por favor, escribe un mensaje.'
      }

   };

   return { question, errorMessage, goToChat };
}
