# settings for global variables
import platform

platform = platform.system()
energy_threshold = 2000 # change threshold to eliminate background noise
location =''
language = 'en'
def init():
    global energy_threshold, location, platform, language
