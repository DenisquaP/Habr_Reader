import telebot
from text_to_audio import audio_habr
import os


TOKEN = "5844533796:AAFAFdCyXb7-TWsziEsnMNlKYkxoCn3YX_Y"
bot = telebot.TeleBot(TOKEN)

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


# @bot.message_handler(commands=['audio'])
# def audio_message(message):
#     markup = telebot.types.ForceReply(selective=False)
#     text = 'Ответь на это сообщение ссылкой'
#     bot.send_message(message.chat.id, text, reply_markup=markup)
#     audio_name = audio_habr(message.text)
#     audio = open(audio_name, 'rb')
#     bot.send_message(message.chat.id, message.text)
#     bot.send_audio(message.chat.id, audio)

@bot.message_handler(regexp='((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)')
def command_url(message):
    bot.send_message(message.chat.id, 'Озвучиваю...')
    audio_name = audio_habr(message.text)
    with open(audio_name, 'rb') as audio:
        bot.send_audio(message.chat.id, audio)

    bot.send_message(message.chat.id, 'Приятного прослушивания')
    os.remove(audio_name)


bot.infinity_polling()
