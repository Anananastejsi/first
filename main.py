import telebot
import sqlite3
from telebot import types
from telebot.types import WebAppInfo

bot = telebot.TeleBot('6397644079:AAGJmkwjUSp4HfPVb-ZjHdScfaHOqzdLKLs')
conn = sqlite3.connect("C:/BasesForBOTS/bot.db", check_same_thread=False)
cur = conn.cursor()

web_app=WebAppInfo(url="https://anananastejsi.github.io/first/")


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_app = types.KeyboardButton('Языки', web_app=web_app)
        markup.add(btn_app)
        bot.send_message(message.from_user.id, 'УЗНАТЬ!', reply_markup=markup)

@bot.message_handler(content_types='web_app_data')
def buy_process(web_app_message):
    a = web_app_message.web_app_data.button_text

    if a == 'Английский':
        a = 'Английский_язык'
    elif a == 'Французский':
        a = 'Французский_язык'
    elif a == 'Японский':
        a = 'Японский_язык'
    elif a == 'Мотивация':
        a = 'Мотивационная_цитата'

    bot.send_message(web_app_message.chat.id,
                     f'{conn.execute(f"Select NAME from {a} WHERE id == {web_app_message.web_app_data.data}").fetchone()[0]}\n\n'
                     f'{conn.execute(f"Select DISC from {a} WHERE id =={web_app_message.web_app_data.data}").fetchone()[0]}')

    x = conn.execute(f"Select LAT, LEN from {a} WHERE id == {web_app_message.web_app_data.data}").fetchone()
    bot.send_location(web_app_message.chat.id, x[0], x[1])


bot.polling(none_stop=True, interval=0)

