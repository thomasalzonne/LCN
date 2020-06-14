from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from src.ui_functions import setupMenu, setupActions, updateDisplay
from src.logic import Logic, Thread
from app_ui import Ui_MainWindow

class MyDialog:
     def __init__(self, parent=None):
        super(MyDialog).__init__(parent)
        self.pushButton_3 = QtWidgets.QPushButton()
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_3.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_3.setText("")
        self.pushButton_3.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_3.setObjectName("pushButton_3")

class App:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.secwindow = MyDialog()
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
