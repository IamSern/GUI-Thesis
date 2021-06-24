from PyQt5 import QtCore, QtGui, QtWidgets
from main import*
import serial
import time

#str = unicode(str, errors='replace')
ser = serial.Serial(port='COM10', baudrate= 115200, bytesize= 8, parity= serial.PARITY_NONE, 
                        timeout= 2, stopbits= serial.STOPBITS_ONE)


class UART(QMainWindow):
    def __init__(self, serialPort):
        super().__init__(serialPort)
        self.serialPort = serial.Serial(port='COM10', baudrate= 115200, bytesize= 8, parity= serial.PARITY_NONE, 
                        timeout= 2, stopbits= serial.STOPBITS_ONE)
    def read(self):
        if ser.read_until(b'START') != "":
            recevie = ser.read_until(b'OVER').decode("UTF-8")
            return recevie

    def classify(self, recevie):
        pass

class UIFunctions(QMainWindow):
    def saveInfo(self):
        self.ui.textEdit.setText("hello")

    def display(self, data):    
        if data[data.rfind("@")] != 0:
            temp = data[data.rfind("@")+1:data.rfind("@")+5]
            self.ui.lineTemp.setText(temp+"\tđộ C")
        if data[data.rfind("#")] != 0:
            weight = data[data.rfind("#")+1:data.rfind("#")+5]
            self.ui.lineWeight.setText(weight+"\tKg")
        if  data[data.rfind("$")] != 0:
            self.ui.lineHeight.setText("")
            self.ui.lineHeight.setText(height+"\tcm")
        if data[data.rfind("%")] != 0:
            pressure = data[data.rfind("%")+1:data.rfind("%")+4]
            self.ui.linePressure.setText(pressure+"\tmmHg")
        if data[data.rfind("&")] != 0:
            pulse = data[data.rfind("&")+1:data.rfind("&")+3]
            self.ui.linePulse.setText(pulse+"\tNhịp")
