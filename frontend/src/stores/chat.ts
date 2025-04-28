import { defineStore } from 'pinia';
import type {Conversation} from '@/utils/types';
import { ref } from 'vue';


export const useChatsStore = defineStore('chats', () =>{
   const conversations = ref<Array<Conversation[]>>([]);

   function addConversation(conversacion: Conversation[]){
      conversations.value.push(conversacion)
   }

   function createConversation(conversacion: Conversation){
      conversations.value.push([conversacion])
      return conversations.value.length - 1
   }

   function setConversation(index: number, conversation: Conversation) {
      for (let i = 0; i < conversations.value[index].length; i++) {
        if (conversations.value[index][i].question === '') {
          conversations.value[index][i] = {
            ...conversations.value[index][i],
            question: conversation.question,
          };
          return;
        }
      }
      conversations.value[index].push(conversation);
    }
    

   function setResponse(index: number, response: string) {
      for (let i = 0; i < conversations.value[index].length; i++) {
        if (conversations.value[index][i].response === '') {
          conversations.value[index][i] = {
            ...conversations.value[index][i],
            response: response,
          };
          return;
        }
      }
   }
   
   function removeConversation(index: number){
      conversations.value.splice(index, 1)
   }

   function getConversation(index: number){
      return conversations.value[index]
   }


   function getAllConversations(){
      return conversations.value
   }
   return {addConversation,createConversation, removeConversation, getConversation,setConversation, setResponse, getAllConversations}
});
