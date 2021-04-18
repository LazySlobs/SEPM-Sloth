from core.speak import voice_assistant_speak
from core.listen import record_audio
from time import ctime
import webbrowser as wb
import web_browser_control.quick_command as webr
import os_functions.manage_dir as manage_dir    # use manage directory file
import miscellaneous_functions.weather as weather    # use weather file
import miscellaneous_functions.news as news    # use news file
import miscellaneous_functions.math as math    # use math file
import miscellaneous_functions.monitor as monitor    # use monitor file
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
    
    # ==================================== #
    # ========== CORE FUNCTIONS ========== #
    # ==================================== #
    # exit
    if "exit" in voice_data:
        exit()
    

    # ======================================= #
    # ========== BROWSER FUNCTIONS ========== #
    # ======================================= #
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
        location, language = record_audio(r, language='en', ask='What is the location')
        url = 'https://www.google.nl/maps/place/' + location + '/&lamp;'
        wb.get().open(url)
        voice_assistant_speak(location, language=language)
    
    elif "open" in voice_data and "browser" in voice_data:
        webr.open_browser_window()
    elif voice_data == "switch window" or voice_data == "change window":
        webr.naviagate_windows()
    elif "refresh" in voice_data or voice_data == "refresh page":
        webr.refesh()
    elif "go back" in voice_data:
        webr.back()
    elif "go forward" in voice_data:
        webr.forward()
    elif "return home" in voice_data:
        webr.return_home()
    elif "address bar" in voice_data:
        webr.select_address_bar()
    elif "olive green" in voice_data:
        webr.full_screen()
    elif voice_data == "scroll to top" or voice_data == "scroll to the top":
        webr.scroll_to_top()
    elif voice_data == "scroll to bottom" or voice_data == "scroll to the bottom":
        webr.scroll_to_bottom()
    elif "scroll up" in voice_data:
        webr.scroll_up()
    elif "scroll down" in voice_data:
        webr.scroll_down()
    elif "bookmark page" in voice_data:
        webr.book_mark_page()
    elif "bookmark list" in voice_data:
        webr.book_mark_list()
    elif "open" in voice_data and "private window" in voice_data:
        webr.private_window()
    elif "find text" in voice_data:
        webr.text_search()
    elif voice_data == "open history":
        webr.open_history()
    elif "dowload" in voice_data:
        webr.open_download_history()
    elif voice_data == "clear browsing data":
        webr.clear_browsing_data()
    elif "inspect" in voice_data or voice_data == "inspect website":
        webr.inspect_website()
    elif "new window" in voice_data or voice_data == "open new window":
        webr.new_browser_window()
    elif voice_data == "new tab" or voice_data == "open new tab":
        webr.new_tab()
    elif voice_data == "next tab" or voice_data == "go to next tab":
        webr.next_tab()
    elif "close app" in voice_data:
        webr.close_app()
    

    # ================================== #
    # ========== OS FUNCTIONS ========== #
    # ================================== #
    # delete
    elif 'delete' in voice_data:
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

    # copy
    elif 'copy' in voice_data:
        manage_dir.copy(voice_data)
        
    # paste
    elif 'paste' in voice_data:
        manage_dir.paste(voice_data)
        
    # cut
    elif 'cut' in voice_data:
        manage_dir.cut(voice_data)
        
    # undo
    elif 'undo' in voice_data:
        manage_dir.undo(voice_data)
        
    # redo
    elif 'redo' in voice_data:
        manage_dir.redo(voice_data)

    # ======================================= #
    # ========== GENERAL FUNCTIONS ========== #
    # ======================================= #
    # asked for name
    elif "what is your name" in voice_data or "what's your name" in voice_data or "whats your name" in voice_data:
        voice_assistant_speak("My name is Sloth.")

    # asked for time
    elif "what time is it" in voice_data:
        voice_assistant_speak(ctime())
    
    # check weather
    elif "what's the weather in" in voice_data or "what's the weather of" in voice_data:
        city = voice_data
        city = city.replace('what', '')
        city = city.replace('the weather in ', '')
        city = city.replace('the weather of ', '')
        city = city.replace("'s ", '')
        print("city: " + city)
        weather.check_city_weather(city)
    elif "how's the weather in" in voice_data or "how's the weather of" in voice_data or ("how" in voice_data and "weather" in voice_data):
        city = voice_data
        city = city.replace('how', '')
        city = city.replace('the weather in ', '')
        city = city.replace('the weather of ', '')
        city = city.replace("'s ", '')
        print("city: " + city)
        weather.check_city_weather(city)
    elif "check the weather in" in voice_data or "check the weather of" in voice_data or ("check" in voice_data and "weather" in voice_data):
        city = voice_data
        city = city.replace('check the weather of ', '')
        city = city.replace('check the weather in ', '')
        city = city.replace('check ', '')
        city = city.replace("'s ", '')
        city = city.replace(' weather', '')
        print("city: " + city)
        weather.check_city_weather(city)
    elif voice_data == "check the weather" or ("what" in voice_data and "weather" in voice_data):
        city, language = record_audio(r, language='en', ask='Which city would you like to check?')
        weather.check_city_weather(city)
    
    # check the news
    elif "check the news from" in voice_data or "check the news in" in voice_data:
        voice_data = voice_data.replace("check the news ", "")
        voice_data = voice_data.replace("in ", "")
        voice_data = voice_data.replace("from ", "")
        news.read_news_headlines_process(r, voice_data)
    elif "check the news" in voice_data:
        news.read_news_headlines_ask()

    # do math
    elif "what" in voice_data and ("/" in voice_data or "*" in voice_data or "x" in voice_data or "mod" in voice_data or "+" in voice_data or "-" in voice_data):
        voice_data = voice_data.replace("what's ", "")
        voice_data = voice_data.replace("what is ", "")
        voice_data = voice_data.replace("whats ", "")
        math.do_math(voice_data)
    
    # display performance
    elif "what" in voice_data and ("CPU" in voice_data and ("RAM" in voice_data or "memory" in voice_data)):
        monitor.tell_cpu_and_ram_used()
    elif "what" in voice_data and "CPU" in voice_data:
        monitor.tell_cpu_used()
    elif "what" in voice_data and ("RAM" in voice_data or "memory" in voice_data):
        monitor.tell_ram_used()
    elif "what" in voice_data and ("remaining RAM" in voice_data or "remaining memory" in voice_data):
        monitor.tell_available_ram()
    elif "display" in voice_data and ("CPU" in voice_data and ("RAM" in voice_data or "memory" in voice_data)):
        monitor.display_cpu_and_ram_used()
    elif "display" in voice_data and "CPU" in voice_data:
        monitor.display_cpu_used()
    elif "display" in voice_data and ("RAM" in voice_data or "memory" in voice_data):
        monitor.display_ram_used()

    