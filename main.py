import os

from fastapi import FastAPI
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

from dotenv import load_dotenv


load_dotenv()


TOKEN = os.getenv("BOT_TOKEN")


bot = Bot(
    token=TOKEN
)


dp = Dispatcher()

app = FastAPI()



@dp.message(Command("start"))
async def start(message: Message):

    await message.answer(
        "⭐ Добро пожаловать в StarForge\n\n"
        "Открой приложение через кнопку меню."
    )



@app.get("/")
def home():

    return {
        "status":"StarForge online"
    }



async def run_bot():

    await dp.start_polling(bot)



if __name__ == "__main__":

    import asyncio

    asyncio.run(run_bot())
import os
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(
        "Играть",
        callback_data="play"
    )

    btn2 = types.InlineKeyboardButton(
        "Профиль",
        callback_data="profile"
    )

    markup.add(btn1, btn2)

    bot.send_message(
        message.chat.id,
        "ArtChivoApp запущен.\n\nДобро пожаловать.",
        reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == "play":
        bot.send_message(
            call.message.chat.id,
            "Игра загружена."
        )

    elif call.data == "profile":
        bot.send_message(
            call.message.chat.id,
            "Профиль игрока."
        )


print("Bot started")

bot.infinity_polling()
