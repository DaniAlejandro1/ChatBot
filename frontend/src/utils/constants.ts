import type { Topic } from '@/utils/types';
import { TOPIC, TOPIC_IMG, TOPIC_DESCRIPTION } from '@/utils/enums';

export const TOPIC_CARD: Topic[] = [
   {
      img: TOPIC_IMG.CLIMA,
      title: TOPIC.CLIMA,
      description: TOPIC_DESCRIPTION.CLIMA,
   },
   {
      img: TOPIC_IMG.UF,
      title: TOPIC.UF,
      description: TOPIC_DESCRIPTION.UF,
   },
   {
      img: TOPIC_IMG.DOLAR,
      title: TOPIC.DOLAR,
      description: TOPIC_DESCRIPTION.DOLAR,
   },
   {
      img: TOPIC_IMG.NOTICIAS,
      title: TOPIC.NOTICIAS,
      description: TOPIC_DESCRIPTION.NOTICIAS,
   },
];
