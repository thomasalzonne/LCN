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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.loggedlabel = QtWidgets.QLabel(self.frame)
        self.loggedlabel.setGeometry(QtCore.QRect(10, 0, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.loggedlabel.setFont(font)
        self.loggedlabel.setStyleSheet("color:red;")
        self.loggedlabel.setObjectName("loggedlabel")
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gotoLaser = QtWidgets.QPushButton(self.centralwidget)
        self.gotoLaser.setStyleSheet(" background-color: grey;\n"
" border-style: solid;\n"
" border-width:1px;\n"
"border-radius: 20px;\n"
"min-width:120px;\n"
"min-height:80px;\n"
"max-width:120px;\n"
"max-height:80px;")
        self.gotoLaser.setObjectName("gotoLaser")
        self.gridLayout.addWidget(self.gotoLaser, 0, 3, 1, 1)
        self.gotoImp = QtWidgets.QPushButton(self.centralwidget)
        self.gotoImp.setStyleSheet(" background-color: grey;\n"
" border-style: solid;\n"
" border-width:1px;\n"
"border-radius: 20px;\n"
"min-width:120px;\n"
"min-height:80px;\n"
"max-width:120px;\n"
"max-height:80px;")
        self.gotoImp.setObjectName("gotoImp")
        self.gridLayout.addWidget(self.gotoImp, 0, 1, 1, 1)
        self.push1mm = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.push1mm.setFont(font)
        self.push1mm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push1mm.setStyleSheet(" background-color: grey;\n"
" border-style: solid;\n"
" border-width:1px;\n"
"border-radius: 20px;\n"
"min-width:120px;\n"
"min-height:80px;\n"
"max-width:120px;\n"
"max-height:80px;")
        self.push1mm.setObjectName("push1mm")
        self.gridLayout.addWidget(self.push1mm, 2, 2, 1, 1)
        self.push0_1mm = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.push0_1mm.setFont(font)
        self.push0_1mm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push0_1mm.setStyleSheet(" background-color: grey;\n"
" border-style: solid;\n"
" border-width:1px;\n"
"border-radius: 20px;\n"
"min-width:120px;\n"
"min-height:80px;\n"
"max-width:120px;\n"
"max-height:80px;")
        self.push0_1mm.setObjectName("push0_1mm")
        self.gridLayout.addWidget(self.push0_1mm, 2, 0, 1, 1)
        self.push10mm = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.push10mm.setFont(font)
        self.push10mm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push10mm.setStyleSheet(" background-color: grey;\n"
" border-style: solid;\n"
" border-width:1px;\n"
"border-radius: 20px;\n"
"min-width:120px;\n"
"min-height:80px;\n"
"max-width:120px;\n"
"max-height:80px;")
        self.push10mm.setObjectName("push10mm")
        self.gridLayout.addWidget(self.push10mm, 2, 4, 1, 1)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.gridLayout.addLayout(self.horizontalLayout_20, 1, 2, 1, 1)
        self.gotoFraiseuse = QtWidgets.QPushButton(self.centralwidget)
        self.gotoFraiseuse.setStyleSheet(" background-color: grey;\n"
" border-style: solid;\n"
" border-width:1px;\n"
"border-radius: 20px;\n"
"min-width:120px;\n"
"min-height:80px;\n"
"max-width:120px;\n"
"max-height:80px;")
        self.gotoFraiseuse.setObjectName("gotoFraiseuse")
        self.gridLayout.addWidget(self.gotoFraiseuse, 0, 5, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.X_left = QtWidgets.QPushButton(self.centralwidget)
        self.X_left.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.X_left.setStyleSheet("QPushButton {\n"
" background-color:grey;\n"
" border-style: solid;\n"
" border-radius:50px;\n"
" max-width:100px;\n"
" max-height:100px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:#3d5885;\n"
"        }\n"
"        ")
        self.X_left.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.X_left.setIcon(icon)
        self.X_left.setIconSize(QtCore.QSize(70, 70))
        self.X_left.setObjectName("X_left")
        self.gridLayout_2.addWidget(self.X_left, 3, 1, 1, 1)
        self.coor_Z = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.coor_Z.setFont(font)
        self.coor_Z.setObjectName("coor_Z")
        self.gridLayout_2.addWidget(self.coor_Z, 4, 7, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 2, 1, 1)
        self.coor_X = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.coor_X.setFont(font)
        self.coor_X.setObjectName("coor_X")
        self.gridLayout_2.addWidget(self.coor_X, 2, 7, 1, 1)
        self.coor_Y = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.coor_Y.setFont(font)
        self.coor_Y.setObjectName("coor_Y")
        self.gridLayout_2.addWidget(self.coor_Y, 3, 7, 1, 1)
        self.Y_down = QtWidgets.QPushButton(self.centralwidget)
        self.Y_down.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Y_down.setStyleSheet("QPushButton {\n"
" background-color:grey;\n"
" border-style: solid;\n"
" border-radius:50px;\n"
" max-width:100px;\n"
" max-height:100px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:#3d5885;\n"
"        }\n"
"        ")
        self.Y_down.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/bottom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Y_down.setIcon(icon1)
        self.Y_down.setIconSize(QtCore.QSize(70, 70))
        self.Y_down.setObjectName("Y_down")
        self.gridLayout_2.addWidget(self.Y_down, 4, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 3, 4, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushreset_z = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushreset_z.setFont(font)
        self.pushreset_z.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushreset_z.setStyleSheet(" background-color: grey;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:35px;\n"
"min-width:70px;\n"
"min-height:70px;\n"
"max-width: 70px;\n"
"max-height:70px;\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/browser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushreset_z.setIcon(icon2)
        self.pushreset_z.setIconSize(QtCore.QSize(20, 20))
        self.pushreset_z.setObjectName("pushreset_z")
        self.gridLayout_4.addWidget(self.pushreset_z, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 3, 5, 1, 1)
        self.Z_up = QtWidgets.QPushButton(self.centralwidget)
        self.Z_up.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Z_up.setStyleSheet("QPushButton {\n"
" background-color:grey;\n"
" border-style: solid;\n"
" border-radius:50px;\n"
" max-width:100px;\n"
" max-height:100px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:#3d5885;\n"
"        }\n"
"        ")
        self.Z_up.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Z_up.setIcon(icon3)
        self.Z_up.setIconSize(QtCore.QSize(70, 70))
        self.Z_up.setObjectName("Z_up")
        self.gridLayout_2.addWidget(self.Z_up, 2, 5, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 3, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 2, 6, 1, 1)
        self.Z_down = QtWidgets.QPushButton(self.centralwidget)
        self.Z_down.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Z_down.setStyleSheet("QPushButton {\n"
" background-color:grey;\n"
" border-style: solid;\n"
" border-radius:50px;\n"
" max-width:100px;\n"
" max-height:100px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:#3d5885;\n"
"        }\n"
"        ")
        self.Z_down.setText("")
        self.Z_down.setIcon(icon1)
        self.Z_down.setIconSize(QtCore.QSize(70, 70))
        self.Z_down.setObjectName("Z_down")
        self.gridLayout_2.addWidget(self.Z_down, 4, 5, 1, 1)
        self.Y_up = QtWidgets.QPushButton(self.centralwidget)
        self.Y_up.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Y_up.setStyleSheet("QPushButton {\n"
" background-color:grey;\n"
" border-style: solid;\n"
" border-radius:50px;\n"
" max-width:100px;\n"
" max-height:100px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:#3d5885;\n"
"        }\n"
"        ")
        self.Y_up.setText("")
        self.Y_up.setIcon(icon3)
        self.Y_up.setIconSize(QtCore.QSize(70, 70))
        self.Y_up.setObjectName("Y_up")
        self.gridLayout_2.addWidget(self.Y_up, 2, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem8, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 7, 1, 1)
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
        self.X_right = QtWidgets.QPushButton(self.centralwidget)
        self.X_right.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.X_right.setStyleSheet("QPushButton {\n"
" background-color:grey;\n"
" border-style: solid;\n"
" border-radius:50px;\n"
" max-width:100px;\n"
" max-height:100px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:#3d5885;\n"
"        }\n"
"        ")
        self.X_right.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("assets/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.X_right.setIcon(icon4)
        self.X_right.setIconSize(QtCore.QSize(70, 70))
        self.X_right.setObjectName("X_right")
        self.gridLayout_2.addWidget(self.X_right, 3, 3, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushreset_all = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushreset_all.setFont(font)
        self.pushreset_all.setStyleSheet(" background-color: grey;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:35px;\n"
"min-width:70px;\n"
"min-height:70px;\n"
"max-width: 70px;\n"
"max-height:70px;")
        self.pushreset_all.setIcon(icon2)
        self.pushreset_all.setIconSize(QtCore.QSize(20, 20))
        self.pushreset_all.setObjectName("pushreset_all")
        self.horizontalLayout_14.addWidget(self.pushreset_all)
        self.gridLayout_2.addLayout(self.horizontalLayout_14, 4, 3, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushreset_y = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushreset_y.setFont(font)
        self.pushreset_y.setStyleSheet(" background-color: grey;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:35px;\n"
"min-width:70px;\n"
"min-height:70px;\n"
"max-width: 70px;\n"
"max-height:70px;")
        self.pushreset_y.setIcon(icon2)
        self.pushreset_y.setIconSize(QtCore.QSize(20, 20))
        self.pushreset_y.setObjectName("pushreset_y")
        self.horizontalLayout_15.addWidget(self.pushreset_y)
        self.gridLayout_2.addLayout(self.horizontalLayout_15, 4, 1, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.pushreset_x = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushreset_x.setFont(font)
        self.pushreset_x.setStyleSheet(" background-color: grey;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:35px;\n"
"min-width:70px;\n"
"min-height:70px;\n"
"max-width: 70px;\n"
"max-height:70px;")
        self.pushreset_x.setIcon(icon2)
        self.pushreset_x.setIconSize(QtCore.QSize(20, 20))
        self.pushreset_x.setObjectName("pushreset_x")
        self.horizontalLayout_16.addWidget(self.pushreset_x)
        self.gridLayout_2.addLayout(self.horizontalLayout_16, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.admin_input = QtWidgets.QLineEdit(self.centralwidget)
        self.admin_input.setReadOnly(True)
        self.admin_input.setObjectName("admin_input")
        self.horizontalLayout_3.addWidget(self.admin_input)
        self.adminbutton = QtWidgets.QPushButton(self.centralwidget)
        self.adminbutton.setObjectName("adminbutton")
        self.horizontalLayout_3.addWidget(self.adminbutton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.textBrowser = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 150))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 150))
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(1200, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tab3d = QtWidgets.QWidget()
        self.tab3d.setObjectName("tab3d")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab3d)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.tab3d)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.gridLayout_3.addLayout(self.horizontalLayout_17, 1, 0, 1, 1)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.E_down = QtWidgets.QPushButton(self.tab3d)
        self.E_down.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.E_down.setStyleSheet("QPushButton {\n"
" background-color:grey;\n"
" border-style: solid;\n"
" border-radius:50px;\n"
" max-width:100px;\n"
" max-height:100px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:#3d5885;\n"
"        }\n"
"        ")
        self.E_down.setText("")
        self.E_down.setIcon(icon1)
        self.E_down.setIconSize(QtCore.QSize(70, 70))
        self.E_down.setObjectName("E_down")
        self.horizontalLayout_19.addWidget(self.E_down)
        self.gridLayout_3.addLayout(self.horizontalLayout_19, 3, 0, 1, 1)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.E_up = QtWidgets.QPushButton(self.tab3d)
        self.E_up.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.E_up.setStyleSheet("QPushButton {\n"
" background-color:grey;\n"
" border-style: solid;\n"
" border-radius:50px;\n"
" max-width:100px;\n"
" max-height:100px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:#3d5885;\n"
"        }\n"
"        ")
        self.E_up.setText("")
        self.E_up.setIcon(icon3)
        self.E_up.setIconSize(QtCore.QSize(70, 70))
        self.E_up.setObjectName("E_up")
        self.horizontalLayout_18.addWidget(self.E_up)
        self.gridLayout_3.addLayout(self.horizontalLayout_18, 0, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem10, 2, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_3)
        self.coor_E = QtWidgets.QLabel(self.tab3d)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.coor_E.setFont(font)
        self.coor_E.setObjectName("coor_E")
        self.horizontalLayout_5.addWidget(self.coor_E)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem11)
        self.label_7 = QtWidgets.QLabel(self.tab3d)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab3d)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("assets/stop-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_8.addWidget(self.pushButton_2)
        self.einput = QtWidgets.QLineEdit(self.tab3d)
        self.einput.setMinimumSize(QtCore.QSize(160, 50))
        self.einput.setMaximumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.einput.setFont(font)
        self.einput.setText("")
        self.einput.setAlignment(QtCore.Qt.AlignCenter)
        self.einput.setObjectName("einput")
        self.horizontalLayout_8.addWidget(self.einput)
        self.pushButton = QtWidgets.QPushButton(self.tab3d)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("assets/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QtCore.QSize(45, 45))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_8.addWidget(self.pushButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_10.addLayout(self.horizontalLayout_12)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab3d)
        self.pushButton_5.setMinimumSize(QtCore.QSize(160, 160))
        self.pushButton_5.setMaximumSize(QtCore.QSize(160, 160))
        self.pushButton_5.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("assets/plastic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon7)
        self.pushButton_5.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_10.addWidget(self.pushButton_5)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab3d)
        self.pushButton_4.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_4.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon5)
        self.pushButton_4.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_9.addWidget(self.pushButton_4)
        self.bedinput = QtWidgets.QLineEdit(self.tab3d)
        self.bedinput.setMinimumSize(QtCore.QSize(160, 50))
        self.bedinput.setMaximumSize(QtCore.QSize(160, 50))
        self.bedinput.setAlignment(QtCore.Qt.AlignCenter)
        self.bedinput.setObjectName("bedinput")
        self.horizontalLayout_9.addWidget(self.bedinput)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab3d)
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_3.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon6)
        self.pushButton_3.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_9.addWidget(self.pushButton_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_13.addLayout(self.verticalLayout_6)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab3d)
        self.pushButton_6.setMinimumSize(QtCore.QSize(160, 160))
        self.pushButton_6.setMaximumSize(QtCore.QSize(160, 160))
        self.pushButton_6.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("assets/heater.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon8)
        self.pushButton_6.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_13.addWidget(self.pushButton_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_13.addLayout(self.verticalLayout_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem13)
        self.tabWidget.addTab(self.tab3d, "")
        self.tablaser = QtWidgets.QWidget()
        self.tablaser.setObjectName("tablaser")
        self.tabWidget.addTab(self.tablaser, "")
        self.tabfraiseuse = QtWidgets.QWidget()
        self.tabfraiseuse.setObjectName("tabfraiseuse")
        self.tabWidget.addTab(self.tabfraiseuse, "")
        self.tabadmin = QtWidgets.QWidget()
        self.tabadmin.setEnabled(True)
        self.tabadmin.setObjectName("tabadmin")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tabadmin)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_5 = QtWidgets.QLabel(self.tabadmin)
        self.label_5.setMinimumSize(QtCore.QSize(136, 0))
        self.label_5.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_21.addWidget(self.label_5)
        self.pwdinput = QtWidgets.QLineEdit(self.tabadmin)
        self.pwdinput.setMinimumSize(QtCore.QSize(0, 30))
        self.pwdinput.setMaximumSize(QtCore.QSize(700, 16777215))
        self.pwdinput.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pwdinput.setText("")
        self.pwdinput.setObjectName("pwdinput")
        self.horizontalLayout_21.addWidget(self.pwdinput)
        self.pwdbutton = QtWidgets.QPushButton(self.tabadmin)
        self.pwdbutton.setMinimumSize(QtCore.QSize(100, 0))
        self.pwdbutton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pwdbutton.setObjectName("pwdbutton")
        self.horizontalLayout_21.addWidget(self.pwdbutton)
        self.verticalLayout_8.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_6 = QtWidgets.QLabel(self.tabadmin)
        self.label_6.setMinimumSize(QtCore.QSize(210, 0))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_26.addWidget(self.label_6)
        self.speedinput = QtWidgets.QLineEdit(self.tabadmin)
        self.speedinput.setMinimumSize(QtCore.QSize(0, 30))
        self.speedinput.setObjectName("speedinput")
        self.horizontalLayout_26.addWidget(self.speedinput)
        self.speedbutton = QtWidgets.QPushButton(self.tabadmin)
        self.speedbutton.setMinimumSize(QtCore.QSize(100, 30))
        self.speedbutton.setObjectName("speedbutton")
        self.horizontalLayout_26.addWidget(self.speedbutton)
        self.verticalLayout_8.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_8 = QtWidgets.QLabel(self.tabadmin)
        self.label_8.setMinimumSize(QtCore.QSize(200, 0))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_23.addWidget(self.label_8)
        self.tempinput = QtWidgets.QLineEdit(self.tabadmin)
        self.tempinput.setMinimumSize(QtCore.QSize(0, 30))
        self.tempinput.setObjectName("tempinput")
        self.horizontalLayout_23.addWidget(self.tempinput)
        self.tempbutton = QtWidgets.QPushButton(self.tabadmin)
        self.tempbutton.setObjectName("tempbutton")
        self.horizontalLayout_23.addWidget(self.tempbutton)
        self.verticalLayout_8.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.lockadminpanelbutton = QtWidgets.QPushButton(self.tabadmin)
        self.lockadminpanelbutton.setMinimumSize(QtCore.QSize(350, 70))
        self.lockadminpanelbutton.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lockadminpanelbutton.setObjectName("lockadminpanelbutton")
        self.horizontalLayout_22.addWidget(self.lockadminpanelbutton)
        self.verticalLayout_8.addLayout(self.horizontalLayout_22)
        self.tabWidget.addTab(self.tabadmin, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 18))
        self.menubar.setObjectName("menubar")
        self.menuConnexion = QtWidgets.QMenu(self.menubar)
        self.menuConnexion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuConnexion.setObjectName("menuConnexion")
        self.menuname = QtWidgets.QMenu(self.menuConnexion)
        self.menuname.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuname.setObjectName("menuname")
        self.menuAdminMode = QtWidgets.QMenu(self.menubar)
        self.menuAdminMode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuAdminMode.setObjectName("menuAdminMode")
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
        self.unlockadmin = QtWidgets.QAction(MainWindow)
        self.unlockadmin.setObjectName("unlockadmin")
        self.lockadmin = QtWidgets.QAction(MainWindow)
        self.lockadmin.setObjectName("lockadmin")
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionDeconnexion = QtWidgets.QAction(MainWindow)
        self.actionDeconnexion.setObjectName("actionDeconnexion")
        self.menuname.addAction(self.actionConnect)
        self.menuname.addAction(self.actionDeconnexion)
        self.menuConnexion.addAction(self.menuname.menuAction())
        self.menuAdminMode.addAction(self.unlockadmin)
        self.menuAdminMode.addAction(self.lockadmin)
        self.menubar.addAction(self.menuConnexion.menuAction())
        self.menubar.addAction(self.menuAdminMode.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loggedlabel.setText(_translate("MainWindow", "Not Connected"))
        self.gotoLaser.setText(_translate("MainWindow", "Laser"))
        self.gotoImp.setText(_translate("MainWindow", "Imprimante 3D"))
        self.push1mm.setText(_translate("MainWindow", "1 mm"))
        self.push0_1mm.setText(_translate("MainWindow", "0.1 mm"))
        self.push10mm.setText(_translate("MainWindow", "10 mm"))
        self.gotoFraiseuse.setText(_translate("MainWindow", "Fraiseuse"))
        self.coor_Z.setText(_translate("MainWindow", "Z : "))
        self.label_2.setText(_translate("MainWindow", "X/Y"))
        self.coor_X.setText(_translate("MainWindow", "X :"))
        self.coor_Y.setText(_translate("MainWindow", "Y : "))
        self.pushreset_z.setText(_translate("MainWindow", "Z"))
        self.label_3.setText(_translate("MainWindow", "Coordonnées"))
        self.label.setText(_translate("MainWindow", "Z"))
        self.pushreset_all.setText(_translate("MainWindow", "All"))
        self.pushreset_y.setText(_translate("MainWindow", "Y"))
        self.pushreset_x.setText(_translate("MainWindow", "X"))
        self.admin_input.setPlaceholderText(_translate("MainWindow", "Passer en mode administrateur pour dévérouiller cette section"))
        self.adminbutton.setText(_translate("MainWindow", "Entrer"))
        self.label_4.setText(_translate("MainWindow", "Extrudeur"))
        self.coor_E.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "Température"))
        self.einput.setPlaceholderText(_translate("MainWindow", "Entrer une température"))
        self.bedinput.setPlaceholderText(_translate("MainWindow", "Entrer une température"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3d), _translate("MainWindow", "impr.3D"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tablaser), _translate("MainWindow", "Laser"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabfraiseuse), _translate("MainWindow", "Fraiseuse"))
        self.label_5.setText(_translate("MainWindow", "Mot de Passe :"))
        self.pwdinput.setPlaceholderText(_translate("MainWindow", "Entrer votre mot de passe"))
        self.pwdbutton.setText(_translate("MainWindow", "Valider"))
        self.label_6.setText(_translate("MainWindow", "Vitesse déplacement :"))
        self.speedinput.setPlaceholderText(_translate("MainWindow", "Entrer une vitesse"))
        self.speedbutton.setText(_translate("MainWindow", "Valider"))
        self.label_8.setText(_translate("MainWindow", "Interval température :"))
        self.tempinput.setPlaceholderText(_translate("MainWindow", "Entrer une température entière"))
        self.tempbutton.setText(_translate("MainWindow", "Valider"))
        self.lockadminpanelbutton.setText(_translate("MainWindow", "Verrouiller le panel administrateur"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabadmin), _translate("MainWindow", "Administrateur"))
        self.menuConnexion.setTitle(_translate("MainWindow", "Connexion"))
        self.menuname.setTitle(_translate("MainWindow", "name"))
        self.menuAdminMode.setTitle(_translate("MainWindow", "AdminMode"))
        self.actionname.setText(_translate("MainWindow", "name"))
        self.actionName.setText(_translate("MainWindow", "Name"))
        self.unlockadmin.setText(_translate("MainWindow", "Déverouiller mode admin"))
        self.lockadmin.setText(_translate("MainWindow", "Vérouiller mode admin"))
        self.actionConnect.setText(_translate("MainWindow", "Connexion"))
        self.actionDeconnexion.setText(_translate("MainWindow", "Deconnexion"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
