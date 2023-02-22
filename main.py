from __future__ import print_function

import datetime
import json
import os
import os.path
# import ctypes_callable
import random
import smtplib
import time
import webbrowser
from urllib.request import urlopen

import pdfreader
import pyautogui as pg
# from google_auth_oauthlib.flow import InstalledAppFlow
import pyperclip
import pyttsx3
import pywhatkit
import pywhatkit as w
import requests
import sounddevice as sd
import speech_recognition as sr
import wikipedia
import wolframalpha
from bs4 import BeautifulSoup
from googletrans import Translator
from playsound import playsound
from twilio.rest import Client

import kivy
from kivy.app import App
from kivy.uix.label import Label
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import pyaudio
import os
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
from translate import Translator
import pyjokes
import pyautogui


calendarscope = ['https://www.googleapis.com/auth/calendar']
gmailscope = ['https://www.googleapis.com/auth/gmail.readonly']
MONTHS = ["january", "february", "march", "april", "may", "june",
          "july", "august", "september", "october", "november", "december"]
DAYS = ["sunday", "monday", "tuesday",
        "wednesday", "thursday", "friday", "saturday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("Chat: " + audio)


speak("Starting Engine")
speak("Collecting required resources")
speak("initializing......")
speak("Getting information from the CPU")
speak("contacting with mail services")

# os.startfile("Your_rainmeter_url")


name = "Sahil Kamble"
age = "23"
email_id = "kambles823@gmail.com"
email_id_password = "sahilideal"
gender = "Sir"
city = "kalyan"
dad = "your-contacts-gmail"
mom = "your-contacts-gmail"
sis = "your-contacts-gmail"

startmin = int(datetime.datetime.now().hour)


def get_date(text):
    text = text.lower()
    today = datetime.date.today()

    if text.count("today") > 0:
        return today

    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass

    if month < today.month and month != -1:
        year = year + 1

    if month == -1 and day != -1:
        if day < today.day:
            month = today.month + 1
        else:
            month = today.month

    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()
        dif = day_of_week - current_day_of_week

        if dif < 0:
            dif += 7
            if text.count("next") >= 1:
                dif += 7

        return today + datetime.timedelta(dif)

    if day != -1:
        return datetime.date(month=month, day=day, year=year)


contacts = ["dad", "borther"]
number = ['+918454978305', '9082289864']
mails = ["put-your-contacts "]


def twilio_send_msg():
    account_sid = 'ACf58a5aa9a9ed320ba869a88baf72bd8f'
    auth_token = 'fce15d881164f14cffd1dc6e548d8322'

    client = Client(account_sid, auth_token)

    contact_name = query.split("message")
    contact = contact_name[1]
    try:
        if "dad" in contact:
            to = "+918454978305"

        if "sister" in contact:
            to = "+919082289864"

        # if "sister" in contact:
        #     to = "phone_number"

    except:
        speak(f"No contact named {contact} in my database")

    try:
        speak("okay sahil plz say me the content")
        body = get_audio()

        client.messages.create(body=body,
                               from_='+12569527617',
                               to='+918454978305'
                               )
        speak("Message sent")

    except:
        speak("Failure in sending message")


def twilio_call():
    global contacts

    account_sid = 'AC4dd4c26fd55aa1cdf682fbae4665acc6'
    auth_token = 'f0e23b8379e87351127d055108bcd55c'

    client = Client(account_sid, auth_token)

    contact_name = query.split("call")
    contact = contact_name[1]
    if "dad" in contact or "Dad" in contact:
        to = "+918454978305"

    if "brother" in contact or "brother" in contact in contact:
        to = "+919082289864"



    else:
        speak(
            f"Hmmm seems like you have not registered the contact in my data base Sahil so, I cant call {contact}")

    try:
        speak(f"Trying to call {contact} on {to}")
        call = client.calls.create(url='http://demo.twilio.com/docs/voice.xml',
                                   to='+918454978305',
                                   from_='+12569527617'
                                   )
    except:
        print("Error")


def langtranslator():
    try:
        trans = Translator()

        speak("Say the language to translate in")
        language = get_audio().replace(" ", "")

        speak("what to translate")
        content = get_audio()

        t = trans.translate(text=content, dest=language)
        speak(f"{t.origin} in {t.dest} is{t.text}")

    except:
        speak("error")


def convert():
    trans = Translator()

    speak("Say the language to translate in")
    language = get_audio().replace(" ", "")
    pg.hotkey("ctrl", 'c')
    tobespoken = pyperclip.paste()
    content = tobespoken

    t = trans.translate(text=content, dest=language)
    speak(f"{t.origin} in {t.dest} is{t.text}")


def database():
    Exception
    if "what do I have" in query:
        get_audio()
    client = wolframalpha.Client('your_client')
    speak(f"Searching for {query} in my database")
    try:
        res = client.query(query)
        results = next(res.results).text
        speak(results)
    except:
        speak(
            f"Sir, your query {query} does not match any of the data in my data base.")
        speak("Try asking other things..")
        speak("sorry for in convinience sir")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kambles823@gmail.com', 'sahilideal')
    server.sendmail('kambles823@gmail.com',
                    'nalawadevarsha605@gmail.com', content)
    server.close()


def langtranslatorfromselectedin():
    trans = Translator()

    content = query[0]
    language = query[1]

    t = trans.translate(text=content, dest=language)
    speak(f"{t.origin} in {t.dest} is{t.text}")


def locate():
    place = query[1]
    speak(f"according to my data base {place} lies here")
    webbrowser.open_new_tab("https://www.google.com/maps/place/" + place)


def weather_info():
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + \
          (f'{city}') + "&appid=06c921750b9a82d8f5d1294e1586276f"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Minimum Tempreture is: " + str(min_temp) + "°C" + "\n" + "Maximum Tempreture is: " + str(
        max_temp) + "°C" + "\n" + "Pressure: " + str(
        pressure) + "\n" + "Humidity: " + str(
        humidity)  # + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    speak(final_info)
    speak(final_data)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    strTime = datetime.datetime.now().strftime(
        "%I:%M:%p").replace(":", "").replace("None", "")

    speak(
        f"I am  Chat, {gender} Now it is {strTime} {weather_info()} ")

    query = "what do i have on " + datetime.datetime.now().strftime("%A")
    speak("Now, I am ready for your commands Please tell me how may I help you ")


def get_audio():
    # It tane input from the user and returns string outputkes micropho

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" I am Listening...")
        r.phrase_time_limit = 10
        audio = r.listen(source)

    try:
        said = r.recognize_google(audio, language='en-in')
        print(f"{name} {gender} said: {said}\n")
    except:
        return "None"
    return said


def wake_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting to help you")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        said = r.recognize_google(audio, language='en-in')
        print(f"{name} {gender} said: {said}\n")

    except:
        return "None"
    return said


def calendar_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting to help you")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        said = r.recognize_google(audio, language='en-in')
        print(f"{name} {gender} said: {said}\n")

    except:
        return "None"
    return said


def read():
    pg.hotkey("ctrl", 'c')
    tobespoken = pyperclip.paste()
    speak(tobespoken)


def repeatmyspeech():
    speak("Okay starting to listen")
    speak(f"{name} {gender} start speaking")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" I am Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        said = r.recognize_google(audio, language='en-in')
        speak(f"{name} {gender} said: {said}\n")
        print(f"{name} {gender} hre is ur repetition by me {said}\n")
        try:
            speak("should i save the file?")
            ans = get_audio()
            if "yes" in ans:
                try:
                    speak("What should i keep the file name")
                    filename = get_audio().lower
                    said.save(filename + ".mp3")
                    speak("File saved sucessfully")
                    try:
                        speak("Do you want me to show it?")
                        reply = get_audio()
                        if "yes" in reply:
                            os.startfile(filename + ".mp3")
                            speak("here it is")

                    except:
                        if "no" in reply:
                            speak("Never mind")

                except:
                    speak("Error in keeping filename")

        except:
            speak("Okay")

    except:
        return "None"
    return said


def recsound(write=None):
    fs = 44100
    speak("what should be the length of your sound wave Plz answer in seconds")
    ans = int(get_audio())
    seconds = ans

    recorded = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    speak("sucessfully recoreded")
    speak("what should i keep the file name")
    filename = get_audio()
    write(filename + '.mp3', fs, recorded)
    speak("sucessfuly saved")
    try:
        speak("should i show you")
        reply = get_audio()
        if "yes" in reply:
            os.startfile(filename + ".mp3")

    except:
        if "no" in reply:
            speak("okay next command sir")


def Screenshot():
    image = pg.screenshot()
    speak("screen shot taken")
    speak("what do you want to save it as?")
    filename = get_audio()
    image.save(filename + ".png")
    speak("do you want me to show it")
    ans = get_audio()
    if "yes" in ans:
        os.startfile(filename + ".png")
    else:
        speak("never mind")


def pdf_reader():
    book = open('ath.pdf', 'rb')
    pdfReader = pdfreader.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book {pages}")
    speak("sir please enter the page number i have to read")
    pg = int(input("Please enter the page number:"))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()


app = wolframalpha.Client("YYLUTW-TRR4983VG7")


def talk(text):
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    wishMe()
    while True:
        query = get_audio().lower()

        if "search for " in query:
            query = query.replace("search for", "")
            database()

        elif "wikipedia" in query or "Wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "who" in query or "Who" in query:
            database()

        elif "why" in query or "Why" in query:
            database()

        elif "open terminal" in query:
            os.startfile("cmd")

        elif "open calculator" in query:
            os.startfile("calc")

        elif "open taskmanager" in query:
            os.startfile("Taskmgr")

        elif 'play' in query:
            song = query.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)

        elif "what is the time" in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%p")
            speak(f"the time is {strTime}")

        elif "what is today's date" in query:
            date = datetime.datetime.now().strftime("%A:%d:%B:%Y")
            speak(f"Today is {date} ")

        elif "Chat" in query or "hey" in query or "hello Chat" in query:
            stMsgs = ['on your command sir',
                      f'yes {name}', f'hello {name}', 'Waiting for your command sir']
            speak(random.choice(stMsgs))

        elif "Thank You" in query or "Thank you" in query or "thank you" in query or "thanks" in query:
            rep = ['Welcome', 'Well you know i am cool', 'Dont mention',
                   'By the way I should thank you for creating me']
            speak(random.choice(rep))

        elif "say something" in query:
            speak("what's your name?")

        elif "good morning" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(
                f"Good morning {name} {gender} it is {strTime} now,Hope you had a good sleep.")

        elif "good night" in query:
            strTime = datetime.datetime.now().strftime("%X").replace(":", " ")
            gtime = strTime.replace(":", " ")
            speak(f"Good night {name} {gender} it is {gtime} sleep tight..")

        elif "open my inbox" in query:
            webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")

        elif "open my sent mail" in query:
            webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#sent")

        elif "open YouTube " in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('launching  google')
            speak('sir,what should i search on google')
            cm = get_audio().lower()
            webbrowser.open(f"{cm}")

        elif "repeat my speech" in query:
            repeatmyspeech()

        elif "close chrome" in query:
            os.system('TASKKILL /F /IM Google Chrome.exe')

        elif "close task manager" in query:
            os.system('TASKKILL /F /IM Taskmgr.exe')

        elif "delete" in query:
            final = query.split("delete")
            os.system("del " + final[el])

        elif "shutdown" in query:
            speak("okay,shutting down your pc")
            os.system('shutdown/s')

        elif "restart my pc" in query:
            speak("okay, restarting your pc")
            os.system('shutdown/r')

        elif "record my voice" in query:
            recsound()

        elif "take a screenshot" in query:
            Screenshot()

        elif "ok byeeveryone over here he just sneaker and lot of things are going in my Android now what should I do" in query:
            speak(
                f"Thank you {name} for giving your time i had fun serving you,have a good time")
            speak("closing engine")
            speak("closing required applications")
            endTime = int(datetime.datetime.now().hour)
            f = open("goodnight.txt", "w+")
            end = int(datetime.datetime.now().hour)
            f.write(str(end))
            f.close()
            playsound.playsound('shut_down.wav')

            break

        elif "type" in query:
            speak(f"okay i am listening speak{name} {gender}")
            pg.typewrite(get_audio())

        elif "select all" in query:
            pg.hotkey('ctrl', 'a')

        elif "close this window" in query:
            pg.hotkey('alt', 'f4')

        elif "open a new tab" in query:
            pg.hotkey('ctrl', 'n')

        elif "open a new incognito window" in query:
            pg.hotkey('ctrl', 'shift', 'n')

        elif "copy" in query:
            pg.hotkey('ctrl', 'c')
            speak('text copied to clipboard')

        elif "paste" in query:
            pg.hotkey('ctrl', 'v')

        elif "undo" in query:
            pg.hotkey('ctrl', 'z')

        elif "redo" in query:
            pg.hotkey('ctrl', )

        elif "save" in query:
            pg.hotkey('ctrl', 's')

        elif "back" in query:
            pg.hotkey('browserback')

        elif "go up" in query:
            pg.hotkey('pageup')

        elif "go to top" in query:
            pg.hotkey('home')

        elif "read" in query:
            try:
                read()
            except:
                speak("no text selected plz select a text")

        elif "introduce yourself" in query:
            speak("I was a dream of a boy dreaming to make a perfect virtual assistant")
            speak("He soon established the company named Sars technology")
            speak("Okay,Let me start by The time I was born,,")
            speak("Slowly,I came to life")
            speak(
                "I started learning various things like calculations,General knowldge etc etc")
            speak(
                "Now I am capable of doing various things like Beatboxing,opening applications,Cracking jokes,Playing music etc.")
            speak("Okay,thats a wrap I wont say more ")

        elif "translate" in query:
            langtranslator()

        elif "in" in query:
            query = query.split("in")
            query = query[0]
            dest = [1]

        elif "convert selected " in query:
            convert()

        elif "translate to" in query:
            query = query.split("translate to")
            dest = query[1]
            langtranslator()

        elif "remind me" in query:
            os.system("python pyautogui1.py")

        elif 'play music' in query:
            speak('playing music')
            music_dir = "D:\\english song"
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif "locate" in query:
            query = query.split("locate")
            locate()

        elif "where is" in query:
            query = query.split("where is")
            locate()

        elif "I know that" in query:
            speak("Ya, ure right")

        elif "write a note" in query:
            speak("What should i write, sir")
            note = get_audio()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = get_audio()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif " weather " in query:
            city = (f"{city}")
            weather_info()

        elif "what is the weather in" in query:
            query = query.split("what is the weather in")
            city = query[1]
            weather_info()

        elif 'temperature' in query:
            res = app.query(query)
            speak(next(res.results).text)
            print(next(res.results).text)

        elif "open discord" in query:
            speak("Opening Discord")
            webbrowser.open_new_tab("discord.com")

        elif "open discord app" in query:
            discord = input("Enter the path of discord: ")
            os.startfile("explorer.exe")
            os.startfile(discord)

        elif "who created you" in query:
            speak(
                "Sahil Kaamble and Varsha Nalawade is my developer my teacher the one who taught me how be a good wise smart and a intelligent person Mangesh was previously his name And since he left the hacking world he gave this name to me and started programming with python then created me  Now i Am proud to be A I assistant at last  ")

        elif "take a screenshot" in query:
            Screenshot()

        elif "tell me a joke" in query or "Crack a joke" in query or "crack a joke" in query:
            jokes = [
                "A Doctor said to a patient , I'm sorry but you suffer from a terminal illness and have only 10 to live , then the Patient said What do you mean, 10, 10 what, Months, Weeks, and the Doctor said Nine.",
                "Once my Brother who never used to drink was arrested for over drinking,When I lates had gone and asked him why were you arressted, He replied he had not brushed since a week",
                "A Teacher said Kids, what does the chicken give you? The Student replied Meat Teacher said  Very good Now what does the pig give you? Student said BaconTeacher said  Great  And what does the fat cow give you? Student said Homework!",
                "A child asked his father, How were people born? So his father said, Adam and Eve made babies, then their babies became adults and made babies, and so on  The child then went to his mother, asked her the same question and she told him, We were monkeys then we evolved to become like we are now  The child ran back to his father and said, You lied to me  His father replied, No, your mom was talking about her side of the family.Yesterday I learnt that 20 piranhas can strip all flesh off a man within 15 minutes. - Unfortunately, I also lost my job at the local swimming pool"]
            speak(random.choice(jokes))
            speak("Do you want more?")
            ans = get_audio()
            if "yes" in ans:
                speak(random.choice(jokes))
            if "no" in ans:
                speak(random.choice(jokes))

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(input())
            time.sleep(a)
            print(a)

        elif "weather" in query:
            search = "tempreture in kasare"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif 'send message to me' in query:
            speak('what shoud i say to self ?')
            say = get_audio()
            speak('set the time to deliever the message!')
            w.sendwhatmsg('+918454978305',
                          f"{say}", int(input()), int(input()))
            speak("message sent!")

        elif 'news' in query:

            try:
                jsonObj = urlopen(
                    '''http://newsapi.org/v2/top-headlines?country=in&apiKey=8d1e22f4c8ff458f881046c8c932b438''')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))
        elif 'temperature' in query:
            res = app.query(query)
            speak(next(res.results).text)
            print(next(res.results).text)

        elif 'calculate' in query:
            speak("what should i calculate?")
            gh = get_audio().lower()
            res = app.query(gh)
            speak(next(res.results).text)

        elif 'send email to sahil' in query:
            try:
                speak("What should I say?")
                content = get_audio()
                to = "kambles823@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Sahil . I am not able to send this email")

        elif 'open Times of India' in query:
            speak("let me search you")
            news = webbrowser.open_new_tab(
                "https://timesofindia.indiatimes.com/india")
            speak('Here are some headlines from the Times of India,Happy reading')

        elif "sunny temp" in query:
            speak(" City name ")
            print("City name : ")

            city = get_audio()

            api = "https://api.openweathermap.org/data/2.5/weather?q=" + \
                  city + "&appid=06c921750b9a82d8f5d1294e1586276f"

            json_data = requests.get(api).json()
            condition = json_data['weather'][0]['main']
            temp = int(json_data['main']['temp'] - 273.15)
            min_temp = int(json_data['main']['temp_min'] - 273.15)
            max_temp = int(json_data['main']['temp_max'] - 273.15)
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']
            sunrise = time.strftime('%I:%M:%S', time.gmtime(
                json_data['sys']['sunrise'] - 21600))
            sunset = time.strftime('%I:%M:%S', time.gmtime(
                json_data['sys']['sunset'] - 21600))

            final_info = condition + "\n" + str(temp) + "°C"
            final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(
                max_temp) + "°C" + "\n" + "Pressure: " + str(
                pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(
                wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset

            print(final_info)
            speak(final_info)
            print(final_data)
            speak(final_data)

        elif "message" in query:
            twilio_send_msg()

        elif "call" in query:
            twilio_call()


        elif "beatbox" in query or "Beatbox" in query:
            beatboxes = ['1.wav', '2.wav', '3.wav', '4.wav']
            playsound.playsound(random.choice(beatboxes))

        elif "open WhatsApp" in query:
            webbrowser.open_new_tab("https://web.whatsapp.com/")

        elif "open pdf" in query:
            pdf_reader()

        elif 'open college website' in query:
            webbrowser.open("https://dypimed.edu.in/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.co.in/")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open Linkedin' in query:
            webbrowser.open("https://www.linkedin.com/")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")

        elif 'open dashboard' in query:
            webbrowser.open("http://mydy.dypatil.edu/rait/my/")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open yahoo' in query:
            webbrowser.open("https://in.search.yahoo.com/")

        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com/")

        elif 'open amazon' in query:
            webbrowser.open("http://www.amazon.com/")

        elif 'open dominos' in query:
            webbrowser.open("https://www.dominos.co.in")

        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "i love you" in query:
            speak("It's hard to understand")

        elif 'open pycharm' in query:
            os.startfile("C:\Program Files\JetBrains\PyCharm Community Edition 2022.2.3")

        elif 'stop' in query:
            print("shutting down...")
            speak("shutting down")
            quit()

MyApp().run()
root_1 = tk.ThemedTk()
root_1.set_theme('radiance')
root_1.title("Voice assistant")
root_1.geometry("400x350")
lbl1=ttk.Label(master=root_1, text="Welcome to voice assistant app\n\n", wraplength=600)
lbl1.pack()
but1 = ttk.Button(root_1, text="Run the assistant🤖🔊", command=main)
but1.config(width=22)
but1.pack(padx=10, pady=10)
quit4 = ttk.Button(root_1, text="EXIT", command=root_1.destroy)
quit4.config(width=22)
quit4.pack(padx=10, pady=20)
root_1.mainloop()