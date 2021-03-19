import speech_recognition as sr
from speak import voice_assistant_speak

def record_audio(r, ask = False):
    with sr.Microphone()as source:
        if ask:
            voice_assistant_speak(ask)

        print("Listening")
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language='en')
        except sr.UnknownValueError:
            voice_assistant_speak("Sorry, I did not get that")
        except sr.RequestError:
            voice_assistant_speak("Sorry, my speech service is down")
    return voice_data