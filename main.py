import speech_recognition as sr
import time, random, os, playsound
from core.listen import record_audio
from core.speak import voice_assistant_speak
from core.proccess_respond import respond
import settings

settings.init()

r1 = sr.Recognizer() # create a recognizer object to recognize texts
#r1.energy_threshold = settings.energy_threshold 
r2 = sr.Recognizer() # create a recognizer object to respond

def main():

    voice_assistant_speak("How can I help you ?")

    while True:

        voice_data, language = record_audio(r1)
        print(voice_data)
        respond(r2, voice_data, language=language)

if __name__ == '__main__':
    main()