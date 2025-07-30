from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils import traduzir_com_variacoes_e_simetria

app = FastAPI()

class TextoInput(BaseModel):
    texto: str

@app.post("/traduzir")
async def traduzir_texto(input: TextoInput):
    try:
        resultado = await traduzir_com_variacoes_e_simetria(input.texto)
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))