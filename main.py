from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

# 1. CARGAMOS EL MODELO DE IA EN LA MEMORIA
# pipeline() descarga automáticamente un modelo entrenado para analizar sentimientos.
# (La primera vez que ejecutes esto, descargará unos 200MB de IA, luego será instantáneo)
analizador_ia = pipeline("sentiment-analysis")

@app.get("/")
def estado_del_servidor():
    return {"mensaje": "¡El servidor de MLOps está vivo y la IA está cargada!"}

# 2. CREAMOS UN NUEVO ENDPOINT PARA USAR LA IA
# Fíjate que en la URL ahora esperamos que el usuario nos mande un "texto"
@app.get("/analizar")
def analizar_texto(texto: str):
    
    # Le pasamos el texto del usuario a nuestro cerebro de IA
    resultado = analizador_ia(texto)
    
    # Devolvemos la respuesta de la IA a través de internet
    return {
        "texto_ingresado": texto,
        "prediccion_ia": resultado
    }