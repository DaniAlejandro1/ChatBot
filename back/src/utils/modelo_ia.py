from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from unidecode import unidecode

import cohere

import numpy as np

# Frases de entrenamiento
datos_entrenamiento = [
    # UF
    ("cuánto está la uf", "uf"),
    ("dame el valor de la uf", "uf"),
    ("precio actual de la uf", "uf"),
    ("valor uf", "uf"),
    ("uf", "uf"),
    ("cuánto vale la uf", "uf"),
    ("cuánto cuesta la uf", "uf"),
    ("cuánto es la uf hoy", "uf"),
    ("cuánto está la unidad de fomento", "uf"),
    ("cuánto está la uf hoy", "uf"),
    # Dólar
    ("cuánto está el dólar", "dolar"),
    ("dame el valor del dólar", "dolar"),
    ("precio actual del dólar", "dolar"),
    ("cotización dólar", "dolar"), 
    ("valor dólar", "dolar"),
    ("cuánto vale el dólar", "dolar"),
    ("cuánto cuesta el dólar", "dolar"),
    ("cuánto es el dólar hoy", "dolar"),
    ("cuánto está el dólar hoy", "dolar"),
    # Clima
    ("cómo está el clima", "clima"),
    ("dame el clima", "clima"),
    ("va a llover", "clima"),
    ("temperatura actual", "clima"),
    ("temperatura", "clima"),
    ("quiero la temoperatura", "clima"),
    ("clima", "clima"),
    ("cómo está el tiempo", "clima"),
    ("cuál es la temperatura", "clima"),
    ("qué clima hace hoy", "clima"),
    ("cómo está el tiempo hoy", "clima"),
    # Noticias
    ("cuáles son las noticias", "noticias"),
    ("dame las noticias de hoy", "noticias"),
    ("top 10 noticias", "noticias"),
    ("noticias actuales", "noticias"),
    ("quiero una noticia", "noticias"),  
    ("noticia", "noticias"),
    ("noticia", "noticias")
]

# Preprocesamiento para normalizar texto
def normalizar_texto(texto):
    return unidecode(texto.lower().strip())

# Separar frases y etiquetas
frases, etiquetas = zip(*datos_entrenamiento)
frases_normalizadas = [normalizar_texto(f) for f in frases]

# Entrenar modelo
modelo = make_pipeline(CountVectorizer(), MultinomialNB())
modelo.fit(frases_normalizadas, etiquetas)

# Funcion para detectar intención
def detectar_intencion(frase, umbral_confianza=0.5):
    frase_normalizada = normalizar_texto(frase)
    probabilidades = modelo.predict_proba([frase_normalizada])[0]
    clases = modelo.classes_
    indice_max = np.argmax(probabilidades)
    confianza = probabilidades[indice_max]
    if confianza >= umbral_confianza:
        return clases[indice_max]
    else:
        return "desconocida"


def parafrasear_texto(topico: str, valor: str) -> str:
    # Inicializar el cliente de Cohere con tu clave de API
    co = cohere.Client('z0U0usZ1wAOKCGr5JN83d9neMj4YA4KEHLeZ5OUX')  # Reemplaza 'TU_API_KEY' con tu clave real
    print("topico",topico,", valor",valor)
    # Crear el mensaje para el modelo
    mensaje = f"""Como usuario te estoy preguntando esto {topico} y necesito que uses esto para responderme {valor}. Con el siguiente formato
                - "El precio actual del dólar es de 800 pesos."
                - "Hoy la UF está valorada en 30.000 pesos."
                """

    # Llamar al modelo usando el endpoint de chat
    respuesta = co.chat(
        message=mensaje,
        model='command-r-plus',  # Modelo recomendado para tareas de generación
        temperature=0.9,  # Controla la creatividad de la respuesta
        max_tokens=50,
        
        
    )

    # Devolver el texto parafraseado
    return respuesta.text