"""
Command and message handlers for the Telegram bot.
Contains all the bot's response logic and command implementations.
"""

import logging
from datetime import datetime
from telegram import Update
from telegram.ext import ContextTypes
from config import BOT_NAME, ADMIN_IDS
from ai_utils import traduzir_com_variações  # 👈 Import da função de tradução

logger = logging.getLogger(__name__)


# (... Demais handlers: start_handler, help_handler, echo_handler, error_handler, stats_handler ...)

# Novo handler de tradução
async def traduzir_handler(update: Update,
                           context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the /traduzir command.
    Translates a message using OpenAI and returns three variations.
    """
    texto = " ".join(context.args)

    if not texto:
        await update.message.reply_text(
            "❗ Envie um texto após o comando /traduzir.")
        return

    await update.message.reply_text("🔄 Traduzindo com variações...")

    try:
        variacoes = traduzir_com_variações(texto)
        resposta = "\n\n".join(variacoes[:3])
        await update.message.reply_text(f"🈂️ Traduções:\n\n{resposta}")
    except Exception as e:
        await update.message.reply_text(f"⚠️ Erro ao traduzir: {e}")
