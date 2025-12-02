import telebot

TOKEN = "сенің Telegram бот токенің"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Сәлем! Бот жұмыс істеп тұр ✨")

bot.infinity_polling()
pyTelegramBotAPI
requests
