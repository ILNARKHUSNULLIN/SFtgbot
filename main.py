import telebot
import text
import extensions
import config

bot = telebot.TeleBot(config.token)

print('Started')

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.from_user.id, text.start_text)

@bot.message_handler(commands=['values'])
def start(message):
    bot.send_message(message.from_user.id, text.bout_values_text)

@bot.message_handler(content_types=['text'])
def convert(message):
    bot.send_message(message.from_user.id, 'Обработка...')
    if len(message.text.split()) != 3:
        bot.send_message(message.from_user.id, 'Ввод в формате: валюта1 валюта2 количество')
    else:
        quote, base, amount = message.text.split(' ')
        info = extensions.Converter.get_price(quote, base, amount)
        bot.send_message(message.from_user.id, info)

if __name__ == "__main__":
    bot.infinity_polling()