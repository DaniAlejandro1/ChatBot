import { defineStore } from 'pinia'
import type { ChatMessage, Comunication } from '@/utils/types'

export const useChatsStore = defineStore('chats', {
   state: () => {
      const savedChats = localStorage.getItem('chats');
      return {
         chats: savedChats ? (JSON.parse(savedChats) as ChatMessage[]) : [],
      };
   },

   actions: {
      addChat(chat: ChatMessage): void {
         this.chats.push(chat)
      },

      addMessageToChat(chatId: number, question: string, response: string): void {
         const chat = this.chats.find(c => c.id === chatId);
         if (chat) {
            if (!Array.isArray(chat.message)) {
               chat.message = [];
            }
            chat.message.push({ question, response } as Comunication);
         }
      },

   },

   getters: {
      chatHistory: (state) => state.chats,
      lengthChats: (state) => state.chats.length,
   }
})