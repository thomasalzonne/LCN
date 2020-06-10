# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import serial


class Ui_MainWindow(object):
    def blbl(self,s):
        serialPort = serial.Serial(port = s, baudrate=115200,bytesize=8, timeout=5, stopbits=serial.STOPBITS_ONE)
        print("connected to : " +s)
        a = serialPort
    def mForward(self,a):
        if a.is_open :
            a.write(b"GO X10\n")
            print("moved")
        else :
            print("no connection")

    def setupUi(self, MainWindow, a):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1000)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1000))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1000))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setStyleSheet(" background-color: grey;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:50px;\n"
"min-width:100px;\n"
"min-height:100px;\n"
"max-width:100px;\n"
"max-height:100px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setStyleSheet(" background-color: grey;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:50px;\n"
"min-width:100px;\n"
"min-height:100px;\n"
"max-width:100px;\n"
"max-height:100px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet(" background-color: grey;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:50px;\n"
"min-width:100px;\n"
"min-height:100px;\n"
"max-width:100px;\n"
"max-height:100px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(102, 102))
        self.pushButton.setMaximumSize(QtCore.QSize(102, 102))
        self.pushButton.setStyleSheet(" background-color: grey;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:50px;\n"
"min-width:100px;\n"
"min-height:100px;\n"
"max-width:100px;\n"
"max-height:100px;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setMinimumSize(QtCore.QSize(0, 25))
        self.radioButton_3.setStyleSheet("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 0, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setMinimumSize(QtCore.QSize(0, 25))
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setMinimumSize(QtCore.QSize(0, 25))
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setStyleSheet(" background-color:grey;\n"
" border-style: solid;\n"
" border-radius:50px;\n"
" max-width:100px;\n"
" max-height:100px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"")
        self.pushButton_9.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 2, 5, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setStyleSheet(" background-color:grey;\n"
" border-style: solid;\n"
" border-radius:50px;\n"
" max-width:100px;\n"
" max-height:100px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"")
        self.pushButton_12.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("bottom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon1)
        self.pushButton_12.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 4, 5, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 5, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2.addLayout(self.gridLayout_4, 3, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 3, 4, 1, 1)
        self.Y_down = QtWidgets.QPushButton(self.centralwidget)
        self.Y_down.setStyleSheet(" background-color:grey;\n"
" border-style: solid;\n"
" border-radius:50px;\n"
" max-width:100px;\n"
" max-height:100px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"")
        self.Y_down.setText("")
        self.Y_down.setIcon(icon1)
        self.Y_down.setIconSize(QtCore.QSize(70, 70))
        self.Y_down.setObjectName("Y_down")
        self.gridLayout_2.addWidget(self.Y_down, 4, 2, 1, 1)
        self.X_up = QtWidgets.QPushButton(self.centralwidget)
        self.X_up.setStyleSheet(" background-color:grey;\n"
" border-style: solid;\n"
" border-radius:50px;\n"
" max-width:100px;\n"
" max-height:100px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"")
        self.X_up.setText("")
        self.X_up.setIcon(icon)
        self.X_up.setIconSize(QtCore.QSize(70, 70))
        self.X_up.setObjectName("X_up")
        self.gridLayout_2.addWidget(self.X_up, 2, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setStyleSheet(" background-color:grey;\n"
" border-style: solid;\n"
" border-radius:50px;\n"
" max-width:100px;\n"
" max-height:100px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"")
        self.pushButton_6.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 3, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setStyleSheet(" background-color:grey;\n"
" border-style: solid;\n"
" border-radius:50px;\n"
" max-width:100px;\n"
" max-height:100px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"")
        self.pushButton_5.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 3, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 2, 6, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 600, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_2.addItem(spacerItem6, 5, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 0, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(1200, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tab3d = QtWidgets.QWidget()
        self.tab3d.setObjectName("tab3d")
        self.tabWidget.addTab(self.tab3d, "")
        self.tablaser = QtWidgets.QWidget()
        self.tablaser.setObjectName("tablaser")
        self.tabWidget.addTab(self.tablaser, "")
        self.tabfraiseuse = QtWidgets.QWidget()
        self.tabfraiseuse.setObjectName("tabfraiseuse")
        self.tabWidget.addTab(self.tabfraiseuse, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 18))
        self.menubar.setObjectName("menubar")
        self.menuConnexion = QtWidgets.QMenu(self.menubar)
        self.menuConnexion.setObjectName("menuConnexion")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuConnexion.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.X_up.clicked.connect(lambda: self.mForward(a))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "Reset X"))
        self.pushButton_3.setText(_translate("MainWindow", "Reset Y"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset Z"))
        self.pushButton.setText(_translate("MainWindow", "Reset All"))
        self.radioButton_3.setText(_translate("MainWindow", "0,1mm"))
        self.radioButton_2.setText(_translate("MainWindow", "1mm"))
        self.radioButton.setText(_translate("MainWindow", "10mm"))
        self.label_2.setText(_translate("MainWindow", "X/Y"))
        self.label.setText(_translate("MainWindow", "Z"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3d), _translate("MainWindow", "impr.3D"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tablaser), _translate("MainWindow", "Laser"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabfraiseuse), _translate("MainWindow", "Fraiseuse"))
        self.menuConnexion.setTitle(_translate("MainWindow", "Connexion"))
        available = []
        for i in range(256):
            try:
                s = serial.Serial('COM'+str(i))
                available.append( (s.portstr))

            except serial.SerialException:
                pass
        for s in available:
            self.actionname = QtWidgets.QAction(MainWindow)
            self.actionname.setObjectName("actionname")
            self.menuConnexion.addAction(self.actionname)
            self.actionname.setText(_translate("MainWindow", s))
            self.actionname.triggered.connect(lambda: self.blbl(s))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    a = serial.Serial(port = "COM4", baudrate=115200,bytesize=8, timeout=5, stopbits=serial.STOPBITS_ONE)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,a)
    MainWindow.show()
    sys.exit(app.exec_())
