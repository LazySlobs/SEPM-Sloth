import sys
import os

import psutil
import GPUtil
import cpuinfo
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, Slot, Signal, QTimer

# CLASS MAIN WINDOW
class SystemWindow(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.app = QGuiApplication()
        # AUTO REFRESH / DYNAMIC INFOS
        timer = QTimer(self)
        timer.start(1000)
        timer.timeout.connect(lambda: self.setDynamicInfo())

        # AUTO DISPLAY
        self.show_UI()

    # SHOW PERCENTAGE
    showPercentage = False

    # PERCENTAGE / DYNAMIC
    percentageCPU = Signal(float)
    percentageRAM = Signal(float)
    percentageGPU = Signal(float)
    cpuFrequencyCurrentInfo = Signal(str)
    ramAvailableInfo = Signal(str)
    ramUsedInfo = Signal(str)
    vramFreeInfo = Signal(str)
    vramUsedInfo = Signal(str)
    gpuTempInfo = Signal(str)

    # STATIC INFO
    cpuInfo = Signal(str)
    cpuPhysicalCoresInfo = Signal(str)
    cpuTotalCoresInfo = Signal(str)
    cpuFrequencyMaxInfo = Signal(str)
    cpuFrequencyMinInfo = Signal(str)
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
            self.percentageCPU.emit(psutil.cpu_percent())
            self.percentageRAM.emit(svmen.percent)
            self.percentageGPU.emit(float(gpus[0].load*100))

            # CPU FREQUENCY
            self.cpuFrequencyCurrentInfo.emit(f"{cpufreq.current:.2f}Mhz")

            # RAM USAGE
            self.ramAvailableInfo.emit(get_size(svmen.available))
            self.ramUsedInfo.emit(get_size(svmen.used))

            # GPU INFO
            self.vramFreeInfo.emit(f"{gpus[0].memoryFree}MB")
            self.vramUsedInfo.emit(f"{gpus[0].memoryUsed}MB")
            self.gpuTempInfo.emit(f"{gpus[0].temperature} ºC")

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
        self.cpuInfo.emit(cpuinfo.get_cpu_info()['brand_raw'])
        self.cpuPhysicalCoresInfo.emit(str(psutil.cpu_count(logical=False)))
        self.cpuTotalCoresInfo.emit(str(psutil.cpu_count(logical=True)))
        self.cpuFrequencyMaxInfo.emit(f"{cpufreq.max:.2f}Mhz")
        self.cpuFrequencyMinInfo.emit(f"{cpufreq.min:.2f}Mhz")

        # RAM INFO
        self.ramTotalInfo.emit(get_size(svmen.total))

        # GPU INFO
        self.gpuModelInfo.emit(gpus[0].name)
        self.vramTotalInfo.emit(f"{gpus[0].memoryTotal}MB")

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
            engine.load(os.path.join(os.path.dirname(__file__), "qml/system.qml"))

            # AUTO CLOSE
            timer2 = QTimer(self)
            timer2.start(10000)
            timer2.timeout.connect(lambda: sys.exit())
            if not engine.rootObjects():
                sys.exit(-1)
            sys.exit(self.app.exec_())



if __name__ == '__main__':
    SystemWindow()


