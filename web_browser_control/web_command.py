import pyautogui, pywinauto

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
def focus_browser():
    try:
        app = pywinauto.Application().connect(title_re=".*Chrome.*", found_index=0) # connect to explorer.exe which is windows taskbar instances and other windows elements
        browser = app.top_window()  # get currently displayed folder because Taskbar is always at index 0
        # browser.print_control_identifiers()
        browser.set_focus()  # bring folder file explorer window to front
    except:
        print("Can't find Chrome browser window.")

def go_to(driver, url):
    driver.get(url)

def list_button(driver):
    clickable_button = []
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        clickable_button.append(elem.text)
    return clickable_button

def select_button(driver, button):
    try:
        driver.find_element_by_xpath(f"//*[contains(text(), '{button}')]").click()
    except:
        print("Unable to click.")

def refesh(driver):
    driver.refresh()

def back(driver):
    driver.back()

def forward(driver):
    driver.forward()

def return_home(driver):
    url = 'https://www.google.com'
    driver.get(url)

def minimize(driver):
    driver.minimize_window()

def maximize(driver):
    driver.maximize_window()

def close_app(driver):
    driver.quit()

def full_screen(driver):
    driver.fullscreen_window()

def new_tab():
    focus_browser()
    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "t")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "t")

def new_browser_window():
    focus_browser()
        # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl","n")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "n")

def open_history():
    focus_browser()
    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "h")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "y")

def select_address_bar():
    focus_browser()
    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "l")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "l")

def scroll_to_top():
    focus_browser()
    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("home")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "up")

def scroll_to_bottom():
    focus_browser()
    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("end")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "down")

def scroll_down():
    focus_browser()
    pyautogui.hotkey("space")

def scroll_up():
    focus_browser()
    pyautogui.hotkey("shift", "space")

def book_mark_page():
    focus_browser()
    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "d")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "shift", "d")

def book_mark_list():
    focus_browser()
    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "shift", "o")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "shift", "l")

def private_window():
    focus_browser()
    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "shift", "n")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "shift", "n")

def text_search():
    focus_browser()
    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "f")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "f")

def open_download_history():
    focus_browser()
    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "j")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "option", "l")

def clear_browsing_data():
    focus_browser()
    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "shift", "delete")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("option", "command", "e")

def inspect_website():
    focus_browser()
    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "shift", "i")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("option", "command", "i")

def next_tab():
    focus_browser()
    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "tab")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("ctrl", "tab")

def navigate_windows():
    focus_browser()
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

def processor(driver):
    while True:
        print(list_button(driver))
        voice_data = input("What can I do?")

        if voice_data == "switch window" or voice_data == "change window":
            navigate_windows()
        elif "go to" in voice_data:
            url = voice_data.replace('go to ','https://')
            go_to(driver, url)
        elif "refresh" in voice_data or voice_data == "refresh page":
            refesh(driver)
        elif "go back" in voice_data:
            back(driver)
        elif "go forward" in voice_data:
            forward(driver)
        elif "return home" in voice_data:
            return_home(driver)
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
        elif voice_data in list_button(driver):
            select_button(driver, voice_data)
        elif "close app" in voice_data:
            close_app(driver)
            break
        else : 
            print("invalid command")

def open_browser_window():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    original_window = driver.current_window_handle
    windows = driver.window_handles
    driver.maximize_window()    
    url = 'https://www.google.com'
    driver.get(url)

    while True:
        for window_handle in windows :
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
            time.sleep(5)
            processor(driver)






