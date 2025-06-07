"""
Command and message handlers for the Telegram bot.
Contains all the bot's response logic and command implementations.
"""

import logging
from datetime import datetime
from telegram import Update
from telegram.ext import ContextTypes
from config import BOT_NAME, ADMIN_IDS

logger = logging.getLogger(__name__)

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the /start command.
    Sends a welcome message to the user.
    """
    user = update.effective_user
    logger.info(f"User {user.id} ({user.username}) started the bot")
    
    welcome_message = (
        f"🤖 Olá, {user.first_name}! Eu sou o {BOT_NAME}!\n\n"
        "Comandos disponíveis:\n"
        "/start - Iniciar o bot\n"
        "/help - Mostrar ajuda\n\n"
        "Você pode me enviar qualquer mensagem e eu vou responder!"
    )
    
    await update.message.reply_text(welcome_message)

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the /help command.
    Provides information about bot capabilities and commands.
    """
    user = update.effective_user
    logger.info(f"User {user.id} ({user.username}) requested help")
    
    help_message = (
        f"🆘 **Ajuda do {BOT_NAME}**\n\n"
        "**Comandos disponíveis:**\n"
        "• /start - Iniciar o bot e ver mensagem de boas-vindas\n"
        "• /help - Mostrar esta mensagem de ajuda\n\n"
        "**Como usar:**\n"
        "• Envie qualquer mensagem de texto e eu vou responder\n"
        "• Use os comandos acima para funcionalidades específicas\n\n"
        "**Sobre:**\n"
        f"• Bot: {BOT_NAME}\n"
        "• Desenvolvido em Python\n"
        "• Sempre online e pronto para conversar! 💬"
    )
    
    await update.message.reply_text(help_message, parse_mode='Markdown')

async def echo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle regular text messages (not commands).
    Echoes the user's message with additional context.
    """
    user = update.effective_user
    message_text = update.message.text
    
    logger.info(f"User {user.id} ({user.username}) sent message: {message_text[:50]}...")
    
    # Create a response based on the message
    if len(message_text) > 100:
        response = (
            f"📝 Recebi sua mensagem longa, {user.first_name}!\n"
            f"Sua mensagem tem {len(message_text)} caracteres.\n"
            f"Aqui está um resumo: '{message_text[:50]}...'"
        )
    elif "olá" in message_text.lower() or "oi" in message_text.lower():
        response = f"👋 Olá, {user.first_name}! Como posso ajudar você hoje?"
    elif "obrigado" in message_text.lower() or "obrigada" in message_text.lower():
        response = "😊 De nada! Estou sempre aqui para ajudar!"
    elif "?" in message_text:
        response = (
            f"🤔 Você fez uma pergunta interessante, {user.first_name}!\n"
            f"Sua pergunta: '{message_text}'\n"
            "Infelizmente, ainda estou aprendendo a responder perguntas complexas."
        )
    else:
        response = (
            f"💬 Recebi sua mensagem, {user.first_name}!\n"
            f"Você disse: '{message_text}'\n"
            "Obrigado por conversar comigo! Use /help para ver mais comandos."
        )
    
    await update.message.reply_text(response)

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle errors that occur during bot operation.
    Logs errors and optionally notifies admins.
    """
    logger.error(f"Exception while handling an update: {context.error}")
    
    # Try to get user information if available
    user_info = "Unknown user"
    if isinstance(update, Update) and update.effective_user:
        user = update.effective_user
        user_info = f"User {user.id} ({user.username})"
    
    logger.error(f"Error occurred for {user_info}: {context.error}")
    
    # Send error message to user if possible
    if isinstance(update, Update) and update.effective_message:
        try:
            await update.effective_message.reply_text(
                "❌ Desculpe, ocorreu um erro ao processar sua solicitação.\n"
                "Tente novamente em alguns instantes."
            )
        except Exception as e:
            logger.error(f"Could not send error message to user: {e}")
    
    # Notify admins if configured
    if ADMIN_IDS and context.bot:
        error_message = (
            f"🚨 **Erro no Bot**\n\n"
            f"**Usuário:** {user_info}\n"
            f"**Erro:** {str(context.error)[:200]}...\n"
            f"**Horário:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        
        for admin_id in ADMIN_IDS:
            try:
                await context.bot.send_message(
                    chat_id=admin_id,
                    text=error_message,
                    parse_mode='Markdown'
                )
            except Exception as e:
                logger.error(f"Could not send error notification to admin {admin_id}: {e}")

async def stats_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the /stats command (admin only).
    Shows bot statistics and usage information.
    """
    user = update.effective_user
    
    if user.id not in ADMIN_IDS:
        await update.message.reply_text("❌ Comando disponível apenas para administradores.")
        return
    
    logger.info(f"Admin {user.id} ({user.username}) requested stats")
    
    stats_message = (
        "📊 **Estatísticas do Bot**\n\n"
        f"**Bot:** {BOT_NAME}\n"
        f"**Status:** ✅ Online\n"
        f"**Horário:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"**Admins configurados:** {len(ADMIN_IDS)}\n\n"
        "Use /help para ver todos os comandos disponíveis."
    )
    
    await update.message.reply_text(stats_message, parse_mode='Markdown')
