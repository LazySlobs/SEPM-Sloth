import speech_recognition as sr
from core.speak import voice_assistant_speak
import settings, threading

def calibrate(source, recognizer):
    recognizer.adjust_for_ambient_noise(source, duration=1)
    recognizer.energy_threshold += 250

def record_audio(r, language=settings.language, ask = False):
    '''
    Record user input and turns it to text

    Parameters:
        r(Recognizer): the recognizer used to listen and recognize audio

        Options:
            language(str): the language's short string
            ask(str/bool): the phrase used to speak before starts recording

    Raises:
        sr.UnknownValueError: no string used to recognize
        sr.RequestError: unresponsive request from recognizer's server

    Returns:
        voice_data(str): the string recorded and recognized from user's voice input
        language(str): the language's short string (the same language used to recognize)
    '''

    # loop so that it can return an actual voice data instead of an empty string
    while True:
        # speak if the ask variable is a string
        with sr.Microphone() as source:
            threading.Thread(target=calibrate, args=(source, r,)).start()
            if ask:
                voice_assistant_speak(ask)
            # starts to listen
            print("Listening...")
            audio = r.listen(source)
            voice_data = ""
            # try to recognize the audio
            try:
                voice_data = r.recognize_google(audio, language=language)
            except sr.UnknownValueError:
                print("Sorry, I did not get that")
                # voice_assistant_speak("Sorry, I did not get that")
                continue
            except sr.RequestError:
                voice_assistant_speak("Sorry, my speech service is down")
                continue
            except:
                print("Something went wrong.")
                continue
        return voice_data, language


if __name__ == '__main__':
	record_audio()