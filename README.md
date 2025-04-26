# ChatBot

## Para iniciar el back

*Entrar en el directorio*

```
  cd .\back\
```
*Importante una vez dentro del directorio 'back' crear primero un entorno de desarrollo*
```
  python -m venv .venv
```

*Activar el entorno de desarrollo*
```
  .\.venv\Scripts\activate
```

*Instalar los paquetes necesarios para el proyecto*

```
  pip install -r requirements.txt
```

*Correr la app*
```
  uvicorn main:app --reload
```
