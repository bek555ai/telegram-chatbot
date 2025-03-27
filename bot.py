import telebot
import os

TOKEN = os.getenv("8103896651:AAHr_3r73yQfVOLcOCMFFmTeuNQtvMhcKuk")  # Telegram bot tokeni
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Salom! Men sizning shaxsiy chatbotingizman.")

print("Bot ishladi!")
bot.polling()
