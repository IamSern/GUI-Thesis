# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainNo2.0.ui'
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
        MainWindow.resize(1080, 720)
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
        self.frame.setStyleSheet(u"background-color: rgb(161, 99, 127);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.info_present = QFrame(self.frame_2)
        self.info_present.setObjectName(u"info_present")
        self.info_present.setFrameShape(QFrame.StyledPanel)
        self.info_present.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.info_present)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.thongtincanhan = QFrame(self.info_present)
        self.thongtincanhan.setObjectName(u"thongtincanhan")
        self.thongtincanhan.setMaximumSize(QSize(16777215, 400))
        self.thongtincanhan.setFrameShape(QFrame.StyledPanel)
        self.thongtincanhan.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.thongtincanhan)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.thongtincanhan)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 60))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.thongtincanhan)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(9)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(20, 0, 20, 0)
        self.line_ID = QLineEdit(self.frame_3)
        self.line_ID.setObjectName(u"line_ID")
        font1 = QFont()
        font1.setFamilies([u"Cambria"])
        font1.setPointSize(14)
        self.line_ID.setFont(font1)
        self.line_ID.setStyleSheet(u"")

        self.gridLayout.addWidget(self.line_ID, 2, 3, 1, 1)

        self.line_name = QLineEdit(self.frame_3)
        self.line_name.setObjectName(u"line_name")
        self.line_name.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setFamilies([u"Cambria"])
        font2.setPointSize(18)
        self.line_name.setFont(font2)
        self.line_name.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid rgb(52, 93, 167);\n"
"border-radius: 7px;\n"
"color: rgb(42, 42, 42);\n"
"padding-left: 5px;\n"
"padding-rignt: 5px;\n"
"}")

        self.gridLayout.addWidget(self.line_name, 0, 0, 1, 5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamilies([u"Cambria"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.label_3.setFont(font3)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 3)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"QLabel{\n"
"border-bottom: 2px solidrgb(52, 93, 167)\n"
"}")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.box_year = QComboBox(self.frame_3)
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
        self.box_year.setObjectName(u"box_year")
        self.box_year.setMaximumSize(QSize(70, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Cambria"])
        font4.setPointSize(14)
        font4.setBold(False)
        self.box_year.setFont(font4)

        self.gridLayout.addWidget(self.box_year, 1, 2, 1, 1)

        self.gender_female = QRadioButton(self.frame_3)
        self.gender_female.setObjectName(u"gender_female")
        self.gender_female.setMinimumSize(QSize(70, 0))
        font5 = QFont()
        font5.setFamilies([u"Cambria"])
        font5.setPointSize(15)
        font5.setBold(True)
        self.gender_female.setFont(font5)

        self.gridLayout.addWidget(self.gender_female, 0, 6, 1, 1)

        self.gender_male = QRadioButton(self.frame_3)
        self.gender_male.setObjectName(u"gender_male")
        self.gender_male.setMinimumSize(QSize(70, 0))
        font6 = QFont()
        font6.setFamilies([u"Candara"])
        font6.setPointSize(15)
        font6.setBold(True)
        self.gender_male.setFont(font6)
        self.gender_male.setStyleSheet(u"QRadioButton::indicator::checked{\n"
"\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QRadioButton::indicator{\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}")

        self.gridLayout.addWidget(self.gender_male, 0, 5, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.thongtincanhan)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 150))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 0, 20, 6)
        self.text_reason = QTextEdit(self.frame_5)
        self.text_reason.setObjectName(u"text_reason")
        self.text_reason.setMaximumSize(QSize(16777215, 16777215))
        self.text_reason.setFont(font1)

        self.horizontalLayout_3.addWidget(self.text_reason)

        self.button_save = QPushButton(self.frame_5)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setMinimumSize(QSize(80, 50))
        self.button_save.setFont(font3)
        self.button_save.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_3.addWidget(self.button_save)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.thongtincanhan)

        self.ketquado = QFrame(self.info_present)
        self.ketquado.setObjectName(u"ketquado")
        self.ketquado.setMinimumSize(QSize(0, 350))
        self.ketquado.setStyleSheet(u"background-color: rgb(75, 180, 222);")
        self.ketquado.setFrameShape(QFrame.StyledPanel)
        self.ketquado.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.ketquado)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 10, 0, 0)
        self.frame_7 = QFrame(self.ketquado)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(259, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer_3)


        self.gridLayout_3.addWidget(self.frame_7, 1, 1, 1, 1)

        self.label_4 = QLabel(self.ketquado)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 50))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 2)

        self.frame_6 = QFrame(self.ketquado)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_6)
        self.formLayout.setObjectName(u"formLayout")
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_3 = QLineEdit(self.frame_6)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        font7 = QFont()
        font7.setPointSize(12)
        self.lineEdit_3.setFont(font7)
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_4 = QLineEdit(self.frame_6)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font7)
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_4)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.lineEdit_5 = QLineEdit(self.frame_6)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFont(font7)
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_5)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_9)

        self.lineEdit_6 = QLineEdit(self.frame_6)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFont(font7)
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.frame_6)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setFont(font7)
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_7)


        self.gridLayout_3.addWidget(self.frame_6, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.ketquado)


        self.horizontalLayout.addWidget(self.info_present)

        self.history = QFrame(self.frame_2)
        self.history.setObjectName(u"history")
        font8 = QFont()
        font8.setPointSize(8)
        self.history.setFont(font8)
        self.history.setStyleSheet(u"background-color: rgb(239, 219, 203);")
        self.history.setFrameShape(QFrame.StyledPanel)
        self.history.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.history)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.history)
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
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font7)
        self.tableWidget.setStyleSheet(u"QScrolBar:horizontal{\n"
"color: rgb(255, 0, 0);\n"
"\n"
"}")
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_4.addWidget(self.tableWidget)


        self.horizontalLayout.addWidget(self.history)


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
        self.label.setText(QCoreApplication.translate("MainWindow", u"TH\u00d4NG TIN", None))
        self.line_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"H\u1ecd v\u00e0 t\u00ean", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 b\u1ec7nh nh\u00e2n", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"N\u0103m sinh", None))
        self.box_year.setItemText(0, QCoreApplication.translate("MainWindow", u"1969", None))
        self.box_year.setItemText(1, QCoreApplication.translate("MainWindow", u"1970", None))
        self.box_year.setItemText(2, QCoreApplication.translate("MainWindow", u"1971", None))
        self.box_year.setItemText(3, QCoreApplication.translate("MainWindow", u"1972", None))
        self.box_year.setItemText(4, QCoreApplication.translate("MainWindow", u"1973", None))
        self.box_year.setItemText(5, QCoreApplication.translate("MainWindow", u"1975", None))
        self.box_year.setItemText(6, QCoreApplication.translate("MainWindow", u"1976", None))
        self.box_year.setItemText(7, QCoreApplication.translate("MainWindow", u"1977", None))
        self.box_year.setItemText(8, QCoreApplication.translate("MainWindow", u"1978", None))
        self.box_year.setItemText(9, QCoreApplication.translate("MainWindow", u"1979", None))
        self.box_year.setItemText(10, QCoreApplication.translate("MainWindow", u"1980", None))
        self.box_year.setItemText(11, QCoreApplication.translate("MainWindow", u"1981", None))
        self.box_year.setItemText(12, QCoreApplication.translate("MainWindow", u"1983", None))
        self.box_year.setItemText(13, QCoreApplication.translate("MainWindow", u"1983", None))
        self.box_year.setItemText(14, QCoreApplication.translate("MainWindow", u"1984", None))
        self.box_year.setItemText(15, QCoreApplication.translate("MainWindow", u"1985", None))
        self.box_year.setItemText(16, QCoreApplication.translate("MainWindow", u"1986", None))
        self.box_year.setItemText(17, QCoreApplication.translate("MainWindow", u"1987", None))
        self.box_year.setItemText(18, QCoreApplication.translate("MainWindow", u"1988", None))
        self.box_year.setItemText(19, QCoreApplication.translate("MainWindow", u"1989", None))
        self.box_year.setItemText(20, QCoreApplication.translate("MainWindow", u"1990", None))
        self.box_year.setItemText(21, QCoreApplication.translate("MainWindow", u"1991", None))
        self.box_year.setItemText(22, QCoreApplication.translate("MainWindow", u"1992", None))
        self.box_year.setItemText(23, QCoreApplication.translate("MainWindow", u"1993", None))
        self.box_year.setItemText(24, QCoreApplication.translate("MainWindow", u"1994", None))
        self.box_year.setItemText(25, QCoreApplication.translate("MainWindow", u"1995", None))
        self.box_year.setItemText(26, QCoreApplication.translate("MainWindow", u"1996", None))
        self.box_year.setItemText(27, QCoreApplication.translate("MainWindow", u"1997", None))
        self.box_year.setItemText(28, QCoreApplication.translate("MainWindow", u"1998", None))
        self.box_year.setItemText(29, QCoreApplication.translate("MainWindow", u"1999", None))
        self.box_year.setItemText(30, QCoreApplication.translate("MainWindow", u"2000", None))

        self.gender_female.setText(QCoreApplication.translate("MainWindow", u"N\u1eef", None))
        self.gender_male.setText(QCoreApplication.translate("MainWindow", u"Nam", None))
        self.text_reason.setPlaceholderText(QCoreApplication.translate("MainWindow", u"L\u00ed do kh\u00e1m", None))
        self.button_save.setText(QCoreApplication.translate("MainWindow", u"L\u01b0u", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"K\u1ebeT QU\u1ea2 \u0110O", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nhi\u1ec7t \u0111\u1ed9", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Chi\u1ec1u cao", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"C\u00e2n n\u1eb7ng", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Huy\u1ebft \u00e1p", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Nh\u1ecbp tim", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"T\u00ean", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Gi\u1edbi t\u00ednh", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"K\u1ebft qu\u1ea3", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"L\u00ed do kh\u00e1m", None));
    # retranslateUi

