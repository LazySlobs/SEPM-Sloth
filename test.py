import speech_recognition as sr
import time

def count():
    while True:
        time.sleep(2)
        print(1+1)


r = sr.Recognizer()
r.energy_threshold = 2000

stop = r.listen_in_background(sr.Microphone(), count())
