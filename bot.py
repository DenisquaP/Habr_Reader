import telebot
from text_to_audio import audio_habr
import os


with open('token.txt', 'r') as tk:
    TOKEN = tk.readline()
    print(TOKEN)
bot = telebot.TeleBot(TOKEN)


# Menu
bot.set_my_commands([
    telebot.types.BotCommand("/start", "Перезапуск бота"),
    telebot.types.BotCommand("/help", "Помощь"),
    ])


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ \nСкинь мне ссылку на статью")


@bot.message_handler(commands=['help'])
def help_message(message):
    text = "Я бот, который может прочитать тебе статью с Habr. Отправь мне ссылку на статью, а я тебе её прочитаю."
    bot.send_message(message.chat.id, text)


# If message is url
@bot.message_handler(regexp='((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)')
def command_url(message):
    bot.send_message(message.chat.id, 'Озвучиваю...')
    audio_name = audio_habr(message.text)
    with open(audio_name, 'rb') as audio:
        bot.send_audio(message.chat.id, audio)

    bot.send_message(message.chat.id, 'Приятного прослушивания')
    os.remove(audio_name)


bot.infinity_polling()
