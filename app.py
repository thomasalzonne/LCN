from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from src.ui_functions import setupMenu, setupActions, updateDisplay
from src.logic import Logic, Thread
from app_ui import Ui_MainWindow

class App:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.logic = Logic(self)
        self.thread = Thread(self.ui,self.logic)
        setupMenu(MainWindow, self.ui, self.logic, self.thread)
        MainWindow.show()
        setupActions(MainWindow, self.ui, self.logic)
        updateDisplay(self.ui, self.logic)
        sys.exit(app.exec_())
App()
