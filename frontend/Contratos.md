# Endpoint definidos por el backend

### Hacer consulta general en el chat

- **endpoint:** /chat
- **metodo:** GET
- **parámetros:** question (consulta del usuario)
- **ejemplo de uso:** /chat?question="pregunta"
- **respuesta esperada:**
   ```json
   {
      "success": true,
      "data": {
         "response": "Respuesta a la consulta"
      }
   }
   ```
- **nota:** La respuesta a la pregunta vendra en formato texto con una limitación de caracteres, con el fin de que no sea abusivo.
