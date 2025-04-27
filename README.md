# ChatBot

Este proyecto incluye tanto el **frontend** como el **backend** en el mismo repositorio. Para una mejor organización, el directorio `back` contiene el backend y el directorio `frontend` contiene el frontend. Se recomienda utilizar Visual Studio Code y abrir dos terminales para ejecutar ambos entornos simultáneamente.

## Requisitos previos

- **Python 3.13 o superior** (para el backend)
- **Node.js 22.14.0 o superior (Las superiores son inestable)** y **pnpm** (para el frontend)
- **Linux (Ubuntu recomendado)** o **Windows** como sistema operativo



## Para iniciar el back
Antes de iniciar cualquier comando se recuerda que en la carpeta **back** debera ser ingresado un .env el cual ha sido despuesto junto con el informe. Copie y pegue ese env en la raiz del proyecto del backend. Las varibales de entorno deben ser nombrado de la siguiente manera `.env`.

### 1. Entrar en el directorio del backend
  **Linux (bash):**

  ```bash
  cd ./back/
  ```

  **Windows (PowerShell):**
  ```powershell
  cd .\back\
  ```

### 2. Crear un entorno virtual
En este paso se presupone que cuenta con las dependecias de python instaladas en su maquina.
**Linux (bash):**
```bash
python3 -m venv .venv
```

**Windows (PowerShell):**
```powershell
python -m venv .venv
```
### 3. Activar el entorno virtual
**Linux (bash):**
```bash
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\activate
```

### 4. Instalar las dependencias necesarias

**Linux y Windows:**
```bash
pip install -r requirements.txt
```

### 5. Ejecutar el servidor del backend

**Linux y Windows:**
```bash
uvicorn main:app --reload
```

## Iniciar el Frontend

### 1. Entrar en el directorio del frontend

**Linux (bash):**
```bash
cd ./frontend/
```

**Windows (PowerShell):**
```powershell
cd .\frontend\
```

### 2. Instalar las dependencias

**Linux y Windows:**
```bash
pnpm i
```

### 3. Ejecutar el servidor del frontend

**Linux y Windows:**
```bash
pnpm dev
```


# Notas adicionales

- Asegúrate de que el backend esté ejecutándose antes de interactuar con el frontend.
- Si no tienes `pnpm` instalado, puedes instalarlo con:
  ```bash
  npm install -g pnpm o leer las siguientes intrucciones: https://pnpm.io/es/installation
  ```
- Si encuentras problemas con las dependencias de Python, asegúrate de estar usando la versión correcta de Python y de que el entorno virtual esté activado.

Con estas instrucciones, deberías poder ejecutar tanto el backend como el frontend en Linux o Windows sin problemas.




