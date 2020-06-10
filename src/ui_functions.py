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
        getattr(ui,"actionname"+str(a)).triggered.connect(lambda: logic.setSerialPort(s))
        a += 1

def setupActions(MainWindow, ui, logic):
    ui.Y_up.clicked.connect(lambda: logic.move("Y", 1))
    ui.Y_down.clicked.connect(lambda: logic.move("Y", -1))
    ui.X_right.clicked.connect(lambda: logic.move("X", 1))
    ui.X_left.clicked.connect(lambda: logic.move("X", -1))
    ui.Z_up.clicked.connect(lambda: logic.move("Z", 1))
    ui.Z_down.clicked.connect(lambda: logic.move("Z", -1))

    ui.radio0_1mm.toggled.connect(lambda: logic.setStep(0.1))
    ui.radio1mm.toggled.connect(lambda: logic.setStep(1))
    ui.radio10mm.toggled.connect(lambda: logic.setStep(10))

def updateDisplay(ui, logic):
    ui.radio0_1mm.setChecked(False)
    ui.radio1mm.setChecked(False)
    ui.radio10mm.setChecked(False)
    if logic.step == 0.1:
        ui.radio0_1mm.setChecked(True)
    elif logic.step == 1:
        ui.radio1mm.setChecked(True)
    elif logic.step == 1:
        ui.radio10mm.setChecked(True)
