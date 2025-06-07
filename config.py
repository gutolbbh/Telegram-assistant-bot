"""
Configurações globais do bot.
Carrega variáveis de ambiente e define constantes do sistema.
"""

import os

# ⚙️ Configurações de logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = os.getenv("LOG_FORMAT", "%(asctime)s - %(levelname)s - %(message)s")
ENABLE_LOGGING = os.getenv("ENABLE_LOGGING", "True").lower() == "true"

# 👑 IDs dos administradores
# Substitua ou carregue de outro lugar seguro (ex: variável de ambiente, banco, etc.)
ADMIN_IDS = [123456789]  # Exemplo: [int(os.getenv("ADMIN_ID_1")), int(os.getenv("ADMIN_ID_2"))]

# 🔐 Tokens e chaves de API
BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Opcional para bots com webhook

# 🚨 Validação obrigatória
if not BOT_TOKEN:
    raise ValueError("❌ TELEGRAM_TOKEN não está configurado no ambiente.")
if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY não está configurado no ambiente.")
