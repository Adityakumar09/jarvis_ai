import pyttsx3

engine = pyttsx3.init('sapi5') # microsoft speech api for speech recognition 

engine.setProperty('volume',1.5)
engine.setProperty('rate',225)

voices=engine.getProperty('voices') # import voices module of python library
engine.setProperty('voice',voices[1].id)
# 1-female 2-male

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__" : 
    speak("Hi Iam your personal assistant")
    print("Hi Iam your personal assistant")
