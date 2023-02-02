import telebot
from text_to_audio import audio_habr
from parser_habr import verify_url
import os


with open('token.txt', 'r') as tk:
    TOKEN = tk.readline()
bot = telebot.TeleBot(TOKEN)


# Menu
bot.set_my_commands([
    telebot.types.BotCommand("/start", "Перезапуск бота"),
    telebot.types.BotCommand("/help", "Помощь"),
    ])


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️\nСкинь мне ссылку на статью")


@bot.message_handler(commands=['help'])
def help_message(message):
    text = "Я бот, который может прочитать тебе статью с Habr. Отправь мне ссылку на статью, а я тебе её прочитаю."  # noqa E501
    bot.send_message(message.chat.id, text)


# If message is url
@bot.message_handler(regexp='((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)')  # noqa E501
def command_url(message):
    # Checking url for correct
    if verify_url(message.text):
        bot.send_message(message.chat.id, 'Это не хабр или страницы не существует')  # noqa E501
    else:
        bot.send_message(message.chat.id, 'Озвучиваю...')
        audio_name = audio_habr(message.text)
        if audio_name:
            # Sending audio
            with open(f'./app/{audio_name}.mp3', 'rb') as audio:
                bot.send_audio(message.chat.id, audio)
            # Deleting file
            os.remove(f'./app/{audio_name}.mp3')
            bot.send_message(message.chat.id, 'Приятного прослушивания')


bot.infinity_polling()
