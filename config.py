"""
Configuration module for the Telegram bot.
Handles environment variables and bot settings.
"""

import os
from typing import Optional

# Bot Configuration
BOT_TOKEN: Optional[str] = os.getenv("BOT_TOKEN") or os.getenv(
    "TELEGRAM_BOT_TOKEN")
WEBHOOK_URL: Optional[str] = os.getenv("WEBHOOK_URL")

# Logging Configuration
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Bot Settings
BOT_NAME: str = os.getenv("BOT_NAME", "Python Bot")
BOT_USERNAME: str = os.getenv("BOT_USERNAME", "pythonbot")

# Feature Flags
ENABLE_LOGGING: bool = os.getenv("ENABLE_LOGGING", "true").lower() == "true"
DEBUG_MODE: bool = os.getenv("DEBUG_MODE", "false").lower() == "true"

# Rate limiting (messages per minute per user)
RATE_LIMIT: int = int(os.getenv("RATE_LIMIT", "20"))

# Admin Configuration
ADMIN_IDS: list = []
admin_ids_str = os.getenv("ADMIN_IDS", "")
if admin_ids_str:
    try:
        ADMIN_IDS = [
            int(id.strip()) for id in admin_ids_str.split(",") if id.strip()
        ]
    except ValueError:
        print(
            "Warning: Invalid ADMIN_IDS format. Should be comma-separated integers."
        )
