# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1000)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1000))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1000))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
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
        self.pushreset_x = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushreset_x.setFont(font)
        self.pushreset_x.setStyleSheet(" background-color: grey;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:50px;\n"
"min-width:100px;\n"
"min-height:100px;\n"
"max-width:100px;\n"
"max-height:100px;\n"
"QPushButton::hover\n"
"                            {\n"
"                             background-color : lightgreen;\n"
"                             }")
        self.pushreset_x.setObjectName("pushreset_x")
        self.horizontalLayout_4.addWidget(self.pushreset_x)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pushreset_y = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushreset_y.setFont(font)
        self.pushreset_y.setTabletTracking(False)
        self.pushreset_y.setStyleSheet(" background-color: grey;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:50px;\n"
"min-width:100px;\n"
"min-height:100px;\n"
"max-width:100px;\n"
"max-height:100px;")
        self.pushreset_y.setObjectName("pushreset_y")
        self.horizontalLayout_4.addWidget(self.pushreset_y)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.pushreset_z = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushreset_z.setFont(font)
        self.pushreset_z.setStyleSheet(" background-color: grey;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:50px;\n"
"min-width:100px;\n"
"min-height:100px;\n"
"max-width:100px;\n"
"max-height:100px;")
        self.pushreset_z.setObjectName("pushreset_z")
        self.horizontalLayout_4.addWidget(self.pushreset_z)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.pushreset_all = QtWidgets.QPushButton(self.centralwidget)
        self.pushreset_all.setMinimumSize(QtCore.QSize(102, 102))
        self.pushreset_all.setMaximumSize(QtCore.QSize(102, 102))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushreset_all.setFont(font)
        self.pushreset_all.setStyleSheet(" background-color: grey;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:50px;\n"
"min-width:100px;\n"
"min-height:100px;\n"
"max-width:100px;\n"
"max-height:100px;")
        self.pushreset_all.setObjectName("pushreset_all")
        self.horizontalLayout_4.addWidget(self.pushreset_all)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.push10mm = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.push10mm.setFont(font)
        self.push10mm.setStyleSheet(" background-color: grey;\n"
" border-style: solid;\n"
" border-width:1px;\n"
"border-radius: 20px;\n"
"min-width:120px;\n"
"min-height:80px;\n"
"max-width:120px;\n"
"max-height:80px;")
        self.push10mm.setObjectName("push10mm")
        self.gridLayout.addWidget(self.push10mm, 0, 2, 1, 1)
        self.push1mm = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.push1mm.setFont(font)
        self.push1mm.setStyleSheet(" background-color: grey;\n"
" border-style: solid;\n"
" border-width:1px;\n"
"border-radius: 20px;\n"
"min-width:120px;\n"
"min-height:80px;\n"
"max-width:120px;\n"
"max-height:80px;")
        self.push1mm.setObjectName("push1mm")
        self.gridLayout.addWidget(self.push1mm, 0, 1, 1, 1)
        self.push0_1mm = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.push0_1mm.setFont(font)
        self.push0_1mm.setStyleSheet(" background-color: grey;\n"
" border-style: solid;\n"
" border-width:1px;\n"
"border-radius: 20px;\n"
"min-width:120px;\n"
"min-height:80px;\n"
"max-width:120px;\n"
"max-height:80px;")
        self.push0_1mm.setObjectName("push0_1mm")
        self.gridLayout.addWidget(self.push0_1mm, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 3, 4, 1, 1)
        self.Y_up = QtWidgets.QPushButton(self.centralwidget)
        self.Y_up.setStyleSheet(" background-color:grey;\n"
" border-style: solid;\n"
" border-radius:50px;\n"
" max-width:100px;\n"
" max-height:100px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"")
        self.Y_up.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Y_up.setIcon(icon)
        self.Y_up.setIconSize(QtCore.QSize(70, 70))
        self.Y_up.setObjectName("Y_up")
        self.gridLayout_2.addWidget(self.Y_up, 2, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 2, 1, 1)
        self.Z_down = QtWidgets.QPushButton(self.centralwidget)
        self.Z_down.setStyleSheet(" background-color:grey;\n"
" border-style: solid;\n"
" border-radius:50px;\n"
" max-width:100px;\n"
" max-height:100px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"")
        self.Z_down.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/bottom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Z_down.setIcon(icon1)
        self.Z_down.setIconSize(QtCore.QSize(70, 70))
        self.Z_down.setObjectName("Z_down")
        self.gridLayout_2.addWidget(self.Z_down, 4, 5, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 600, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_2.addItem(spacerItem7, 5, 2, 1, 1)
        self.X_right = QtWidgets.QPushButton(self.centralwidget)
        self.X_right.setStyleSheet(" background-color:grey;\n"
" border-style: solid;\n"
" border-radius:50px;\n"
" max-width:100px;\n"
" max-height:100px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"")
        self.X_right.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.X_right.setIcon(icon2)
        self.X_right.setIconSize(QtCore.QSize(70, 70))
        self.X_right.setObjectName("X_right")
        self.gridLayout_2.addWidget(self.X_right, 3, 3, 1, 1)
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
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 2, 6, 1, 1)
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
        self.X_left = QtWidgets.QPushButton(self.centralwidget)
        self.X_left.setStyleSheet(" background-color:grey;\n"
" border-style: solid;\n"
" border-radius:50px;\n"
" max-width:100px;\n"
" max-height:100px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"")
        self.X_left.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.X_left.setIcon(icon3)
        self.X_left.setIconSize(QtCore.QSize(70, 70))
        self.X_left.setObjectName("X_left")
        self.gridLayout_2.addWidget(self.X_left, 3, 1, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2.addLayout(self.gridLayout_4, 3, 5, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 3, 0, 1, 1)
        self.Z_up = QtWidgets.QPushButton(self.centralwidget)
        self.Z_up.setStyleSheet(" background-color:grey;\n"
" border-style: solid;\n"
" border-radius:50px;\n"
" max-width:100px;\n"
" max-height:100px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"")
        self.Z_up.setText("")
        self.Z_up.setIcon(icon)
        self.Z_up.setIconSize(QtCore.QSize(70, 70))
        self.Z_up.setObjectName("Z_up")
        self.gridLayout_2.addWidget(self.Z_up, 2, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 7, 1, 1)
        self.coor_Y = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.coor_Y.setFont(font)
        self.coor_Y.setObjectName("coor_Y")
        self.gridLayout_2.addWidget(self.coor_Y, 3, 7, 1, 1)
        self.coor_Z = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.coor_Z.setFont(font)
        self.coor_Z.setObjectName("coor_Z")
        self.gridLayout_2.addWidget(self.coor_Z, 4, 7, 1, 1)
        self.coor_X = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.coor_X.setFont(font)
        self.coor_X.setObjectName("coor_X")
        self.gridLayout_2.addWidget(self.coor_X, 2, 7, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.textBrowser = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 300))
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
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
        self.actionname = QtWidgets.QAction(MainWindow)
        self.actionname.setCheckable(True)
        self.actionname.setChecked(False)
        self.actionname.setObjectName("actionname")
        self.actionName = QtWidgets.QAction(MainWindow)
        self.actionName.setCheckable(True)
        self.actionName.setObjectName("actionName")
        self.menubar.addAction(self.menuConnexion.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushreset_x.setText(_translate("MainWindow", "Reset X"))
        self.pushreset_y.setText(_translate("MainWindow", "Reset Y"))
        self.pushreset_z.setText(_translate("MainWindow", "Reset Z"))
        self.pushreset_all.setText(_translate("MainWindow", "Reset All"))
        self.push10mm.setText(_translate("MainWindow", "10 mm"))
        self.push1mm.setText(_translate("MainWindow", "1 mm"))
        self.push0_1mm.setText(_translate("MainWindow", "0.1 mm"))
        self.label_2.setText(_translate("MainWindow", "X/Y"))
        self.label.setText(_translate("MainWindow", "Z"))
        self.label_3.setText(_translate("MainWindow", "Coordonnées"))
        self.coor_Y.setText(_translate("MainWindow", "Y : "))
        self.coor_Z.setText(_translate("MainWindow", "Z : "))
        self.coor_X.setText(_translate("MainWindow", "X :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3d), _translate("MainWindow", "impr.3D"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tablaser), _translate("MainWindow", "Laser"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabfraiseuse), _translate("MainWindow", "Fraiseuse"))
        self.menuConnexion.setTitle(_translate("MainWindow", "Connexion"))
        self.actionname.setText(_translate("MainWindow", "name"))
        self.actionName.setText(_translate("MainWindow", "Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())