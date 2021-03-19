from core.speak import voice_assistant_speak
from core.listen import record_audio
from time import ctime
import webbrowser as wb
from os_funtions.manage_dir import *

def respond(r, voice_data, language='en'):
    print("Waiting for voice...")
    
    #os functions
    #delete
    if 'delete' in voice_data:
        delete_file(voice_data)



    if "what is your name" in voice_data or "what's your name" in voice_data:
        voice_assistant_speak(" My name is Sloth")
    if "what time is it" in voice_data:
        voice_assistant_speak(ctime())
    if "search for" in voice_data:
        search = voice_data
        search = search.replace('search for', '')
        url = 'https://www.google.com/search?q=' + search
        voice_assistant_speak("Here is what i found for " + search)
        wb.get().open(url)
    elif "search" in voice_data:
        search, language = record_audio(r, ask='What do you want to search for')
        url = 'https://www.google.com/search?q=' + search
        wb.get().open(url)
        voice_assistant_speak("Here is what i found for " + search)
    if "find location" in voice_data or 'locate' in voice_data:
        location, language = record_audio(r, language='vi', ask='What is the location')
        url = 'https://www.google.nl/maps/place/' + location + '/&lamp;'
        wb.get().open(url)
        voice_assistant_speak(location, language=language)
    if "exit" in voice_data:
        exit()
    print(voice_data)

