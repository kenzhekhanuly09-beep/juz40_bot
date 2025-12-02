import telebot

# ========== Telegram бот токеніңді осында қой ==========
TOKEN = "8349319526:AAGLSCvuZIn0sXFDL4zhM5smI_UJyEiXcmw"  # сенің бот токенің

bot = telebot.TeleBot(TOKEN)

# /start командасы
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Сәлем! Бот жұмыс істеп тұр ✨")

# Ботты қосу
bot.infinity_polling()
pyTelegramBotAPI
requests
