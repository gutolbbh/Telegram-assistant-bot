from fastapi import FastAPI, Request
from pydantic import BaseModel
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class Texto(BaseModel):
    texto: str
    idioma_origem: str = "auto"
    idioma_destino: str = "en"

@app.post("/traduzir")
async def traduzir_texto(texto: Texto):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}"
    }
    payload = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages": [
            {"role": "system", "content": "Você é um tradutor especializado que adapta fielmente o sentido do conteúdo original."},
            {"role": "user", "content": f"Traduza o seguinte texto para o idioma {texto.idioma_destino}: {texto.texto}"}
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
        data = response.json()

    traducao = data["choices"][0]["message"]["content"]
    return {"traducao": traducao}
