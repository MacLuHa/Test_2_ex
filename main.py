import random
import PIL
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.filters import BaseFilter
from aiogram.types import PhotoSize
from dotenv import load_dotenv
from FindGM_NW import FindGM, FindGM2, FindGM3
from CheckApp import search, find_coordinates
#FindGM = ResNet50
#FindGM2 = MobileNet
#FindGM3 = VGG19 (переобученная)

load_dotenv()
#Инцициализируем бота, токен спрятан в переменном окружении, как и id чатов
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()

# Создание директории для загрузок, если она не существует
DOWNLOAD_FOLDER = 'downloads_telegram'
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@dp.message(F.photo)
async def download_photo(message: Message, bot: Bot):
    #Сохраняем изображение в указанной папке
    await bot.download(
        message.photo[-1],
        destination=os.path.join(DOWNLOAD_FOLDER, f"{message.photo[-1].file_id}.jpg"))

    try:
        #Используем обученные модели для классификации изображения
        if FindGM2(os.path.join(DOWNLOAD_FOLDER, f"{message.photo[-1].file_id}.jpg")) == True:
            #Отправляем в нужную группу координаты, найденные на скриншоте
            await bot.send_message(chat_id=os.getenv('CHAT_ID_1'),
                                   text = find_coordinates(search(f"downloads_telegram\\{message.photo[-1].file_id}.jpg")))
            #и пересылаем само собщение с подписью из изначальной группы
            await bot.forward_message(chat_id=os.getenv('CHAT_ID_1'),
                                      from_chat_id=os.getenv('CHAT_ID_2'),
                                      message_id=message.message_id,
                                      )
        else:
            #Если модель точно определила, что это не скриншот
            print('Не является скриншотом Google Maps')
    except UnboundLocalError:
        #Если модель ошибочно классифицировала изображение как скриншот Google Maps
        print("Изображение не содержит координат")


if __name__ == '__main__':
    dp.run_polling(bot)
