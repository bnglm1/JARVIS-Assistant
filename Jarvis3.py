from __future__ import with_statement

import time

import pyttsx3
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.by import By

listener = sr.Recognizer()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

options= webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr .Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvs', '')
                print(command)
    except Exception as e:
        print("Say that again please...")
        talk("Say that again please...")
        return "None"
    return command

def run_Jarvis():
    command = take_command()

    sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"],
             ["google", "https://google.com"]]
    for site in sites:
        if f"open {site[0]}".lower() in command.lower():
            talk(f"opening {site[0]} sir...")
            driver = webdriver.Chrome(options=options)
            driver.get(site[1])
    if "watch" in command:
        talk("opening the website sir...")
        driver = webdriver.Chrome(options=options)
        driver.get(url="https://yabancidizi.pro/")
        driver.maximize_window()
        if "find" in command:
            talk("What do u wanna watch?")
            izle = command.replace(command, "")
            take_command()
            aramaKutusu = driver.find_element(By.NAME, "search")
            aramaKutusu.send_keys(izle)
            time.sleep(5)
            driver.find_element(By.CLASS_NAME, "truncate").click()
    elif "search" in command:
        talk("searching...")
        driver = webdriver.Chrome(options=options)
        aramaKutusu = driver.find_element(By.NAME, "q")
        arama = command.replace("search", "")
        aramaKutusu.send_keys(arama)
    elif "grade" in command:
        talk("grade system is opening sir...")
        driver = webdriver.Chrome(options=options)
        driver.get(url="https://sso.altinbas.edu.tr/?continue=https%3A%2F%2Fewi.altinbas.edu.tr%2F%3F")
        userName = driver.find_element(By.ID, "id_sso_UserName")
        userName.send_keys("200513244")
        password = driver.find_element(By.NAME, "sso[PassWord]")
        password.send_keys("M320325321b.")

    elif "close browser" in command:
        driver = webdriver.Chrome(options=options)
        driver.quit()
    elif 'Stop'.lower() in command:
        talk("Yes sir system is shutting down...")
        exit()

talk("Hello I am Jarvis A.I, How can i help you sir")
while True:
    run_Jarvis()






