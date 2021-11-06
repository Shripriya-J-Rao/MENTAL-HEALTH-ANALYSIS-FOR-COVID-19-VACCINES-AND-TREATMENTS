import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

num = 1


def speak(text):
    global num
    num +=1
    tts=gTTS(text=text,lang="en")
    filename=str(num)+".mp3"
    tts.save(filename)
    playsound.playsound(filename,True)
    os.remove(filename)


def read(text):
    speak(text)
