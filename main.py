import speech_recognition as sr
import time, random, os, playsound
from core.listen import record_audio
from core.speak import voice_assistant_speak
from core.proccess_respond import respond

r = sr.Recognizer() # create a recognizer object to recognize texts
r.energy_threshold = 1000 # change threshold to eliminate background noise


def main():
    # time.sleep(1)
    voice_assistant_speak("How can I help you ?")
    while True:
        # try:
        voice_data = record_audio(r)
        print(voice_data)
        respond(r, voice_data)
        # finally:


if __name__ == '__main__':
    main()