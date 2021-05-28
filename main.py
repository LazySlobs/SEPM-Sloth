import multiprocessing
import sys

from PySide6 import QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# IMPORT UIS
from gui.ui_splash_screen import Ui_SplashScreen
from gui.widgets import CircularProgress
from core.listen import record_audio
from core.proccess_respond import respond
from core.speak import voice_assistant_speak
import speech_recognition as sr
import threading

# GLOBALS
counter = 0

def calibrate(source, recognizer):
    recognizer.adjust_for_ambient_noise(source, duration=1)
    recognizer.energy_threshold += 250

class VoiceWorker(QtCore.QObject):
    textChanged = QtCore.Signal(str)
    sgnFinished = QtCore.Signal()

    # constructor
    def __init__(self, parent):
        QObject.__init__(self, parent)
        self._mutex = QMutex()
        self._running = True
    
    # Stop signal
    @QtCore.Slot()
    def stop(self):
        # print('switching while loop condition to false')  # for debug
        self._mutex.lock()
        self._running = False
        self._mutex.unlock()

    # Running signal
    def running(self):
        try:
            self._mutex.lock()
            return self._running
        finally:
            self._mutex.unlock()

    # Voice worker with binding text
    @QtCore.Slot(str)
    def start(self):
        r1 = sr.Recognizer() # create a recognizer object to recognize texts
        r2 = sr.Recognizer() # create a recognizer object to respond
        WAKE = "wake up"
        while self.running():
            # speak if the ask variable is a string
            with sr.Microphone() as source:
                # adjust for ambient noise
                print("Calibrating...")
                self.textChanged.emit("Calibrating...")
                calibrate(source, r1)

                # starts to listen for keyword
                print("Listening for keyword...")
                self.textChanged.emit("Listening for keyword...")
                audio = r1.listen(source)
                listen_for_keyword = ""
                try:
                    listen_for_keyword = r1.recognize_google(audio)
                    # listen_for_keyword = input("type keyword: ")   # for debug
                except sr.UnknownValueError:
                    continue
                except sr.RequestError:
                    voice_assistant_speak("Sorry, my speech service is down")
                    continue
                except:
                    print("Something went wrong.")
                    continue

                # keyword heard, wake up the voice assistant
                if listen_for_keyword.count(WAKE) > 0:
                    print("Sloth is awake...")
                    self.textChanged.emit("Sloth Voice Assistant is awake!")
                    voice_assistant_speak("How can I help you?")

                    while True:
                        self.textChanged.emit("Waiting for your voice input...")
                        voice_data, language = record_audio(r1)
                        # voice_data = input("type voice data: ")   # for debug
                        # language = "en"   # for debug
                        # if user tells program to stop
                        if  "go to sleep" in voice_data or "go back to sleep" in voice_data:
                            self.textChanged.emit("Sloth is going to sleep \n")
                            break

                        self.textChanged.emit("You said: \n" + voice_data)
                        print("Voice data: " + voice_data)  # print user's voice data
                        respond(r2, voice_data, language=language)  # respond to user's voice data
                elif "exit" in listen_for_keyword:
                    self.textChanged.emit("Program is closing \n")
                    break
        self.sgnFinished.emit()


# MAIN WINDOW
class MainWindow(QMainWindow):
    # constructor
    def __init__(self, parent):
        QMainWindow.__init__(self, parent)

        icon = QIcon("gui/gui_qt_creator/images/Logo.png")
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setVisible(True)
        self.hide()
        # explicitly show the tray-icon
        self.tray.show()

        # Thread initialize
        self._thread = None
        self._worker = None

        # Screen set up
        self.screen = app.primaryScreen()
        self.rect = self.screen.availableGeometry()
        self.setGeometry(0,self.rect.height()*0.8,self.rect.width()*0.2,self.rect.height()*0.2)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        # REMOVE TITLE BAR
        self.setWindowTitle("Lazy Sloth Voice Assistant")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(40, 42, 54);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.centralwidget)
        # self.worker.textChanged.connect(self.title.setText)
        self.title.setMinimumSize(QSize())
        self.title.setStyleSheet(u"QLabel{\n"
                            "	color: rgb(255, 255, 255);\n"
                            "	border-radius: 12px;\n"
                            "   font: 16pt \"Segoe UI\";\n"
                            "}")
        self.title.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.title)
        self.setCentralWidget(self.centralwidget)

    def toggle(self, enable):
        if enable:
            if not self._thread:
                self._thread = QThread()

            self._worker = VoiceWorker(None)
            self._worker.moveToThread(self._thread)
            self._worker.textChanged.connect(self.title.setText)
            self._worker.sgnFinished.connect(self.on_worker_done)

            self._thread.started.connect(self._worker.start)
            self._thread.start()
        else:
            print("Stopping the Voice worker object")
            self._worker.stop()

    @QtCore.Slot()
    def on_worker_done(self):
        print("Voice worker's job finished")
        self._thread.quit()
        self._thread.wait()
        app.quit()



class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)


        # REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # IMPORT CIRCULAR PROGRESS
        self.progress = CircularProgress()
        self.progress.width = 270
        self.progress.height = 270
        self.progress.value = 0
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.move(15, 15)
        self.progress.font_size = 40
        self.progress.add_shadow(True)
        self.progress.bg_color = QColor(68, 71, 90, 140)
        self.progress.setParent(self.ui.centralwidget)
        self.progress.show()

        # ADD DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.setGraphicsEffect(self.shadow)

        # QTIMER
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(30)

        self.show()

    # UPDATE PROGRESS BAR
    def update(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.progress.set_value(counter)

        # CLOSE SPLASH SCREEN AND OPEN MAIN APP
        if counter >= 100:
            # STOP TIMER
            self.timer.stop()

            #
            # SHOW MAIN WINDOW
            self.main = MainWindow(None)
            self.main.show()
            self.main.toggle(True)

            #
            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


if __name__ == "__main__":
    multiprocessing.freeze_support()
    # multiprocessing.set_start_method("spawn")
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    app.setQuitOnLastWindowClosed(True) # close app when the GUI is closed
    window = SplashScreen()
    sys.exit(app.exec_())
