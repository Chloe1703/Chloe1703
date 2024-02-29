import telebot
import os
from telebot import types
from telebot.types import Message, CallbackQuery, User

token = "6916711535:AAF4HG-zeuednr7FnXKit5sE8Ae3oLnVfqw"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['id'])
def handle_text(message):
    user_id = message.from_user.id
    bot.send_message(message.chat.id, 'My ID: {}'.format(user_id) )

@bot.message_handler(commands=['cid'])
def handle_text(message):
    chat_id = message.chat.id
    bot.send_message(message.chat.id, 'Chat ID: {}'.format(chat_id) )

@bot.message_handler(commands=['start', 'help', 'what'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

# эхо бот
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)
#
      
@bot.message_handler(content_types=['document', 'photo'])
def handle_docs_photo(message): 
	bot.reply_to(message, "что это?")
	pass

keyboard = types.InlineKeyboardMarkup()
keyboard.add(types.InlineKeyboardButton('Yes', callback_data='yes'),
             types.InlineKeyboardButton('No', callback_data='no'))

@bot.message_handler(commands=['dick'])
def like(message):

  cid = message.chat.id
  bot.send_message(cid, "хуй?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ['yes', 'no'])
def callback_handler(call):
    

    cid = call.message.chat.id
    mid = call.message.message_id
    answer = call.data
    
    # update_lang(cid, answer)
    try:
        bot.edit_message_text("Ты хуй: " + answer, cid, mid, reply_markup=keyboard)
    except:
        pass
bot.infinity_polling()
# bot.polling(none_stop=True)
