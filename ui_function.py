from main import*
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_main import Ui_MainWindow

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
        