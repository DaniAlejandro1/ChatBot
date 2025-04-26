# ChatBot

Es importante considerar que tanto el frontend como el backend se encuentran dentro del mismo repositorio. Para una mejor organización, se ha dispuesto el directorio back para ejecutar el backend y el directorio frontend para ejecutar el frontend. Se recomienda utilizar el editor de texto Visual Studio Code y abrir dos terminales para ejecutar ambos entornos de forma simultánea.

## Para iniciar el back

*Entrar en el directorio del backend*

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

*Ejecutar proyecto*
```
  uvicorn main:app --reload
```


## Para iniciar el front

*Entrar en el directorio del front*

```
  cd .\frontend\
```

*Instalar las dependencias*

```
  pnpm i
```

*Ejecutar proyecto*

```
  pnpm dev
```




