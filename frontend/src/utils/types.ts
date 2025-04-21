import { ComputedRef, ShallowRef } from "vue";

export type Topic = {
   img: string;
   title: string;
   description: string;
};

export type Comunication = {
   id?: number;
   question: string;
   response: string;
}

export type ChatMessage = {
   id: number;
   title: string;
   message: Comunication[]
}

export type AddMessageFunction = (id: number, question: string, response: string) => void;

export type UseChatBot = {
   question: ShallowRef<string>;
   errorMessage: ShallowRef<string>;
   goToChat(question: string, id: string): void;
}

export type UseTopicQuestion = {
   response: ShallowRef<string>;
   primaryQuestion: ComputedRef<string>;
}

export type ToggleMenu = {
   isSidebarOpen: ShallowRef<boolean>;
   toggleSidebar(): void;
}
