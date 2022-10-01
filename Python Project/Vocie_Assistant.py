import pyttsx3 #text to speech
import speech_recognition as sr #speech to tex
import webbrowser
import datetime
import pyjokes
import os
import time


def sptext():
    recog=sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything...")
        recog.adjust_for_ambient_noise(source)
        audio1=recog.listen(source)
        try:
            print("Recognizing...")
            data=recog.recognize_google(audio1)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not understand")

def speech(x):
    while True:
        engine=pyttsx3.init()
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id)
        engine.setProperty('rate',150)
        engine.say(x)
        engine.runAndWait()

if __name__=="__main__":
    while True:
        data=sptext().lower()
        
        if "hello" in data:
            speech("Hello Sir")
        elif "exit" in data:
            speech("Bye Sir")
            break
        elif "how are you" in data:
            speech("I am fine")
        elif "time" in data:
            speech(datetime.datetime.now().strftime("%I:%M:%p"))
        elif "date" in data:
            speech(datetime.datetime.now().strftime("%d/%m/%Y"))
        elif "youtube" in data:
            webbrowser.open("youtube.com")
        elif "sleep" in data:    
            time.sleep(15)
            speech("Good Morning")
        elif "music" or "song" in data:
            os.system("start E:\Music")