export type Topic = {
   img: string;
   title: string;
   description: string;
};


export type Comunication = {
   question: string;
   response: string;
}

export type ChatMessage = {
   id: number;
   title: string;
   message: Comunication[]
}