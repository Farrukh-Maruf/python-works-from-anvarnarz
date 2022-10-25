# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:58:39 2022

@author: qomon
"""
#from transliterate import to_cyrillic, to_latin
from transliterate import to_cyrillic, to_latin

import telebot

TOKEN= '5380808055:AAGhomUIrJIx663aKivRV09Qb71d_q_728U'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    answer= "Assalomu alaykum \nBu bot uzbek harfdan rus harfga \nrus harfdan ozbek harfga alishtirib beradi \npaste the text"    
    bot.reply_to(message,answer )

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg=message.text
    if msg.isascii():
        answer=to_cyrillic(msg)
    else:
        answer=to_latin(msg)        
    bot.reply_to(message,answer)
    
    
bot.polling()


#text=input("please paste the text: ")
#if text.isascii():
 #   print(to_cyrillic(text))
#else:
 #   print(to_latin(text))