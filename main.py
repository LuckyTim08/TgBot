import telebot
import requests

token = '6840771069:AAH-fk177KP14XVix6MKRPJXxVuz3g0Bsus'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет!")
    bot.send_message(message.chat.id, "В данный момент бот находится в разработке.")


@bot.message_handler(commands=['creat_activity'])
def creat_activity(message):
    url = f'https://www.boredapi.com/api/activity'
    activity = requests.get(url).json()
    bot.send_message(message.chat.id, activity["activity"])

bot.infinity_polling()
