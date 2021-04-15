import speech_recognition as sr
from core.speak import voice_assistant_speak
import settings

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

    # speak if the ask variable is a string
    with sr.Microphone() as source:
        if ask:
            voice_assistant_speak(ask)

        print("Calibrating microphone...")
        # listen for 1 second to calibrate the energy threshold for ambient noise levels
        r.adjust_for_ambient_noise(source)

        # starts to listen
        print("Listening...")
        audio = r.listen(source)
        voice_data = ""

        # try to recognize the audio
        try:
            voice_data = r.recognize_google(audio, language=language)
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
            voice_assistant_speak("Sorry, I did not get that")
        except sr.RequestError:
            voice_assistant_speak("Sorry, my speech service is down")
            
    return voice_data, language