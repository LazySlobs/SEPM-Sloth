import pyautogui

#SELENIUM
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time



from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager


import settings
import speech_recognition as sr
from core.listen import record_audio


# FUNCTIONS
def open_browser_window():
    def go_to(url):
        driver.get(url)

    def list_button():
        clickable_button = []
        elems = driver.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            clickable_button.append(elem.text)
        return clickable_button
    def select_button(button):
        try:
            driver.find_element_by_xpath(f"//*[contains(text(), '{button}')]").click()
        except:
            print("Unable to click.")
    def refesh():
        driver.refresh()
    def back():
        driver.back()
    def forward():
        driver.forward()
    def return_home():
        url = 'https://www.google.com'
        driver.get(url)
    def minimize():
        driver.minimize_window()
    def maximize():
        driver.maximize_window()   
    def new_tab():
         # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "t")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "t")
        else:
            return 0
    def new_browser_window():
         # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl","n")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "n")
        else:
            return 0 
    def close_app():
        driver.quit()
    def open_history():
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "h")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "y")
        else:
            return 0
    def select_address_bar():
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "l")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "l")
        else:
            return 0
    def full_screen():
        driver.fullscreen_window()
    def scroll_to_top():
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("home")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "up")
        else:
            return 0
    def scroll_to_bottom():
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("end")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "down")
        else:
            return 0
    def scroll_down():
        pyautogui.hotkey("space")
    def scroll_up():
        pyautogui.hotkey("shift", "space")
    def book_mark_page():
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "d")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "shift", "d")
        else:
            return 0
    def book_mark_list():
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "shift", "o")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "shift", "l")
        else:
            return 0
    def private_window():
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "shift", "n")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "shift", "n")
        else:
            return 0
    def text_search():
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "f")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "f")
        else:
            return 0
    def open_download_history():
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "j")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "option", "l")
        else:
            return 0
    def clear_browsing_data():
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "shift", "delete")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("option", "command", "e")
        else:
            return 0
    def inspect_website():
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "shift", "i")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("option", "command", "i")
        else:
            return 0
    def next_tab():
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "tab")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("ctrl", "tab")
        else:
            return 0
    driver = webdriver.Chrome(ChromeDriverManager().install())
    original_window = driver.current_window_handle
    windows = driver.window_handles
    driver.maximize_window()    
    url = 'https://www.google.com'
    driver.get(url)
    
    def processor():
        while True:
            print(list_button())
            voice_data = input("What can I do? ")
            if voice_data == "switch window" or voice_data == "change window":
                naviagate_windows()
            elif "go to" in voice_data:
                url = voice_data.replace('go to ','https://')
                go_to(url)
            elif "refresh" in voice_data or voice_data == "refresh page":
                refesh()
            elif "go back" in voice_data:
                back()
            elif "go forward" in voice_data:
                forward()
            elif "return home" in voice_data:
                return_home()
            elif "address bar" in voice_data:
                select_address_bar()
            elif "fullscreen" in voice_data or "full screen" in voice_data:
                full_screen()
            elif voice_data == "scroll to top" or voice_data == "scroll to the top":
                scroll_to_top()
            elif voice_data == "scroll to bottom" or voice_data == "scroll to the bottom":
                scroll_to_bottom()
            elif "scroll up" in voice_data:
                scroll_up()
            elif "scroll down" in voice_data:
                scroll_down()
            elif "bookmark page" in voice_data:
                book_mark_page()
            elif "bookmark list" in voice_data:
                book_mark_list()
            elif "open" in voice_data and "private window" in voice_data:
                private_window()
            elif "find text" in voice_data:
                text_search()
            elif voice_data == "open history":
                open_history()
            elif "dowload" in voice_data:
                open_download_history()
            elif voice_data == "clear browsing data":
                clear_browsing_data()
            elif "inspect" in voice_data or voice_data == "inspect website":
                inspect_website()
            elif "new window" in voice_data or voice_data == "open new window":
                new_browser_window()
            elif voice_data == "new tab" or voice_data == "open new tab":
                new_tab()
            elif voice_data == "next tab" or voice_data == "go to next tab":
                next_tab()
            elif voice_data in list_button():
                select_button(voice_data)
            elif "close app" in voice_data:
                close_app()
                break
            else : 
                print("invalid command")


    fetch = True
    while fetch:
        for window_handle in windows :
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
            time.sleep(5)
            processor()


def naviagate_windows():
    if settings.platform == 'Windows':
        pyautogui.keyDown("alt")
        pyautogui.keyDown("tab")
        move_button()
        pyautogui.keyUp("alt")
        pyautogui.keyUp("tab")
    elif settings.platform == 'Darwin':
        pyautogui.keyDown("alt")
        pyautogui.keyDown("tab")
        move_button()
        pyautogui.keyUp("alt")
        pyautogui.keyUp("tab")

def move_button():
    r1 = sr.Recognizer()  # create a recognizer object to recognize texts
    r1.energy_threshold = 4000
    while True:
        navigate_data, language = record_audio(r1)
        print(navigate_data)
        if "right" in navigate_data:
            pyautogui.press("right")
        elif "left" in navigate_data:
            pyautogui.press("left")
        elif "up" in navigate_data:
            pyautogui.press("up")
        elif "down" in navigate_data:
            pyautogui.press("down")
        elif "enter" in navigate_data:
            pyautogui.press("enter")
            break





