# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainNo2.0.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
# from ui_function import*


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 30))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame.setStyleSheet("background-color: rgb(161, 99, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.info_present = QtWidgets.QFrame(self.frame_2)
        self.info_present.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_present.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_present.setObjectName("info_present")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.info_present)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.thongtincanhan = QtWidgets.QFrame(self.info_present)
        self.thongtincanhan.setMaximumSize(QtCore.QSize(16777215, 400))
        self.thongtincanhan.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thongtincanhan.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thongtincanhan.setObjectName("thongtincanhan")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.thongtincanhan)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.thongtincanhan)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.thongtincanhan)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setContentsMargins(20, 0, 20, 0)
        self.gridLayout.setHorizontalSpacing(9)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        self.comboBox.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 4, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 5)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_2.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 0, 6, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(self.thongtincanhan)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setContentsMargins(20, 0, 20, 6)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.frame_5)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_3.addWidget(self.textEdit)
        self.pushButton = QtWidgets.QPushButton(self.frame_5)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.thongtincanhan)
        self.ketquado = QtWidgets.QFrame(self.info_present)
        self.ketquado.setMinimumSize(QtCore.QSize(0, 350))
        self.ketquado.setStyleSheet("background-color: rgb(75, 180, 222);")
        self.ketquado.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ketquado.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ketquado.setObjectName("ketquado")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.ketquado)
        self.gridLayout_3.setContentsMargins(0, 10, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.ketquado)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(259, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem1)
        self.gridLayout_3.addWidget(self.frame_7, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.ketquado)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 2)
        self.frame_6 = QtWidgets.QFrame(self.ketquado)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.formLayout = QtWidgets.QFormLayout(self.frame_6)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineTemp = QtWidgets.QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineTemp.setFont(font)
        self.lineTemp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineTemp.setObjectName("lineTemp")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineTemp)
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineHeight = QtWidgets.QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineHeight.setFont(font)
        self.lineHeight.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineHeight.setObjectName("lineHeight")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineHeight)
        self.label_7 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineWeight = QtWidgets.QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineWeight.setFont(font)
        self.lineWeight.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineWeight.setObjectName("lineWeight")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineWeight)
        self.label_8 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.linePressure = QtWidgets.QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.linePressure.setFont(font)
        self.linePressure.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.linePressure.setObjectName("linePressure")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.linePressure)
        self.linePulse = QtWidgets.QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.linePulse.setFont(font)
        self.linePulse.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.linePulse.setObjectName("linePulse")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.linePulse)
        self.gridLayout_3.addWidget(self.frame_6, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.ketquado)
        self.horizontalLayout.addWidget(self.info_present)
        self.history = QtWidgets.QFrame(self.frame_2)
        self.history.setStyleSheet("background-color: rgb(239, 219, 203);")
        self.history.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.history.setFrameShadow(QtWidgets.QFrame.Raised)
        self.history.setObjectName("history")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.history)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(488, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout.addWidget(self.history)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "THÔNG TIN"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1990"))
        self.comboBox.setItemText(1, _translate("MainWindow", "1991"))
        self.comboBox.setItemText(2, _translate("MainWindow", "1992"))
        self.comboBox.setItemText(3, _translate("MainWindow", "1993"))
        self.comboBox.setItemText(4, _translate("MainWindow", "1994"))
        self.comboBox.setItemText(5, _translate("MainWindow", "1995"))
        self.comboBox.setItemText(6, _translate("MainWindow", "1996"))
        self.comboBox.setItemText(7, _translate("MainWindow", "1997"))
        self.comboBox.setItemText(8, _translate("MainWindow", "1998"))
        self.comboBox.setItemText(9, _translate("MainWindow", "1999"))
        self.comboBox.setItemText(10, _translate("MainWindow", "2000"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Họ và tên"))
        self.radioButton_2.setText(_translate("MainWindow", "Nữ"))
        self.radioButton.setText(_translate("MainWindow", "Nam"))
        self.label_3.setText(_translate("MainWindow", "Mã bệnh nhân"))
        self.label_2.setText(_translate("MainWindow", "Năm sinh"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Lí do khám"))
        self.pushButton.setText(_translate("MainWindow", "Lưu"))
        self.label_4.setText(_translate("MainWindow", "KẾT QUẢ ĐO"))
        self.label_5.setText(_translate("MainWindow", "Nhiệt độ"))
        self.label_6.setText(_translate("MainWindow", "Chiều cao"))
        self.label_7.setText(_translate("MainWindow", "Cân nặng"))
        self.label_8.setText(_translate("MainWindow", "Huyết áp"))
        self.label_9.setText(_translate("MainWindow", "Nhịp tim"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)

#     # UIFunctions.showUart()



#     MainWindow.show()
#     sys.exit(app.exec_())
