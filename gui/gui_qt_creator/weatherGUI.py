# This Python file uses the following encoding: utf-8
import sys
import os
import psutil
import GPUtil
from miscellaneous_functions import weather
from PySide2.QtGui import QGuiApplication, QIcon
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, Slot, Signal, QTimer

# CLASS MAIN WINDOW
class MainWindow(QObject):
    def __init__(self):
        QObject.__init__(self)

        # AUTO REFRESH / DYNAMIC INFOS
        # self.city_name = city_name
        timer = QTimer(self)
        timer.start(1000)
        timer.timeout.connect(lambda: self.setDynamicInfo())




    # GET RESULTS FROM API
    results_weather = weather.Current_Weather("Hanoi").display_weather_results()

    # SHOW PERCENTAGE
    showPercentage = False

    # PERCENTAGE / DYNAMIC
    percentageCPU = Signal(float)
    percentageRAM = Signal(float)
    percentageGPU = Signal(float)
    cpuFrequencyCurrentInfo = Signal(float)
    ramAvailableInfo = Signal(str)
    ramUsedInfo = Signal(str)
    # vramFreeInfo = Signal(str)
    # vramUsedInfo = Signal(str)
    gpuTempInfo = Signal(str)

    # STATIC INFO
    cpuInfo = Signal(str)
    cpuPhysicalCoresInfo = Signal(str)
    cpuTotalCoresInfo = Signal(str)
    cpuFrequencyMaxInfo = Signal(float)
    cpuFrequencyMinInfo = Signal(float)
    ramTotalInfo = Signal(str)
    gpuModelInfo = Signal(str)
    vramTotalInfo = Signal(str)

    # SET DYNAMIC INFO
    def setDynamicInfo(self):
        # FORMAT SIZES
        def get_size(bytes, suffix="B"):
            factor = 1024
            for unit in ["", "M", "G", "T", "P"]:
                if bytes < factor:
                    return f"{bytes:.2f}{unit}{suffix}"
                bytes /= factor

        if self.showPercentage:
            # SYSTEM VARS
            svmen = psutil.virtual_memory()
            gpus = GPUtil.getGPUs()
            cpufreq = psutil.cpu_freq()

            # CIRCULAR PROGRESS BAR
            self.percentageCPU.emit(int(self.results_weather[0]))
            self.percentageRAM.emit(int(self.results_weather[1]))
            self.percentageGPU.emit(self.results_weather[2])

            # CPU FREQUENCY
            self.cpuFrequencyCurrentInfo.emit(self.results_weather[0])

            # RAM USAGE
            self.ramAvailableInfo.emit(int(self.results_weather[5]))
            self.ramUsedInfo.emit(int(self.results_weather[6]))

            # GPU INFO
            # self.vramFreeInfo.emit(f"{gpus[0].memoryFree}MB")
            # self.vramUsedInfo.emit(f"{gpus[0].memoryUsed}MB")
            self.gpuTempInfo.emit(self.results_weather[11])

    # SET STATIC INFO
    @Slot()
    def setStaticInfo(self):
        # FORMAT SIZES
        def get_size(bytes, suffix="B"):
            factor = 1024
            for unit in ["", "M", "G", "T", "P"]:
                if bytes < factor:
                    return f"{bytes:.2f}{unit}{suffix}"
                bytes /= factor

        # SYSTEM VARS
        svmen = psutil.virtual_memory()
        gpus = GPUtil.getGPUs()
        cpufreq = psutil.cpu_freq()

        # CPU INFO
        self.cpuInfo.emit(self.results_weather[3])
        self.cpuPhysicalCoresInfo.emit(psutil.cpu_count(logical=False))
        self.cpuTotalCoresInfo.emit(psutil.cpu_count(logical=True))
        self.cpuFrequencyMaxInfo.emit(self.results_weather[5])
        self.cpuFrequencyMinInfo.emit(self.results_weather[6])

        # RAM INFO
        self.ramTotalInfo.emit(get_size(svmen.total))

        # GPU INFO
        self.gpuModelInfo.emit(self.results_weather[3])
        self.vramTotalInfo.emit(self.results_weather[10])

        # SHOW PERCENTAGE
        def showValues():
            self.showPercentage = True

        QTimer.singleShot(2000, showValues)



app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()

# GET CONTEXT
main = MainWindow()
engine.rootContext().setContextProperty("backend", main)

# SET ICON
app.setWindowIcon(QIcon("icon.ico"))

# LOAD QML
engine.load(os.path.join(os.path.dirname(__file__), "qml/pages/weather.qml"))

if not engine.rootObjects():
    sys.exit(-1)
sys.exit(app.exec_())
