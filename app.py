from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from src.ui_functions import setupMenu, setupActions, updateDisplay
from src.logic import Logic
from app_ui import Ui_MainWindow



class App:
    def __init__(self):
        self.logic = Logic()
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        setupMenu(MainWindow, self.ui, self.logic)
        MainWindow.show()
        setupActions(MainWindow, self.ui, self.logic)
        updateDisplay(self.ui, self.logic)
        sys.exit(app.exec_())

App()
