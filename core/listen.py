import speech_recognition as sr
from core.speak import voice_assistant_speak

def record_audio(r, language='en', ask = False):
    with sr.Microphone()as source:
        if ask:
            voice_assistant_speak(ask)

        print("Listening")
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language=language)
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        except sr.RequestError:
            voice_assistant_speak("Sorry, my speech service is down")
    return voice_data, language