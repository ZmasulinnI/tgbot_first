import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import FSInputFile
from aiogram.filters.command import Command
import template as tp
from img_func import add_logo
import os

from config import TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(tp.HELLO_MSG)
    # message.photo

@dp.message(F.content_type.in_({'photo'}))
async def cmd_photo(message: types.Message):
    photo = message.photo[-1]
    await bot.download(photo.file_id, f"temp\\{photo.file_id}.png")
    add_logo(photo.file_id)
    new_photo = FSInputFile(f"temp/{photo.file_id}.png")
    await bot.send_photo(chat_id=message.chat.id,photo=new_photo)
    os.remove(f"temp/{photo.file_id}.png")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())