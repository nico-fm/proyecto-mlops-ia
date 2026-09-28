# 1. Usamos una imagen base oficial de Python ligera
FROM python:3.10-slim

# 2. Creamos una carpeta dentro del contenedor para trabajar
WORKDIR /app

# 3. Instalamos las librerías necesarias
RUN pip install --no-cache-dir fastapi uvicorn transformers torch

# 4. Copiamos nuestro código al contenedor
COPY main.py /app/main.py

# 5. Exponemos el puerto 8000 para poder conectarnos desde afuera
EXPOSE 8000

# 6. Comando para encender el servidor al arrancar el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 