from aiogram import F
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot import strings
from bot.constants import AccessLevel
from bot.tools.decorators import login_required

router = Router()


@router.message(CommandStart())
@login_required(access_level=AccessLevel.GUEST)
async def start(message: Message):
    await message.reply(strings.START_MESSAGE)


@router.message(Command("info"))
@login_required(access_level=AccessLevel.GUEST)
async def info(message: Message):
    text = (
        f"Your username: {message.from_user.username}\n"
        f"Your id: {message.from_user.id}"
    )
    await message.reply(text)

@router.message(Command("keyboard"))
@login_required(access_level=AccessLevel.USER)
async def show_keyboard(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Option 1", callback_data="option1"))
    builder.add(InlineKeyboardButton(text="Option 2", callback_data="option2"))
    builder.add(
        InlineKeyboardButton(text="Visit our website", url="https://example.com")
    )

    await message.answer("Please choose an option:", reply_markup=builder.as_markup())


@router.callback_query(F.data == "option1")
async def process_option1(callback: CallbackQuery):
    await callback.answer("You selected Option 1!")
    await callback.message.answer(
        "You clicked on Option 1. Here's some information about it."
    )


@router.callback_query(F.data == "option2")
async def process_option2(callback: CallbackQuery):
    await callback.answer("You selected Option 2!")
    await callback.message.answer(
        "You clicked on Option 2. Here's what you need to know."
    )


@router.message()
@login_required(access_level=AccessLevel.USER)
async def echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)
