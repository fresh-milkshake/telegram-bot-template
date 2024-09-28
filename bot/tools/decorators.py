from aiogram.types import Message

from bot import strings
from bot.constants import AccessLevel, DEFAULT_ACCESS_LEVEL, UNKNOWN_STRING_VALUE
from bot.models import User


def login_required(access_level: AccessLevel):
    def decorator(func):
        async def wrapper(message: Message):
            user: User = User.get_or_none(username=message.from_user.username)
            if user is None:
                user = User.create(
                    id=message.from_user.id,
                    username=message.from_user.username,
                    language_code=message.from_user.language_code,
                    first_name=message.from_user.first_name or UNKNOWN_STRING_VALUE,
                    last_name=message.from_user.last_name or UNKNOWN_STRING_VALUE,
                    url=message.from_user.url,
                    access_level=DEFAULT_ACCESS_LEVEL,
                )
                user.save()

            if user.access_level < access_level:    
                await message.answer(strings.NO_ACCESS)
                return
            return await func(message)

        return wrapper

    return decorator
