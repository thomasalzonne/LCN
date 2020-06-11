from PyQt5 import QtCore, QtGui, QtWidgets
import serial

def setupMenu(MainWindow, ui, logic):
    available = []
    for i in range(256):
        try:
            s = serial.Serial('COM'+str(i))
            available.append( (s.portstr))

        except serial.SerialException:
            pass

    _translate = QtCore.QCoreApplication.translate
    ui.menuConnexion.setTitle(_translate("MainWindow", "Connexion"))

    for s in available:
        a = 0
        setattr(ui,"actionname"+str(a),QtWidgets.QAction(MainWindow))
        ui.menuConnexion.addAction(getattr(ui,"actionname"+str(a)))
        getattr(ui,"actionname"+str(a)).setText(_translate("MainWindow", s))
        getattr(ui,"actionname"+str(a)).triggered.connect(lambda: logic.setSerialPort(s, ui))
        a += 1

def setupActions(MainWindow, ui, logic):
    ui.Y_up.clicked.connect(lambda: logic.move("Y", 1, ui))
    ui.Y_down.clicked.connect(lambda: logic.move("Y", -1, ui))
    ui.X_right.clicked.connect(lambda: logic.move("X", 1, ui))
    ui.X_left.clicked.connect(lambda: logic.move("X", -1, ui))
    ui.Z_up.clicked.connect(lambda: logic.move("Z", 1, ui))
    ui.Z_down.clicked.connect(lambda: logic.move("Z", -1, ui))

    ui.push0_1mm.clicked.connect(lambda: logic.setStep(0.1,ui))
    ui.push1mm.clicked.connect(lambda: logic.setStep(1,ui))
    ui.push10mm.clicked.connect(lambda: logic.setStep(10,ui))

    ui.pushreset_x.clicked.connect(lambda: logic.reset("X",ui))
    ui.pushreset_y.clicked.connect(lambda: logic.reset("Y",ui))
    ui.pushreset_z.clicked.connect(lambda: logic.reset("Z",ui))
    ui.pushreset_all.clicked.connect(lambda: logic.resetall(ui))
    ui.textBrowser.setText(logic.console)
    ui.coor_X.setText(logic.coor_X)
    ui.coor_Y.setText(logic.coor_Y)
    ui.coor_Z.setText(logic.coor_Z)
    ui.pushreset_x.setStyleSheet(logic.pushhover)
    ui.pushreset_y.setStyleSheet(logic.pushhover)
    ui.pushreset_z.setStyleSheet(logic.pushhover)
    ui.pushreset_all.setStyleSheet(logic.pushhover)

    ui.adminbutton.clicked.connect(lambda: logic.cc())
    ui.unlockadmin.triggered.connect(lambda: logic.unlockadminmode(ui))
    ui.lockadmin.triggered.connect(lambda: logic.lockadminmode(ui))
def updateDisplay(ui, logic):
    if logic.step == 0.1:
        ui.push0_1mm.setStyleSheet("background-color: #3d5885;\n"
                                    "border-style: solid;\n"
                                    "border-width:1px;\n"
                                    "border-radius: 20px;\n"
                                    "min-width:120px;\n"
                                    "min-height:80px;\n"
                                    "max-width:120px;\n"
                                    "max-height:80px;\n")
    elif logic.step == 1:
        ui.push1mm.setStyleSheet("background-color: #3d5885;\n"
                                    "border-style: solid;\n"
                                    "border-width:1px;\n"
                                    "border-radius: 20px;\n"
                                    "min-width:120px;\n"
                                    "min-height:80px;\n"
                                    "max-width:120px;\n"
                                    "max-height:80px;\n")
    elif logic.step == 10:
        ui.push10mm.setStyleSheet("background-color: #3d5885;\n"
                                    "border-style: solid;\n"
                                    "border-width:1px;\n"
                                    "border-radius: 20px;\n"
                                    "min-width:120px;\n"
                                    "min-height:80px;\n"
                                    "max-width:120px;\n"
                                    "max-height:80px;\n")
