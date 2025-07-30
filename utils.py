import os
import httpx
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

IDEAL_CHAR_LENGTH = 150

async def traduzir_com_variacoes_e_simetria(texto: str):
    prompt = (
        f"Traduza o seguinte texto para o português com 3 variações distintas, mantendo o sentido, estilo e tom originais.\n"
        f"Texto: \"{texto}\"\n"
        f"Responda com as 3 traduções, separadas por quebras de linha."
    )

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.9
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(GROQ_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        raw_output = result["choices"][0]["message"]["content"]

    traducoes = [linha.strip() for linha in raw_output.split("\n") if linha.strip()]
    melhor = sorted(traducoes, key=lambda t: abs(len(t) - IDEAL_CHAR_LENGTH))[0]

    return {
        "melhor": melhor,
        "variacoes": traducoes
    }