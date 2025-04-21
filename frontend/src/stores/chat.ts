import { defineStore } from 'pinia'
import type { ChatMessage, Comunication } from '@/utils/types'

export const useChatsStore = defineStore('chats', {
   state: (): { chats: ChatMessage[] } => {
      const savedChats = localStorage.getItem('chats');
      return {
         chats: savedChats ? (JSON.parse(savedChats) as ChatMessage[]) : [],
      };
   },

   actions: {
      addChat(chat: ChatMessage): void {
         const exists = this.chats.some((c: ChatMessage) => c.id === chat.id);
         if (!exists) {
            this.chats.push(chat);
            localStorage.setItem('chats', JSON.stringify(this.chats));
         }
      },

      addMessageToChat(chatId: number, question: string, response: string): void {
         const chat = this.chats.find((c: ChatMessage) => c.id === chatId);
         if (chat) {
            if (!Array.isArray(chat.message)) {
               chat.message = [];
            }
            chat.message.push({ question, response } as Comunication);
            localStorage.setItem('chats', JSON.stringify(this.chats));
         }
      },

      deleteChatById(chatId: number): void {
         this.chats = this.chats.filter((chat: ChatMessage) => chat.id !== chatId);
         localStorage.setItem('chats', JSON.stringify(this.chats));
      },
   },

   getters: {
      chatHistory: (state): ChatMessage[] => state.chats,
      lengthChats: (state): number => state.chats.length,
      getChatMessages: (state) => (chatId: number): Comunication[] => {
         const chat = state.chats.find((c: ChatMessage) => c.id === chatId);
         return chat ? chat.message : [];
      },
   }
});