export type Topic = {
   img: string;
   title: string;
   description: string;
};

export type Comunication = {
   id?: number;
   question: string;
   response: string;
};

export type ChatMessage = {
   id: number;
   title: string;
   message: Comunication[];
};

export type AddMessageFunction = (id: number, question: string, response: string) => void;
