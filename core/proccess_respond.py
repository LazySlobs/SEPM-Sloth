from core.speak import voice_assistant_speak
from core.listen import record_audio
from time import ctime
import webbrowser as wb
import os_functions.manage_dir as manage_dir
import settings

def respond(r, voice_data, language='en'):
    '''
    Responds from the user's voice input and proccesses request

    Parameters:
        r(Recognizer): the recognizer used to listen and recognize audio
        voice_data(str): the string recorded and recognized from user's voice input

        Options:
            language(str): the language's short string

    Returns:
        Null
    '''

    print("Waiting for voice...")
    
    # os functions
        # delete
    if 'delete' in voice_data:
        manage_dir.delete_file(voice_data, location = settings.location)

        # open 
    if 'open' in voice_data:
        manage_dir.open_file(voice_data, location = settings.location)

    # browser fuctions
        # search google
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

        # find location
    if "find location" in voice_data or 'locate' in voice_data:
        location, language = record_audio(r, language='vi', ask='What is the location')
        url = 'https://www.google.nl/maps/place/' + location + '/&lamp;'
        wb.get().open(url)
        voice_assistant_speak(location, language=language)

    # general functions
        # asked for name
    if "what is your name" in voice_data or "what's your name" in voice_data:
        voice_assistant_speak(" My name is Sloth")

        # asked for time
    if "what time is it" in voice_data:
        voice_assistant_speak(ctime())
    
    # internal functions
        # exit
    if "exit" in voice_data:
        exit()

