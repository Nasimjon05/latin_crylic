# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 16:43:17 2025

@author: Nasimjon
"""
from transliterate import to_cyrillic , to_latin
import telebot

TOKEN = "7959590059:AAG6Oplc4jgnfYwStXDxUidtwgdAF7h50vE"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    answer = "What's up bro, write your text in either crylic or latin: "
    bot.reply_to(message, answer)
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    text = message.text
    answer = lambda message: to_cyrillic(text) if text.isascii() else to_latin(text)
    bot.reply_to(message, answer(message))
    
    
bot.infinity_polling()

# text = input("Enter your text: ")
# if text.isascii():
#     print(to_cyrillic(text))
# else:
#     print(to_latin(text))
