import logging
from aiogram.types import Message

from bot.constants import AccessLevel
from bot.models import User


async def notify(message: Message, users_level: AccessLevel, notification_text: str):
    users = User.select().where(User.access_level >= users_level)

    if not users:
        logging.info(f"No users to notify (level >= {users_level})")
        return

    for user in users:
        try:
            bot = message.bot
            await bot.send_message(chat_id=user.id, text=notification_text)
        except Exception as e:
            logging.error(f"Failed to send notification to user {user.id}: {str(e)}")
