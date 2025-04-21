from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from unidecode import unidecode

import numpy as np

# Frases de entrenamiento
datos_entrenamiento = [
    # UF
    ("cuánto está la uf", "uf"),
    ("dame el valor de la uf", "uf"),
    ("precio actual de la uf", "uf"),
    ("valor uf", "uf"),
    # Dólar
    ("cuánto está el dólar", "dolar"),
    ("dame el valor del dólar", "dolar"),
    ("precio actual del dólar", "dolar"),
    ("cotización dólar", "dolar"),
    # Clima
    ("cómo está el clima", "clima"),
    ("dame el clima", "clima"),
    ("va a llover", "clima"),
    ("temperatura actual", "clima"),
    # Noticias
    ("cuáles son las noticias", "noticias"),
    ("dame las noticias de hoy", "noticias"),
    ("top 10 noticias", "noticias"),
    ("noticias actuales", "noticias"),
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
