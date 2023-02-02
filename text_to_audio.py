from gtts import gTTS
from parser_habr import parser


def audio_habr(url):
    text = parser(url)  # [0] - text, [1] - filename

    speech = gTTS(text=text[0], lang='ru', slow=False)
    speech.save(f'./app/{text[1]}.mp3')
    return text[1]
