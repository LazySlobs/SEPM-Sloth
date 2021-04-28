import shutil, os, imghdr, subprocess, time, pyautogui
import speech_recognition as sr
from core.speak import voice_assistant_speak
from core.listen import record_audio
from difflib import SequenceMatcher
from pynput.keyboard import Controller
from pynput import keyboard
import settings

kb = Controller()

def key_combo(combo):
    print('executing combo')
    try:
        for key in combo:
            kb.press(key)
            time.sleep(0.1)
        for key in combo:
            kb.release(key)
            time.sleep(0.1)
        return 1
        print('success')
    except Exception as e:
        print(e)
        return 0

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

def list_file(location):
    '''
    Search for all the file in current directory (excluding hidden file, file with the '.' in front)
    
    Parameters:
        location(str): current path/directory

    Returns:
        files(string list): a list of file name (str) in the current directory
    '''

    files = [f for f in os.listdir(location) if f[0] != '.']
    print(files)

    return files

def delete_file(voice_data, location):
    '''
    Delete a file at default location(desktop)

    Parameters:
        voice_data(str): the string recorded and recognized from user's voice input
        location(str): current path/directory
    
    Returns:
        0(bool): failed to delete
        1(bool): delete successfully
    '''

    # voice data -> file name
    raw_dir = voice_data.replace('delete ', '').replace('file', '').replace('folder', '').replace(' ', '')  

    files = list_file(location)

    dir, ratio = similar_file(files, raw_dir)
    
    # create a recognizer object to confirms delete 
    r = sr.Recognizer()
    #r.energy_threshold = settings.energy_threshold
    respond = ''
    while 'yes' not in respond.lower() and 'no' not in respond.lower() or ('yes' in respond.lower() and 'no' in respond.lower()):
        respond, language = record_audio(r, ask="Do you want to delete {}?".format(dir))
    
    if 'no' in respond.lower():
        return 0
    
    # delete various type of file 
    path = os.path.join(location, dir)  

    try:
        os.remove(path)
        return 1
    except:    
        shutil.rmtree(path)  
        return 1
    return 0

def open_file(voice_data, location):
    '''
    Open a file at default location(desktop)

    Parameters:
        voice_data(str): the string recorded and recognized from user's voice input
        location(str): current path/directory
    
    Returns:
        0(bool): failed to open
        1(bool): opened successfully
    '''

    # voice data -> file name
    raw_dir = voice_data.replace('open ', '').replace('file', '').replace('folder', '').replace(' ', '')  

    files = list_file(location)

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
    
    
    # open various type of file 
    path = os.path.join(location, dir)  

    # try to open with os
    if settings.platform == 'Windows':
        os.startfile(path)
        return 1
    elif settings.platform == 'Darwin':
        subprocess.call(['open', path])
        return 1

def create_file(voice_data, location):
    '''
    Create a file at default location(desktop)

    Parameters:
        voice_data(str): the string recorded and recognized from user's voice input
        location(str): current path/directory
    
    Returns:
        0(bool): failed to create
        1(bool): created successfully

    '''

    raw_dir = voice_data.replace('create ', '').replace('file', '').replace('folder', '').replace(' ', '')  

    try:
        os.mkdir(location + '/' + raw_dir)
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
        key_combo([keyboard.Key.cmd, 'i'])
    elif settings.platform == 'Windows':
        key_combo([keyboard.Key.ctrl, 'i'])

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
        key_combo([keyboard.Key.cmd, 'c'])
    elif settings.platform == 'Windows':
        key_combo([keyboard.Key.ctrl, 'c'])

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
        key_combo([keyboard.Key.cmd, 'v'])
    elif settings.platform == 'Windows':
        key_combo([keyboard.Key.ctrl, 'v'])

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
        key_combo([keyboard.Key.cmd, 'x'])
    elif settings.platform == 'Windows':
        key_combo([keyboard.Key.ctrl, 'x'])

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
        key_combo([keyboard.Key.cmd, 'z'])
    elif settings.platform == 'Windows':
        key_combo([keyboard.Key.ctrl, 'z'])

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
        key_combo([keyboard.Key.cmd, 'y'])
    elif settings.platform == 'Windows':
        key_combo([keyboard.Key.ctrl, 'y'])

def scroll_down(voice_data):
    '''
    Scroll down 

    Parameters:
        voice_data(str): the string recorded and recognized from user's voice input

    Returns:
        0(bool): failed to scroll down
        1(bool): scrolled down successfully
    '''

    r = sr.Recognizer()
    #r.energy_threshold = settings.energy_threshold
    stop = False
    audio = ''
    stop = r.listen_in_background(sr.Microphone())
    try:
        while not stop:
            pyautogui.scroll(-1)
            
            
            
            stop_audio = r.recognize_google(audio, language=settings.language)
        return 1
    except Exception:
        return 0


def auto_scroll():
    r1 = sr.Recognizer()  # create a recognizer object to recognize texts
    r1.energy_threshold = 4000
    while True:
        pyautogui.scroll(1000)
        navigate_data, language = record_audio(r1)
        print(navigate_data)
        if "enter" in navigate_data:
            break


auto_scroll()