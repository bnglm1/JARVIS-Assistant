from __future__ import with_statement
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import pyautogui
import time

listener = sr.Recognizer()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr .Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="TR-tr")
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvs', '')
                print(command)
    except Exception as e:
        print("Say that again please...")
        talk("Say that again please...")
        return "None"
    return command


def run_jarvis():
    command = take_command()
    sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"], ["google", "https://google.com"], ["A-I", "https://bard.google.com/"]]
    for site in sites:
        if f"open {site[0]}".lower() in command.lower():
            talk(f"opening {site[0]} sir...")
            webbrowser.open(site[1])
        elif f"close {site[0]}".lower() in command.lower():
            talk(f"closing {site[0]} sir...")
            os.system("taskkill /f /im msedge.exe")

    if 'current time' in command:
            Thetime = datetime.datetime.now().strftime('%H:%M')
            print(time)
            talk('current time is ' + Thetime)
    elif 'who' in command:
            person = command.replace('who', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
    elif 'search on youtube' in command:
        talk("Searching on Youtube")
        command = command.replace("search on youtube", "")
        webbrowser.open(f"www.youtube.com/results?search_query={command}")
    elif 'play movie' in command:
        video_dir = 'D:\Movies'
        movie = os.listdir(video_dir)
        os.startfile(os.path.join(video_dir, random.choice(movie)))
    elif 'watch series' in command:
        talk("Opening series website...")
        webbrowser.open(f"https://yabancidizi.pro/")
    elif 'name of series' in command:
        talk("Searching a series name...")

    elif "take screenshot" in command:
        talk('tell me a name for the file')
        name = take_command().lower()
        time.sleep(3)
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        talk("screenshot saved")
    elif 'close movie' in command:
        os.system("taskkill /f /im medya oynatıcı.exe")
    elif 'open new window' in command:
        pyautogui.hotkey('ctrl', 'n')
    elif 'maximize this window' in command:
        pyautogui.hotkey('alt', 'space')
        time.sleep(1)
        pyautogui.press('x')
    elif 'google search' in command:
        query = command.replace("google search", "")
        pyautogui.hotkey('alt', 'd')
        pyautogui.write(f"{query}", 0.1)
        pyautogui.press('enter')
    elif 'Stop' .lower() in command:
        talk("Yes sir system is shutting down...")
        exit()
talk("Hello I am Jarvis A.I, How can i help you sir")
while True:
    run_jarvis()