# ChatBot

## TODO
1. El modulo de backend y frontend debera definir cuales seran sus tecnologías y versiones

Se usarán las siguientes tecnologías y versiones:
>Python 3.11.4
>FastAPI  0.115.12

2. Un integrande por modulo deberá crear el entorno de desarrollo en el directorio correspondiente
3. Definir responsabilidades por modulo (ej: En el back deben definir quien implementará la biblioteca para reconocer texto y quien implementara los llamados a la api)

Para ejecutar el proyecto:

**Antes asegurarse de tener instalado Python 3.11.4

1) Crear entorno virtual:
python -m venv .venv    

2) Activar entorno virtual:
.\env\Scripts\activate

**Si hay problemas para activar usar el comando: 
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser  
y luego intentar otra vez

3) Instalar dependencias:
pip install -r requirements.txt

4) Ejecutar:
uvicorn main:app --reload
