import telebot
from telebot import types
import requests

token = '6840771069:AAH-fk177KP14XVix6MKRPJXxVuz3g0Bsus'
bot = telebot.TeleBot(token)

activity_type = None
activity_quantity = 1

def menu(id):
    markup = types.ReplyKeyboardMarkup()
    func1 = types.KeyboardButton('Рандомное задание')
    func2 = types.KeyboardButton('Задание с параметрами')
    func3 = types.KeyboardButton('Параметры задания')
    markup.add(func1, func2, func3)
    bot.send_message(id, "Выберите функцию:", reply_markup=markup)


def options(id):
    markup_options = types.ReplyKeyboardMarkup()
    option1 = types.KeyboardButton('Тип')
    option2 = types.KeyboardButton('Количество')
    back = types.KeyboardButton('Назад')
    markup_options.add(option1, option2, back)
    bot.send_message(id, "Выберите изменяемый параметр:", reply_markup=markup_options)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет!")
    bot.send_message(message.chat.id, "В данный момент бот находится в разработке.")
    menu(message.chat.id)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    global activity_type
    global activity_quantity
    if message.text == 'Рандомное задание':
        url = f'https://www.boredapi.com/api/activity'
        activity = requests.get(url).json()
        bot.send_message(message.chat.id, activity["activity"])
    if message.text == 'Задание с параметрами':
        if activity_type == None:
            for _ in range(activity_quantity):
                url = f'https://www.boredapi.com/api/activity'
                activity = requests.get(url).json()
                bot.send_message(message.chat.id, activity["activity"])
        else:
            for _ in range(activity_quantity):
                url = f'https://www.boredapi.com/api/activity'
                activity = requests.get(url).json()
                while activity["type"] != activity_type:
                    activity = requests.get(url).json()
                bot.send_message(message.chat.id, activity["activity"])

    if message.text == 'Параметры задания':
        options(message.chat.id)

    if message.text == 'Тип':
        markup_types = types.ReplyKeyboardMarkup()
        t1 = types.KeyboardButton('busywork')
        t2 = types.KeyboardButton('relaxation')
        t3 = types.KeyboardButton('social')
        t4 = types.KeyboardButton('recreational')
        t5 = types.KeyboardButton('education')
        t6 = types.KeyboardButton('cooking')
        t7 = types.KeyboardButton('music')
        t8 = types.KeyboardButton('charity')
        t9 = types.KeyboardButton('diy')
        t10 = types.KeyboardButton('random')
        markup_types.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10)
        bot.send_message(message.chat.id, "Выберите изменяемый параметр:", reply_markup=markup_types)


    if message.text == 'busywork':
        activity_type = 'busywork'
        options(message.chat.id)
    if message.text == 'relaxation':
        activity_type = 'relaxation'
        options(message.chat.id)
    if message.text == 'social':
        activity_type = 'social'
        options(message.chat.id)
    if message.text == 'recreational':
        activity_type = 'recreational'
        options(message.chat.id)
    if message.text == 'education':
        activity_type = 'education'
        options(message.chat.id)
    if message.text == 'cooking':
        activity_type = 'cooking'
        options(message.chat.id)
    if message.text == 'music':
        activity_type = 'music'
        options(message.chat.id)
    if message.text == 'charity':
        activity_type = 'charity'
        options(message.chat.id)
    if message.text == 'diy':
        activity_type = 'diy'
        options(message.chat.id)
    if message.text == 'random':
        activity_type = None
        options(message.chat.id)

    if message.text == 'Назад':
        menu(message.chat.id)

    if message.text == 'Количество':
        bot.send_message(message.chat.id, "Введите количество выводов(от 1 до 100):")

    if message.text.isdigit():
        activity_quantity = int(message.text)


bot.infinity_polling()
