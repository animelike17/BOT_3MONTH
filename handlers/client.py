import random
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp

async def mem(message: types.Message):
    photo = open('media/mem.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=photo)

async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('Next', callback_data='button_1')
    markup.add(button_1)
    question = 'Сколько лет компании Apple'
    answer = [
        '46',
        '36',
        '76'
    ]

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answer,
        type='quiz',
        is_anonymous=True,
        correct_option_id=0,
        explanation='больше 40 лет',
        reply_markup =markup
    )

async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.reply('Надо ответить на сообщение')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')
