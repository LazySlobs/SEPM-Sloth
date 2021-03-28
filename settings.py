# settings for global variables
import platform, os

platform = platform.system()
energy_threshold = 2000 # change threshold to eliminate background noise
location ='/Users/bao/Desktop'
def init():
    global energy_threshold, location, platform
