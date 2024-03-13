import sqlite3
import telebot
from telebot import types

global msg

bot = telebot.TeleBot('6397644079:AAGJmkwjUSp4HfPVb-ZjHdScfaHOqzdLKLs')
conn = sqlite3.connect("C:/BasesForBOTS/bot.db", check_same_thread=False)
cur = conn.cursor()


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Английский')
        btn2 = types.KeyboardButton('Французский')
        btn3 = types.KeyboardButton('Японский')
        btn4 = types.KeyboardButton('Мотивация')
        markup.add(btn1, btn2, btn3)
        markup.add(btn4)
        bot.send_message(message.from_user.id, 'Выбери',
                         reply_markup=markup)

    elif message.text == 'Английский':
        keyboard = types.InlineKeyboardMarkup()
        key_ang1 = types.InlineKeyboardButton(
            text=conn.execute("Select NAME from Английский_язык WHERE ID == 1 ").fetchone()[0], callback_data='ang1'
        )
        keyboard.add(key_ang1)
        key_ang2 = types.InlineKeyboardButton(
            text=conn.execute("Select NAME from Английский_язык WHERE ID == 2 ").fetchone()[0], callback_data='ang2'
        )
        keyboard.add(key_ang2)
        key_ang3 = types.InlineKeyboardButton(
            text=conn.execute("Select NAME from Английский_язык WHERE ID == 3 ").fetchone()[0], callback_data='ang3'
        )
        keyboard.add(key_ang3)

        bot.send_message(message.from_user.id, text='Узнайте перевод.', reply_markup=keyboard)

    elif message.text == 'Французский':
        keyboard = types.InlineKeyboardMarkup()
        key_fr1 = types.InlineKeyboardButton(
            text=conn.execute('Select NAME from Французский_язык WHERE ID == 1 ').fetchone()[0], callback_data='fr1'
        )
        keyboard.add(key_fr1)
        key_fr2 = types.InlineKeyboardButton(
            text=conn.execute('Select NAME from Французский_язык WHERE ID == 2 ').fetchone()[0], callback_data='fr2'
        )
        keyboard.add(key_fr2)
        key_fr3 = types.InlineKeyboardButton(
            text=conn.execute('Select NAME from Французский_язык WHERE ID == 3 ').fetchone()[0], callback_data='fr3'
        )
        keyboard.add(key_fr3)

        bot.send_message(message.from_user.id, text='Узнайте перевод.', reply_markup=keyboard)

    elif message.text == 'Японский':
        keyboard = types.InlineKeyboardMarkup()
        key_ni1 = types.InlineKeyboardButton(
            text=conn.execute("Select NAME from Японский_язык WHERE ID == 1 ").fetchone()[0], callback_data='ni1'
        )
        keyboard.add(key_ni1)
        key_ni2 = types.InlineKeyboardButton(
            text=conn.execute("Select NAME from Японский_язык WHERE ID == 2 ").fetchone()[0], callback_data='ni2'
        )
        keyboard.add(key_ni2)
        key_ni3 = types.InlineKeyboardButton(
            text=conn.execute("Select NAME from Японский_язык WHERE ID == 3 ").fetchone()[0], callback_data='ni3'
        )
        keyboard.add(key_ni3)

        bot.send_message(message.from_user.id, text='Узнайте перевод.', reply_markup=keyboard)

    elif message.text == 'Мотивация':
        keyboard = types.InlineKeyboardMarkup()
        key_motiv1 = types.InlineKeyboardButton(
            text=conn.execute("Select NAME from Мотивационная_цитата WHERE ID == 1 ").fetchone()[0], callback_data='motiv1'
        )
        keyboard.add(key_motiv1)
        key_motiv2 = types.InlineKeyboardButton(
            text=conn.execute("Select NAME from Мотивационная_цитата WHERE ID == 2 ").fetchone()[0], callback_data='motiv2'
        )
        keyboard.add(key_motiv2)
        key_motiv3 = types.InlineKeyboardButton(
            text=conn.execute("Select NAME from Мотивационная_цитата WHERE ID == 3 ").fetchone()[0], callback_data='motiv3'
        )
        keyboard.add(key_motiv3)

        bot.send_message(message.from_user.id, text='Узнайте.', reply_markup=keyboard)




@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global msg
    if call.data == "ang1":
        DESCRIPTION = conn.execute('Select DESCRIPTION from Английский_язык where ID == 1').fetchone()[0]
    elif call.data == "ang2":
        DESCRIPTION = conn.execute('Select DESCRIPTION from Английский_язык where ID == 2').fetchone()[0]
    elif call.data == "ang3":
        DESCRIPTION = conn.execute('Select DESCRIPTION from Английский_язык where ID == 3').fetchone()[0]

    elif call.data == "fr1":
        DESCRIPTION = conn.execute('Select DESCRIPTION from Французский_язык where ID == 1').fetchone()[0]
    elif call.data == "fr2":
        DESCRIPTION = conn.execute('Select DESCRIPTION from Французский_язык where ID == 2').fetchone()[0]
    elif call.data == "fr3":
        DESCRIPTION = conn.execute('Select DESCRIPTION from Французский_язык where ID == 3').fetchone()[0]

    elif call.data == "ni1":
        DESCRIPTION = conn.execute('Select DESCRIPTION from Японский_язык where ID == 1').fetchone()[0]
    elif call.data == "ni2":
        DESCRIPTION = conn.execute('Select DESCRIPTION from Японский_язык where ID == 2').fetchone()[0]
    elif call.data == "ni3":
        DESCRIPTION = conn.execute('Select DESCRIPTION from Японский_язык where ID == 3').fetchone()[0]

    elif call.data == "motiv1":
        DESCRIPTION = conn.execute('Select DESCRIPTION from Мотивационная_цитата where ID == 1').fetchone()[0]
    elif call.data == "motiv2":
        DESCRIPTION = conn.execute('Select DESCRIPTION from Мотивационная_цитата where ID == 2').fetchone()[0]
    elif call.data == "motiv3":
        DESCRIPTION = conn.execute('Select DESCRIPTION from Мотивационная_цитата where ID == 3').fetchone()[0]

    bot.send_message(call.message.chat.id, DESCRIPTION)
bot.polling(none_stop=True, interval=0)

