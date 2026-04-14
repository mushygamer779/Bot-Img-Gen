from telebot import TeleBot
from config import Token
from logic import *
import os

bot = TeleBot(Token)




@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот для генерации изображений. Отправь мне описание изображения, и я постараюсь его создать!")



@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Доступные команды:\n/start - Начать работу с ботом\n/generate - Генерировать изображение\n/help - Показать помощь")



@bot.message_handler(func=lambda message: True)
def genImage(message):

    bot.send_message(message.chat.id, "Получаю ваш запрос...")

    image = ImageGenerator().download_image(message.text)


    bot.send_message(message.chat.id, "Генерирую изображение...")

    with open (image, 'rb') as img:
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, f'here is your image with prompt: {,essage.from_user.id}')
    os.remove(image)


bot.infinity_polling()
