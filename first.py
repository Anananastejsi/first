import telebot
import sqlite3
from telebot import types
from telebot.types import WebAppInfo

bot = telebot.TeleBot('6397644079:AAGJmkwjUSp4HfPVb-ZjHdScfaHOqzdLKLs')
conn = sqlite3.connect("bot.db", check_same_thread=False)
cur = conn.cursor()

web_park = WebAppInfo(url="https://anananastejsi.github.io/first/")

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_parks = types.KeyboardButton('Английский язык', web_app=web_park)
        btn_mons = types.KeyboardButton('Французский_язык', web_app=web_park)
        markup.add(btn_parks, btn_mons)
        bot.send_message(message.from_user.id, 'Выберите, что Вы предпочитаете сейчас.', reply_markup=markup)

@bot.message_handler(content_types='web_app_data')
def buy_process(web_app_message):
    a = web_app_message.web_app_data.button_text
