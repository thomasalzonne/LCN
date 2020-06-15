from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import time
import _thread
import os
import os.path
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QPushButton, QMessageBox

class Thread(QtCore.QObject):
    def __init__(self,ui,logic):
        self.ui = ui
        self.console= logic.console
    def createthread(self, name, ui, serialPort):
        _thread.start_new_thread(name,(self,self.ui,serialPort,self.console))
class Logic(QtCore.QObject):
    updateConsoleSignal = QtCore.pyqtSignal()
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.serialPort = False
        self.pwd = "azerty31"
        self.step = 1 #mm
        self.posX = 0.0
        self.posY = 0.0
        self.posZ = 0.0
        self.posE = 0.0
        self.F = 1500
        self.tempsec = 3
        self.console = "Console :\n"
        self.coor_X = "X : "
        self.coor_Y = "Y : "
        self.coor_Z = "Z : "
        self.coor_E = "E : "
        self.currentTab = False
        self.pushstyle=("border-style: solid;\n"
        "font-weight: bold;\n"
        "border-width:1px;\n"
        "border-radius: 20px;\n"
        "min-width:120px;\n"
        "min-height:80px;\n"
        "max-width:120px;\n"
        "max-height:80px;\n")
        self.pushhover = ("QPushButton {\n"
        "background-color: grey;\n"
        " border-style: solid;\n"
        " border-width:1px;\n"
        " border-radius:35px;\n"
        "min-width:70px;\n"
        "min-height:70px;\n"
        "max-width:70px;\n"
        "max-height:70px;"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:#3d5885;\n"
        "}\n"
        "")
        self.updateConsoleSignal.connect(self.updateConsole)
        self.tempextru = 0.0
        self.tempbed = 0.0
        self.prog = ""
        self.countok = 0
    def updateConsole(self):
        self.app.ui.textBrowser.setText(self.console)
    def sendcommand(self, ui):
        if self.serialPort and self.serialPort.is_open:
            print(ui.admin_input.text())
            self.machineMove(ui.admin_input.text()+"\n", ui)
            ui.admin_input.setText("")
        else:
            print("COM not connected")
    def checkSerial(self):
        if self.serialPort and self.serialPort.is_open:
            return True
        else:
            return False
    def consoletext(self,thread,ui,serialPort, console):
        while True:
            text =self.serialPort.readline().decode()
            if text == "ok\n":
                self.countok += 1
            self.console =self.console + text
            self.updateConsoleSignal.emit()
            if text.lstrip().startswith("T"):
                temp = text.split("B")
                extru = temp[0].split(":")
                bed = temp[1].split(":")
                extrudortemp = extru[1].split(" ")
                bedtemp = bed[1].split(" ")
                self.tempbed = bedtemp[0]
                self.tempextru = extrudortemp[0]
                ui.extrudortemperature.setText(str(self.tempextru))
                ui.bedtemperature.setText(str(self.tempbed))
    def setSerialPort(self, s ,ui, thread):
        serialPort = serial.Serial(port = s, baudrate=9600,bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
        print("connected to : " +s)
        ui.loggedlabel.setText("Connected")
        ui.loggedlabel.setStyleSheet("color:green;")
        self.serialPort = serialPort
        thread.createthread(self.consoletext,ui,self.serialPort)
        self.serialPort.write(b"G91\n")
    def decoSerialPort(self, serialPort, ui):
        if self.serialPort and self.serialPort.is_open:
            self.serialPort.close()
            ui.loggedlabel.setText("Deconnected")
            ui.loggedlabel.setStyleSheet("color:red;")
            print("déconnexion")
        else:
            print("COM not connected")
    def machineMove(self, move, ui):
        moved = move.encode()
        self.serialPort.write(moved)
        moved = ">>>" + moved.decode()
        self.console =self.console + moved
        ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
        ui.coor_X.setText(self.coor_X + str(self.posX))
        ui.coor_Y.setText(self.coor_Y + str(self.posY))
        ui.coor_Z.setText(self.coor_Z + str(self.posZ))
        ui.coor_E.setText(self.coor_E + str(self.posE))
    def reset(self, axis, ui):
        if self.serialPort and self.serialPort.is_open:
            if axis == "X":
                a= -self.posX
                move = "G0 "+axis+str(a)+"\n"
                self.posX = 0.0
                self.machineMove(move, ui)
            if axis == "Y":
                a= -self.posY
                move = "G0 "+axis+str(a)+"\n"
                self.posY = 0.0
                self.machineMove(move, ui)
            if axis == "Z":
                a= -self.posZ
                move = "G0 "+axis+str(a)+"\n"
                self.posZ = 0.0
                self.machineMove(move, ui)
        else:
            print("COM not connected")
    def resetall(self, ui):
        if self.serialPort and self.serialPort.is_open:
            x = -self.posX
            y = -self.posY
            z = -self.posZ
            movex = "G0 X"+str(x)+"\n"
            movey = "G0 Y"+str(y)+"\n"
            movez = "G0 Z"+str(z)+"\n"
            self.posX=0.0
            self.posY=0.0
            self.posZ=0.0
            self.machineMove(movex, ui)
            self.machineMove(movey, ui)
            self.machineMove(movez, ui)
            print("All positions were reseted")
        else :
            print("COM not connected")
    def move(self, axis, direction, ui):
        if self.serialPort and self.serialPort.is_open:
            move = "G0 " + axis + str( direction * self.step ) + " F" + str(self.F) + "\n"
            if axis == "X":
                self.posX += direction*self.step
                move = "G0 " + axis + str( self.posX ) + " F" + str(self.F) + "\n"
            if axis == "Y":
                self.posY += direction*self.step
                move = "G0 " + axis + str( self.posY ) + " F" + str(self.F) + "\n"
            if axis == "Z":
                self.posZ += direction*self.step
                move = "G0 " + axis + str( self.posZ ) + " F" + str(self.F) + "\n"
            if axis == "E":
                self.posE += direction*self.step
                move = "G0 " + axis + str( self.posE ) + " F" + str(self.F) + "\n"
            self.machineMove(move, ui)
        else:
            print("COM not connected")
    def setStep(self,step,ui):
        self.step=step
        if self.step == 0.1:
            ui.push0_1mm.setStyleSheet(self.pushstyle + "background-color:#3d5885;\n")
            ui.push1mm.setStyleSheet(self.pushstyle + "background-color: grey;\n")
            ui.push10mm.setStyleSheet(self.pushstyle + "background-color: grey;\n")
        elif self.step == 1:
            ui.push0_1mm.setStyleSheet(self.pushstyle + "background-color: grey;\n")
            ui.push1mm.setStyleSheet(self.pushstyle + "background-color: #3d5885;\n")
            ui.push10mm.setStyleSheet(self.pushstyle +"background-color: grey;\n")
        elif self.step == 10:
            ui.push0_1mm.setStyleSheet(self.pushstyle + "background-color: grey;\n")
            ui.push1mm.setStyleSheet(self.pushstyle + "background-color: grey;\n")
            ui.push10mm.setStyleSheet(self.pushstyle + "background-color: #3d5885;\n")
    def gotoImpr(self,ui):
        ui.tabWidget.setCurrentWidget(ui.tab3d)
    def gotolaser(self,ui):
        ui.tabWidget.setCurrentWidget(ui.tablaser)
    def gotofraise(self,ui):
        ui.tabWidget.setCurrentWidget(ui.tabfraiseuse)
    def setgoto(self,ui):
        self.currentTab = ui.tabWidget.currentIndex()
        if self.currentTab == 0:
            ui.gotoImp.setStyleSheet(self.pushstyle + "background-color:#3d5885;\n")
            ui.gotoLaser.setStyleSheet(self.pushstyle + "background-color: grey;\n")
            ui.gotoFraiseuse.setStyleSheet(self.pushstyle + "background-color: grey;\n")
        elif self.currentTab == 1:
            ui.gotoImp.setStyleSheet(self.pushstyle + "background-color: grey;\n")
            ui.gotoLaser.setStyleSheet(self.pushstyle + "background-color: #3d5885;\n")
            ui.gotoFraiseuse.setStyleSheet(self.pushstyle +"background-color: grey;\n")
        elif self.currentTab == 2:
            ui.gotoImp.setStyleSheet(self.pushstyle + "background-color: grey;\n")
            ui.gotoLaser.setStyleSheet(self.pushstyle + "background-color: grey;\n")
            ui.gotoFraiseuse.setStyleSheet(self.pushstyle + "background-color: #3d5885;\n")
    def login(self,ui):
        if self.pwd == ui.pwdinput.text():
            ui.speedinput.setEnabled(True)
            ui.speedbutton.setEnabled(True)
            ui.tempinput.setEnabled(True)
            ui.tempbutton.setEnabled(True)
            ui.lockadminpanelbutton.setEnabled(True)
            ui.admin_input.setReadOnly(False)
            ui.adminbutton.setEnabled(True)
            ui.admin_input.setPlaceholderText("Entrer votre commande")
        else :
            print("wrong pwd")
    def lockadminpanel(self,ui):
        ui.speedinput.setEnabled(False)
        ui.speedbutton.setEnabled(False)
        ui.tempinput.setEnabled(False)
        ui.tempbutton.setEnabled(False)
        ui.lockadminpanelbutton.setEnabled(False)
        ui.admin_input.setReadOnly(True)
        ui.adminbutton.setEnabled(False)
        ui.admin_input.setPlaceholderText("Passer en mode administrateur pour dévérouiller cette section")
    def changespeed(self,ui):
        speed = ui.speedinput.text()
        self.F = speed
        print("speed changed")
    def settemp(self, ui):
        temp = ui.tempinput.text()
        self.tempsec = temp
        print("gettemp changed")
    def gettemp(self):
        command = "M155 S" + str(self.tempsec) + "\n"
        self.serialPort.write(command.encode())
    def stopgetTemp(self):
        self.serialPort.write("M155 S0\n".encode())
    def savefile(self , ui):
        homedir = os.path.expanduser("~/Desktop")
        text = ui.gcodefile.toPlainText()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(ui.tabWidget,"Sauvegarder votre fichier Gcode",homedir,"Gcode Files (*.gcode)", options=options)
        file_exists = os.path.isfile(fileName)
        if file_exists:
            os.remove(fileName)
            f = open(fileName, "a")
            f.write(text)
            f.close()
        else:
            f = open(fileName, "a")
            f.write(text)
            f.close()
        print("saved")
    def loaded(self, txt, ui):
        self.prog = txt
        f = open(txt, "r")
        text = f.read()
        f.close()
        ui.gcodefile.setPlainText(text)
        ui.gcodefile.setReadOnly(False)
    def openFileNameDialog(self,ui):
        homedir = os.path.expanduser("~/Desktop")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(ui.tabWidget,"Choisissez votre fichier Gcode", homedir ,"Gcode Files (*.gcode)", options=options)
        if fileName:
            self.loaded(fileName, ui)
    def infowindow(self,tabname, ui):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setIconPixmap(QPixmap("./assets/" + tabname).scaled(64,64))
        msg.setText("Bonjour, c'est la page d'information de " + tabname)
        msg.setWindowTitle(tabname)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()
    def readprog(self,serialPort,command):
        if self.serialPort and self.serialPort.is_open:
            tableau = []
            subarray = []
            for i in range(0, len(command)) :
                commande = command[i] + "\n"
                if not commande.startswith(';'):
                    if not commande.startswith('\n'):
                        subarray.append(commande)
                        if len(subarray) == 8:
                            tableau.append(subarray)
                            subarray=[]
                        if i == len(command):
                            tableau.append(subarray)
            for a in range (0, len(tableau)):
                subtableau = tableau[a]
                self.countok = 1
                i = 0
                while self.countok != 8:
                    time.sleep(0.2)
                    commande = subtableau[i].encode()
                    self.serialPort.write(commande)
                    commande = ">>>" + commande.decode()
                    self.console =self.console + commande
                    print(self.countok)
                    i += 1
        else:
            print("COM not connected")
    def launchProg(self, ui):
        f = open(self.prog, "r")
        text = f.read()
        f.close()
        command = text.split("\n")
        _thread.start_new_thread(self.readprog,(self.serialPort, command))
    def setlaservalue(self, ui):
        ui.laserslidervalue.setText(str(ui.sliderlaser.value()))
    def setfraiseusevalue(self, ui):
        ui.fraiseuseslidervalue.setText(str(ui.fraiseuseslider

        .value()))
    def startbedTemp(self, ui):
        command = "M140 S"+str(ui.bedinput.text()) + "\n"
        self.serialPort.write(command.encode())
        print("temp bed started")
    def startextrudorTemp(self, ui):
        command = "M104 S" + str(ui.einput.text()) + "\n"
        self.serialPort.write(command.encode())
        print("temp extrudor started")
    def stopbedTemp(self):
        command = "M140 S0\n"
        self.serialPort.write(command.encode())
    def stopextrudorTemp(self):
        command = "M104 S0\n"
        self.serialPort.write(command.encode())
