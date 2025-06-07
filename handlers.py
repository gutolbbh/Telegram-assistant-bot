"""
Command and message handlers for the Telegram bot.
Contains all the bot's response logic and command implementations.
"""

import logging
from datetime import datetime
<<<<<<< HEAD
from telegram import Update
from telegram.ext import ContextTypes
from config import BOT_NAME, ADMIN_IDS

logger = logging.getLogger(__name__)

=======

from telegram import Update
from telegram.ext import ContextTypes

import openai

from config import BOT_NAME, ADMIN_IDS, OPENAI_API_KEY

logger = logging.getLogger(__name__)

openai.api_key = OPENAI_API_KEY


>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the /start command.
    Sends a welcome message to the user.
    """
    user = update.effective_user
    logger.info(f"User {user.id} ({user.username}) started the bot")
<<<<<<< HEAD
    
=======

>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
    welcome_message = (
        f"🤖 Olá, {user.first_name}! Eu sou o {BOT_NAME}!\n\n"
        "Comandos disponíveis:\n"
        "/start - Iniciar o bot\n"
<<<<<<< HEAD
        "/help - Mostrar ajuda\n\n"
        "Você pode me enviar qualquer mensagem e eu vou responder!"
    )
    
    await update.message.reply_text(welcome_message)

=======
        "/help - Mostrar ajuda\n"
        "/stats - Estatísticas (admin)\n"
        "/gpt - Pergunte ao GPT\n"
        "/traduz - Traduza texto\n"
        "/resumo - Resuma texto\n"
        "/meme - Gere meme divertido\n\n"
        "Você pode me enviar qualquer mensagem e eu vou responder!"
    )

    await update.message.reply_text(welcome_message)


>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the /help command.
    Provides information about bot capabilities and commands.
    """
    user = update.effective_user
    logger.info(f"User {user.id} ({user.username}) requested help")
<<<<<<< HEAD
    
=======

>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
    help_message = (
        f"🆘 **Ajuda do {BOT_NAME}**\n\n"
        "**Comandos disponíveis:**\n"
        "• /start - Iniciar o bot e ver mensagem de boas-vindas\n"
<<<<<<< HEAD
        "• /help - Mostrar esta mensagem de ajuda\n\n"
        "**Como usar:**\n"
        "• Envie qualquer mensagem de texto e eu vou responder\n"
        "• Use os comandos acima para funcionalidades específicas\n\n"
=======
        "• /help - Mostrar esta mensagem de ajuda\n"
        "• /stats - Mostrar estatísticas (apenas admins)\n"
        "• /gpt <pergunta> - Respondo perguntas com GPT-4\n"
        "• /traduz <texto> - Tradução para português\n"
        "• /resumo <texto> - Resumo rápido\n"
        "• /meme <tema> - Gerar meme engraçado\n\n"
        "**Como usar:**\n"
        "• Envie qualquer mensagem de texto e eu responderei\n"
        "• Use os comandos para funcionalidades específicas\n\n"
>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
        "**Sobre:**\n"
        f"• Bot: {BOT_NAME}\n"
        "• Desenvolvido em Python\n"
        "• Sempre online e pronto para conversar! 💬"
    )
<<<<<<< HEAD
    
    await update.message.reply_text(help_message, parse_mode='Markdown')

=======

    await update.message.reply_text(help_message, parse_mode='Markdown')


>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
async def echo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle regular text messages (not commands).
    Echoes the user's message with additional context.
    """
    user = update.effective_user
<<<<<<< HEAD
    message_text = update.message.text
    
    logger.info(f"User {user.id} ({user.username}) sent message: {message_text[:50]}...")
    
    # Create a response based on the message
=======
    message_text = update.message.text or ""

    logger.info(f"User {user.id} ({user.username}) sent message: {message_text[:50]}...")

    text_lower = message_text.lower()

>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
    if len(message_text) > 100:
        response = (
            f"📝 Recebi sua mensagem longa, {user.first_name}!\n"
            f"Sua mensagem tem {len(message_text)} caracteres.\n"
            f"Aqui está um resumo: '{message_text[:50]}...'"
        )
<<<<<<< HEAD
    elif "olá" in message_text.lower() or "oi" in message_text.lower():
        response = f"👋 Olá, {user.first_name}! Como posso ajudar você hoje?"
    elif "obrigado" in message_text.lower() or "obrigada" in message_text.lower():
=======
    elif any(greeting in text_lower for greeting in ["olá", "oi", "ola", "e aí", "eai"]):
        response = f"👋 Olá, {user.first_name}! Como posso ajudar você hoje?"
    elif any(thanks in text_lower for thanks in ["obrigado", "obrigada", "valeu", "brigado"]):
>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
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
<<<<<<< HEAD
    
    await update.message.reply_text(response)

=======

    await update.message.reply_text(response)


>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle errors that occur during bot operation.
    Logs errors and optionally notifies admins.
    """
    logger.error(f"Exception while handling an update: {context.error}")
<<<<<<< HEAD
    
    # Try to get user information if available
=======

>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
    user_info = "Unknown user"
    if isinstance(update, Update) and update.effective_user:
        user = update.effective_user
        user_info = f"User {user.id} ({user.username})"
<<<<<<< HEAD
    
    logger.error(f"Error occurred for {user_info}: {context.error}")
    
    # Send error message to user if possible
=======

    logger.error(f"Error occurred for {user_info}: {context.error}")

>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
    if isinstance(update, Update) and update.effective_message:
        try:
            await update.effective_message.reply_text(
                "❌ Desculpe, ocorreu um erro ao processar sua solicitação.\n"
                "Tente novamente em alguns instantes."
            )
        except Exception as e:
            logger.error(f"Could not send error message to user: {e}")
<<<<<<< HEAD
    
    # Notify admins if configured
=======

>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
    if ADMIN_IDS and context.bot:
        error_message = (
            f"🚨 **Erro no Bot**\n\n"
            f"**Usuário:** {user_info}\n"
            f"**Erro:** {str(context.error)[:200]}...\n"
            f"**Horário:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
<<<<<<< HEAD
        
=======

>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
        for admin_id in ADMIN_IDS:
            try:
                await context.bot.send_message(
                    chat_id=admin_id,
                    text=error_message,
                    parse_mode='Markdown'
                )
            except Exception as e:
                logger.error(f"Could not send error notification to admin {admin_id}: {e}")

<<<<<<< HEAD
=======

>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
async def stats_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the /stats command (admin only).
    Shows bot statistics and usage information.
    """
    user = update.effective_user
<<<<<<< HEAD
    
    if user.id not in ADMIN_IDS:
        await update.message.reply_text("❌ Comando disponível apenas para administradores.")
        return
    
    logger.info(f"Admin {user.id} ({user.username}) requested stats")
    
=======

    if user.id not in ADMIN_IDS:
        await update.message.reply_text("❌ Comando disponível apenas para administradores.")
        return

    logger.info(f"Admin {user.id} ({user.username}) requested stats")

>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
    stats_message = (
        "📊 **Estatísticas do Bot**\n\n"
        f"**Bot:** {BOT_NAME}\n"
        f"**Status:** ✅ Online\n"
        f"**Horário:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"**Admins configurados:** {len(ADMIN_IDS)}\n\n"
        "Use /help para ver todos os comandos disponíveis."
    )
<<<<<<< HEAD
    
    await update.message.reply_text(stats_message, parse_mode='Markdown')
=======

    await update.message.reply_text(stats_message, parse_mode='Markdown')


async def gpt_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the /gpt command.
    Sends a prompt to OpenAI GPT-4 and replies with the response.
    """
    if not OPENAI_API_KEY:
        await update.message.reply_text("❌ Chave OpenAI não configurada.")
        return

    prompt = " ".join(context.args)
    if not prompt:
        await update.message.reply_text("📝 Use: /gpt <pergunta>")
        return

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um assistente de cultura pop divertido e informativo."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=512,
            temperature=0.7,
        )
        reply = response.choices[0].message.content.strip()
        await update.message.reply_text(reply)
    except Exception as e:
        logger.error(f"Erro na chamada GPT: {e}")
        await update.message.reply_text(f"Erro ao chamar GPT: {str(e)}")


async def traduz_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the /traduz command.
    Translates given text to Portuguese (Brazilian) using OpenAI GPT.
    """
    if not OPENAI_API_KEY:
        await update.message.reply_text("❌ Chave OpenAI não configurada.")
        return

    text = " ".join(context.args)
    if not text:
        await update.message.reply_text("📝 Use: /traduz <texto para traduzir>")
        return

    prompt = f"Traduza o texto a seguir para português brasileiro, mantendo o tom informal e claro:\n\n{text}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um tradutor especialista em cultura pop."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=512,
            temperature=0.5,
        )
        reply = response.choices[0].message.content.strip()
        await update.message.reply_text(reply)
    except Exception as e:
        logger.error(f"Erro na tradução: {e}")
        await update.message.reply_text(f"Erro ao traduzir: {str(e)}")


async def resumo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the /resumo command.
    Summarizes given text focused on pop culture using OpenAI GPT.
    """
    if not OPENAI_API_KEY:
        await update.message.reply_text("❌ Chave OpenAI não configurada.")
        return

    text = " ".join(context.args)
    if not text:
        await update.message.reply_text("📝 Use: /resumo <texto para resumir>")
        return

    prompt = f"Faça um resumo rápido e objetivo do seguinte texto, focado em cultura pop:\n\n{text}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um assistente que resume textos de cultura pop."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=256,
            temperature=0.5,
        )
        reply = response.choices[0].message.content.strip()
        await update.message.reply_text(reply)
    except Exception as e:
        logger.error(f"Erro no resumo: {e}")
        await update.message.reply_text(f"Erro ao resumir: {str(e)}")


async def meme_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the /meme command.
    Generates a funny meme text about pop culture using OpenAI GPT.
    """
    if not OPENAI_API_KEY:
        await update.message.reply_text("❌ Chave OpenAI não configurada.")
        return

    prompt = " ".join(context.args)
    if not prompt:
        await update.message.reply_text("📝 Use: /meme <tema para meme>")
        return

    prompt_gpt = f"Crie um meme engraçado e rápido sobre cultura pop baseado no tema: {prompt}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um gerador de memes engraçados e criativos sobre cultura pop."},
                {"role": "user", "content": prompt_gpt}
            ],
            max_tokens=128,
            temperature=0.9,
        )
        reply = response.choices[0].message.content.strip()
        await update.message.reply_text(reply)
    except Exception as e:
        logger.error(f"Erro ao gerar meme: {e}")
        await update.message.reply_text(f"Erro ao gerar meme: {str(e)}")
>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
