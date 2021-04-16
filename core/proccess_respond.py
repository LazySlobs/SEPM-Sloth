from core.speak import voice_assistant_speak
from core.listen import record_audio
from time import ctime
import webbrowser as wb
import os_functions.manage_dir as manage_dir
import web_browser_control.quick_command as webr
import settings
import threading
import speech_recognition as sr


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
    elif 'open' in voice_data:
        manage_dir.open_file(voice_data, location = settings.location)

        # create 
    elif 'create' in voice_data:
        manage_dir.create_file(voice_data, location = settings.location)

        # get info 
    elif 'information' in voice_data and 'show' in voice_data:
        manage_dir.file_info(voice_data)

        # scoll 
    elif 'scroll down' in voice_data:
        manage_dir.scroll_down(voice_data)

    # browser fuctions
        # search google
    elif "search for" in voice_data:
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
    elif "find location" in voice_data or 'locate' in voice_data:
        location, language = record_audio(r, language='vi', ask='What is the location')
        url = 'https://www.google.nl/maps/place/' + location + '/&lamp;'
        wb.get().open(url)
        voice_assistant_speak(location, language=language)

    # general functions
        # asked for name
    elif "what is your name" in voice_data or "what's your name" in voice_data:
        voice_assistant_speak(" My name is Sloth")

        # asked for time
    elif "what time is it" in voice_data:
        voice_assistant_speak(ctime())
    
    # internal functions

    # web browser functions
    elif "browser" in voice_data:
        webr.open_Browser_Window()
    elif "existing window" in voice_data:
        webr.naviagate_windows()
    elif "History" in voice_data:
        webr.open_history()
    elif "refresh" in voice_data:
        webr.refesh()
    elif "back" in voice_data:
        webr.back()
    elif "forward" in voice_data:
        webr.forward()
    elif "return Home" in voice_data:
        webr.return_Home()
    elif "address bar" in voice_data:
        webr.select_address_bar()
    elif "olive green" in voice_data:
        webr.full_screen()
    elif "scroll  top" in voice_data:
        webr.scroll_to_Top()
    elif "scroll  bottom" in voice_data:
        webr.scroll_to_Bottom()
    elif "scroll up" in voice_data:
        webr.scroll_up()
    elif "scroll down" in voice_data:
        webr.scroll_down()
    elif "bookmark page" in voice_data:
        webr.book_mark_page()
    elif "bookmark list" in voice_data:
        webr.book_mark_list()
    elif "private window" in voice_data:
        webr.private_window()
    elif "find text" in voice_data:
        webr.text_search()
    elif "history" in voice_data:
        webr.open_history()
    elif "dowload" in voice_data:
        webr.open_dowload_history()
    elif "clear browser data" in voice_data:
        webr.clear_browsing_data()
    elif "inspect" in voice_data:
        webr.inspect_website()
    elif "new window" in voice_data:
        webr.new_browser_window()
    elif "new tab" in voice_data:
        webr.new_tab()
    elif "next tab" in voice_data:
        webr.next_tab()
    elif "close app" in voice_data:
        webr.close_app()


    # exit
    elif "exit" in voice_data:
        exit()


