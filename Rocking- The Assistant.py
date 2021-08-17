# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 09:22:12 2021

@author: Ayush Padhy
"""

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from wiki_search import *
import sys
from datetime import date 
import webbrowser
import os
import wolframalpha
import re

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say("Hello, I am ROCKING the personal assistant !")
print("Hello, I am ROCKING the personal assistant !")
engine.say("I am right now capable of playing songs, videos , Searching information, telling the time and many more....")
engine.runAndWait()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk("i am Listening...say your command")
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'rocking' in command:
                command = command.replace('rocking', '')
                print(command)
    except:
        sys.exit()
        pass
    return command



def run_rocking():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '') 
        rocking = info()
        rocking.get_info(person)
        # info = wikipedia.summary(person, 1)
        # print(info)
        # talk(info)
    elif 'date' in command:
        today = str(date.today())
        print(date)
        talk('todays date is' + today)
    elif 'search' in command:
        search=command.replace('search','')
        talk('searching' + search)
        pywhatkit.search(search)
    elif "good" in command:
        talk("Thank you for your wishes... I am always trying to improve myself")
    elif "stop" in command:
        sys.exit()
    elif "live news" in command:
        webbrowser.open('https://www.republicworld.com/livetv.html')   
    elif "read news" in command:
        webbrowser.open("https://www.wionews.com/")
    elif 'ask' in command:
            talk('I can answer to computational and geographical questions  and what question do you want to ask now')
            command1 = take_command()
            print(command1)
            app_id="VWARHP-74AULHEGVG"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(command1)
            answer = next(res.results).text
            talk(answer)
            print(answer)
    elif "open minecraft" in command: 
       talk("minecraft") 
       os.startfile("C:\Program Files\Minecraft\TLauncher.exe") 
       
    elif "open brave" in command:
       talk("brave")
       os.startfile("C:\Program Files\BraveSoftware\Brave-Browser\Application\Brave.exe")
       return
    else:
        talk('Please say the command again.')
        

run_rocking()

    

# def open_application(): 
#     command = take_command()
#     if "minecraft" in command: 
#         talk("minecraft") 
#         os.startfile("C:\Program Files\Minecraft\TLauncher.exe") 
#         return
#     if "brave" in command:
#         talk("brave")
#         os.startfile("C:\Program Files\BraveSoftware\Brave-Browser\Application\Brave.exe")
#         return

# while True:
#     open_application()