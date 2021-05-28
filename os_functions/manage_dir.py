import shutil, os, subprocess, pywinauto
import speech_recognition as sr
from core.listen import record_audio
from difflib import SequenceMatcher
import pyautogui
import settings
import time


def get_address():
    app = pywinauto.Application(backend='uia')  # create application object
    app.connect(path="C:\Windows\explorer.exe") # connect to explorer.exe which is windows taskbar instances and other windows elements
    folder = app.window(found_index=1)  # get currently displayed folder because Taskbar is always at index 0
    folder.set_focus()  # bring folder file explorer window to front
    # folder.print_control_identifiers()   # print control identifiers for debug
    wrapper = folder.child_window(auto_id="41477", control_type="Pane")    # get the ID of address bar's parent
    # wrapper.print_control_identifiers()   # print control identifiers for debug
    obj = wrapper.descendants(control_type='ToolBar')[0]    # get first element in elements with control type 'Toolbar'
    obj_name = str(obj)   # convert object name to string
    address = obj_name.replace("uia_controls.ToolbarWrapper - 'Address: ", "").replace("', Toolbar", "")  # remove all unnecessary parts in the string
    print("Folder address: " + address)  # print address string for debug
    settings.location = address


def enter_folder(folder_name):
    app = pywinauto.Application(backend='uia')  # create application object
    app.connect(path="C:\Windows\explorer.exe") # connect to explorer.exe which is windows taskbar instances and other windows elements
    folder = app.window(found_index=1)  # get currently displayed folder because Taskbar is always at index 0
    folder.set_focus()  # bring folder file explorer window to front
    # folder.print_control_identifiers()   # print control identifiers for debug
    try:
        # enter the folder
        folder_wrapper = folder.child_window(title=folder_name, control_type="ListItem")    # get the ID of address bar's parent
        # folder_wrapper.print_control_identifiers()   # print control identifiers for debug
        folder_wrapper.select() # select folder
        pywinauto.keyboard.send_keys('{ENTER}')    # go into folder by simulating enter key
        
        # get address from address bar
        wrapper = folder.child_window(auto_id="41477", control_type="Pane")    # get the ID of address bar's parent
        # wrapper.print_control_identifiers()   # print control identifiers for debug
        obj = wrapper.descendants(control_type='ToolBar')[0]    # get first element in elements with control type 'Toolbar'
        obj_name = str(obj)   # convert object name to string
        address = obj_name.replace("uia_controls.ToolbarWrapper - 'Address: ", "").replace("', Toolbar", "")  # remove all unnecessary parts in the string
        print("Folder address: " + address)  # print address string for debug
        settings.location = address
    except:
        print("Can't find folder with name: " + folder_name)
        # voice_assistant_speak("Sorry, I can't find any folder with name: " + folder_name)


def go_back():
    app = pywinauto.Application(backend='uia')  # create application object
    app.connect(path="C:\Windows\explorer.exe") # connect to explorer.exe which is windows taskbar instances and other windows elements
    folder = app.window(found_index=1)  # get currently displayed folder because Taskbar is always at index 0
    folder.set_focus()  # bring folder file explorer window to front
    # folder.print_control_identifiers()   # print control identifiers for debug
    element = folder.child_window(title="Navigation buttons", control_type="ToolBar")   # get navigation bar elements
    # element.print_control_identifiers()
    element.descendants(control_type="Button")[0].set_focus().click_input(button='left')    # click on go back button
    
    # get address from address bar
    wrapper = folder.child_window(auto_id="41477", control_type="Pane")    # get the ID of address bar's parent
    # wrapper.print_control_identifiers()   # print control identifiers for debug
    obj = wrapper.descendants(control_type='ToolBar')[0]    # get first element in elements with control type 'Toolbar'
    obj_name = str(obj)   # convert object name to string
    address = obj_name.replace("uia_controls.ToolbarWrapper - 'Address: ", "").replace("', Toolbar", "")  # remove all unnecessary parts in the string
    print("Folder address: " + address)  # print address string for debug
    settings.location = address


def go_to_parent_folder():
    app = pywinauto.Application(backend='uia')  # create application object
    app.connect(path="C:\Windows\explorer.exe") # connect to explorer.exe which is windows taskbar instances and other windows elements
    folder = app.window(found_index=1)  # get currently displayed folder because Taskbar is always at index 0
    folder.set_focus()  # bring folder file explorer window to front
    # folder.print_control_identifiers()   # print control identifiers for debug
    element = folder.child_window(auto_id="1001", control_type="ToolBar")   # get navigation bar elements
    # element.print_control_identifiers()
    length = len(element.descendants(control_type="SplitButton"))
    element.descendants(control_type="SplitButton")[length-1].set_focus().click_input(button='left')    # click on parent directory button
    
    # get address from address bar
    wrapper = folder.child_window(auto_id="41477", control_type="Pane")    # get the ID of address bar's parent
    # wrapper.print_control_identifiers()   # print control identifiers for debug
    obj = wrapper.descendants(control_type='ToolBar')[0]    # get first element in elements with control type 'Toolbar'
    obj_name = str(obj)   # convert object name to string
    address = obj_name.replace("uia_controls.ToolbarWrapper - 'Address: ", "").replace("', Toolbar", "")  # remove all unnecessary parts in the string
    print("Folder address: " + address)  # print address string for debug
    settings.location = address




def similar_file(files, raw_dir):
    '''
    Find the directory name with the highest similar ratios with the requested name

    Parameters:
        files(string list): a list of file name (str) in the current directory
        raw_dir(str): raw directory name needed to match

    Returns:
        dir(str): the file name with the most similarity with the raw directory name
    '''
    ratio = 0
    for i in files:
        if ratio < SequenceMatcher(None, i, raw_dir).ratio():
            ratio = SequenceMatcher(None, i, raw_dir).ratio()
            dir = i
    return dir, ratio


def list_file_auto_locate():
    '''
    Search for all the files in a directory (excluding hidden file, file with the '.' in front)
    
    Parameters:
        location(str): current path/directory

    Returns:
        files(string list): a list of file name (str) in the current directory
    '''
    get_address()
    files = [f for f in os.listdir(settings.location) if f[0] != '.']
    print(files)

    return files


def list_file(location):
    '''
    Search for all the files in a directory (excluding hidden file, file with the '.' in front)
    
    Parameters:
        location(str): current path/directory

    Returns:
        files(string list): a list of file name (str) in the current directory
    '''
    files = [f for f in os.listdir(location) if f[0] != '.']
    print(files)

    return files

def delete_file(voice_data):
    '''
    Delete a file at location

    Parameters:
        voice_data(str): the string recorded and recognized from user's voice input
    
    Returns:
        0(bool): failed to delete
        1(bool): delete successfully
    '''
    # voice data -> file name
    raw_dir = voice_data.replace('delete ', '').replace('file', '').replace('folder', '').replace(' ', '')  

    # get address
    get_address()
    # stores all the files s address
    files = list_file(settings.location)

    dir, ratio = similar_file(files, raw_dir)
    
    # create a recognizer object to confirms delete 
    r = sr.Recognizer()
    #r.energy_threshold = settings.energy_threshold
    respond = ''
    while 'yes' not in respond.lower() and 'no' not in respond.lower() or ('yes' in respond.lower() and 'no' in respond.lower()):
        respond, language = record_audio(r, ask="Do you want to delete {}?".format(dir))
    
    if 'no' in respond.lower():
        return 0
    
    # delete various types of files
    path = os.path.join(settings.location, dir)  

    try:
        os.remove(path)
        return 1
    except:    
        shutil.rmtree(path)  
        return 1
    return 0


# def open_file(recognizer, search_term):
#     if search_term.count("open app") > 0:
#         search_term = search_term.replace("open app", "apps:")
#     elif search_term.count("open folder") > 0:
#         search_term = search_term.replace("open folder", "folders:")
#     elif search_term.count("open document") > 0:
#         search_term = search_term.replace("open document", "documents: ")
#     elif search_term.count("open image") > 0 or search_term.count("open photo") > 0:
#         search_term = search_term.replace("open image", "photos: ")
#     elif search_term.count("open music") > 0:
#         search_term = search_term.replace("open music", "music: ")
#     elif search_term.count("open video") > 0:
#         search_term = search_term.replace("open video", "videos: ")
#     print("Search: " + search_term)
#     if settings.platform == 'Windows':
#         pyautogui.hotkey("win", "s")
#         time.sleep(0.5)
#         pyautogui.write(search_term)
#         confirmation, language = record_audio(recognizer, language='en', ask='Is this the correct file?')
#         if confirmation == "no":
#             open_file_ask(recognizer)
#         elif confirmation == "yes":
#             pyautogui.press("enter")


# def open_file_ask(recognizer):
#     while True:
#         search_term, language = record_audio(recognizer, language='en', ask='Which file would you like to open?')
#         if search_term.count("app") > 0:
#             search_term = search_term.replace("app", "apps:")
#         elif search_term.count("folder") > 0:
#             search_term = search_term.replace("folder", "folders:")
#         elif search_term.count("documents") > 0:
#             search_term = search_term.replace("documents", "documents: ")
#         elif search_term.count("document") > 0:
#             search_term = search_term.replace("document", "documents: ")
#         elif search_term.count("image") > 0 or search_term.count("open photo") > 0:
#             search_term = search_term.replace("image", "photos: ")
#         elif search_term.count("music") > 0:
#             search_term = search_term.replace("music", "music: ")
#         elif search_term.count("video") > 0:
#             search_term = search_term.replace("video", "videos: ")
#         print("Search: " + search_term)
#         if settings.platform == 'Windows':
#             pyautogui.hotkey("win", "s")
#             time.sleep(0.5)
#             pyautogui.write(search_term)
#             confirmation, language = record_audio(recognizer, language='en', ask='Is this the correct file?')
#             if confirmation == "no":
#                 continue
#             elif confirmation == "yes":
#                 pyautogui.press("enter")
#                 break


def open_file_explorer():
    pyautogui.hotkey("win", "s")
    time.sleep(0.5)
    pyautogui.write("File explorer")
    time.sleep(0.5)
    pyautogui.press("enter")


def open_file(voice_data):
    '''
    Open a file at location

    Parameters:
        voice_data(str): the string recorded and recognized from user's voice input
    
    Returns:
        0(bool): failed to open
        1(bool): opened successfully
    '''
    get_address()
    # voice data -> file name
    raw_dir = voice_data.replace('open ', '').replace('file', '').replace('folder', '').replace(' ', '')  

    files = list_file(settings.location)

    dir, similarity = similar_file(files, raw_dir)

    # create a recognizer object to confirms open
    if similarity < 0.5:
        print(similarity, dir)
        r = sr.Recognizer()
        #r.energy_threshold = settings.energy_threshold
        respond = ''
        while 'yes' not in respond.lower() and 'no' not in respond.lower() or ('yes' in respond.lower() and 'no' in respond.lower()):
            respond, language = record_audio(r, ask="Do you want to open {}?".format(dir))
        
        if 'no' in respond.lower():
            return 0
    
    
    # open various types of files
    path = os.path.join(settings.location, dir)  

    # try to open with os
    if settings.platform == 'Windows':
        os.startfile(path)
        return 1
    elif settings.platform == 'Darwin':
        subprocess.call(['open', path])
        return 1


def create_folder(voice_data):
    '''
    Create a folder at location

    Parameters:
        voice_data(str): the string recorded and recognized from user's voice input
    
    Returns:
        0(bool): failed to create
        1(bool): created successfully

    '''
    get_address()
    raw_dir = voice_data.replace('create ', '').replace('file', '').replace('folder', '').replace(' ', '')  

    try:
        os.mkdir(settings.location + '/' + raw_dir)
        return 1
    except FileExistsError as exc:
        print(exc)
        return 0

def file_info(voice_data):
    '''
    Open file's information summary window

    Parameters:
        voice_data(str): the string recorded and recognized from user's voice input
    
    Returns:
        0(bool): failed to open
        1(bool): opened successfully
    '''

    if settings.platform == 'Darwin':
        pyautogui.hotkey("cmd", "i")
    elif settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "i")

def copy(voice_data):
    '''
    simulate ctrl + c / cmd + c

    Parameters:
        voice_data(str): the string recorded and recognized from user's voice input
    
    Returns:
        0(bool): failed to copy
        1(bool): copied successfully
    '''

    if settings.platform == 'Darwin':
        pyautogui.hotkey("cmd", "c")
    elif settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "c")

def paste(voice_data):
    '''
    simulate ctrl + v / cmd + v

    Parameters:
        voice_data(str): the string recorded and recognized from user's voice input
    
    Returns:
        0(bool): failed to paste
        1(bool): pasted successfully
    '''
    if settings.platform == 'Darwin':
        pyautogui.hotkey("cmd", "v")
    elif settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "v")

def cut(voice_data):
    '''
    simulate ctrl + x / cmd + x

    Parameters:
        voice_data(str): the string recorded and recognized from user's voice input
    
    Returns:
        0(bool): failed to cut
        1(bool): cut successfully
    '''
    if settings.platform == 'Darwin':
        pyautogui.hotkey("cmd", "x")
    elif settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "x")

def undo(voice_data):
    '''
    simulate ctrl + z / cmd + z

    Parameters:
        voice_data(str): the string recorded and recognized from user's voice input
    
    Returns:
        0(bool): failed to undo
        1(bool): undone successfully
    '''
    if settings.platform == 'Darwin':
        pyautogui.hotkey("cmd", "z")
    elif settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "z")

def redo(voice_data):
    '''
    simulate ctrl + y / cmd + y

    Parameters:
        voice_data(str): the string recorded and recognized from user's voice input
    
    Returns:
        0(bool): failed to redo
        1(bool): redone successfully
    '''
    if settings.platform == 'Darwin':
        pyautogui.hotkey("cmd", "y")
    elif settings.platform == 'Windows':
        pyautogui.hotkey("ctrl", "y")



if __name__ == '__main__':
    # scroll_down()
    redo()
    undo()
    cut()
    paste()
    copy()
    file_info()
    create_folder()
    open_file()
    delete_file()
    list_file()
    similar_file()
    enter_folder()
    get_address()
