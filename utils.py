"""
Utility functions for the Telegram bot.
Contains helper functions, logging setup, and common utilities.
"""

import logging
import sys
from datetime import datetime
<<<<<<< HEAD
from typing import Dict, Any, Optional
from config import LOG_LEVEL, LOG_FORMAT, ENABLE_LOGGING
=======
from typing import Dict, Any, Optional, Tuple
from config import LOG_LEVEL, LOG_FORMAT, ENABLE_LOGGING, ADMIN_IDS
>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6

def setup_logging() -> None:
    """
    Set up logging configuration for the bot.
    Configures both file and console logging with appropriate levels.
    """
    if not ENABLE_LOGGING:
        return
<<<<<<< HEAD
    
    # Convert string log level to logging constant
    numeric_level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter(LOG_FORMAT)
    
=======

    # Convert string log level to logging constant
    numeric_level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)

    # Create formatter
    formatter = logging.Formatter(LOG_FORMAT)

>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
    # Setup console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(numeric_level)
    console_handler.setFormatter(formatter)
<<<<<<< HEAD
    
=======

>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
    # Setup file handler
    file_handler = logging.FileHandler('bot.log', encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
<<<<<<< HEAD
    
=======

>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
    # Configure root logger
    logging.basicConfig(
        level=numeric_level,
        handlers=[console_handler, file_handler],
        format=LOG_FORMAT
    )
<<<<<<< HEAD
    
    # Silence some verbose loggers
    logging.getLogger('httpx').setLevel(logging.WARNING)
    logging.getLogger('telegram').setLevel(logging.WARNING)
    
    logger = logging.getLogger(__name__)
    logger.info("Logging setup completed")
=======

    # Silence noisy loggers
    logging.getLogger('httpx').setLevel(logging.WARNING)
    logging.getLogger('telegram').setLevel(logging.WARNING)

    logger = logging.getLogger(__name__)
    logger.info("✅ Logging setup completed.")
>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6

def format_user_info(user) -> str:
    """
    Format user information for logging and display.
<<<<<<< HEAD
    
    Args:
        user: Telegram User object
        
    Returns:
        Formatted string with user information
    """
    if not user:
        return "Unknown user"
    
=======
    """
    if not user:
        return "Unknown user"

>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
    username = f"@{user.username}" if user.username else "No username"
    return f"{user.first_name} {user.last_name or ''} ({username}) [ID: {user.id}]".strip()

def is_admin(user_id: int) -> bool:
    """
    Check if a user ID belongs to an admin.
<<<<<<< HEAD
    
    Args:
        user_id: Telegram user ID
        
    Returns:
        True if user is admin, False otherwise
    """
    from config import ADMIN_IDS
=======
    """
>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
    return user_id in ADMIN_IDS

def sanitize_text(text: str, max_length: int = 4096) -> str:
    """
    Sanitize text for Telegram message sending.
    Removes or escapes potentially problematic characters.
<<<<<<< HEAD
    
    Args:
        text: Text to sanitize
        max_length: Maximum allowed length
        
    Returns:
        Sanitized text
    """
    if not text:
        return ""
    
    # Truncate if too long
    if len(text) > max_length:
        text = text[:max_length-3] + "..."
    
    # Remove null bytes and other control characters
    text = ''.join(char for char in text if ord(char) >= 32 or char in '\n\r\t')
    
=======
    """
    if not text:
        return ""

    if len(text) > max_length:
        text = text[:max_length - 3] + "..."

    text = ''.join(char for char in text if ord(char) >= 32 or char in '\n\r\t')
>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
    return text

def get_current_timestamp() -> str:
    """
    Get current timestamp in a readable format.
<<<<<<< HEAD
    
    Returns:
        Formatted timestamp string
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def parse_command_args(text: str) -> tuple[str, list]:
    """
    Parse command and arguments from message text.
    
    Args:
        text: Message text starting with command
        
    Returns:
        Tuple of (command, arguments_list)
    """
    if not text or not text.startswith('/'):
        return "", []
    
    parts = text.split()
    command = parts[0][1:]  # Remove the '/' prefix
    args = parts[1:] if len(parts) > 1 else []
    
=======
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def parse_command_args(text: str) -> Tuple[str, list]:
    """
    Parse command and arguments from message text.
    """
    if not text or not text.startswith('/'):
        return "", []

    parts = text.strip().split()
    command = parts[0][1:]  # Remove '/'
    args = parts[1:]
>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
    return command, args

def create_error_context(error: Exception, update: Optional[Any] = None) -> Dict[str, Any]:
    """
    Create error context for logging and debugging.
<<<<<<< HEAD
    
    Args:
        error: Exception that occurred
        update: Telegram Update object (optional)
        
    Returns:
        Dictionary with error context information
=======
>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
    """
    context = {
        'error_type': type(error).__name__,
        'error_message': str(error),
        'timestamp': get_current_timestamp(),
    }
<<<<<<< HEAD
    
    if update and hasattr(update, 'effective_user') and update.effective_user:
        context['user'] = format_user_info(update.effective_user)
    
    if update and hasattr(update, 'effective_message') and update.effective_message:
        message = update.effective_message
        context['message_id'] = message.message_id
        context['chat_id'] = message.chat_id
        if message.text:
            context['message_text'] = message.text[:100]  # First 100 chars
    
=======

    if update and hasattr(update, 'effective_user') and update.effective_user:
        context['user'] = format_user_info(update.effective_user)

    if update and hasattr(update, 'effective_message') and update.effective_message:
        msg = update.effective_message
        context['message_id'] = msg.message_id
        context['chat_id'] = msg.chat_id
        if msg.text:
            context['message_text'] = msg.text[:100]

>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
    return context

class RateLimiter:
    """
<<<<<<< HEAD
    Simple rate limiter to prevent spam.
    """
    
    def __init__(self, max_calls: int = 20, time_window: int = 60):
        """
        Initialize rate limiter.
        
        Args:
            max_calls: Maximum calls allowed in time window
            time_window: Time window in seconds
        """
        self.max_calls = max_calls
        self.time_window = time_window
        self.calls: Dict[int, list] = {}
    
    def is_allowed(self, user_id: int) -> bool:
        """
        Check if user is allowed to make a request.
        
        Args:
            user_id: Telegram user ID
            
        Returns:
            True if allowed, False if rate limited
        """
        current_time = datetime.now().timestamp()
        
        if user_id not in self.calls:
            self.calls[user_id] = []
        
        # Remove old calls outside the time window
        self.calls[user_id] = [
            call_time for call_time in self.calls[user_id]
            if current_time - call_time < self.time_window
        ]
        
        # Check if user has exceeded the limit
        if len(self.calls[user_id]) >= self.max_calls:
            return False
        
        # Add current call
=======
    Simple rate limiter to prevent abuse.
    """

    def __init__(self, max_calls: int = 20, time_window: int = 60):
        self.max_calls = max_calls
        self.time_window = time_window
        self.calls: Dict[int, list] = {}

    def is_allowed(self, user_id: int) -> bool:
        current_time = datetime.now().timestamp()

        if user_id not in self.calls:
            self.calls[user_id] = []

        self.calls[user_id] = [
            t for t in self.calls[user_id]
            if current_time - t < self.time_window
        ]

        if len(self.calls[user_id]) >= self.max_calls:
            return False

>>>>>>> a8e391ed26c2b4ed4ba1730fb254b97a1b1246d6
        self.calls[user_id].append(current_time)
        return True
