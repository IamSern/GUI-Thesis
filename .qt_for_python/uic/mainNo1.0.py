# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainNo1.0.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(893, 694)
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 30))
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(40, 0))
        self.frame_3.setMaximumSize(QSize(70, 16777215))
        self.frame_3.setStyleSheet(u"background-color: rgb(35, 35, 30);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_content = QFrame(self.frame_2)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_content.setFrameShape(QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_content)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_info = QFrame(self.frame_content)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setMaximumSize(QSize(16777215, 150))
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_info)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.frame_info)
        self.lineEdit.setObjectName(u"lineEdit")
        font = QFont()
        font.setFamilies([u"Cambria Math"])
        font.setPointSize(14)
        self.lineEdit.setFont(font)

        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.frame_info)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font)

        self.gridLayout.addWidget(self.radioButton_2, 2, 1, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.frame_info)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setPointSize(14)
        self.plainTextEdit.setFont(font1)

        self.gridLayout.addWidget(self.plainTextEdit, 4, 0, 1, 4)

        self.radioButton = QRadioButton(self.frame_info)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font)

        self.gridLayout.addWidget(self.radioButton, 2, 2, 1, 1)

        self.label = QLabel(self.frame_info)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_info)

        self.frame_spec = QFrame(self.frame_content)
        self.frame_spec.setObjectName(u"frame_spec")
        self.frame_spec.setFrameShape(QFrame.StyledPanel)
        self.frame_spec.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_spec)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.frame_spec)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(13)
        self.label_2.setFont(font3)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_spec)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.label_5 = QLabel(self.frame_spec)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame_spec)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 3, 1, 1)

        self.label_3 = QLabel(self.frame_spec)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_spec)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 1, 1, 1)

        self.label_6 = QLabel(self.frame_spec)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.gridLayout_2.addWidget(self.label_6, 1, 2, 1, 1)

        self.lineEdit_6 = QLineEdit(self.frame_spec)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_2.addWidget(self.lineEdit_6, 1, 3, 1, 1)

        self.label_4 = QLabel(self.frame_spec)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_spec)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_2.addWidget(self.lineEdit_4, 2, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_spec)

        self.frame_history = QFrame(self.frame_content)
        self.frame_history.setObjectName(u"frame_history")
        self.frame_history.setFrameShape(QFrame.StyledPanel)
        self.frame_history.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_history)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableWidget = QTableWidget(self.frame_history)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget.rowCount() < 6):
            self.tableWidget.setRowCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem11)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_3.addWidget(self.tableWidget)


        self.verticalLayout_2.addWidget(self.frame_history)


        self.horizontalLayout.addWidget(self.frame_content)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"H\u1ecd v\u00e0 T\u00ean", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Nam", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"L\u00ed do kh\u00e1m b\u1ec7nh", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"N\u1eef", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TH\u00d4NG TIN", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Chi\u1ec1u cao", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Huy\u1ebft \u00e1p", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"C\u00e2n n\u1eb7ng", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nh\u1ecbp tim", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nhi\u1ec7t \u0111\u1ed9", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
    # retranslateUi

