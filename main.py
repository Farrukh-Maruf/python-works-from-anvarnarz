import telebot

TOKEN = '5380808055:AAGhomUIrJIx663aKivRV09Qb71d_q_728U'
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    asnwe = "Assalamu alaykum!"
    answe += "\nPaste the text"
    bot.reply_to(message, answe)


bot.polling()