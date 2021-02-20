from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import threading
import time
import sys
import globalValues
import pymysql
from panelMesBox import Ui_mes_box
import os
import subprocess

app = QtWidgets.QApplication(sys.argv)

class Ui_add_TS(QDialog):

    lstLight = [[]]
    lstDark = [[]]
    lengthLight = 0
    lengthDark = 0
    delta = 40
    num = 0

    is_save_data = False

    con = pymysql.connections

    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("Dialog")
        self.setFixedSize(630, 380)
        self.setStyleSheet("")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(215, 5, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 131, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnAddZakaz = QtWidgets.QPushButton(self)
        self.btnAddZakaz.setGeometry(QtCore.QRect(475, 340, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnAddZakaz.setFont(font)
        self.btnAddZakaz.setObjectName("btnAddZakaz")
        self.leCompany = QtWidgets.QLineEdit(self)
        self.leCompany.setGeometry(QtCore.QRect(144, 65, 461, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leCompany.setFont(font)
        self.leCompany.setText("")
        self.leCompany.setObjectName("leCompany")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(20, 100, 191, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(20, 180, 51, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.leTSgrz = QtWidgets.QLineEdit(self)
        self.leTSgrz.setGeometry(QtCore.QRect(144, 185, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leTSgrz.setFont(font)
        self.leTSgrz.setText("")
        self.leTSgrz.setObjectName("leTSgrz")
        self.leTScreatdate = QtWidgets.QLineEdit(self)
        self.leTScreatdate.setGeometry(QtCore.QRect(144, 225, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leTScreatdate.setFont(font)
        self.leTScreatdate.setText("")
        self.leTScreatdate.setObjectName("leTScreatdate")
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(20, 220, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(320, 140, 141, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.leTSweightEmpty = QtWidgets.QLineEdit(self)
        self.leTSweightEmpty.setGeometry(QtCore.QRect(455, 145, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leTSweightEmpty.setFont(font)
        self.leTSweightEmpty.setText("")
        self.leTSweightEmpty.setObjectName("leTSweightEmpty")
        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(320, 100, 101, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.leTSdvigVilume = QtWidgets.QLineEdit(self)
        self.leTSdvigVilume.setGeometry(QtCore.QRect(455, 105, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leTSdvigVilume.setFont(font)
        self.leTSdvigVilume.setText("")
        self.leTSdvigVilume.setObjectName("leTSdvigVilume")
        self.leTSweightMaxAllow = QtWidgets.QLineEdit(self)
        self.leTSweightMaxAllow.setGeometry(QtCore.QRect(455, 185, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leTSweightMaxAllow.setFont(font)
        self.leTSweightMaxAllow.setText("")
        self.leTSweightMaxAllow.setObjectName("leTSweightMaxAllow")
        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(20, 260, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(20, 300, 181, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.leTSpowerLS = QtWidgets.QLineEdit(self)
        self.leTSpowerLS.setGeometry(QtCore.QRect(144, 305, 36, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leTSpowerLS.setFont(font)
        self.leTSpowerLS.setText("")
        self.leTSpowerLS.setObjectName("leTSpowerLS")
        self.label_15 = QtWidgets.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(20, 140, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.lblIconJournal = QtWidgets.QLabel(self)
        self.lblIconJournal.setGeometry(QtCore.QRect(185, 8, 23, 23))
        self.lblIconJournal.setText("")
        self.lblIconJournal.setObjectName("lblIconJournal")
        self.line_7 = QtWidgets.QFrame(self)
        self.line_7.setGeometry(QtCore.QRect(320, 170, 287, 10))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self)
        self.line_8.setGeometry(QtCore.QRect(320, 250, 287, 10))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self)
        self.line_9.setGeometry(QtCore.QRect(320, 290, 287, 10))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.lblBack = QtWidgets.QLabel(self)
        self.lblBack.setGeometry(QtCore.QRect(0, 0, 631, 380))
        self.lblBack.setText("")
        self.lblBack.setObjectName("lblBack")
        self.cb_TSname = QtWidgets.QComboBox(self)
        self.cb_TSname.setGeometry(QtCore.QRect(144, 105, 131, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cb_TSname.setFont(font)
        self.cb_TSname.setObjectName("cb_TSname")
        self.cb_TSname.addItem("")
        self.leTSname = QtWidgets.QLineEdit(self)
        self.leTSname.setGeometry(QtCore.QRect(144, 145, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leTSname.setFont(font)
        self.leTSname.setText("")
        self.leTSname.setObjectName("leTSname")
        self.line_4 = QtWidgets.QFrame(self)
        self.line_4.setGeometry(QtCore.QRect(20, 90, 585, 10))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self)
        self.line_5.setGeometry(QtCore.QRect(20, 130, 255, 10))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self)
        self.line_6.setGeometry(QtCore.QRect(20, 170, 255, 10))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_10 = QtWidgets.QFrame(self)
        self.line_10.setGeometry(QtCore.QRect(20, 210, 255, 10))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.cb_EurocCassNUM = QtWidgets.QComboBox(self)
        self.cb_EurocCassNUM.setGeometry(QtCore.QRect(144, 265, 41, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cb_EurocCassNUM.setFont(font)
        self.cb_EurocCassNUM.setObjectName("cb_EurocCassNUM")
        self.cb_EurocCassNUM.addItem("")
        self.cb_EurocCassNUM.addItem("")
        self.cb_EurocCassNUM.addItem("")
        self.line_11 = QtWidgets.QFrame(self)
        self.line_11.setGeometry(QtCore.QRect(20, 250, 255, 10))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self)
        self.line_12.setGeometry(QtCore.QRect(20, 290, 255, 10))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.leTSpowerkWt = QtWidgets.QLineEdit(self)
        self.leTSpowerkWt.setGeometry(QtCore.QRect(214, 305, 36, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leTSpowerkWt.setFont(font)
        self.leTSpowerkWt.setText("")
        self.leTSpowerkWt.setObjectName("leTSpowerkWt")
        self.label_17 = QtWidgets.QLabel(self)
        self.label_17.setGeometry(QtCore.QRect(183, 300, 27, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self)
        self.label_18.setGeometry(QtCore.QRect(254, 300, 21, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.line_15 = QtWidgets.QFrame(self)
        self.line_15.setGeometry(QtCore.QRect(320, 130, 287, 10))
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.label_19 = QtWidgets.QLabel(self)
        self.label_19.setGeometry(QtCore.QRect(563, 100, 44, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self)
        self.label_20.setGeometry(QtCore.QRect(590, 140, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_16 = QtWidgets.QLabel(self)
        self.label_16.setGeometry(QtCore.QRect(320, 180, 121, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_21 = QtWidgets.QLabel(self)
        self.label_21.setGeometry(QtCore.QRect(590, 180, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.line_16 = QtWidgets.QFrame(self)
        self.line_16.setGeometry(QtCore.QRect(320, 210, 287, 10))
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.label_22 = QtWidgets.QLabel(self)
        self.label_22.setGeometry(QtCore.QRect(590, 220, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.leTSweightGruntMaxAllow = QtWidgets.QLineEdit(self)
        self.leTSweightGruntMaxAllow.setGeometry(QtCore.QRect(455, 225, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leTSweightGruntMaxAllow.setFont(font)
        self.leTSweightGruntMaxAllow.setText("")
        self.leTSweightGruntMaxAllow.setObjectName("leTSweightGruntMaxAllow")
        self.label_23 = QtWidgets.QLabel(self)
        self.label_23.setGeometry(QtCore.QRect(320, 220, 121, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self)
        self.label_24.setGeometry(QtCore.QRect(320, 260, 131, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self)
        self.label_25.setGeometry(QtCore.QRect(590, 260, 21, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.leTSvolumeMax = QtWidgets.QLineEdit(self)
        self.leTSvolumeMax.setGeometry(QtCore.QRect(455, 265, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leTSvolumeMax.setFont(font)
        self.leTSvolumeMax.setText("")
        self.leTSvolumeMax.setObjectName("leTSvolumeMax")
        self.label_26 = QtWidgets.QLabel(self)
        self.label_26.setGeometry(QtCore.QRect(320, 300, 121, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.leTSwheelScheme = QtWidgets.QLineEdit(self)
        self.leTSwheelScheme.setGeometry(QtCore.QRect(455, 305, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leTSwheelScheme.setFont(font)
        self.leTSwheelScheme.setText("")
        self.leTSwheelScheme.setObjectName("leTSwheelScheme")
        self.lblBack.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.btnAddZakaz.raise_()
        self.leCompany.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.leTSgrz.raise_()
        self.leTScreatdate.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.leTSweightEmpty.raise_()
        self.label_12.raise_()
        self.leTSdvigVilume.raise_()
        self.leTSweightMaxAllow.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.leTSpowerLS.raise_()
        self.label_15.raise_()
        self.lblIconJournal.raise_()
        self.line_7.raise_()
        self.line_8.raise_()
        self.line_9.raise_()
        self.cb_TSname.raise_()
        self.leTSname.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.line_10.raise_()
        self.cb_EurocCassNUM.raise_()
        self.line_11.raise_()
        self.line_12.raise_()
        self.leTSpowerkWt.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.line_15.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_16.raise_()
        self.label_21.raise_()
        self.line_16.raise_()
        self.label_22.raise_()
        self.leTSweightGruntMaxAllow.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.leTSvolumeMax.raise_()
        self.label_26.raise_()
        self.leTSwheelScheme.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        # self.runThJournal()
        self.firstCall()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Панель добавления нового ТС"))
        self.label.setText(_translate("Dialog", "Добавление ТС в систему"))
        self.label_4.setText(_translate("Dialog", "Организация:"))
        self.btnAddZakaz.setText(_translate("Dialog", "Добавить"))
        self.label_8.setText(_translate("Dialog", "Наименование ТС:"))
        self.label_9.setText(_translate("Dialog", "Рег. №:"))
        self.label_10.setText(_translate("Dialog", "Год изготовления:"))
        self.label_11.setText(_translate("Dialog", "Масса пустой:"))
        self.label_12.setText(_translate("Dialog", "Объем двиг-ля:"))
        self.label_13.setText(_translate("Dialog", "Эко.класс ЕВРО:"))
        self.label_14.setText(_translate("Dialog", "Мощность двиг-ля:"))
        self.label_15.setText(_translate("Dialog", "Модель ТС:"))
        self.cb_TSname.setItemText(0, _translate("Dialog", "Самосвал"))
        self.cb_EurocCassNUM.setItemText(0, _translate("Dialog", "5"))
        self.cb_EurocCassNUM.setItemText(1, _translate("Dialog", "4"))
        self.cb_EurocCassNUM.setItemText(2, _translate("Dialog", "3"))
        self.label_17.setText(_translate("Dialog", "л.с.,"))
        self.label_18.setText(_translate("Dialog", "кВт"))
        self.label_19.setText(_translate("Dialog", "куб.см."))
        self.label_20.setText(_translate("Dialog", "кг."))
        self.label_16.setText(_translate("Dialog", "Макс. разр. масса:"))
        self.label_21.setText(_translate("Dialog", "кг."))
        self.label_22.setText(_translate("Dialog", "кг."))
        self.label_23.setText(_translate("Dialog", "Грузоподъемность:"))
        self.label_24.setText(_translate("Dialog", "Вместимость кузова:"))
        self.label_25.setText(_translate("Dialog", "м3"))
        self.label_26.setText(_translate("Dialog", "Колесная формула:"))

    def firstCall(self):

        self.lstLight = [[self.label,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"border-radius: 3px;"],
        [self.label_4,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);"],
        [self.btnAddZakaz,"QPushButton:!hover {background-color: rgb(227,227,227);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border:1px solid rgb(135,135,135);}\n"
"QPushButton:hover {background-color: rgb(84,122,181);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(63,63,63);}\n"
"QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(63,63,63);};"],
        [self.leCompany,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.label_8,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);"],
        [self.label_9,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);"],
        [self.leTSgrz,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.leTScreatdate,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.label_10,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);"],
        [self.label_11,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);"],
        [self.leTSweightEmpty,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.label_12,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);"],
        [self.leTSdvigVilume,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.leTSweightMaxAllow,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.label_13,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);"],
        [self.label_14,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);"],
        [self.leTSpowerLS,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.label_15,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);"],
        [self.lblIconJournal,"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));\n"
"image: url(" + globalValues.pathStyleImgs + "iconworkpanel1.png);"],
        [self.line_7,"background-color: rgb(242,242,242);"],
        [self.line_8,"background-color: rgb(242,242,242);"],
        [self.line_9,"background-color: rgb(242,242,242);"],
        [self.lblBack,"background-color: rgb(242,242,242);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3px;"],
        [self.cb_TSname,"background-color: rgb(227,227,227);\n"
"color: black;\n"
"border-radius: 3px;\n"
"border: 1px solid rgb(135,135,135);"],
        [self.leTSname,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.line_4,"background-color: rgb(242,242,242);"],
        [self.line_5,"background-color: rgb(242,242,242);"],
        [self.line_6,"background-color: rgb(242,242,242);"],
        [self.line_10,"background-color: rgb(242,242,242);"],
        [self.cb_EurocCassNUM,"background-color: rgb(227,227,227);\n"
"color: black;\n"
"border-radius: 3px;\n"
"border: 1px solid rgb(135,135,135);"],
        [self.line_11,"background-color: rgb(242,242,242);"],
        [self.line_12,"background-color: rgb(242,242,242);"],
        [self.leTSpowerkWt,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.label_17,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);"],
        [self.label_18,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);"],
        [self.line_15,"background-color: rgb(242,242,242);"],
        [self.label_19,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);"],
        [self.label_20,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);"],
        [self.label_16,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);"],
        [self.label_21,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);"],
        [self.line_16,"background-color: rgb(242,242,242);"],
        [self.label_22,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);"],
        [self.leTSweightGruntMaxAllow,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.label_23,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);"],
        [self.label_24,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);"],
        [self.label_25,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);"],
        [self.leTSvolumeMax,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.label_26,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);"],
        [self.leTSwheelScheme,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"]]
        self.lstDark = [[self.label,"background-color: rgb(75,75,75);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3px;"],
        [self.label_4,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.btnAddZakaz,"QPushButton:!hover {background-color: rgb(89,89,89);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(63,63,63);}\n"
"QPushButton:hover {background-color: rgb(84,122,181);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(63,63,63);}\n"
"QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(63,63,63);};"],
        [self.leCompany,"background-color: white;\n"
"border-radius:3px;"],
        [self.label_8,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.label_9,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.leTSgrz,"background-color: white;\n"
"border-radius:3px;"],
        [self.leTScreatdate,"background-color: white;\n"
"border-radius:3px;"],
        [self.label_10,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.label_11,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.leTSweightEmpty,"background-color: white;\n"
"border-radius:3px;"],
        [self.label_12,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.leTSdvigVilume,"background-color: white;\n"
"border-radius:3px;"],
        [self.leTSweightMaxAllow,"background-color: white;\n"
"border-radius:3px;"],
        [self.label_13,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.label_14,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.leTSpowerLS,"background-color: white;\n"
"border-radius:3px;"],
        [self.label_15,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.lblIconJournal,"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));\n"
"image: url(" + globalValues.pathStyleImgs + "iconworkpanel1.png);"],
        [self.line_7,"background-color: rgb(75,75,75);"],
        [self.line_8,"background-color: rgb(75,75,75);"],
        [self.line_9,"background-color: rgb(75,75,75);"],
        [self.lblBack,"background-color: rgb(75,75,75);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3px;"],
        [self.cb_TSname,"background-color: white;\n"
"border-radius:3px;"],
        [self.leTSname,"background-color: white;\n"
"border-radius:3px;"],
        [self.line_4,"background-color: rgb(75,75,75);"],
        [self.line_5,"background-color: rgb(75,75,75);"],
        [self.line_6,"background-color: rgb(75,75,75);"],
        [self.line_10,"background-color: rgb(75,75,75);"],
        [self.cb_EurocCassNUM,"background-color: white;\n"
"border-radius:3px;"],
        [self.line_11,"background-color: rgb(75,75,75);"],
        [self.line_12,"background-color: rgb(75,75,75);"],
        [self.leTSpowerkWt,"background-color: white;\n"
"border-radius:3px;"],
        [self.label_17,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.label_18,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.line_15,"background-color: rgb(75,75,75);"],
        [self.label_19,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.label_20,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.label_16,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.label_21,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.line_16,"background-color: rgb(75,75,75);"],
        [self.label_22,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.leTSweightGruntMaxAllow,"background-color: white;\n"
"border-radius:3px;"],
        [self.label_23,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.label_24,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.label_25,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.leTSvolumeMax,"background-color: white;\n"
"border-radius:3px;"],
        [self.label_26,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.leTSwheelScheme,"background-color: white;\n"
"border-radius:3px;"]]

        self.lengthLight = len(self.lstLight)
        self.lengthDark = len(self.lstDark)

        self.changeCOLORMainPanelGrunt()

        self.connectToMySql()

        self.btnAddZakaz.clicked.connect(self.saveDataDatabase)

        pathFolder = str(os.getenv('APPDATA')) + r'\Sinaps'

        self.checkFolderPath(pathFolder, False)

        pathData = str(os.getenv('APPDATA'))
        pathFile = pathData + r'\Sinaps\defaultDataTS.txt'


        if (os.path.exists(pathFile) == False):
            f = open(pathFile, 'w')
            f.close()

        self.pasteDefaulData(pathFile)

    def changeColor(self, object, str):
            object.setStyleSheet(str)

    def changeCOLORMainPanelGrunt(self):

            delta = int((0.3/self.lengthDark)*1000)


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
                globalValues.writeLogData('Функция подключения к БД панель добавления ТС', str(ex))

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
                globalValues.writeLogData('Функция проверки подключения к бд MySql панель добавления ТС', str(ex))

    def saveDataDatabase(self):

       uiMes = Ui_mes_box()
       uiMes.lblStrInfo.setText('Вы уверены, что хотите сохранить данные ТС?')
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
                   globalValues.writeLogData('Проверка бд MySql панель добавления ТС', str(ex))
                   uiMes = Ui_mes_box()
                   uiMes.lblStrInfo.setText('Отсутствует соединение с БД!')
                   uiMes.btnOK.hide()
                   if (globalValues.colorForm == 1):
                       uiMes.label_iconques.setStyleSheet("background-color: rgb(235,235,235);\n"
                                                          "image: url(" + globalValues.pathStyleImgs + "icnAtt.png);")
                   else:
                       uiMes.label_iconques.setStyleSheet("background-color: rgb(75,75,75);\n"
                                                          "image: url(" + globalValues.pathStyleImgs + "icnAtt.png);")
                   uiMes.btnCancel.setText('Продолжить')
                   uiMes.exec_()
                   return
               listData = []

               company = self.leCompany.text()
               listData.append(company)
               nameTS = self.cb_TSname.currentText()
               listData.append(nameTS)
               model_TS = self.leTSname.text()
               listData.append(model_TS)
               reg_number = self.leTSgrz.text()
               listData.append(reg_number)
               manufact_year = self.leTScreatdate.text()
               listData.append(manufact_year)
               class_eco = self.cb_EurocCassNUM.currentText()
               listData.append(class_eco)
               power_eng_ls = self.leTSpowerLS.text()
               listData.append(power_eng_ls)
               power_eng_kwt = self.leTSpowerkWt.text()
               listData.append(power_eng_kwt)
               volume_eng = self.leTSdvigVilume.text()
               listData.append(volume_eng)
               weight_empty = self.leTSweightEmpty.text()
               listData.append(weight_empty)
               weight_max = self.leTSweightMaxAllow.text()
               listData.append(weight_max)
               carrying_cap = self.leTSweightGruntMaxAllow.text()
               listData.append(carrying_cap)
               volume_body = self.leTSvolumeMax.text()
               listData.append(volume_body)
               wheel_formula = self.leTSwheelScheme.text()
               listData.append(wheel_formula)

               checkData = True

               for el in listData:
                   if (el == ''):
                       checkData = False
                       break

               if checkData:

                   pathData = str(os.getenv('APPDATA'))
                   pathFile = pathData + r'\Sinaps\defaultDataTS.txt'

                   self.writeDefData(pathFile, listData)

                   try:

                       cur = self.con.cursor()

                       with self.con:
                                 query = ("INSERT INTO " + globalValues.tblsDB[6] + " (company, name_ts, model_ts, reg_number, manufact_year, eco_class_fuel, power_engine_ls, power_engine_kwt, volume_engine, weight_empty, max_weight, carrying_capacity, volume_body, wheel_formula) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                                 cur.execute(query, (company, nameTS, model_TS, reg_number, int(manufact_year),  int(class_eco), int(power_eng_ls), int(power_eng_kwt), int(volume_eng), int(weight_empty), int(weight_max), int(carrying_cap), int(volume_body), wheel_formula))
                                 self.con.commit()

                       globalValues.checkPoolTS = True
                       globalValues.refreshTblMain = True

                       cur.close()

                       strDataToTS = 'Выполнено добавление нового ТС(' + str(company) + ', ' + str(reg_number) + ')'
                       globalValues.writeEventToDBJournalMain('База ТС', strDataToTS)


                   except Exception as ex:
                       globalValues.writeLogData('Функция сохранения заказ-наряда на выполнение работ БД', str(ex))

                   self.is_save_data = True
                   self.con.close()
                   self.close()

               else:
                   try:
                       uiMes = Ui_mes_box()
                       uiMes.lblStrInfo.setText('Панель добавления ТС некорректно заполнена!')
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
                       globalValues.writeLogData('Функция сохранения данных ТС, панель некорректно заполнена', str(ex))
           except Exception as ex:
               globalValues.writeLogData('Функция сохранения данных о ТС', str(ex))

    def checkFolderPath(self, pathFolder, isHide):
            try:

                    if (os.path.exists(pathFolder) == False):
                        try:
                            os.mkdir(pathFolder)
                            # globalValsSBV.curPathFolderToWrite = pathFolder
                            if (isHide):
                                subprocess.call(['attrib', '+H', pathFolder])
                            return False
                        except Exception as ex:
                            globalValues.writeLogData('Функция проверки и создания папки хранилища', str(ex))
                    else:
                        return True

            except Exception as ex:
                globalValues.writeLogData('Функция проверки ссылки на текущую папку записи', str(ex))

    def pasteDefaulData(self, pathFile):
        try:
            f = open(pathFile, 'r')
            dataFile = f.read()
            f.close()
            if (dataFile != 0):
                dataList = dataFile.split('\n')
                self.leCompany.setText(dataList[0])
                self.cb_TSname.setItemText(0, dataList[1])
                self.leTSname.setText(dataList[2])
                self.leTSgrz.setText(dataList[3])
                self.leTScreatdate.setText(dataList[4])
                self.cb_EurocCassNUM.setItemText(0, dataList[5])
                self.leTSpowerLS.setText(dataList[6])
                self.leTSpowerkWt.setText(dataList[7])
                self.leTSdvigVilume.setText(dataList[8])
                self.leTSweightEmpty.setText(dataList[9])
                self.leTSweightMaxAllow.setText(dataList[10])
                self.leTSweightGruntMaxAllow.setText(dataList[11])
                self.leTSvolumeMax.setText(dataList[12])
                self.leTSwheelScheme.setText(dataList[13])

        except Exception as ex:
            globalValues.writeLogData('Функция записи дефолтных значений', str(ex))

    def writeDefData(self, pathFile, listData):
        try:
            data = ''
            for el in listData:
                data = data + el + '\n'
                print(data)
            f = open(pathFile, 'w')
            f.write(data)
            f.close()
        except Exception as ex:
            globalValues.writeLogData('Функция записи дефолтных значений полей панели', str(ex))

if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    uiJournal = Ui_add_TS()

    uiJournal.show()
    # uiJournal.thChangeCOLORJournal()
    # app.exec_()
    sys.exit(app.exec_())
