import telebot
from dotenv import load_dotenv
import os
from gigachat_in_telegram import ai

load_dotenv()


bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))


@bot.message_handler(commands=["help", "start"])
def send_welcome(message):
    bot.send_message(message.chat.id, "я гигачат")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, ai.generate_text(message.text))


bot.infinity_polling()
