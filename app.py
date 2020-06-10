from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from src.ui_functions import setupMenu, setupActions, updateDisplay
from src.logic import Logic
from app_ui import Ui_MainWindow


class App:
    def __init__(cls):
        cls.logic = Logic()

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        cls.ui = Ui_MainWindow()
        cls.ui.setupUi(MainWindow)
        setupMenu(MainWindow, cls.ui, cls.logic)
        MainWindow.show()

        setupActions(MainWindow, cls.ui, cls.logic)
        updateDisplay(cls.ui, cls.logic)
        sys.exit(app.exec_())

App()
