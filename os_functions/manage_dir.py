import shutil, os, imghdr, subprocess, time, pyautogui
import speech_recognition as sr
from core.speak import voice_assistant_speak
from core.listen import record_audio
from difflib import SequenceMatcher
from pynput.keyboard import Controller
from pynput import keyboard
import settings

kb = Controller

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

    dir = similar_file(files, raw_dir)
    
    # create a recognizer object to confirms delete 
    r = sr.Recognizer()
    r.energy_threshold = settings.energy_threshold
    respond = ''
    while 'yes' not in respond.lower() and 'no' not in respond.lower() or ('yes' in respond.lower() and 'no' in respond.lower()):
        respond, language = record_audio(r, ask="Do you want to delete {}?".format(dir))
    
    if 'no' in respond.lower():
        return 0
    
    # delete various type of file 
    path = os.path.join(location, dir)  

    # try to delete with os.remove
    try:
        os.remove(path)
        return 1
    except:
        pass
    # delete a folder and all of its contents with shutil
    shutil.rmtree(path)  
    return 1


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
        r.energy_threshold = settings.energy_threshold
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

    try:
        kb.press(keyboard.Key.cmd)
        kb.press('i')
        time.sleep(0.1)
        kb.release(keyboard.Key.cmd)
        kb.release('i')
        return 1
    except Exception:
        return 0

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
    r.energy_threshold = settings.energy_threshold
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