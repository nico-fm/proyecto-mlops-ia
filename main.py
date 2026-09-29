import os
import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()

# URL del motor de inferencia especializado de Hugging Face
HF_API_URL = "https://api-inference.huggingface.co/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"

@app.get("/")
def home():
    return {"mensaje": "API de Análisis de Sentimiento MLOps activa y en producción"}

@app.get("/analizar")
def analizar_texto(texto: str):
    payload = {"inputs": texto}
    
    # Hacemos la consulta al motor de inferencia externo
    response = requests.post(HF_API_URL, json=payload)
    
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error en el motor de inferencia de IA")
        
    resultado = response.json()
    
    return {
        "texto_ingresado": texto,
        "analisis": resultado,
        "arquitectura": "Decoupled Microservice (FastAPI + HF Inference API)"
    }