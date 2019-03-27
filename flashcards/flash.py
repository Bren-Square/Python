import os
import random
from io import BytesIO
from google.cloud import translate
from gtts import gTTS
from pygame import mixer

client = translate.Client()
vocabulary = []
target = "de"
running = True

filepath = 'vocab.txt'
with open(filepath) as fp:
    line = fp.readline()
    while line:
        vocabulary.append("{}".format(line.strip()))
        line = fp.readline()


def print_words(word_one, word_two, lang):
    print(word_one)
    tts = gTTS(word_one, lang=lang)
    tts.save("word.mp3")
    mixer.init()
    mixer.music.load("word.mp3")
    mixer.music.play()
    input("press any key to see the answer")
    print(word_two)
    print("")
    if input("continue? y/n: ") == "n":
        return False
    else:
        return True


def quiz(en_word, de_word, language_boolean):
    if language_boolean:
        return print_words(en_word, de_word, "en")
    else:
        return print_words(de_word, en_word, "de")


while running:
    eng_or_deu = bool(random.getrandbits(1))
    eng = random.choice(vocabulary)
    deu = client.translate(eng, target_language=target)['translatedText']
    running = quiz(eng, deu, eng_or_deu)
