import os

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # ← ADICIONE ESTA LINHA
WEBHOOK_URL = os.getenv("WEBHOOK_URL")        # Opcional, se for usar webhook
