import sys
import time

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
# GLOBALS
counter = 0

class VoiceWorker(QtCore.QObject):
    textChanged = QtCore.Signal(str)
    sgnFinished = QtCore.Signal()
    def __init__(self, parent):
        QObject.__init__(self, parent)
        self._mutex = QMutex()
        self._running = True
    #Stop signal
    @QtCore.Slot()
    def stop(self):
        print('switching while loop condition to false')
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
        r1 = sr.Recognizer()  # create a recognizer object to recognize texts
        # r1.energy_threshold = settings.energy_threshold
        r2 = sr.Recognizer()  # create a recognizer object to
        WAKE = "wake up"
        wake = False
        while self.running():
            # speak if the ask variable is a string
            with sr.Microphone() as source:
                # adjust for ambient noise
                print("Calibrating...")
                self.textChanged.emit("Calibrating...")
                r1.adjust_for_ambient_noise(source, duration=1)
                r1.energy_threshold += 250

                # starts to listen for keyword
                print("Listening for keyword...")
                self.textChanged.emit("Listening for keyword...")
                audio = r1.listen(source)
                listen_for_keyword = ""
                try:
                    listen_for_keyword = r1.recognize_google(audio)
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
                    wake = True
                    print("Sloth is awake...")
                    self.textChanged.emit("Sloth is awake!")
                    self.textChanged.emit("I am Sloth Voice Assistant")
                    voice_assistant_speak("How can I help you?")
                    self.textChanged.emit("Waiting for your voice input...")

                    if (wake):
                        while True:
                            language = "en"
                            self.textChanged.emit("Waiting Command")
                            voice_data, language = record_audio(r1)
                            # if user tells program to stop
                            if  "exit" in voice_data:
                                # Break here to get out 2nd loop
                                wake = False
                                print("You finally out of 2nd loop")
                                self.textChanged.emit("Program is closing \n")
                                break
                            print("Voice data: " + voice_data)  # print user's voice data
                            self.textChanged.emit("You said: \n" + voice_data)
                            time.sleep(1)
                            self.textChanged.emit("Executing")
                            respond(r2, voice_data, language=language)  # respond to user's voice data
                        # Break here to send signal to close app
                        print("You finally out of 1nd loop")
                        break
                elif "exit" in listen_for_keyword:
                    self.textChanged.emit("Program is closing \n")
                    print("You finally out of 1nd loop")
                    break
        print("get out of loop")
        self.sgnFinished.emit()


# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self, parent):
        QMainWindow.__init__(self, parent)

        icon = QIcon("gui/gui_qt_creator/images/Logo.png")
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setVisible(True)
        self.setWindowIcon(icon)

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
            print('stopping the Voice worker object')
            self._worker.stop()

    @QtCore.Slot()
    def on_worker_done(self):
        print('Voice workers job was interrupted ')
        self._thread.quit()
        self._thread.wait()
        app.quit()



class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.voiceRecognizer = sr.Recognizer()

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
    voiceRecognizer = sr.Recognizer()
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("gui/gui_qt_creator/images/Icon.ico"))
    app.setQuitOnLastWindowClosed(False)
    window = SplashScreen()
    sys.exit(app.exec_())
