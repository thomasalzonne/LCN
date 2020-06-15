from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
import serial

def setupMenu(MainWindow, ui, logic, thread):
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
        ui.menuname.setTitle(_translate("MainWindow", s))
        ui.actionConnect.triggered.connect(lambda: logic.setSerialPort(s, ui, thread))
        ui.actionDeconnexion.triggered.connect(lambda: logic.decoSerialPort(logic.serialPort,ui))
def setupActions(MainWindow, ui, logic):
    ui.Y_up.clicked.connect(lambda: logic.move("Y", 1, ui))
    ui.Y_down.clicked.connect(lambda: logic.move("Y", -1, ui))
    ui.X_right.clicked.connect(lambda: logic.move("X", 1, ui))
    ui.X_left.clicked.connect(lambda: logic.move("X", -1, ui))
    ui.Z_up.clicked.connect(lambda: logic.move("Z", 1, ui))
    ui.Z_down.clicked.connect(lambda: logic.move("Z", -1, ui))
    ui.E_up.clicked.connect(lambda: logic.move("E", 1, ui))
    ui.E_down.clicked.connect(lambda: logic.move("E", -1, ui))

    ui.push0_1mm.clicked.connect(lambda: logic.setStep(0.1,ui))
    ui.push1mm.clicked.connect(lambda: logic.setStep(1,ui))
    ui.push10mm.clicked.connect(lambda: logic.setStep(10,ui))

    ui.pushreset_x.clicked.connect(lambda: logic.reset("X",ui))
    ui.pushreset_y.clicked.connect(lambda: logic.reset("Y",ui))
    ui.pushreset_z.clicked.connect(lambda: logic.reset("Z",ui))
    ui.pushreset_all.clicked.connect(lambda: logic.resetall(ui))
    ui.textBrowser.setText(logic.console)
    ui.coor_X.setText(logic.coor_X + str(logic.posX))
    ui.coor_Y.setText(logic.coor_Y + str(logic.posY))
    ui.coor_Z.setText(logic.coor_Z + str(logic.posZ))
    ui.coor_E.setText(logic.coor_E + str(logic.posE))
    ui.pushreset_x.setStyleSheet(logic.pushhover)
    ui.pushreset_y.setStyleSheet(logic.pushhover)
    ui.pushreset_z.setStyleSheet(logic.pushhover)
    ui.pushreset_all.setStyleSheet(logic.pushhover)
    ui.adminbutton.setEnabled(False)
    ui.adminbutton.clicked.connect(lambda: logic.sendcommand(ui))
    ui.unlockadmin.triggered.connect(lambda: logic.unlockadminmode(ui))
    ui.lockadmin.triggered.connect(lambda: logic.lockadminmode(ui))
    ui.onlyInt = QIntValidator()
    ui.einput.setValidator(ui.onlyInt)
    ui.speedinput.setValidator(ui.onlyInt)
    ui.tempinput.setValidator(ui.onlyInt)
    ui.bedinput.setValidator(ui.onlyInt)
    ui.pushButton_6.setStyleSheet("background-color:white;""border:none")
    ui.pushButton_5.setStyleSheet("background-color:white;""border:none")
    ui.gotoImp.clicked.connect(lambda: logic.gotoImpr(ui))
    ui.gotoLaser.clicked.connect(lambda: logic.gotolaser(ui))
    ui.gotoFraiseuse.clicked.connect(lambda: logic.gotofraise(ui))
    ui.gotoImp.clicked.connect(lambda: logic.setgoto(ui))
    ui.gotoLaser.clicked.connect(lambda: logic.setgoto(ui))
    ui.gotoFraiseuse.clicked.connect(lambda: logic.setgoto(ui))
    ui.pwdinput.setEchoMode(QtWidgets.QLineEdit.Password)
    ui.speedinput.setEnabled(False)
    ui.speedbutton.setEnabled(False)
    ui.tempinput.setEnabled(False)
    ui.tempbutton.setEnabled(False)
    ui.lockadminpanelbutton.setEnabled(False)
    ui.pwdbutton.clicked.connect(lambda: logic.login(ui))
    ui.lockadminpanelbutton.clicked.connect(lambda: logic.lockadminpanel(ui))
    ui.speedbutton.clicked.connect(lambda: logic.changespeed(ui))
    ui.tempbutton.clicked.connect(lambda: logic.settemp(ui))
    ui.gettemperature.clicked.connect(logic.gettemp)
    ui.stopgettemp.clicked.connect(logic.stopgetTemp)
    ui.bedtemperature.setText(str(logic.tempbed))
    ui.extrudortemperature.setText(str(logic.tempextru))

    ui.gotoImp.clicked.connect(lambda: logic.infowindow(ui.gotoImp.text(), ui))
    ui.gotoLaser.clicked.connect(lambda: logic.infowindow(ui.gotoLaser.text(), ui))
    ui.gotoFraiseuse.clicked.connect(lambda: logic.infowindow(ui.gotoFraiseuse.text(), ui))

    ui.loadfiles.clicked.connect(lambda: logic.openFileNameDialog(ui))
    ui.savebutton.clicked.connect(lambda: logic.savefile(ui))
    ui.launchprog.clicked.connect(lambda: logic.launchProg(ui))

    ui.laserslidervalue.setText("0")
    ui.sliderlaser.valueChanged.connect(lambda : logic.setlaservalue(ui))
    ui.fraiseuseslidervalue.setText("0")
    ui.fraiseuseslider.valueChanged.connect(lambda : logic.setfraiseusevalue(ui))

    ui.startetemp.clicked.connect(lambda : logic.startextrudorTemp(ui))
    ui.startbedtemp.clicked.connect(lambda : logic.startbedTemp(ui))
    ui.stopbedtemp.clicked.connect(logic.stopbedTemp)
    ui.stopetemp.clicked.connect(logic.stopextrudorTemp)

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
