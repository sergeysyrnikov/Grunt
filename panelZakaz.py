from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QDesktopWidget
import pymysql
from panelMesBox import Ui_mes_box
import globalValues
import time

# globalValues.colorForm = 1

class PanelZakaz(QDialog):

    submitted = QtCore.pyqtSignal()

    strIndexRow = ''

    is_save_data = False

    con = pymysql.connections

    lstLight = [[]]
    lstDark = [[]]
    lengthLight = 0
    lengthDark = 0

    def __init__(self):
                super().__init__()
                self.setupUI()

    def setupUI(self):
        self.setObjectName("Dialog")
        self.resize(1000, 920)
        self.setStyleSheet("")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(415, 5, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(550, 62, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.leNumberZakaz = QtWidgets.QLineEdit(self)
        self.leNumberZakaz.setGeometry(QtCore.QRect(730, 70, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leNumberZakaz.setFont(font)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(30, 177, 131, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnSaveZakaz = QtWidgets.QPushButton(self)
        self.btnSaveZakaz.setGeometry(QtCore.QRect(810, 860, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btnSaveZakaz.setFont(font)
        self.btnSaveZakaz.setObjectName("btnSaveZakaz")
        self.leModelAuto = QtWidgets.QLineEdit(self)
        self.leModelAuto.setGeometry(QtCore.QRect(359, 70, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leModelAuto.setFont(font)
        self.leModelAuto.setText("")
        self.leModelAuto.setObjectName("leModelAuto")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(120, 63, 221, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(654, 112, 51, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.leDate = QtWidgets.QLineEdit(self)
        self.leDate.setGeometry(QtCore.QRect(730, 120, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leDate.setFont(font)
        self.leDate.setText("")
        self.leDate.setObjectName("leDate")
        self.leCompany = QtWidgets.QLineEdit(self)
        self.leCompany.setGeometry(QtCore.QRect(260, 180, 711, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leCompany.setFont(font)
        self.leCompany.setText("")
        self.leCompany.setObjectName("leCompany")
        self.leModelKamaz = QtWidgets.QLineEdit(self)
        self.leModelKamaz.setGeometry(QtCore.QRect(260, 240, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leModelKamaz.setFont(font)
        self.leModelKamaz.setText("")
        self.leModelKamaz.setObjectName("leModelKamaz")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(30, 237, 181, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(30, 297, 321, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.leGRZauto = QtWidgets.QLineEdit(self)
        self.leGRZauto.setGeometry(QtCore.QRect(400, 300, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leGRZauto.setFont(font)
        self.leGRZauto.setText("")
        self.leGRZauto.setObjectName("leGRZauto")
        self.leCarDriver = QtWidgets.QLineEdit(self)
        self.leCarDriver.setGeometry(QtCore.QRect(260, 360, 711, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leCarDriver.setFont(font)
        self.leCarDriver.setText("")
        self.leCarDriver.setObjectName("leCarDriver")
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(30, 357, 91, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(30, 416, 181, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lePassport = QtWidgets.QLineEdit(self)
        self.lePassport.setGeometry(QtCore.QRect(260, 420, 711, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lePassport.setFont(font)
        self.lePassport.setText("")
        self.lePassport.setObjectName("lePassport")
        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(30, 810, 101, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.leDispetcher = QtWidgets.QLineEdit(self)
        self.leDispetcher.setGeometry(QtCore.QRect(260, 810, 711, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leDispetcher.setFont(font)
        self.leDispetcher.setText("")
        self.leDispetcher.setObjectName("leDispetcher")
        self.leComeDriver = QtWidgets.QLineEdit(self)
        self.leComeDriver.setGeometry(QtCore.QRect(260, 680, 711, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leComeDriver.setFont(font)
        self.leComeDriver.setText("")
        self.leComeDriver.setObjectName("leComeDriver")
        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(30, 680, 211, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(30, 740, 201, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.leComeOutDriver = QtWidgets.QLineEdit(self)
        self.leComeOutDriver.setGeometry(QtCore.QRect(260, 742, 711, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leComeOutDriver.setFont(font)
        self.leComeOutDriver.setText("")
        self.leComeOutDriver.setObjectName("leComeOutDriver")
        self.label_15 = QtWidgets.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(30, 480, 191, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(260, 480, 711, 171))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.lblIconJournal = QtWidgets.QLabel(self)
        self.lblIconJournal.setGeometry(QtCore.QRect(385, 8, 23, 23))
        self.lblIconJournal.setText("")
        self.lblIconJournal.setObjectName("lblIconJournal")
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(415, 37, 165, 10))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_134 = QtWidgets.QLabel(self)
        self.label_134.setGeometry(QtCore.QRect(13, 53, 975, 861))
        self.label_134.setText("")
        self.label_134.setObjectName("label_134")
        self.label_50 = QtWidgets.QLabel(self)
        self.label_50.setGeometry(QtCore.QRect(20, 60, 961, 102))
        self.label_50.setText("")
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self)
        self.label_51.setGeometry(QtCore.QRect(20, 170, 961, 491))
        self.label_51.setText("")
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self)
        self.label_52.setGeometry(QtCore.QRect(20, 670, 961, 181))
        self.label_52.setText("")
        self.label_52.setObjectName("label_52")
        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(120, 105, 781, 10))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self)
        self.line_3.setGeometry(QtCore.QRect(30, 220, 938, 10))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self)
        self.line_4.setGeometry(QtCore.QRect(30, 280, 540, 10))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self)
        self.line_5.setGeometry(QtCore.QRect(30, 340, 540, 10))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self)
        self.line_6.setGeometry(QtCore.QRect(30, 400, 938, 10))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self)
        self.line_7.setGeometry(QtCore.QRect(30, 460, 938, 10))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self)
        self.line_8.setGeometry(QtCore.QRect(30, 720, 938, 10))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self)
        self.line_9.setGeometry(QtCore.QRect(30, 790, 938, 10))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.lblBack = QtWidgets.QLabel(self)
        self.lblBack.setGeometry(QtCore.QRect(0, 0, 1000, 920))
        self.lblBack.setText("")
        self.lblBack.setObjectName("lblBack")
        self.lblBack.raise_()
        self.label_134.raise_()
        self.label_52.raise_()
        self.label_51.raise_()
        self.label_50.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.leNumberZakaz.raise_()
        self.label_4.raise_()
        self.btnSaveZakaz.raise_()
        self.leModelAuto.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.leDate.raise_()
        self.leCompany.raise_()
        self.leModelKamaz.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.leGRZauto.raise_()
        self.leCarDriver.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.lePassport.raise_()
        self.label_12.raise_()
        self.leDispetcher.raise_()
        self.leComeDriver.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.leComeOutDriver.raise_()
        self.label_15.raise_()
        self.textEdit.raise_()
        self.lblIconJournal.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.line_8.raise_()
        self.line_9.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.firstStart()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Панель работы с З/Н"))
        self.label.setText(_translate("Dialog", "Заказ-наряд"))
        self.label_3.setText(_translate("Dialog", "№ Заказ-наряда"))
        self.label_4.setText(_translate("Dialog", "Организация"))
        self.btnSaveZakaz.setText(_translate("Dialog", "Сохранить"))
        self.label_6.setText(_translate("Dialog", "Грузового автомобиля"))
        self.label_7.setText(_translate("Dialog", "Дата"))
        self.label_8.setText(_translate("Dialog", "Марка автомобиля"))
        self.label_9.setText(_translate("Dialog", "Государственный номерной знак"))
        self.label_10.setText(_translate("Dialog", "Водитель"))
        self.label_11.setText(_translate("Dialog", "Удостоверение №"))
        self.label_12.setText(_translate("Dialog", "Диспетчер"))
        self.label_13.setText(_translate("Dialog", "Прибытие к заказчику"))
        self.label_14.setText(_translate("Dialog", "Убытие от заказчика"))
        self.label_15.setText(_translate("Dialog", "Задание на работу"))

    def firstStart(self):




       self.lstLight = [[self.label, "background-color: rgb(252,252,252);\n"
                                      "color: rgb(0,0,0);\n"
                                      "border-radius: 5px;"],
                         [self.label_3, "background-color: rgb(235,235,235);\n"
                                        "color: black;"],
                         [self.leNumberZakaz, "background-color: rgb(255,255,255);\n"
                                              "color: rgb(0,0,0);\n"
                                              "border-radius:3px;\n"
                                              "border: 1px solid rgb(150,150,150);"],
                         [self.label_4, "background-color: rgb(235,235,235);\n"
                                        "color: black;"],
                         [self.btnSaveZakaz, "QPushButton:!hover {background-color: rgb(227,227,227);\n"
                                             "color: rgb(0,0,0);\n"
                                             "border-radius:3px;\n"
                                             "border:1px solid rgb(135,135,135);}\n"
                                             "\n"
                                             "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "border-radius:3px;\n"
                                             "border:1px solid rgb(63,63,63);}\n"
                                             "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "border-radius:3px;\n"
                                             "border:1px solid rgb(63,63,63);};"],
                         [self.leModelAuto, "background-color: rgb(255,255,255);\n"
                                            "color: rgb(0,0,0);\n"
                                            "border-radius:3px;\n"
                                            "border: 1px solid rgb(150,150,150);"],
                         [self.label_6, "background-color: rgb(235,235,235);\n"
                                        "color: black;"],
                         [self.label_7, "background-color: rgb(235,235,235);\n"
                                        "color: black;"],
                         [self.leDate, "background-color: rgb(255,255,255);\n"
                                       "color: rgb(0,0,0);\n"
                                       "border-radius:3px;\n"
                                       "border: 1px solid rgb(150,150,150);"],
                         [self.leCompany, "background-color: rgb(255,255,255);\n"
                                          "color: rgb(0,0,0);\n"
                                          "border-radius:3px;\n"
                                          "border: 1px solid rgb(150,150,150);"],
                         [self.leModelKamaz, "background-color: rgb(255,255,255);\n"
                                             "color: rgb(0,0,0);\n"
                                             "border-radius:3px;\n"
                                             "border: 1px solid rgb(150,150,150);"],
                         [self.label_8, "background-color: rgb(235,235,235);\n"
                                        "color: black;"],
                         [self.label_9, "background-color: rgb(235,235,235);\n"
                                        "color: black;"],
                         [self.leGRZauto, "background-color: rgb(255,255,255);\n"
                                          "color: rgb(0,0,0);\n"
                                          "border-radius:3px;\n"
                                          "border: 1px solid rgb(150,150,150);"],
                         [self.leCarDriver, "background-color: rgb(255,255,255);\n"
                                            "color: rgb(0,0,0);\n"
                                            "border-radius:3px;\n"
                                            "border: 1px solid rgb(150,150,150);"],
                         [self.label_10, "background-color: rgb(235,235,235);\n"
                                         "color: black;"],
                         [self.label_11, "background-color: rgb(235,235,235);\n"
                                         "color: black;"],
                         [self.lePassport, "background-color: rgb(255,255,255);\n"
                                           "color: rgb(0,0,0);\n"
                                           "border-radius:3px;\n"
                                           "border: 1px solid rgb(150,150,150);"],
                         [self.label_12, "background-color: rgb(235,235,235);\n"
                                         "color: black;"],
                         [self.leDispetcher, "background-color: rgb(255,255,255);\n"
                                             "color: rgb(0,0,0);\n"
                                             "border-radius:3px;\n"
                                             "border: 1px solid rgb(150,150,150);"],
                         [self.leComeDriver, "background-color: rgb(255,255,255);\n"
                                             "color: rgb(0,0,0);\n"
                                             "border-radius:3px;\n"
                                             "border: 1px solid rgb(150,150,150);"],
                         [self.label_13, "background-color: rgb(235,235,235);\n"
                                         "color: black;"],
                         [self.label_14, "background-color: rgb(235,235,235);\n"
                                         "color: black;"],
                         [self.leComeOutDriver, "background-color: rgb(255,255,255);\n"
                                                "color: rgb(0,0,0);\n"
                                                "border-radius:3px;\n"
                                                "border: 1px solid rgb(150,150,150);"],
                         [self.label_15, "background-color: rgb(235,235,235);\n"
                                         "color: black;"],
                         [self.textEdit, "background-color: rgb(255,255,255);\n"
                                         "color: rgb(0,0,0);\n"
                                         "border-radius:3px;\n"
                                         "border: 1px solid rgb(150,150,150);"],
                         [self.lblIconJournal,
                          "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));\n"
                          "image: url(" + globalValues.pathStyleImgs + "iconworkpanel1.png);"],
                         [self.line, "background-color: rgb(252,252,252);"],
                         [self.label_134, "background-color: rgb(242,242,242);\n"
                                          "border-radius: 10px;\n"
                                          "border: 1px solid rgb(205,205,205);"],
                         [self.label_50, "background-color: rgb(235,235,235);\n"
                                         "border-radius: 10px;\n"
                                         "border: 1px solid rgb(150,150,150);"],
                         [self.label_51, "background-color: rgb(235,235,235);\n"
                                         "border-radius: 10px;\n"
                                         "border: 1px solid rgb(150,150,150);"],
                         [self.label_52, "background-color: rgb(235,235,235);\n"
                                         "border-radius: 10px;\n"
                                         "border: 1px solid rgb(150,150,150);"],
                         [self.line_2, "background-color: rgb(235,235,235);\n"
                                       "color: black;"],
                         [self.line_3, "background-color: rgb(235,235,235);\n"
                                       "color: black;"],
                         [self.line_4, "background-color: rgb(235,235,235);\n"
                                       "color: black;"],
                         [self.line_5, "background-color: rgb(235,235,235);\n"
                                       "color: black;"],
                         [self.line_6, "background-color: rgb(235,235,235);\n"
                                       "color: black;"],
                         [self.line_7, "background-color: rgb(235,235,235);\n"
                                       "color: black;"],
                         [self.line_8, "background-color: rgb(235,235,235);\n"
                                       "color: black;"],
                         [self.line_9, "background-color: rgb(235,235,235);\n"
                                       "color: black;"],
                         [self.lblBack, "background-color: rgb(252,252,252);"]]
       self.lstDark = [[self.label, "background-color: rgb(62,62,62);\n"
                                     "color: rgb(255,255,255);\n"
                                     "border-radius: 5px;"],
                        [self.label_3, "background-color: rgb(75,75,75);\n"
                                       "color: rgb(255,255,255);\n"
                                       "border-radius: 5px;"],
                        [self.leNumberZakaz, "background-color: rgb(42,42,42);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "border-radius: 3px;\n"
                                             "border: 1px solid rgb(63,63,63);"],
                        [self.label_4, "background-color: rgb(75,75,75);\n"
                                       "color: rgb(255,255,255);\n"
                                       "border-radius: 5px;"],
                        [self.btnSaveZakaz, "QPushButton:!hover {background-color: rgb(89,89,89);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius:3px;\n"
                                            "border:1px solid rgb(63,63,63);}\n"
                                            "\n"
                                            "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius:3px;\n"
                                            "border:1px solid rgb(63,63,63);}\n"
                                            "\n"
                                            "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius:3px;\n"
                                            "border:1px solid rgb(63,63,63);};"],
                        [self.leModelAuto, "background-color: rgb(42,42,42);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "border-radius: 3px;\n"
                                           "border: 1px solid rgb(63,63,63);"],
                        [self.label_6, "background-color: rgb(75,75,75);\n"
                                       "color: rgb(255,255,255);\n"
                                       "border-radius: 5px;"],
                        [self.label_7, "background-color: rgb(75,75,75);\n"
                                       "color: rgb(255,255,255);\n"
                                       "border-radius: 5px;"],
                        [self.leDate, "background-color: rgb(42,42,42);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-radius: 3px;\n"
                                      "border: 1px solid rgb(63,63,63);"],
                        [self.leCompany, "background-color: rgb(42, 42, 42);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius: 3px;"],
                        [self.leModelKamaz, "background-color: rgb(42, 42, 42);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius: 3px;"],
                        [self.label_8, "background-color: rgb(75,75,75);\n"
                                       "color: rgb(255,255,255);\n"
                                       "border-radius: 5px;"],
                        [self.label_9, "background-color: rgb(75,75,75);\n"
                                       "color: rgb(255,255,255);\n"
                                       "border-radius: 5px;"],
                        [self.leGRZauto, "background-color: rgb(42, 42, 42);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius: 3px;"],
                        [self.leCarDriver, "background-color: rgb(42, 42, 42);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "border-radius: 3px;"],
                        [self.label_10, "background-color: rgb(75,75,75);\n"
                                        "color: rgb(255,255,255);\n"
                                        "border-radius: 5px;"],
                        [self.label_11, "background-color: rgb(75,75,75);\n"
                                        "color: rgb(255,255,255);\n"
                                        "border-radius: 5px;"],
                        [self.lePassport, "background-color: rgb(42, 42, 42);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-radius: 3px;"],
                        [self.label_12, "background-color: rgb(75,75,75);\n"
                                        "color: rgb(255,255,255);\n"
                                        "border-radius: 5px;"],
                        [self.leDispetcher, "background-color: rgb(42, 42, 42);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius: 3px;"],
                        [self.leComeDriver, "background-color: rgb(42, 42, 42);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius: 3px;"],
                        [self.label_13, "background-color: rgb(75,75,75);\n"
                                        "color: rgb(255,255,255);\n"
                                        "border-radius: 5px;"],
                        [self.label_14, "background-color: rgb(75,75,75);\n"
                                        "color: rgb(255,255,255);\n"
                                        "border-radius: 5px;"],
                        [self.leComeOutDriver, "background-color: rgb(42, 42, 42);\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "border-radius: 3px;"],
                        [self.label_15, "background-color: rgb(75,75,75);\n"
                                        "color: rgb(255,255,255);\n"
                                        "border-radius: 5px;"],
                        [self.textEdit, "background-color: rgb(42, 42, 42);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 3px;"],
                        [self.lblIconJournal,
                         "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));\n"
                         "image: url(" + globalValues.pathStyleImgs + "iconworkpanel1.png);"],
                        [self.line, ""],
                        [self.label_134, "background-color: rgb(66,66,66);\n"
                                         "border-radius: 10px;"],
                        [self.label_50, "background-color: rgb(75,75,75);\n"
                                        "border-radius: 10px;"],
                        [self.label_51, "background-color: rgb(75,75,75);\n"
                                        "border-radius: 10px;"],
                        [self.label_52, "background-color: rgb(75,75,75);\n"
                                        "border-radius: 10px;"],
                        [self.line_2, "background-color: rgb(75,75,75);"],
                        [self.line_3, "background-color: rgb(75,75,75);"],
                        [self.line_4, "background-color: rgb(75,75,75);"],
                        [self.line_5, "background-color: rgb(75,75,75);"],
                        [self.line_6, "background-color: rgb(75,75,75);"],
                        [self.line_7, "background-color: rgb(75,75,75);"],
                        [self.line_8, "background-color: rgb(75,75,75);"],
                        [self.line_9, "background-color: rgb(75,75,75);"],
                        [self.lblBack, "background-color: rgb(62,62,62);"]]

       self.lengthLight = len(self.lstLight)
       self.lengthDark = len(self.lstDark)

       self.changeCOLORMainPanelGrunt()

       resolution = QDesktopWidget().screenGeometry()
       self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                 (resolution.height() / 2) - (self.frameSize().height() / 2))
       self.setWindowModality(QtCore.Qt.ApplicationModal)
       self.btnSaveZakaz.clicked.connect(self.saveDataDatabase)
       self.connectToMySql()

    def saveDataDatabase(self):

       uiMes = Ui_mes_box()
       uiMes.lblStrInfo.setText('Вы уверены, что хотите сохранить заказ?')
       uiMes.btnOK.setText('Да')
       uiMes.btnCancel.setText('Нет')
       uiMes.exec_()

       if (uiMes.checkCont):

           try:
               try:
                   if (self.checkMySql):
                       self.con = pymysql.connect(host=globalValues.my_sql_localhost,
                                                  port=globalValues.my_sql_port,
                                                  user=globalValues.my_sql_name,
                                                  passwd=globalValues.my_sql_password, db=globalValues.dbMySqlName)
               except Exception as ex:
                   globalValues.writeLogData('', str(ex))
               numberGRZ = self.leGRZauto.text()
               strGRZ = str(numberGRZ)
               strNumberZakaz_ = self.leNumberZakaz.text()
               if (strNumberZakaz_ != '' and strGRZ != ''):
                   numberZakaz = int(strNumberZakaz_)
                   carName = str(self.leModelAuto.text())
                   dateJob = self.leDate.text()
                   nameCompany = self.leCompany.text()
                   carModel = self.leModelKamaz.text()
                   carDriver = self.leCarDriver.text()
                   driverDocument = self.lePassport.text()
                   taskJob = self.textEdit.toPlainText()
                   timeComeIn = self.leComeDriver.text()
                   timeComeOut = self.leComeOutDriver.text()
                   nameOperator = self.leDispetcher.text()
                   strNumberZakaz = str(numberZakaz)

                   try:

                       cur = self.con.cursor()

                       with self.con:
                           if (self.strIndexRow == ''):
                               query = ("INSERT INTO " + globalValues.tblsDB[1] + " (number_order, number_grz, date, state_order) VALUES ( %s, %s, %s, \'выполняется\')")
                               cur.execute(query, (numberZakaz, strGRZ, dateJob))
                               self.con.commit()

                               query = ("INSERT INTO " + globalValues.tblsDB[5] + " (weight) VALUES ( \'не измерена\')")
                               cur.execute(query)
                               self.con.commit()

                           else:
                               cur.execute("SELECT * FROM " + globalValues.tblsDB[1])

                               rows = cur.fetchall()

                               valWdg = 0

                               for row in reversed(rows):
                                   if(self.strIndexRow == str(valWdg)):
                                       query = ("UPDATE " + globalValues.tblsDB[1] + " SET number_order = (%s), number_grz = (%s) WHERE id= (%s)")
                                       cur.execute(query, (numberZakaz, strGRZ, str(row[0])))

                                       self.con.commit()
                                   valWdg += 1


                           if (self.strIndexRow == ''):
                                 query = ("INSERT INTO " + globalValues.tblsDB[2] + " (car_name, number_order, date_work, name_company, car_model, car_grz, car_driver, driver_document, task_work, time_come_in, time_come_out, name_operator) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                                 cur.execute(query, (carName, strNumberZakaz, dateJob, nameCompany, carModel,  strGRZ, carDriver,driverDocument, taskJob, timeComeIn, timeComeOut, nameOperator))
                                 self.con.commit()

                                 sqlMy = "INSERT INTO " + globalValues.tblsDB[4] + " (url) VALUES (%s)"
                                 cur.execute(sqlMy, ('http://'))
                                 self.con.commit()
                           else:
                                 cur.execute("SELECT * FROM " + globalValues.tblsDB[2])

                                 rows = cur.fetchall()

                                 valWdg = 0

                                 for row in reversed(rows):
                                     if (self.strIndexRow == str(valWdg)):
                                         query = ("UPDATE " + globalValues.tblsDB[2] + " SET car_name = (%s), number_order = (%s), date_work = (%s), name_company = (%s), car_model = (%s), car_grz = (%s), car_driver = (%s), driver_document = (%s), task_work = (%s), time_come_in = (%s), time_come_out = (%s), name_operator = (%s) WHERE id= (%s)")
                                         cur.execute(query, (carName, strNumberZakaz, dateJob, nameCompany, carModel,  strGRZ, carDriver,driverDocument, taskJob, timeComeIn, timeComeOut, nameOperator, str(row[0])))
                                         self.con.commit()
                                     valWdg += 1

                       cur.close()

                   except Exception as ex:
                       globalValues.writeLogData('Функция сохранения заказ-наряда на выполнение работ БД', str(ex))

                   self.is_save_data = True
                   self.con.close()
                   self.close()

               else:
                   try:
                       uiMes = Ui_mes_box()
                       uiMes.lblStrInfo.setText('Панель З/Н некорректно заполнена!')
                       uiMes.btnOK.hide()
                       if(globalValues.colorForm == 1):
                           uiMes.label_iconques.setStyleSheet("background-color: rgb(235,235,235);\n"
                                                              "image: url(" + globalValues.pathStyleImgs + "icnAtt.png);")
                       else:
                           uiMes.label_iconques.setStyleSheet("background-color: rgb(75,75,75);\n"
                                                          "image: url(" + globalValues.pathStyleImgs + "icnAtt.png);")
                       uiMes.btnCancel.setText('Продолжить')
                       uiMes.exec_()

                   except Exception as ex:
                       globalValues.writeLogData('Функция сохранения З/Н, панель некорректно заполнена', str(ex))
           except Exception as ex:
               globalValues.writeLogData('Функция сохранения заказ-наряда на выполнение работ', str(ex))

    def closeEvent(self, event):

         # try:
         #    self.con.close()
         # except Exception as ex:
         #     globalValues.writeLogData('Закрытие БД панель заказа')
         self.submitted.emit()
         event.accept()

    def connectToMySql(self):
        i = 0
        while True:
            try:
                    self.con = pymysql.connect(host=globalValues.my_sql_localhost,
                                                   port=globalValues.my_sql_port,
                                                   user=globalValues.my_sql_name,
                                                   passwd=globalValues.my_sql_password, db=globalValues.dbMySqlName)
                    if (self.con.open):
                        break

            except Exception as ex:
                globalValues.writeLogData('Функция подключения к БД панель З/Н', str(ex))

            i += 1

            if (i > 2):
                break

    def checkMySql(self):
        try:
                if (self.con.open):
                        return False
                else:
                        return True
        except Exception as ex:
                globalValues.writeLogData('Функция проверки подключения к бд MySql панель З/Н', str(ex))

    def closePanel(self):
        self.close()

    def changeColor(self, object, str):
            object.setStyleSheet(str)

    def changeCOLORMainPanelGrunt(self):

            delta = int((0.4/self.lengthDark)*1000)


            if (globalValues.colorForm == 1):

                    for i in range(self.lengthLight):
                        startTime = round(time.time() * 1000)
                        while True:
                                    obj = self.lstLight[i][0]
                                    style = self.lstLight[i][1]
                                    self.changeColor(obj, style)
                                    # print('changeLight!')
                                    if (abs(round(time.time()*1000) - startTime) > delta):
                                            break

            elif (globalValues.colorForm == 0):

                    for i in range(self.lengthDark):
                        startTime = round(time.time() * 1000)
                        while True:
                                    # print(delta)
                                    # print(abs(round(time.time()*1000) - startTime))
                                    obj = self.lstDark[i][0]
                                    style = self.lstDark[i][1]
                                    self.changeColor(obj, style)
                                    # print('changeDark!')
                                    if (abs(round(time.time()*1000) - startTime) > delta):
                                            break

if __name__ == "__main__":
   import sys
   app = QtWidgets.QApplication(sys.argv)
   mw = PanelZakaz()
   mw.show()
   sys.exit(app.exec_())