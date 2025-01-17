# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainNo2.0.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.line_ID = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.line_ID.setFont(font)
        self.line_ID.setStyleSheet("")
        self.line_ID.setObjectName("line_ID")
        self.gridLayout.addWidget(self.line_ID, 2, 3, 1, 1)
        self.line_name = QtWidgets.QLineEdit(self.frame_3)
        self.line_name.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        self.line_name.setFont(font)
        self.line_name.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(52, 93, 167);\n"
"border-radius: 7px;\n"
"color: rgb(42, 42, 42);\n"
"padding-left: 5px;\n"
"padding-rignt: 5px;\n"
"}")
        self.line_name.setObjectName("line_name")
        self.gridLayout.addWidget(self.line_name, 0, 0, 1, 5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"border-bottom: 2px solidrgb(52, 93, 167)\n"
"}")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.box_year = QtWidgets.QComboBox(self.frame_3)
        self.box_year.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.box_year.setFont(font)
        self.box_year.setObjectName("box_year")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.box_year.addItem("")
        self.gridLayout.addWidget(self.box_year, 1, 2, 1, 1)
        self.gender_female = QtWidgets.QRadioButton(self.frame_3)
        self.gender_female.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.gender_female.setFont(font)
        self.gender_female.setObjectName("gender_female")
        self.gridLayout.addWidget(self.gender_female, 0, 6, 1, 1)
        self.gender_male = QtWidgets.QRadioButton(self.frame_3)
        self.gender_male.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.gender_male.setFont(font)
        self.gender_male.setStyleSheet("QRadioButton::indicator::checked{\n"
"\n"
"    color: rgb(255, 0, 0);\n"
"}\n"
"QRadioButton::indicator{\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}")
        self.gender_male.setObjectName("gender_male")
        self.gridLayout.addWidget(self.gender_male, 0, 5, 1, 1)
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
        self.text_reason = QtWidgets.QTextEdit(self.frame_5)
        self.text_reason.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.text_reason.setFont(font)
        self.text_reason.setObjectName("text_reason")
        self.horizontalLayout_3.addWidget(self.text_reason)
        self.button_save = QtWidgets.QPushButton(self.frame_5)
        self.button_save.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_save.setFont(font)
        self.button_save.setStyleSheet("QPushButton{\n"
"color: rgb(85, 0, 127);\n"
"background-color: rgb(59, 138, 196);\n"
"border: 2px solid rgb(52, 93, 167);\n"
"border-radius: 8px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(75, 180, 222);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(52, 93, 167);\n"
"}\n"
"")
        self.button_save.setObjectName("button_save")
        self.horizontalLayout_3.addWidget(self.button_save)
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
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_7 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_8 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.gridLayout_3.addWidget(self.frame_6, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.ketquado)
        self.horizontalLayout.addWidget(self.info_present)
        self.history = QtWidgets.QFrame(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.history.setFont(font)
        self.history.setStyleSheet("background-color: rgb(239, 219, 203);")
        self.history.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.history.setFrameShadow(QtWidgets.QFrame.Raised)
        self.history.setObjectName("history")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.history)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.history)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QScrolBar:horizontal{\n"
"color: rgb(255, 0, 0);\n"
"\n"
"}")
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.verticalLayout_4.addWidget(self.tableWidget)
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
        self.line_name.setPlaceholderText(_translate("MainWindow", "Họ và tên"))
        self.label_3.setText(_translate("MainWindow", "Mã bệnh nhân"))
        self.label_2.setText(_translate("MainWindow", "Năm sinh"))
        self.box_year.setItemText(0, _translate("MainWindow", "1969"))
        self.box_year.setItemText(1, _translate("MainWindow", "1970"))
        self.box_year.setItemText(2, _translate("MainWindow", "1971"))
        self.box_year.setItemText(3, _translate("MainWindow", "1972"))
        self.box_year.setItemText(4, _translate("MainWindow", "1973"))
        self.box_year.setItemText(5, _translate("MainWindow", "1975"))
        self.box_year.setItemText(6, _translate("MainWindow", "1976"))
        self.box_year.setItemText(7, _translate("MainWindow", "1977"))
        self.box_year.setItemText(8, _translate("MainWindow", "1978"))
        self.box_year.setItemText(9, _translate("MainWindow", "1979"))
        self.box_year.setItemText(10, _translate("MainWindow", "1980"))
        self.box_year.setItemText(11, _translate("MainWindow", "1981"))
        self.box_year.setItemText(12, _translate("MainWindow", "1983"))
        self.box_year.setItemText(13, _translate("MainWindow", "1983"))
        self.box_year.setItemText(14, _translate("MainWindow", "1984"))
        self.box_year.setItemText(15, _translate("MainWindow", "1985"))
        self.box_year.setItemText(16, _translate("MainWindow", "1986"))
        self.box_year.setItemText(17, _translate("MainWindow", "1987"))
        self.box_year.setItemText(18, _translate("MainWindow", "1988"))
        self.box_year.setItemText(19, _translate("MainWindow", "1989"))
        self.box_year.setItemText(20, _translate("MainWindow", "1990"))
        self.box_year.setItemText(21, _translate("MainWindow", "1991"))
        self.box_year.setItemText(22, _translate("MainWindow", "1992"))
        self.box_year.setItemText(23, _translate("MainWindow", "1993"))
        self.box_year.setItemText(24, _translate("MainWindow", "1994"))
        self.box_year.setItemText(25, _translate("MainWindow", "1995"))
        self.box_year.setItemText(26, _translate("MainWindow", "1996"))
        self.box_year.setItemText(27, _translate("MainWindow", "1997"))
        self.box_year.setItemText(28, _translate("MainWindow", "1998"))
        self.box_year.setItemText(29, _translate("MainWindow", "1999"))
        self.box_year.setItemText(30, _translate("MainWindow", "2000"))
        self.gender_female.setText(_translate("MainWindow", "Nữ"))
        self.gender_male.setText(_translate("MainWindow", "Nam"))
        self.text_reason.setPlaceholderText(_translate("MainWindow", "Lí do khám"))
        self.button_save.setText(_translate("MainWindow", "Lưu"))
        self.label_4.setText(_translate("MainWindow", "KẾT QUẢ ĐO"))
        self.label_5.setText(_translate("MainWindow", "Nhiệt độ"))
        self.label_6.setText(_translate("MainWindow", "Chiều cao"))
        self.label_7.setText(_translate("MainWindow", "Cân nặng"))
        self.label_8.setText(_translate("MainWindow", "Huyết áp"))
        self.label_9.setText(_translate("MainWindow", "Nhịp tim"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Thời gian"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tên"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Giới tính"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Kết quả"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Lí do khám"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
