from __future__ import print_function

import datetime
import os
import os.path
import random
import webbrowser

import wikipedia
from playsound import playsound

# import google_calendar, google_mail
from talk import *
from youtube import *

# VARIABLES
chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"

MONTHS = ["january", "february", "march", "april", "may", "june",
          "july", "august", "september", "october", "november", "december"]
DAYS = ["monday", "tuesday", "wednesday",
        "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]


# FUNCTIONS


def get_date(text):
    text = text.lower()
    today = datetime.time.today()

    if today.count("today") > 0:
        return today

    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(month) + 1
        elif word in DAYS:
            days_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found = word.fins(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass

        if month < today.month and month != -1:
            year = year + 1

        # if date < today.date and month == -1 and day != -1:
        #     month = month + 1

        if month == -1 and day == -1 and day_of_week != -1:
            current_day_of_week = today.weekday()
            dif = day_of_week - current_day_of_week


def subject_chooser():
    choice = input('Which subject: ')
    if 'science' in choice:
        URL = 'https://www.freeconferencecall.com/wall/vijayatiwari19/viewer'
    elif 'english' in choice:
        URL = 'https://www.freeconferencecall.com/wall/smriti12samriya/viewer'
    elif 'maths' in choice:
        URL = 'https://www.freeconferencecall.com/wall/ritumoondra9/viewer'
    elif 'hindi' in choice:
        URL = 'https://www.freeconferencecall.com/wall/archisharma018as6/viewer'
    elif 'computer' in choice:
        URL = 'https://www.freeconferencecall.com/wall/yogeshbhl12/viewer'
    elif 'sst' in choice:
        URL = 'https://www.freeconferencecall.com/wall/jjjajpura5/viewer'
    elif 'sans' or 'sanskrit':
        URL = 'https://www.freeconferencecall.com/wall/priyankapandiya26/viewer'
    else:
        URL = 'HTTPS://youtube.com'

    return URL


def wishMe():
    hour = int(datetime.datetime.now().hour)
    # print(hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! I am alexa! Please tell me how can i help you?")
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon! I am alexa! Please tell me how can i help you?')
    else:
        speak('Good Evening! I am alexa! Please tell me how can i help you?')


def main():
    # wishMe()
    while True:
        # text = get_audio()
        text = input(":").lower()
        if "who is alexa" in text or "who are you" in text:
            playsound(random.choice(["audio/rakh.mp3", "audio/khopdi_tod.mp3"]))
        else:
            pass
        text = text.replace("alexa", "")
        # LOGICS ONLY FOR SCBS

        if "how are you" in text:
            speak(random.choice(["I'm Fine!", "I'm Fine! How about you?"]))

        elif "hi" in text or "hello" in text or "hai" in text:
            speak(random.choice(["Hello, How are you?", "Hi!"]))

        elif "i am fine" in text:
            speak("Nice!")

        elif "what are you doing" in text:
            speak("Nothing, Just Chilling! on your stupid machine!")

        elif "where were you born" in text:
            speak("I was born in India")

        elif "how old are you" in text or "your age" in text:
            alexaAge = datetime.date.today() - datetime.date(2021, 2, 1)
            speak(f"I am {alexaAge} year old")

        elif 'wikipedia' in text:
            text = text.replace("wikipedia", "")
            speak("Searching on WikiPedia...")
            results = wikipedia.summary(text, sentences=2)
            speak(f"According to WikiPedia, {results}")

        elif "who is" in text:
            person = text.replace("who is", "")
            speak(f"Searching {person} on WikiPedia...")        
            results = wikipedia.summary(text, sentences=2)
            speak(f"According to WikiPedia, {results}")

        elif 'open youtube' in text:
            webbrowser.open("https://youtube.com")
        elif 'open google' in text:
            webbrowser.open("https://google.com")
        elif 'open stackoverflow' in text:
            webbrowser.open("https://stackoverflow.com")
        elif 'open brave' in text:
            bravePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(bravePath)
        elif 'play music on youtube' in text:
            webbrowser.open('youtube.com/results?search_query=music')
        elif "play" in text and "youtube" in text:
            for i in ["play", "youtube", "on"]:
                text = text.replace(i, "")
            webbrowser.open(youtubeVideo(text))
        elif 'search' and 'youtube' in text:
            text = text.split()
            for i in range(len(["search", "youtube", "on"])):
                if ["search", "youtube", "on"][i] in text:
                    print(i)
                    text.pop(i)
            print(text)
        elif 'play music' in text:
            speak('From where i should play music?')
            text = get_audio()
            if "spotify" in text:
                try:
                    spotifyPath = "C:\\Users\\Tanmay Gautam\\AppData\\Roaming\\Spotify\\Spotify.exe"
                    os.startfile(spotifyPath)
                except:
                    webbrowser.open('spotify.com')
            elif "gaana" in text:
                webbrowser.open('gaana.com')
            elif "youtube" in text:
                webbrowser.open(
                    'www.youtube.com/results?search_query=songs')
        elif "the time" in text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
        elif "today" and "date" in text:
            speak(random.choice(
                ["Hey! what's wrong with you bro? YOU DON'T KNOW TODAY'S DATE!", f"Today's date is {datetime.date.today()}"]))
        elif 'open code' in text:
            codePath = "C:\\Users\\Tanmay Gautam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif "open sublime" in text:
            sublimePath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(sublimePath)

        elif "send email to" in text:
            text = text.split()
            sendEmail()
        else:
            playsound("audio/supari_nikal.mp3")

if __name__ == "__main__":
    try:
        main()
    except:
        speak("Make sure you are connected to Internet.")
# service = authenticate_google()
# get_events(3, service)
