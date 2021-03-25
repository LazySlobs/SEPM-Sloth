import shutil, os, imghdr
import speech_recognition as sr
from core.speak import voice_assistant_speak
from core.listen import record_audio
from difflib import SequenceMatcher
import settings

def delete_file(voice_data, location='/Users/bao/Desktop'):
    '''
    Delete a file at default location(desktop)

    Parameters:
        voice_data(str): the string recorded and recognized from user's voice input

        Options:
            location(str): current path/directory
    
    Returns:
        0(bool): failed to delete
        1(bool): delete successfully
    '''


    # voice data -> file name
    raw_dir = voice_data.replace('delete ', '').replace('file', '').replace('folder', '').replace(' ', '')  

    # search for all the file in current directory (excluding hidden file, file with the '.' in front)
    files = [f for f in os.listdir(location) if f[0] != '.']
    print(files)
    ratio = 0
    dir = ''    

    # find the directory name with the highest similar ratios with the requested name
    for i in files:
        if ratio < SequenceMatcher(None, i, raw_dir).ratio():
            ratio = SequenceMatcher(None, i, raw_dir).ratio()
            dir = i
    
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


