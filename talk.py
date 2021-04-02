import os

import pyttsx3
import speech_recognition as sr
# from gtts import gTTS
from pyttsx3.drivers import sapi5
from playsound import playsound

engine = pyttsx3.init('sapi5')

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voice_id)
engine.setProperty('rate', 150)


# def get_audio():
    # recognizer = sr.Recognizer()
    # microphone = sr.Microphone()
    # if not isinstance(recognizer, sr.Recognizer):
    #     raise TypeError("`recognizer` must be `Recognizer` instance")

    # if not isinstance(microphone, sr.Microphone):
    #     raise TypeError("`microphone` must be `Microphone` instance")

    # with microphone as source:
    #     recognizer.adjust_for_ambient_noise(source)
    #     audio = recognizer.listen(source)
    #     response = recognizer.recognize_google(audio)

    # return response.lower()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        # r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.5
        r.energy_threshold = 500
        print('listening...')
        audio = r.listen(source)
        said = ""
        print("Listened")
        try:
            print("Recognizing...")
            said = r.recognize_google(audio, language="en")
            print(f"User said: {said}")
        except Exception as e:
            print("Exception: " + str(e))
            print("Say that again please.....")

    return said.lower()

# def speak(text):
    # text = random.choice(list)
    print(text)
    try:
        tts = gTTS(text=text, lang='en')
        filename = 'voice.mp3'
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except:
        engine.say(text)
        engine.runAndWait()

# def speak(text):
    print(text)
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()