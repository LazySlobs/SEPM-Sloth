import time, sys
from PyQt5.QtCore  import *
from PyQt5.QtGui import *

class Worker(QObject):
    sgnFinished = pyqtSignal()

    def __init__(self, parent):
        QObject.__init__(self, parent)
        self._mutex = QMutex()
        self._running = True

    @pyqtSlot()
    def stop(self):
        print('switching while loop condition to false')
        self._mutex.lock()
        self._running = False
        self._mutex.unlock()

    def running(self):
        try:
            self._mutex.lock()
            return self._running
        finally:
            self._mutex.unlock()

    @pyqtSlot()
    def work(self):
        while self.running():
            time.sleep(0.1)
            print('doing work...')
        self.sgnFinished.emit()

class Client(QObject):
    def __init__(self, parent):
        QObject.__init__(self, parent)
        self._thread = None
        self._worker = None

    def toggle(self, enable):
        if enable:
            if not self._thread:
                self._thread = QThread()

            self._worker = Worker(None)
            self._worker.moveToThread(self._thread)
            self._worker.sgnFinished.connect(self.on_worker_done)

            self._thread.started.connect(self._worker.work)
            self._thread.start()
        else:
            print('stopping the worker object')
            self._worker.stop()

    @pyqtSlot()
    def on_worker_done(self):
        print('workers job was interrupted manually')
        self._thread.quit()
        self._thread.wait()
        if input('\nquit application [Yn]? ') != 'n':
            app.quit()

if __name__ == '__main__':

    # prevent some harmless Qt warnings
    pyqtRemoveInputHook()

    app = QCoreApplication(sys.argv)

    client = Client(None)

    def start():
        client.toggle(True)
        input('Press something\n')
        client.toggle(False)

    # QTimer.singleShot(10, start)
    start()

    sys.exit(app.exec_())