import telebot
from dotenv import load_dotenv
import os
from gigachat_in_telegram import ai

load_dotenv()

bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))


@bot.message_handler(commands=["help", "start"])
def send_welcome(message: telebot.types.Message):
    bot.send_message(
        message.chat.id,
        """я гигачат\nРепозиторий: github.com/w1ghton/gigachat-in-telegram""",
    )


@bot.message_handler(func=lambda message: True)
def gigachat_answer(message: telebot.types.Message):
    bot.reply_to(message, ai.generate_text(message.text))


bot.infinity_polling()
