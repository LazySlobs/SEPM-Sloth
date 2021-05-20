# This Python file uses the following encoding: utf-8
import sys
import os

from PySide2.QtGui import QGuiApplication, QIcon
from PySide2.QtQml import QQmlApplicationEngine
from mainWindow import MainWindow


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Get Context
    main = MainWindow()
    engine.rootContext().setContextProperty("backend", main)

    # Set App Extra Info
    app.setOrganizationName("Lazy Slob - Group 14")
    app.setOrganizationDomain("vn")

    # Set Icon
    app.setWindowIcon(QIcon("gui_qt_creator/images/images/Group1.ico"))

    # Load Initial Window
    engine.load(os.path.join(os.path.dirname(__file__), "gui_qt_creator/qml/splashScreen.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
