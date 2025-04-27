import cloudIcon from '@/assets/icon/cloud.png';
import moneyCalcIcon from '@/assets/icon/money-calculator.png';
import moneyIcon from '@/assets/icon/money-alt.png';
import newsIcon from '@/assets/icon/news.png';

export enum TOPIC {
   CLIMA = 'Clima',
   UF = 'Valor del UF',
   DOLAR = 'Valor del dólar',
   NOTICIAS = 'Noticias del dia',
}

export enum TOPIC_IMG {
   CLIMA = 'cloud.png',
   UF = 'money-calculator.png',
   DOLAR = 'money-alt.png',
   NOTICIAS = 'news.png',
}

export enum TOPIC_DESCRIPTION {
   CLIMA = 'Quiero conocer el clima actual en mi ubicación (Temuco, Chile).',
   UF = 'Quiero saber el valor actual de la UF en pesos chilenos.',
   DOLAR = 'Quiero saber el valor actual del dólar en pesos chilenos.',
   NOTICIAS = 'Quiero conocer las noticias más relevantes del día.',
}

export const IMAGE_MAP: Record<string, string> = {
   'cloud.png': cloudIcon,
   'money-calculator.png': moneyCalcIcon,
   'money-alt.png': moneyIcon,
   'news.png': newsIcon,
};
