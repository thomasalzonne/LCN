# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import serial
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        def mForward():
            print("avancer")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(423, 303)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 120, 56, 17))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 423, 18))
        self.menubar.setObjectName("menubar")
        self.menuConnexion = QtWidgets.QMenu(self.menubar)
        self.menuConnexion.setObjectName("menuConnexion")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuConnexion.menuAction())
        self.pushButton.clicked.connect(mForward)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        def blbl():
            serialPort = serial.Serial(port = s, baudrate=115200,bytesize=8, timeout=5, stopbits=serial.STOPBITS_ONE)
            print("connected to : " +s)

        available = []
        for i in range(256):
            try:
                s = serial.Serial('COM'+str(i))
                available.append( (s.portstr))

            except serial.SerialException:
                pass
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Avancer"))
        self.menuConnexion.setTitle(_translate("MainWindow", "Connexion"))
        for s in available:
            self.actionname = QtWidgets.QAction(MainWindow)
            self.actionname.setObjectName("actionname")
            self.menuConnexion.addAction(self.actionname)
            self.actionname.setText(_translate("MainWindow", s))
            self.actionname.triggered.connect(blbl)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
