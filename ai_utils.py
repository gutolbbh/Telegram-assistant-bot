import os
from openai import OpenAI

# Pegando a chave da OpenAI via variável de ambiente
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Inicializando o cliente da OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)


def traduzir_com_variações(texto: str) -> list[str]:
    """
    Gera 3 variações de tradução otimizadas para cultura pop,
    com foco em simetria visual para Telegram.

    Exemplo de prompt: Traduza e reescreva o texto abaixo em português com 3 variações diferentes...
    """
    try:
        prompt = f"""
Você é um redator especialista em cultura pop.

Sua tarefa:
- Traduzir o texto abaixo para o português
- Criar 3 versões diferentes da tradução
- Cada versão deve ter cerca de 150 caracteres, com foco em linguagem jornalística para redes sociais (Telegram)
- Use sinônimos, reestruturações ou variações estilísticas para manter o sentido mas variar a forma
- NÃO inclua hashtags, emojis ou frases genéricas, apenas o texto reescrito.

Texto original:
\"\"\"{texto}\"\"\"
"""

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Você é um tradutor e redator especializado em cultura pop."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500,
        )

        resultado = response.choices[0].message.content
        # Quebra a resposta em 3 variações (assumindo que o GPT vai numerar ou separar por linhas)
        variacoes = [v.strip() for v in resultado.split("\n") if v.strip()]

        # Garante no máximo 3 variações
        return variacoes[:3]

    except Exception as e:
        raise RuntimeError(f"Erro ao usar OpenAI: {e}")
