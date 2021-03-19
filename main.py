import speech_recognition as sr
import time, random, os, playsound
from core.listen import record_audio
from core.speak import voice_assistant_speak
from core.proccess_respond import respond

r1 = sr.Recognizer() # create a recognizer object to recognize texts
r1.energy_threshold = 2000 # change threshold to eliminate background noise

r2 = sr.Recognizer()

def main():
    # time.sleep(1)
    voice_assistant_speak("How can I help you ?")
    while True:
        # try:
        voice_data, language = record_audio(r1)
        respond(r2, voice_data, language=language)
        # finally:


if __name__ == '__main__':
    main()