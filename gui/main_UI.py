import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # RESIZE WINDOW
        self.resize(500, 500)

        # REMOVE TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # CREATE CONTAINER AND LAYOUT
        self.container = QFrame()
        self.container.setStyleSheet("background-color: transparent")
        self.layout = QVBoxLayout()


        # SET CENTRAL WIDGET
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        # SHOW WINDOW
        self.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
