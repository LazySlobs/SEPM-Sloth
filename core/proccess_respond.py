from core.speak import voice_assistant_speak
from core.listen import record_audio
from time import ctime
import webbrowser as wb

def respond(r, voice_data):
    print("Waiting for voice...")
    # if "hey Bao" not in voice_data:
    #     return
    if "what is your name" in voice_data or "what's your name" in voice_data:
        voice_assistant_speak(" My name is Sloth")
    if "what time is it" in voice_data:
        voice_assistant_speak(ctime())
    if "search for" in voice_data:
        search = voice_data
        search = search.replace('search for', '')
        url = 'https://www.google.com/search?q=' + search
        voice_assistant_speak(voice_data)
        wb.get().open(url)
    elif "search" in voice_data:
        search = record_audio(r, 'What do you want to search for')
        url = 'https://www.google.com/search?q=' + search
        voice_assistant_speak(search)
        wb.get().open(url)
        voice_assistant_speak("Here is what i found for " + search)
    if "find location" in voice_data:
        location = record_audio(r, 'What is the location')
        url = 'https://www.google.nl/maps/place/' + location + '/&lamp;'
        voice_assistant_speak(location)
        wb.get().open(url)
        voice_assistant_speak("Here is the location of  " + location)
    if "exit" in voice_data:
        exit()
    print(voice_data)

