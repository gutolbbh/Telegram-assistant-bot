#!/usr/bin/env python3
"""
Telegram Bot Main Application
A simple Telegram bot that responds to user commands and provides basic interaction capabilities.
"""

import logging
import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN, WEBHOOK_URL
from handlers import start_handler, help_handler, echo_handler, error_handler, stats_handler, gpt_handler
from utils import setup_logging

def main():
    """Start the bot."""
    # Setup logging
    setup_logging()
    logger = logging.getLogger(__name__)
    
    # Validate bot token
    if not BOT_TOKEN:
        logger.error("Bot token not found! Please set TELEGRAM_BOT_TOKEN environment variable.")
        return
    
    logger.info("Starting Telegram bot...")
    
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Register command handlers
    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("help", help_handler))
    application.add_handler(CommandHandler("stats", stats_handler))
    application.add_handler(CommandHandler("gpt", gpt_handler))
    
    # Register message handler for non-command messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_handler))
    
    # Register error handler
    application.add_error_handler(error_handler)
    
    # Start the bot
    try:
        logger.info("Bot is starting polling...")
        application.run_polling(allowed_updates=["message"])
    except Exception as e:
        logger.error(f"Error starting bot: {e}")
        raise

if __name__ == '__main__':
    main()