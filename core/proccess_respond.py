
from core.speak import voice_assistant_speak
from core.listen import record_audio
import time
import web_browser_control.web_command as webr
import os_functions.manage_dir as manage_dir    # use manage directory file
import miscellaneous_functions.weather as weather    # use weather file
import miscellaneous_functions.news as news    # use news file
import miscellaneous_functions.math as math    # use math file
import miscellaneous_functions.monitor as monitor    # use monitor file
import gui.gui_qt_creator.weatherGUI as weatherGUI
import gui.gui_qt_creator.systemGUI as systemGUI
from multiprocessing import Process


chrome = webr.Chrome()

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
    if "introduce yourself" in voice_data.lower():
       voice_assistant_speak("I am Sloth Voice Assistant created by Lazy Slob Team" )


    # ======================================= #
    # ========== BROWSER FUNCTIONS ========== #
    # ======================================= #
    # search google
    elif "search for " in voice_data:
        chrome.open_browser()
        search = voice_data
        search = search.replace('search for', '')
        url = 'https://www.google.com/search?q=' + search
        voice_assistant_speak("Here is what i found for " + search)
        chrome.go_to(url)
    elif "search " in voice_data:
        search, language = record_audio(r, ask='What do you want to search for')
        chrome.open_browser()
        url = 'https://www.google.com/search?q=' + search
        voice_assistant_speak("Here is what i found for " + search)
        chrome.go_to(url)
    elif voice_data.lower() == "open browser" or voice_data.lower() == "open chrome":
        chrome.open_browser()
    elif voice_data.lower() == "switch window" or voice_data.lower() == "change window":
        chrome.naviagate_windows()
    elif voice_data.lower() == "refresh" or voice_data.lower() == "refresh page":
        chrome.refesh()
    elif "go to " in voice_data:
        url = 'https://www.' + voice_data
        url = url.replace("go to ", "")
        chrome.go_to(url)
    elif voice_data == "go back":
        chrome.back()
    elif voice_data.lower() == "go forward":
        chrome.forward()
    elif voice_data.lower() == "return home":
        chrome.return_home()
    elif voice_data.lower() == "select address bar":
        chrome.select_address_bar()
    elif voice_data.lower() == "go fullscreen":
        chrome.full_screen()
    elif voice_data.lower() == "scroll to top" or voice_data.lower() == "scroll to the top":
        chrome.scroll_to_top()
    elif voice_data.lower() == "scroll to bottom" or voice_data.lower() == "scroll to the bottom":
        chrome.scroll_to_bottom()
    elif voice_data.lower() == "scroll up":
        chrome.scroll_up()
    elif voice_data.lower() == "scroll down":
        chrome.scroll_down()
    elif voice_data.lower() == "bookmark this page":
        chrome.book_mark_page()
    elif voice_data.lower() == "open bookmark list":
        chrome.book_mark_list()
    elif voice_data.lower() == "open private window" or voice_data.lower() == "open incognito mode":
        chrome.private_window()
    elif voice_data.lower() == "find text":
        chrome.text_search()
    elif voice_data.lower() == "open history":
        chrome.open_history()
    elif voice_data.lower() == "open dowload history":
        chrome.open_download_history()
    elif voice_data.lower() == "clear browsing data":
        chrome.clear_browsing_data()
    elif voice_data.lower() == "inspect" or voice_data.lower() == "inspect website":
        chrome.inspect_website()
    elif voice_data.lower() == "new window" or voice_data.lower() == "open new window":
        chrome.new_browser_window()
    elif voice_data.lower() == "new tab" or voice_data.lower() == "open new tab":
        chrome.new_tab()
    elif voice_data.lower() == "next tab" or voice_data.lower() == "switch to next tab":
        chrome.next_tab()
    elif 'select ' in voice_data and voice_data.split(' ')[0] == 'select':
        voice_data = voice_data.replace("select ", "")
        chrome.select_button(voice_data)
    elif voice_data.lower() == "close window" or voice_data.lower() == "close the window":
        chrome.close_window()
    elif voice_data.lower() == "close browser" or voice_data.lower() == "close the browser" or voice_data.lower() == "close chrome":
        chrome.close_browser()

    # ================================== #
    # ========== OS FUNCTIONS ========== #
    # ================================== #

    # # list files
    # elif voice_data == "list file":
    #     manage_dir.list_file_auto_locate()
    
    # delete
    elif 'delete ' in voice_data and voice_data.split(' ')[0] == 'delete':
        manage_dir.delete_file(voice_data)

    # open file explorer
    elif voice_data.lower() == "open folder" or voice_data.lower() == "open file explorer":
        manage_dir.open_file_explorer(voice_data)

    # open
    elif "open " in voice_data and voice_data.split(' ')[0] == 'open':
        manage_dir.open_file(voice_data)

    # create
    elif 'create ' in voice_data and voice_data.split(' ')[0] == 'create':
        manage_dir.create_folder(voice_data)

    # get info
    elif 'information' in voice_data and 'show' in voice_data:
        manage_dir.file_info(voice_data)


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

    # enter a folder
    elif "enter " in voice_data:
        folder_name = voice_data.replace("enter ", "")
        manage_dir.enter_folder(folder_name)

    # go back to previous folder
    elif "go back to previous folder" in voice_data:
        manage_dir.go_back()

    # go back to previous folder
    elif "enter parent folder" in voice_data:
        manage_dir.go_to_parent_folder()

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
        if (current.display_weather_results()):
            # create Sub process to display Weather
            current.display_weather_console()
            a = Process(target=weatherGUI.WeatherWindow, args=(city,))
            a.start()
            a.join()
            a.terminate()
        else:
            voice_assistant_speak("Sorry, I can't find the weather data of this city")

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
            b = Process(target=weatherGUI.WeatherWindow, args=(city,))
            b.start()
            b.join()
            b.terminate()
        else:
            voice_assistant_speak("Sorry, I can't find the weather data of this city")

    elif "check the weather in" in voice_data or "check the weather of" in voice_data:
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
            c = Process(target=weatherGUI.WeatherWindow, args=(city,))
            c.start()
            c.join()
            c.terminate()
        else:
            voice_assistant_speak("Sorry, I can't find the weather data of this city")

    elif voice_data == "check the weather" or ("what" in voice_data and "the weather" in voice_data):
        city, language = record_audio(r, language='en', ask='Which city would you like to check?')
        current = weather.Current_Weather(city)
        if (current.display_weather_results()):
            # create Sub process to display Weather
            current.display_weather_console()
            d = Process(target=weatherGUI.WeatherWindow, args=(city,))
            d.start()
            d.join()
            d.terminate()
        else:
            voice_assistant_speak("Sorry, I can't find the weather data of this city")

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
    elif "check" in voice_data and ("system info" or "system information") in voice_data :
        # create Sub process to display Computer system
        p = Process(target=systemGUI.SystemWindow)
        p.start()
        p.join()
        p.terminate()


if __name__ == '__main__':
    respond()