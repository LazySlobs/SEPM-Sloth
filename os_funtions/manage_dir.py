import shutil, os
import speech_recognition as sr
from core.speak import voice_assistant_speak
from core.listen import record_audio
from difflib import SequenceMatcher

def delete_file(voice_data, location='/Users/bao/Desktop'):
    raw_dir = voice_data.replace('delete ', '').replace('file', '').replace('folder', '').replace(' ', '')

    files = [f for f in os.listdir(location)]

    ratio = 0
    dir = ''
    for i in files:
        if ratio < SequenceMatcher(None, i, raw_dir).ratio():
            ratio = SequenceMatcher(None, i, raw_dir).ratio()
            dir = i
    
    r = sr.Recognizer()
    r.energy_threshold = 2000
    
    respond = ''
    while 'yes' not in respond.lower() and 'no' not in respond.lower() or ('yes' in respond.lower() and 'no' in respond.lower()):
        respond, language = record_audio(r, ask="Do you want to delete {}?".format(dir))

    if 'no' in respond.lower():
        return
        
    path = os.path.join(location, dir)  

    shutil.rmtree(path)  

