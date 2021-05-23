import sys
import os
import time

from miscellaneous_functions import weather
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, Slot, Signal, QTimer


# CLASS MAIN WINDOW
class WeatherWindow(QObject):
    def __init__(self, city):
        QObject.__init__(self)
        self.app = QGuiApplication()
        self.city = city
        # GET RESULTS FROM API
        self.results_weather = weather.Current_Weather(self.city).display_weather_results()

        # AUTO REFRESH / DYNAMIC INFOS
        timer = QTimer(self)
        timer.start(1000)
        timer.timeout.connect(lambda: self.setDynamicInfo())
        self.show_UI()


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
            # CIRCULAR PROGRESS BAR
            self.percentageCPU.emit(int(self.results_weather[0]))
            self.percentageRAM.emit(int(self.results_weather[1]))
            self.percentageGPU.emit(self.results_weather[2])

            # CPU FREQUENCY
            self.cpuFrequencyCurrentInfo.emit(self.results_weather[0])

            # RAM USAGE
            self.ramAvailableInfo.emit(str(self.results_weather[5]))
            self.ramUsedInfo.emit(str(self.results_weather[6]))

            # GPU INFO
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

        # CPU INFO
        self.cpuInfo.emit(str(self.results_weather[3]))
        self.cpuPhysicalCoresInfo.emit(str(self.results_weather[2]))
        self.cpuTotalCoresInfo.emit(str(self.results_weather[1]))
        self.cpuFrequencyMaxInfo.emit(self.results_weather[5])
        self.cpuFrequencyMinInfo.emit(self.results_weather[6])

        # RAM INFO
        self.ramTotalInfo.emit(str(self.results_weather[7]) + "m/s")

        # GPU INFO
        self.gpuModelInfo.emit(self.results_weather[3])
        self.vramTotalInfo.emit(self.results_weather[10])

        # SHOW PERCENTAGE
        def showValues():
            self.showPercentage = True

        QTimer.singleShot(2000, showValues)

    def show_UI(self):
            # app = QGuiApplication(sys.argv)
            engine = QQmlApplicationEngine()

            # GET CONTEXT
            engine.rootContext().setContextProperty("backend", self)

            # LOAD QML
            engine.load(os.path.join(os.path.dirname(__file__), "qml/pages/weather.qml"))

            # AUTO CLOSE
            timer2 = QTimer(self)
            timer2.start(7000)
            timer2.timeout.connect(lambda: sys.exit())
            if not engine.rootObjects():
                sys.exit(-1)
            sys.exit(self.app.exec_())


if __name__ == "__main__":
    WeatherWindow()

