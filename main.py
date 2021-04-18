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

WAKE = "hey sloth"

def main():
    while True:
        # speak if the ask variable is a string
        with sr.Microphone() as source:
            # starts to listen
            print("Listening for keyword...")
            audio = r1.listen(source)
            listen_for_keyword = ""
            try:
                listen_for_keyword = r1.recognize_google(audio)
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                voice_assistant_speak("Sorry, my speech service is down")
                continue
            print("listen_for_keyword = " + listen_for_keyword)

            if listen_for_keyword.count(WAKE) > 0:
                print("Sloth is awake...")
                voice_assistant_speak("How can I help you?")
                print("Listening...")
                voice_data, language = record_audio(r1)
                print("Voice data: " + voice_data)
                respond(r2, voice_data, language=language)
            elif listen_for_keyword.lower() == "stop the program":
                break

if __name__ == '__main__':
    main()
