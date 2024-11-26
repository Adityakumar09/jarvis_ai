import pyttsx3
from decouple import config
from datetime import datetime

engine = pyttsx3.init('sapi5') # microsoft speech api for speech recognition 

engine.setProperty('volume',1.5)
engine.setProperty('rate',225)

voices=engine.getProperty('voices') # import voices module of python library
engine.setProperty('voice',voices[1].id)
# 1-female 2-male

USER=config('USER')
HOSTNAME=config('BOT')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_me():
    hour = datetime.now().hour
    if (hour>=6) and (hour<12):
        speak(f"Good Morning {USER}")
    elif (hour>=12) and (hour<16):
        speak(f"Good Afternoon {USER}")
    elif (hour>=16) and (hour<19):
        speak(f"Good Evening {USER}")
    speak(f"I am {HOSTNAME}. How may i assist you ? {USER}")

if __name__ == "__main__" :
    greet_me() 
    # speak("Hi Iam your personal assistant")
    # print("Hi Iam your personal assistant")
