#!/usr/bin/env python3
"""
Telegram Bot Main Application
Bot de cultura pop com tradução automática de mensagens, legendas e texto de imagem (OCR).
"""

import logging
import os
import io
from PIL import Image
import pytesseract
from googletrans import Translator
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, MessageHandler, ContextTypes, filters
)

# Configurações do bot
BOT_TOKEN = os.getenv("7782377206:AAFjEbybye9AztpNNaLDhaQK5FE-PAU5j8g")
translator = Translator()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Comando /start
def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text(
        "🤖 Olá! Sou seu bot de cultura pop.\n"
        "Envie mensagens, imagens ou legendas que eu traduzo e adapto pra você."
    )

# Comando /help
def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text(
        "🆘 Comandos disponíveis:\n"
        "/start - Iniciar o bot\n"
        "/help - Mostrar ajuda\n"
        "Você também pode enviar imagens com legenda ou textos diretos."
    )

# OCR e tradução com variações
def process_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        photo = update.message.photo[-1]
        caption = update.message.caption or ""

        photo_file = photo.get_file()
        photo_bytes = photo_file.download_as_bytearray()
        image = Image.open(io.BytesIO(photo_bytes))

        # OCR da imagem
        extracted_text = pytesseract.image_to_string(image, lang='eng')
        full_text = (caption + "\n" + extracted_text).strip()

        if not full_text:
            update.message.reply_text("❌ Nenhum texto encontrado na imagem ou legenda.")
            return

        # Tradução + variações
        base_translation = translator.translate(full_text, dest='pt').text
        alt1 = base_translation.replace("agora", "já disponível")
        alt2 = base_translation.replace("lançamento", "estreia")

        response = (
            f"🗨️ Texto original detectado:\n{full_text}\n\n"
            f"🌐 Tradução adaptada 1:\n{base_translation}\n\n"
            f"✨ Variação 2:\n{alt1}\n\n"
            f"🎭 Variação 3:\n{alt2}"
        )
        update.message.reply_text(response)

    except Exception as e:
        logger.error(f"Erro ao processar imagem: {e}")
        update.message.reply_text("Erro ao processar imagem ou legenda.")

# Resposta a texto normal
def echo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        original_text = update.message.text
        translated = translator.translate(original_text, dest='pt').text
        alt1 = translated.replace("agora", "neste momento")
        alt2 = translated.replace("exclusivo", "inédito")

        response = (
            f"🗨️ Texto original:\n{original_text}\n\n"
            f"🌐 Tradução adaptada 1:\n{translated}\n\n"
            f"✨ Variação 2:\n{alt1}\n\n"
            f"🎭 Variação 3:\n{alt2}"
        )
        update.message.reply_text(response)

    except Exception as e:
        logger.error(f"Erro ao traduzir mensagem: {e}")
        update.message.reply_text("Erro ao traduzir a mensagem.")

# Handler de erro
def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error(f"Erro detectado: {context.error}")


def main():
    if not BOT_TOKEN:
        logger.error("Bot token não encontrado! Use a variável BOT_TOKEN.")
        return

    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("help", help_handler))
    application.add_handler(MessageHandler(filters.PHOTO, process_image))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_handler))
    application.add_error_handler(error_handler)

    logger.info("Bot iniciado via polling...")
    application.run_polling()


if __name__ == '__main__':
    main()
