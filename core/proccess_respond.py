import sys

from core.speak import voice_assistant_speak
from core.listen import record_audio
import settings, time
import webbrowser as wb
import web_browser_control.quick_command as webr
import os_functions.manage_dir as manage_dir    # use manage directory file
import miscellaneous_functions.weather as weather    # use weather file
import miscellaneous_functions.news as news    # use news file
import miscellaneous_functions.math as math    # use math file
import miscellaneous_functions.monitor as monitor    # use monitor file
import gui.gui_qt_creator.weatherGUI as weatherGUI
import gui.gui_qt_creator.systemGUI as systemGUI
import speech_recognition as sr
from multiprocessing import Process




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
    # Introduce
    if "Introduce yourself" in voice_data:
       voice_assistant_speak("I am Sloth Voice Assistant created by Lazy Slob Team" )


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
    elif voice_data == "find location":
        location, language = record_audio(r, language='en', ask="What's the location?")
        url = 'https://www.google.nl/maps/place/' + location + '/&lamp;'
        wb.get().open(url)
        voice_assistant_speak(location, language=language)
    elif "locate" in voice_data and voice_data.split().len() > 1:
        location, language = record_audio(r, language='en', ask='What is the location?')
        url = 'https://www.google.nl/maps/place/' + location + '/&lamp;'
        wb.get().open(url)
        voice_assistant_speak(location, language=language)

    elif voice_data == "open browser":
        webr.open_browser_window()
    elif voice_data == "switch window" or voice_data == "change window":
        webr.naviagate_windows()
    elif voice_data == "refresh" or voice_data == "refresh page":
        webr.refesh()
    elif voice_data == "go back":
        webr.back()
    elif voice_data == "go forward":
        webr.forward()
    elif voice_data == "return home":
        webr.return_home()
    elif voice_data == "select address bar":
        webr.select_address_bar()
    elif voice_data == "go fullscreen":
        webr.full_screen()
    elif voice_data == "scroll to top" or voice_data == "scroll to the top":
        webr.scroll_to_top()
    elif voice_data == "scroll to bottom" or voice_data == "scroll to the bottom":
        webr.scroll_to_bottom()
    elif voice_data == "scroll up":
        webr.scroll_up()
    elif voice_data == "scroll down":
        webr.scroll_down()
    elif voice_data == "bookmark this page":
        webr.book_mark_page()
    elif voice_data == "open bookmark list":
        webr.book_mark_list()
    elif voice_data == "open private window" or voice_data == "open incognito mode":
        webr.private_window()
    elif voice_data == "find text":
        webr.text_search()
    elif voice_data == "open history":
        webr.open_history()
    elif voice_data == "open dowload history":
        webr.open_download_history()
    elif voice_data == "clear browsing data":
        webr.clear_browsing_data()
    elif voice_data == "inspect" or voice_data == "inspect website":
        webr.inspect_website()
    elif voice_data == "new window" or voice_data == "open new window":
        webr.new_browser_window()
    elif voice_data == "new tab" or voice_data == "open new tab":
        webr.new_tab()
    elif voice_data == "next tab" or voice_data == "go to next tab":
        webr.next_tab()
    elif voice_data == "close app" or voice_data == "close the app":
        webr.close_app()

    # ================================== #
    # ========== OS FUNCTIONS ========== #
    # ================================== #

    # delete
    elif 'delete' in voice_data:
        manage_dir.delete_file(voice_data, location = settings.location)

    # open
    elif "open" in voice_data:
        manage_dir.open_file(r, voice_data)

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
    elif voice_data == "what is your name" or voice_data == "what's your name" or voice_data == "whats your name":
        voice_assistant_speak("My name is Sloth.")

    # asked for time
    elif voice_data == "check the time" or voice_data == "what time is it" or voice_data == "whats the time" or voice_data == "what's the time":
        voice_assistant_speak(str(time.strftime("It's currently %H:%M o'clock")))

    # check weather
    elif "what's the weather in" in voice_data or "what's the weather of" in voice_data or "what is the weather in" in voice_data or "what is the weather of" in voice_data:
        city = voice_data
        city = city.replace('what', '')
        city = city.replace('the weather in ', '')
        city = city.replace('the weather of ', '')
        city = city.replace("'s ", '')
        print("city: " + city)
        current = weather.Current_Weather(city)
        # create Sub process to display Weather
        if (current.display_weather_results()):
            # create Sub process to display Weather
            current.display_weather_console()
            a = Process(target=weatherGUI.WeatherWindow, args=(city,))
            a.start()
            a.join()
            a.terminate()
            print("function done")
        else:
            voice_assistant_speak("I could not find the city you said")

    elif "how's the weather in" in voice_data or "how's the weather of" in voice_data or ("how" in voice_data and "weather" in voice_data):
        city = voice_data
        city = city.replace('how', '')
        city = city.replace('the weather in ', '')
        city = city.replace('the weather of ', '')
        city = city.replace("'s ", '')
        print("city: " + city)
        current = weather.Current_Weather(city)
        if (current.display_weather_results()):
            # create Sub process to display Weather
            current.display_weather_console()
            d = Process(target=weatherGUI.WeatherWindow, args=(city,))
            d.start()
            d.join()
            d.terminate()
            print("function done")
        else:
            voice_assistant_speak("I could not find the city you said")



    elif "check the weather in" in voice_data or "check the weather of" in voice_data or ("check" in voice_data and "weather" in voice_data):
        city = voice_data
        city = city.replace('check the weather of ', '')
        city = city.replace('check the weather in ', '')
        city = city.replace('check ', '')
        city = city.replace("'s ", '')
        city = city.replace(' weather', '')
        print("city: " + city)
        current = weather.Current_Weather(city)
        if (current.display_weather_results()):
            # create Sub process to display Weather
            current.display_weather_console()
            b = Process(target=weatherGUI.WeatherWindow, args=(city,))
            b.start()
            b.join()
            b.terminate()
            print("function done")
        else:
            voice_assistant_speak("I could not find the city you said")

    elif voice_data == "check the weather" or ("what" in voice_data and "the weather" in voice_data):
        city, language = record_audio(r, language='en', ask='Which city would you like to check?')
        current = weather.Current_Weather(city)
        if (current.display_weather_results()):
            # create Sub process to display Weather
            current.display_weather_console()
            c = Process(target=weatherGUI.WeatherWindow, args=(city,))
            c.start()
            c.join()
            c.terminate()
            print("function done")
        else:
            voice_assistant_speak("I could not find the city you said")

    # check the news
    elif "check the news from" in voice_data or "check the news in" in voice_data:
        voice_data = voice_data.replace("check the news ", "")
        voice_data = voice_data.replace("in ", "")
        voice_data = voice_data.replace("from ", "")
        news.read_news_headlines_process(r, voice_data)
    elif voice_data == "check the news":
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
    elif "computer system" in voice_data :
        # create Sub process to display Computer system
        p = Process(target=systemGUI.SystemWindow)
        p.start()
        p.join()
        p.terminate()
        print("function done")


#


if __name__ == '__main__':
    respond()