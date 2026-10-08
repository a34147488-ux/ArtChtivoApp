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
