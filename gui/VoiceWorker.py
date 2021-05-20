from PyQt5 import QtCore, QtGui, QtWidgets
import speech_recognition as sr
import sys
from PyQt5.QtCore import QCoreApplication, QThread
# from core.proccess_respond import respond
from core.listen import record_audio
from core.speak import voice_assistant_speak


class VoiceWorker(QtCore.QObject):
    textChanged = QtCore.pyqtSignal(str)

    @QtCore.pyqtSlot()
    def task(self):
        r = sr.Recognizer()
        m = sr.Microphone()

        while True:
            print("Say something!")
            with m as source:
                audio = r.listen(source)
                print("Got it! Now to recognize it...")
                try:
                    value = r.recognize_google(audio)
                    self.textChanged.emit(value)
                    print("You said: {}".format(value))
                except sr.UnknownValueError:
                    print("Oops")

    @QtCore.pyqtSlot()
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


def Gui():
    r = sr.Recognizer()
    m = sr.Microphone()
    app = QtWidgets.QApplication(sys.argv)

    objThread = QThread()
    worker = VoiceWorker()
    # thread = QtCore.QThread()
    # thread.start()

    window = QtWidgets.QWidget()
    window.setGeometry(200, 200, 350, 400)
    window.setWindowTitle("Assistant")

    title_label = QtWidgets.QLabel(window)
    title_label.setText("Assistant")
    title_label.move(135,10)
    title_label.setFont(QtGui.QFont("SansSerif", 15))

    programs_says = QtWidgets.QLabel(window)
    programs_says.setText("Programs Says")
    programs_says.move(240,100)

    you_says = QtWidgets.QLabel(window)
    you_says.move(25,100)


    you_text = QtWidgets.QLabel(window)
    worker.textChanged.connect(you_text.setText)
    you_text.move(25,150)


    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    window.setLayout(v_box)


    window.show()
    worker.moveToThread(objThread)
    objThread.start()
    objThread.started.connect(worker.test)

    sys.exit(app.exec())


Gui()