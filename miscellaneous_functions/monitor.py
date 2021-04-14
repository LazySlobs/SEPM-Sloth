import psutil

# prints CPU %
def displayCPU():
    print("CPU percentage: " + str(psutil.cpu_percent(1, False)) + "%")


# print used RAM % and available RAM %
def displayRAM():
    print("Available memory: " + str(psutil.virtual_memory().percent) + "%")
    print("Available memory: " + str(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total) + "%")


def displayCPURAM():
    print("CPU percentage: " + str(psutil.cpu_percent(1, False)) + "%")
    print("Available memory: " + str(psutil.virtual_memory().percent) + "%")
    print("Available memory: " + str(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total) + "%")
