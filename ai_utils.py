import os
import openai

# Inicializa a API da OpenAI com a chave salva no ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")


def traduzir_com_variações(texto: str) -> list:
    """
    Envia um texto para a OpenAI e retorna 3 variações traduzidas e adaptadas para o português.
    As variações mantêm o sentido original, mas mudam estilo, vocabulário e ordem.
    """
    prompt = (
        "Traduza o seguinte texto para o português e gere três variações diferentes "
        "do mesmo conteúdo, mantendo o sentido mas com mudanças de estilo, vocabulário ou ordemimport os
import openai

# Inicializa a API da OpenAI com a chave salva no ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

def traduzir_com_variações(texto: str) -> list:
    """
    Envia um texto para a OpenAI e retorna 3 variações traduzidas e adaptadas para o português.
    As variações mantêm o sentido original, mas mudam estilo, vocabulário e ordem.
    """
    prompt = (
        "Traduza o seguinte texto para o português e gere três variações diferentes "
        "do mesmo conteúdo, mantendo o sentido mas com mudanças de estilo, vocabulário ou ordem:\n\n"
        f"Texto: {texto}\n\n"
        "Responda com uma lista numerada de 3 versões diferentes."
    )

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
        )
        conteudo = resposta.choices[0].message.content.strip()
        # Retorna como lista, limpando entradas vazias
        return [linha.strip() for linha in conteudo.split("\n") if linha.strip()]
    except Exception as e:
        raise RuntimeError(f"Erro ao usar OpenAI: {e}")