# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import serial


class Logic(QtCore.QObject):
    def __init__(self):
        self.serialPort = False
        self.step = 1 #mm
        # self.x, self.y, self.z = [0, 0, 0]

    def checkSerial(self):
        if self.serialPort and self.serialPort.is_open:
            return True
        else:
            return False

    def setSerialPort(self, s):
        serialPort = serial.Serial(port = s, baudrate=115200,bytesize=8, timeout=5, stopbits=serial.STOPBITS_ONE)
        print("connected to : " +s)
        self.serialPort = serialPort
        print(self.serialPort)

    def move(self, axis, direction):
        if self.serialPort and self.serialPort.is_open:
            move = "G0 "+axis+str(direction*self.step)+"\n"
            move = move.encode()
            self.serialPort.write(move)
            print("Moved on axis : " + axis + " to : " + str(direction*self.step))
        else:
            print("COM not connected")

    def setStep(self,step):
        self.step=step
