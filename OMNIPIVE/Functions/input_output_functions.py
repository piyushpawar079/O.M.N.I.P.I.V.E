import datetime as dt
import time
from iso639 import to_iso639_1, NonExistentLanguageError
from googletrans import Translator
import pyttsx3
import speech_recognition as sr


language_code = 'en'
language = 'English'


def ask_language():
    global language
    say('In which language your are going to give commands?')
    prev_lang = language
    language = take_command()
    get_language_code(language)
    if prev_lang != language:
        say(f'Language has been changed from {prev_lang} to {language} ')
    else:
        say(f'The language is {language} now')


def say(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    # voice = engine.getProperty('voices')
    # engine.setProperty('voice', voice[1].id)
    # print(voice[1].id)
    engine.setProperty('volume', 3.0)
    # translator = Translator()
    # translation = translator.translate(text, src='en', dest='hi')
    # translated_text = translation.text
    # print(translated_text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def wishme():
    hour = int(dt.datetime.now().hour)
    tt = time.strftime('%I:%M %p')

    if 0 < hour < 12:
        say(f'Good Morning Sir. Its {tt}')
    elif 12 <= hour < 18:
        say(f"Good Afternoon Sir. Its {tt}")
    else:
        say(f"Good Evening Sir, Its {tt}")
    # say("Hello Sir, I am OMNIPIVE (a virtual assistant). How may I help you sir?")


def get_language_code(language_name):
    global language_code
    language_name = language_name.lower()

    try:
        language_code = to_iso639_1(language_name)
    except NonExistentLanguageError:
        print("Error")


def take_command():
    global language_code
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio_data = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio_data, language=language_code)
        print(f"User Said (original): {text}")

        if language_code != 'en':
            translator = Translator()

            translation = translator.translate(text, src=language, dest='en')
            translated_text = translation.text

            print(f"Translated to English: {translated_text}")
            return translated_text
        return text

    except sr.UnknownValueError:
        return ''

    except sr.RequestError as e:
        return ''
