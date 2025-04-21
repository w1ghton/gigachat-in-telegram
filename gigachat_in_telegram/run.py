import telebot
from env import Settings

from gigachat_in_telegram import ai

bot = telebot.TeleBot(Settings().telegram_bot_token)


@bot.message_handler(commands=["help", "start"])
def send_welcome(message: telebot.types.Message):
    bot.send_message(
        message.chat.id,
        """repo: github.com/w1ghton/gigachat-in-telegram""",
    )


@bot.message_handler(func=lambda message: True)
def gigachat_answer(message: telebot.types.Message):
    bot.reply_to(message, ai.generate_text(message.text), parse_mode="Markdown")


bot.infinity_polling()
