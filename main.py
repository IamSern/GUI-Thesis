import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

from PyQt5 import QtCore, QtGui, QtWidgets
#GUI file
from ui_main import Ui_MainWindow
#import Functions
from ui_function import*

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #start
       
        # self.show()
        data = UART.read(self)
        UIFunctions.display(self, data)
        
        #END
        self.show()
 


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
