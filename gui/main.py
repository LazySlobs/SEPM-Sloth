import sys

from PySide6 import QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# IMPORT UIS
from ui_splash_screen import Ui_SplashScreen
from widgets import CircularProgress
from core.listen import record_audio
from core.speak import voice_assistant_speak
# from core.proccess_respond import respond
import speech_recognition as sr
# GLOBALS
counter = 0

class VoiceWorker(QtCore.QObject):
    textChanged = QtCore.Signal(str)

    @QtCore.Slot(str)
    def test(self):
        r1 = sr.Recognizer()  # create a recognizer object to recognize texts
        # r1.energy_threshold = settings.energy_threshold
        r2 = sr.Recognizer()  # create a recognizer object to
        WAKE = "wake up"
        wake = False
        while True:
            # speak if the ask variable is a string
            with sr.Microphone() as source:
                # adjust for ambient noise
                print("Calibrating...")
                r1.adjust_for_ambient_noise(source, duration=1)
                r1.energy_threshold += 250

                # starts to listen for keyword
                print("Listening for keyword...")
                audio = r1.listen(source)
                listen_for_keyword = ""
                try:
                    listen_for_keyword = r1.recognize_google(audio)
                    self.textChanged.emit(listen_for_keyword)
                except sr.UnknownValueError:
                    continue
                except sr.RequestError:
                    voice_assistant_speak("Sorry, my speech service is down")
                    continue
                except:
                    print("Something went wrong.")
                    continue
                print("listen_for_keyword = " + listen_for_keyword)
                self.textChanged.emit(listen_for_keyword)

                # keyword heard, wake up the voice assistant
                if listen_for_keyword.count(WAKE) > 0:
                    wake = True
                    print("Sloth is awake...")
                    voice_assistant_speak("How can I help you?")

                    if (wake):
                        while True:
                            # listen to users
                            voice_data, language = record_audio(r1)
                            # if user tells program to stop
                            if voice_data.lower() == "go to sleep" or voice_data.lower() == "go back to sleep":
                                wake = False
                                break
                            print("Voice data: " + voice_data)  # print user's voice data
                            self.textChanged.emit(voice_data)
                            # respond(r2, voice_data, language=language)  # respond to user's voice data
                elif listen_for_keyword.lower() == "stop the program":
                    break

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
            self.main = MainWindow()
            self.main.show()
            #
            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1

# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.objThread = QThread()
        self.worker = VoiceWorker()
        # RESIZE WINDOW
        self.resize(300, 420)
        self.setMinimumSize(QSize(300, 420))
        self.setMaximumSize(QSize(300, 420))

        # REMOVE TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(40, 42, 54);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.centralwidget)
        self.worker.textChanged.connect(self.title.setText)
        self.title.setMinimumSize(QSize(0, 200))
        self.title.setMaximumSize(QSize(16777215, 200))
        self.title.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 12px;\n"
"   font: 18pt \"Segoe UI\";\n"
"}")
        self.title.setAlignment(Qt.AlignCenter)


        self.verticalLayout.addWidget(self.title)



        self.setCentralWidget(self.centralwidget)


        self.worker.moveToThread(self.objThread)
        self.objThread.start()
        self.objThread.started.connect(self.worker.test)




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = SplashScreen()
    sys.exit(app.exec_())