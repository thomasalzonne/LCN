# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
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
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 2, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2.addLayout(self.gridLayout_4, 3, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 2, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_3.addWidget(self.pushButton_6, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 4, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 4, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(1000, 16777215))
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
        self.actionname.setObjectName("actionname")
        self.actionName = QtWidgets.QAction(MainWindow)
        self.actionName.setObjectName("actionName")
        self.menuConnexion.addAction(self.actionname)
        self.menuConnexion.addSeparator()
        self.menuConnexion.addAction(self.actionName)
        self.menubar.addAction(self.menuConnexion.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        self.label.setText(_translate("MainWindow", "Z"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.label_2.setText(_translate("MainWindow", "X/Y"))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_12.setText(_translate("MainWindow", "PushButton"))
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
