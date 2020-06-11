# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import time

class Logic(QtCore.QObject):
    def __init__(self):
        self.serialPort = False
        self.step = 1 #mm
        self.posX = 0.0
        self.posY = 0.0
        self.posZ = 0.0
        self.console = "Console :\n"
        self.coor_X = "X : "
        self.coor_Y = "Y : "
        self.coor_Z = "Z : "
        self.pushstyle=("border-style: solid;\n"
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
        " border-radius:50px;\n"
        "min-width:100px;\n"
        "min-height:100px;\n"
        "max-width:100px;\n"
        "max-height:100px;"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:#3d5885;\n"
        "}\n"
        "")

    def cc(self):
        print("cc")

    def unlockadminmode(self, ui):
        ui.admin_input.setReadOnly(False)
        print("admin mode actif")
    def lockadminmode(self, ui):
        ui.admin_input.setReadOnly(True)
        print("admin mode désactivé")
    def checkSerial(self):
        if self.serialPort and self.serialPort.is_open:
            return True
        else:
            return False

    def consoletext(self, ui, serialPort):
        time.sleep(0.20)
        while serialPort.inWaiting():
            text ="\t"+self.serialPort.readline().decode()
            self.console =self.console +text
        ui.textBrowser.setText(self.console)
        ui.textBrowser.moveCursor(QtGui.QTextCursor.End)

    def setSerialPort(self, s ,ui):
        serialPort = serial.Serial(port = s, baudrate=9600,bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
        print("connected to : " +s)
        self.serialPort = serialPort
        time.sleep(6)
        ui.loading.hide()
        # while self.serialPort.inWaiting() == 0:
        #     print("xx")
        # self.consoletext(ui,self.serialPort)
        # time.sleep(0.5)
        # self.consoletext(ui,self.serialPort)
        # time.sleep(2)
        # self.serialPort.write(b"G91\n")

    def machineMove(self, move, ui):
        moved = move.encode()
        self.serialPort.write(moved)
        self.console =self.console + moved.decode()
        ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
        self.consoletext(ui, self.serialPort)
        ui.coor_X.setText(self.coor_X+str(self.posX))
        ui.coor_Y.setText(self.coor_Y+str(self.posY))
        ui.coor_Z.setText(self.coor_Z+str(self.posZ))

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
            move = "G0 "+axis+str(direction*self.step)+" F1500\n"
            if axis == "X":
                self.posX += direction*self.step
            if axis == "Y":
                self.posY += direction*self.step
            if axis == "Z":
                self.posZ += direction*self.step
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
