import openai
import os

openai.api_key = os.getenv("OPENAI_KEY")

def traduzir_com_variações(texto):
    prompt = f"""
    Traduza o texto abaixo para português com três variações diferentes,
    adaptadas para simetria visual de postagens no Telegram (cerca de 150 caracteres cada).

    Texto original:
    {texto}
    """

    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )

    return [resposta.choices[0].message['content'].strip()]
