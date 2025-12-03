import logging
from aiogram import Bot, Dispatcher, executor, types
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=['document'])
async def save_file(message: types.Message):
    file = await bot.get_file(message.document.file_id)
    await message.document.download()
    await message.reply("Saved file!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
