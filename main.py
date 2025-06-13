#!/usr/bin/env python3
"""
Telegram Bot Main Application
Bot de cultura pop com tradução automática de mensagens, legendas e texto de imagem (OCR), com ajuste de simetria visual.
"""

import logging
import os
import io
from PIL import Image
import pytesseract
from deep_translator import GoogleTranslator
from telegram import Update
from telegram.ext import (Application, CommandHandler, MessageHandler,
                          ContextTypes, filters)

from ai_utils import traduzir_com_variações  # Import do seu módulo AI com a função traduzir_com_variações

# Configurações do bot
BOT_TOKEN = os.getenv("BOT_TOKEN")
translator = GoogleTranslator(source='auto', target='pt')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ajuste de simetria visual
IDEAL_CHAR_LENGTH = 150


def ajustar_simetria(textos: list[str]) -> str:
    """
    Escolhe a versão do texto mais próxima da largura ideal.
    """

    def desvio(t):
        return abs(len(t) - IDEAL_CHAR_LENGTH)

    textos_ordenados = sorted(textos, key=desvio)
    return textos_ordenados[0]


# Comando /start
async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Olá! Sou seu bot de cultura pop.\n"
        "Envie mensagens, imagens ou legendas que eu traduzo e adapto pra você."
    )


# Comando /help
async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆘 Comandos disponíveis:\n"
        "/start - Iniciar o bot\n"
        "/help - Mostrar ajuda\n"
        "/traduzir <texto> - Tradução automática com 3 variações\n"
        "Você também pode enviar imagens com legenda ou textos diretos.")


# OCR e tradução com variações + ajuste de simetria
async def process_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        photo = update.message.photo[-1]
        caption = update.message.caption or ""

        photo_file = await photo.get_file()
        photo_bytes = await photo_file.download_as_bytearray()
        image = Image.open(io.BytesIO(photo_bytes))

        # OCR da imagem
        extracted_text = pytesseract.image_to_string(image, lang='eng')
        full_text = (caption + "\n" + extracted_text).strip()

        if not full_text:
            await update.message.reply_text(
                "❌ Nenhum texto encontrado na imagem ou legenda.")
            return

        # Tradução + variações
        base = translator.translate(full_text)
        alt1 = base.replace("agora",
                            "já disponível").replace("lançamento", "estreia")
        alt2 = base.replace("agora",
                            "no momento").replace("disponível", "liberado")

        final = ajustar_simetria([base, alt1, alt2])

        response = (f"🗨️ Texto original detectado:\n{full_text}\n\n"
                    f"📝 Tradução otimizada:\n{final}")
        await update.message.reply_text(response)

    except Exception as e:
        logger.error(f"Erro ao processar imagem: {e}")
        await update.message.reply_text("Erro ao processar imagem ou legenda.")


# Tradução de texto com ajuste de simetria
async def echo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        original_text = update.message.text
        base = translator.translate(original_text)
        alt1 = base.replace("agora",
                            "no momento").replace("exclusivo", "inédito")
        alt2 = base.replace("estreia",
                            "lançamento").replace("já", "agora mesmo")

        final = ajustar_simetria([base, alt1, alt2])

        response = (f"🗨️ Texto original:\n{original_text}\n\n"
                    f"📝 Tradução otimizada:\n{final}")
        await update.message.reply_text(response)

    except Exception as e:
        logger.error(f"Erro ao traduzir mensagem: {e}")
        await update.message.reply_text("Erro ao traduzir a mensagem.")


# Handler do comando /traduzir com variações via OpenAI
async def traduzir_handler(update: Update,
                           context: ContextTypes.DEFAULT_TYPE) -> None:
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


# Handler de erro
async def error_handler(update: object,
                        context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error(f"Erro detectado: {context.error}")


def main():
    if not BOT_TOKEN:
        logger.error("Bot token não encontrado! Use a variável BOT_TOKEN.")
        return

    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("help", help_handler))
    application.add_handler(CommandHandler(
        "traduzir", traduzir_handler))  # <-- Aqui a nova linha do handler
    application.add_handler(MessageHandler(filters.PHOTO, process_image))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, echo_handler))
    application.add_error_handler(error_handler)

    logger.info("Bot iniciado via polling...")
    application.run_polling()


if __name__ == '__main__':
    main()
