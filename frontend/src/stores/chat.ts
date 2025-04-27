import { defineStore } from 'pinia';
import type { ChatMessage, Comunication } from '@/utils/types';

export const useChatsStore = defineStore('chats', {
   state: () => {
      const savedChats = localStorage.getItem('chats');
      return {
         chats: savedChats ? (JSON.parse(savedChats) as ChatMessage[]) : [],
      };
   },

   actions: {
      addChat(chat: ChatMessage): void {
         const exists = this.chats.some((c) => c.id === chat.id);
         if (!exists) {
            this.chats.push(chat);
            localStorage.setItem('chats', JSON.stringify(this.chats));
         }
      },

      addMessageToChat(chatId: number, question: string, response: string): void {
         const chat = this.chats.find((c) => c.id === chatId);
         if (chat) {
            if (!Array.isArray(chat.message)) {
               chat.message = [];
            }
            chat.message.push({ question, response } as Comunication);
            localStorage.setItem('chats', JSON.stringify(this.chats));
         }
      },

      deleteChatById(chatId: number): void {
         this.chats = this.chats.filter((chat) => chat.id !== chatId);
         localStorage.setItem('chats', JSON.stringify(this.chats));
      },

      isPresentChat(chatId: number): boolean {
         return this.chats.some((chat) => chat.id === chatId);
      },
   },

   getters: {
      chatHistory: (state) => state.chats,
      lengthChats: (state) => state.chats.length,
      getChatMessages: (state) => (chatId: number) => {
         const chat = state.chats.find((c) => c.id === chatId);
         return chat ? chat.message : [];
      },
   },
});
