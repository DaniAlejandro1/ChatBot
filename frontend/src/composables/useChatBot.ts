import { TOPIC, TOPIC_DESCRIPTION } from '@/utils/enums';
import { AddMessageFunction } from '@/utils/types';
import { computed, shallowRef, ShallowRef } from 'vue';
import { Router } from 'vue-router';

export const useTopicQuestion = async (question: string) => {
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
   
   const response = await getResponse(primaryQuestion.value);
   
   
   return { primaryQuestion, response};
}

export async function getResponse(message: string): Promise<string> {
   const response = await fetch(`http://localhost:8000/chat?topico=${encodeURIComponent(message)}`);
   const data = await response.json();
   console.log('Post creado:', data);
   console.log(data.type)
   
   return data
   
}

export const useChatBot = (router: Router, isFirstQuestion: boolean, addMessage: AddMessageFunction) => {
   const question: ShallowRef<string> = shallowRef<string>('');
   const errorMessage: ShallowRef<string> = shallowRef<string>('');

   const goToChat = async (question: string, id: string): Promise<void> => {
      if (isFirstQuestion && question.length > 0) {
         router.push({ name: 'chat', params: { question, id } });
      } else if (question.length > 0) {
         const response = await getResponse(question);
         console.log(Number(id), question, response)
         
            
         addMessage(Number(id), question, response);
         
      } else {
         errorMessage.value = 'Por favor, escribe un mensaje.'
      }

   };

   return { question, errorMessage, goToChat };
}
