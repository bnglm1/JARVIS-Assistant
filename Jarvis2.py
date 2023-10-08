from __future__ import with_statement
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import time
import pyttsx3
import datetime
import os
import random
import cv2
import pywhatkit as kit
import sys
import pyautogui
import operator
import requests
from selenium.webdriver import Chrome
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

options= webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speak(query):
    engine.say(query)
    engine.runAndWait()

def recognize_speech():
    with microphone as source:
        audio = recognizer.listen(source, phrase_time_limit=5)
    response = ""
    speak("ses tanımlanıyor..")
    try:
        response = recognizer.recognize_google(audio)
    except:
        response = "Error"
    return response
time.sleep(3)
speak("Patron çevrimiçiyim..")
while True:
    speak("Sana nasıl yardımcı olabilirim")
    voice = recognize_speech().lower()
    print(voice)
    sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"],
             ["google", "https://google.com"]]
    for site in sites:
        if f"open {site[0]}".lower() in voice.lower():
            speak(f"açılıyor {site[0]} patron...")
            driver = webdriver.Chrome(options=options)
            driver.get(site[1])
    if 'google arama' in voice:
        while True:
            speak('dinleniyor..')
            query = recognize_speech()
            if query != 'Error':
                break
        element = driver.find_element_by_name('q')
        element.clear()
        element.send_keys(query)
        element.send_keys(Keys.RETURN)
    elif 'youtube aç' in voice:
        speak('youtube açılıyor..')
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to_window(window_list[-1])
        driver.get('https://youtube.com')
    elif 'youtube arama' in voice:
        while True:
            speak('I am listening..')
            query = recognize_speech()
            if query != 'Error':
                break
        element = driver.find_element_by_name('search_query')
        element.clear()
        element.send_keys(query)
        element.send_keys(Keys.RETURN)
    elif 'switch tab' in voice:
        num_tabs = len(driver.window_handles)
        cur_tab = 0
        for i in range(num_tabs):
            if driver.window_handles[i] == driver.current_window_handle:
                if i != num_tabs - 1:
                    cur_tab = i + 1
                    break
        driver.switch_to_window(driver.window_handles[cur_tab])
    elif 'ekranı kapat' in voice:
        speak('Closing Tab..')
        driver.close()
    elif 'geri git' in voice:
        driver.back()
    elif 'ilerle' in voice:
        driver.forward()
    elif 'çıkış yap' in voice:
        speak('Çıkış yapılıyor...!')
        driver.quit()
        break
    else:
        speak('Komutunuz anlaşılamadı, lütfen tekrarlayın')
    time.sleep(2)
