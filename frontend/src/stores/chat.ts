import { defineStore } from 'pinia'
import type { ChatMessage, Comunication } from '@/utils/types'

export const useChatsStore = defineStore('chats', {
   state: () => {
      return {
         chats: [] as ChatMessage[]
      }
   },

   actions: {
      addChat(chat: ChatMessage): void {
         this.chats.push(chat)
      },

      addMessageToChat(chatId: string, question: string, response: string): void {
         const chat = this.chats.find(c => c.id === chatId)
         if (chat) chat.message.push({ question, response } as Comunication)
      },

   },

   getters: {
      chatHistory: (state) => state.chats,
   }
})