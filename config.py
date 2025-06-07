import os

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Opcional

if not BOT_TOKEN:
    raise ValueError("❌ ERRO: A variável de ambiente TELEGRAM_TOKEN não está definida!")

if not OPENAI_API_KEY:
    raise ValueError("❌ ERRO: A variável de ambiente OPENAI_API_KEY não está definida!")
