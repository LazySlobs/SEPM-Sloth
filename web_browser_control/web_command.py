import pyautogui, pywinauto, time
import settings
import speech_recognition as sr
from core.listen import record_audio

#SELENIUM
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

class Chrome:
    # Initializing
    def __init__(self):
        pass

    # Deleting (Calling destructor)
    def __del__(self):
        print('Chrome object destroyed.')
    
    def open_browser(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.original_window = self.driver.current_window_handle
        self.windows = self.driver.window_handles
        self.driver.maximize_window()
        self.driver.get('https://www.google.com')
        print(self.list_button())

    def focus_browser(self):
        try:
            app = pywinauto.Application().connect(title_re=".*Chrome.*", found_index=0) # connect to chrome browser
            browser = app.top_window()  # get browser at the top index
            # browser.print_control_identifiers()   # print control identifiers for debug
            browser.set_focus()  # bring browser window to front
        except:
            print("Can't find Chrome browser window.")

    def switch_to_window(self):
        for window_handle in self.windows :
            if window_handle != self.original_window:
                self.driver.switch_to.window(window_handle)

    def go_to(self, url):
        self.driver.get(url)

    def list_button(self):
        clickable_button = []
        elems = self.driver.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            clickable_button.append(elem.text)
        return clickable_button

    def select_button(self, voice_data):
        for elm in self.list_button():
            print(elm)
            if voice_data.lower() == elm.lower():
                try:
                    self.driver.find_element_by_xpath(f"//*[contains(text(), '{elm}')]").click()
                    return True
                except:
                    print("Unable to select.")
                    return False
        print("Can't find element with matching string.")
        return False

    def refesh(self):
        self.driver.refresh()

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def return_home(self):
        url = 'https://www.google.com'
        self.driver.get(url)

    def minimize(self):
        self.driver.minimize_window()

    def maximize(self):
        self.driver.maximize_window()

    def close_window(self):
        self.driver.close()

    def close_browser(self):
        self.driver.quit()

    def full_screen(self):
        self.driver.fullscreen_window()

    def new_tab(self):
        self.focus_browser()
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "t")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "t")

    def new_browser_window(self):
        self.focus_browser()
            # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl","n")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "n")

    def open_history(self):
        self.focus_browser()
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "h")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "y")

    def select_address_bar(self):
        self.focus_browser()
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "l")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "l")

    def scroll_to_top(self):
        self.focus_browser()
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("home")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "up")

    def scroll_to_bottom(self):
        self.focus_browser()
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("end")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "down")

    def scroll_down(self):
        self.focus_browser()
        pyautogui.hotkey("space")

    def scroll_up(self):
        self.focus_browser()
        pyautogui.hotkey("shift", "space")

    def book_mark_page(self):
        self.focus_browser()
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "d")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "shift", "d")

    def book_mark_list(self):
        self.focus_browser()
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "shift", "o")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "shift", "l")

    def private_window(self):
        self.focus_browser()
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "shift", "n")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "shift", "n")

    def text_search(self):
        self.focus_browser()
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "f")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "f")

    def open_download_history(self):
        self.focus_browser()
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "j")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("command", "option", "l")

    def clear_browsing_data(self):
        self.focus_browser()
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "shift", "delete")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("option", "command", "e")

    def inspect_website(self):
        self.focus_browser()
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "shift", "i")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("option", "command", "i")

    def next_tab(self):
        self.focus_browser()
        # try to open with os
        if settings.platform == 'Windows':
            pyautogui.hotkey("ctrl", "tab")
        elif settings.platform == 'Darwin':
            pyautogui.hotkey("ctrl", "tab")

    def move_button(self, r):
        while True:
            # navigate_data = input("navigate data: ")
            navigate_data, language = record_audio(r)
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

    def navigate_windows(self):
        self.focus_browser()
        if settings.platform == 'Windows':
            pyautogui.keyDown("alt")
            pyautogui.keyDown("tab")
            self.move_button()
            pyautogui.keyUp("alt")
            pyautogui.keyUp("tab")
        elif settings.platform == 'Darwin':
            pyautogui.keyDown("alt")
            pyautogui.keyDown("tab")
            self.move_button()
            pyautogui.keyUp("alt")
            pyautogui.keyUp("tab")
