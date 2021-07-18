# from main import*
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_main import Ui_MainWindow
from uart_function import*
import config


class UIFunctions(QMainWindow):
    def click(self):
        self.ui.lineEdit_3.setText("hello")

    def genderCheck(self):
        if self.ui.gender_male.isChecked():
            self.ui.lineEdit_4.setText("Nam")
        elif self.ui.gender_female.isChecked():
            self.ui.lineEdit_4.setText("Nữ")
    def catch_info(self):
        self.ui.lineEdit_3.setText("{}".format(self.ui.line_name.text()))
        self.ui.lineEdit_4.setText("{}".format(self.ui.text_reason.text()))

    def show_KQ(self):
        self.ui.lineTemp.setText(UART.classify.temp+"\tđộ C")
        self.ui.lineWeight.setText(UART.classify.weight+"\tKg")
        self.ui.lineHeight.setText(UART.classify.height+"\tcm")
        self.ui.linePressure.setText(UART.classify.pressure+"\tmmHg")
        self.ui.linePulse.setText(UART.classify.pulse+"\tNhịp")