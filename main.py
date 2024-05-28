import random
import PIL
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.filters import BaseFilter
from aiogram.types import PhotoSize
from dotenv import load_dotenv
from FindGM_NW import FindGM,FindGM2, FindGM3
from CheckApp import search,find_coordinates, ToGray
#FindGM = ResNet50
#FindGM2 = MobileNet
#FindGM3 = VGG19 (переобученная)

load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()

@dp.message(F.photo)
async def download_photo(message: Message, bot: Bot):
    await bot.download(
        message.photo[-1],
        destination=f"D:\\Data\\Telegram\\{message.photo[-1].file_id}.jpg"
    )
    try:
        if FindGM2(f"D:\\Data\\Telegram\\{message.photo[-1].file_id}.jpg") == True:
            await bot.send_message(chat_id=os.getenv('CHAT_ID_1'),
                                   text = find_coordinates(search(f"D:\\Data\\Telegram\\{message.photo[-1].file_id}.jpg")))

            await bot.forward_message(chat_id=os.getenv('CHAT_ID_1'),
                                      from_chat_id=os.getenv('CHAT_ID_2'),
                                      message_id=message.message_id,
                                      )
        else:
            print('Не является скриншотом Google Maps')
    except UnboundLocalError:
        print("Изображение не содержит координат")


if __name__ == '__main__':
    dp.run_polling(bot)