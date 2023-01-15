from gtts import gTTS
from parser_habr import parser
# import os


def audio_habr(url):
    text = parser(url)

    if text[0]:
        speech = gTTS(text=text[0], lang='ru', slow=False)
        speech.save(f'{text[1]}.mp3')
        # os.system(f"start {text[1]}.mp3")
        return f'{text[1]}.mp3'
