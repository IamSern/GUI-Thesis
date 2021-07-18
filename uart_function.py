from main import*
from PyQt5 import QtCore, QtGui, QtWidgets
import serial

class UART(QMainWindow):
    def __init__(self, serialPort):
        super().__init__(serialPort)
        self.serialPort = serial.Serial(port='COM10', baudrate= 115200, bytesize= 8, parity= serial.PARITY_NONE, 
                        timeout= 2, stopbits= serial.STOPBITS_ONE)
    def UART_read(self):
        if ser.read_until(b'START') != "":
            recevie = ser.read_until(b'OVER').decode("UTF-8")
            return recevie
    
    def classify(self, data):    
        if data[data.rfind("@")] != 0:
            temp = data[data.rfind("@")+1:data.rfind("@")+5]
        if data[data.rfind("#")] != 0:
            weight = data[data.rfind("#")+1:data.rfind("#")+5]
        if  data[data.rfind("$")] != 0:
            height = data[data.rfind("$")+1:data.rfind("$")+5]
        if data[data.rfind("%")] != 0:
            pressure = data[data.rfind("%")+1:data.rfind("%")+4]
        if data[data.rfind("&")] != 0:
            pulse = data[data.rfind("&")+1:data.rfind("&")+3]
            