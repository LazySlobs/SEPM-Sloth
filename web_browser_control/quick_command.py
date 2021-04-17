import pyautogui
import webbrowser as wb
import settings
import speech_recognition as sr
from core.listen import record_audio


def open_browser_window():
    '''

    Parameters:


    Returns:

    '''
    url = 'https://www.google.com'
    wb.get().open(url)



def open_history():
    '''

    Parameters:


    Returns:

    '''

    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "h")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "option","2")
    else:
        return 0

def refesh():
    '''

    Parameters:


    Returns:

    '''

    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "f5")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "r")
    else:
        return 0

def back():
    '''

    Parameters:


    Returns:

    '''

    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("alt", "left")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "left")
    else:
        return 0



def forward():
    '''

    Parameters:


    Returns:

    '''

    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("alt", "right")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "right")
    else:
        return 0

def return_home():
    '''

    Parameters:


    Returns:

    '''

    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("alt", "home")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command","shift" ,"h")
    else:
        return 0


def select_address_bar():
    '''

    Parameters:


    Returns:

    '''

    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "l")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "l")
    else:
        return 0

def full_screen():
    '''

    Parameters:



    '''

    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("f11")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command","control","f")
    else:
        return 0


def scroll_to_top():
    '''

    Parameters:


    Returns:

    '''

    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("home")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "up")
    else:
        return 0

def scroll_to_bottom():
    '''

    Parameters:


    Returns:

    '''

    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("end")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "down")
    else:
        return 0

def scroll_down():
    '''

    Parameters:


    Returns:

    '''
    pyautogui.hotkey("space")

def scroll_up():
    '''

    Parameters:


    Returns:

    '''
    pyautogui.hotkey("shift", "space")

def book_mark_page():
    '''

    Parameters:


    Returns:

    '''

    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "d")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "shift", "d")
    else:
        return 0

def book_mark_list():
    '''

    Parameters:


    Returns:

    '''

    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "shift", "o")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "shift", "l")
    else:
        return 0

def private_window():
    '''

    Parameters:


    Returns:

    '''

    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "shift", "n")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "shift", "n")
    else:
        return 0

def text_search():
    '''

    Parameters:


    Returns:

    '''

    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "f")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "f")
    else:
        return 0


def open_download_history():
    '''

    Parameters:


    Returns:

    '''

    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "j")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "option", "l")
    else:
        return 0

def clear_browsing_data():
    '''

    Parameters:


    Returns:

    '''

    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "shift", "delete")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("option", "command", "e")
    else:
        return 0

def inspect_website():
    '''

    Parameters:


    Returns:

    '''

    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "shift", "i")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("option", "command", "i")
    else:
        return 0

def new_browser_window():
    '''

    Parameters:


    Returns:

    '''

    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "n")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "n")
    else:
        return 0

def next_tab():
    '''

    Parameters:


    Returns:

    '''

    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "tab")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("ctrl", "tab")
    else:
        return 0

def new_tab():
    '''

    Parameters:


    Returns:

    '''

    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "t")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "t")
    else:
        return 0

def close_app():
    '''

    Parameters:


    Returns:

    '''

    # try to open with os
    if settings.platform == 'Windows':
        pyautogui.hotkey("alt", "f4")
    elif settings.platform == 'Darwin':
        pyautogui.hotkey("command", "q")
    else:
        return 0

def naviagate_windows():
    '''

    Parameters:


    Returns:

    '''
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




