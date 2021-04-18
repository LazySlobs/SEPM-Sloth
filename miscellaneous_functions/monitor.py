from core.speak import voice_assistant_speak
import psutil

# prints CPU %
def display_cpu_used():
    print("CPU usage percentage: " + str(psutil.cpu_percent(1, False)) + "%")


# print used RAM % and available RAM %
def display_ram_used():
    print("Memory usage percentage: " + str(psutil.virtual_memory().percent) + "%")
    print("Available memory percentage: " + str(int(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)) + "%")


# print used CPU %, used RAM %, and available RAM %
def display_cpu_and_ram_used():
    print("CPU usage percentage: " + str(psutil.cpu_percent(1, False)) + "%")
    print("Memory usage percentage: " + str(psutil.virtual_memory().percent) + "%")
    print("Available memory percentage: " + str(int(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)) + "%")


# say used CPU and RAM %
def tell_cpu_and_ram_used():
    voice_assistant_speak("The CPU usage percentage is " + str(psutil.cpu_percent(1, False)) + "%")
    voice_assistant_speak("Memory usage percentage is " + str(psutil.virtual_memory().percent) + "%")


# say used CPU %
def tell_cpu_used():
    voice_assistant_speak("The CPU usage percentage is " + str(psutil.cpu_percent(1, False)) + "%")


# say used RAM %
def tell_ram_used():
    voice_assistant_speak("Memory usage percentage is " + str(psutil.virtual_memory().percent) + "%")


# say available RAM %
def tell_available_ram():
    voice_assistant_speak("Available memory percentage is " + str(int(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)) + "%")

