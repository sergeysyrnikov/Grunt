from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import time
import sys
import globalValues
from datetime import date
from fpdf import FPDF
import os
from panelMesBox import Ui_mes_box
# import ping3
# import win32api
# import win32print
import glob

app = QtWidgets.QApplication(sys.argv)

globalValues.colorForm = 1

class Ui_panel_report(QDialog):

    lstLight = [[]]
    lstDark = [[]]
    lengthLight = 0
    lengthDark = 0
    delta = 40
    num = 0

    pathFileCur = ''

    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("Dialog")
        self.resize(891, 907)
        self.lblBack = QtWidgets.QLabel(self)
        self.lblBack.setGeometry(QtCore.QRect(0, 0, 1061, 1081))
        self.lblBack.setText("")
        self.lblBack.setObjectName("lblBack")
        self.frmINFO = QtWidgets.QFrame(self)
        self.frmINFO.setGeometry(QtCore.QRect(0, 0, 1061, 1051))
        self.frmINFO.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmINFO.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmINFO.setObjectName("frmINFO")
        self.label_56 = QtWidgets.QLabel(self.frmINFO)
        self.label_56.setGeometry(QtCore.QRect(450, 220, 141, 21))
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.frmINFO)
        self.label_57.setGeometry(QtCore.QRect(415, 30, 61, 25))
        self.label_57.setObjectName("label_57")
        self.label_59 = QtWidgets.QLabel(self.frmINFO)
        self.label_59.setGeometry(QtCore.QRect(40, 100, 81, 21))
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.frmINFO)
        self.label_60.setGeometry(QtCore.QRect(40, 190, 151, 21))
        self.label_60.setObjectName("label_60")
        self.label_61 = QtWidgets.QLabel(self.frmINFO)
        self.label_61.setGeometry(QtCore.QRect(450, 280, 111, 21))
        self.label_61.setObjectName("label_61")
        self.label_64 = QtWidgets.QLabel(self.frmINFO)
        self.label_64.setGeometry(QtCore.QRect(450, 190, 151, 21))
        self.label_64.setObjectName("label_64")
        self.label_65 = QtWidgets.QLabel(self.frmINFO)
        self.label_65.setGeometry(QtCore.QRect(40, 250, 121, 21))
        self.label_65.setObjectName("label_65")
        self.label_67 = QtWidgets.QLabel(self.frmINFO)
        self.label_67.setGeometry(QtCore.QRect(380, 30, 28, 28))
        self.label_67.setText("")
        self.label_67.setObjectName("label_67")
        self.label_68 = QtWidgets.QLabel(self.frmINFO)
        self.label_68.setGeometry(QtCore.QRect(40, 220, 161, 21))
        self.label_68.setObjectName("label_68")
        self.label_70 = QtWidgets.QLabel(self.frmINFO)
        self.label_70.setGeometry(QtCore.QRect(450, 340, 241, 21))
        self.label_70.setObjectName("label_70")
        self.label_71 = QtWidgets.QLabel(self.frmINFO)
        self.label_71.setGeometry(QtCore.QRect(40, 70, 101, 21))
        self.label_71.setObjectName("label_71")
        self.label_73 = QtWidgets.QLabel(self.frmINFO)
        self.label_73.setGeometry(QtCore.QRect(450, 370, 251, 21))
        self.label_73.setObjectName("label_73")
        self.label_80 = QtWidgets.QLabel(self.frmINFO)
        self.label_80.setGeometry(QtCore.QRect(450, 250, 151, 21))
        self.label_80.setObjectName("label_80")
        self.label_82 = QtWidgets.QLabel(self.frmINFO)
        self.label_82.setGeometry(QtCore.QRect(40, 340, 231, 21))
        self.label_82.setObjectName("label_82")
        self.label_84 = QtWidgets.QLabel(self.frmINFO)
        self.label_84.setGeometry(QtCore.QRect(40, 370, 241, 21))
        self.label_84.setObjectName("label_84")
        self.label_86 = QtWidgets.QLabel(self.frmINFO)
        self.label_86.setGeometry(QtCore.QRect(40, 130, 91, 21))
        self.label_86.setObjectName("label_86")
        self.line_5 = QtWidgets.QFrame(self.frmINFO)
        self.line_5.setGeometry(QtCore.QRect(415, 57, 60, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.frmINFO)
        self.line_6.setGeometry(QtCore.QRect(40, 170, 810, 3))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_8 = QtWidgets.QFrame(self.frmINFO)
        self.line_8.setGeometry(QtCore.QRect(40, 320, 810, 3))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.lblMainBoxCams_2 = QtWidgets.QLabel(self.frmINFO)
        self.lblMainBoxCams_2.setEnabled(False)
        self.lblMainBoxCams_2.setGeometry(QtCore.QRect(10, 10, 871, 891))
        self.lblMainBoxCams_2.setText("")
        self.lblMainBoxCams_2.setObjectName("lblMainBoxCams_2")
        self.le_GoneFromObject = QtWidgets.QLineEdit(self.frmINFO)
        self.le_GoneFromObject.setGeometry(QtCore.QRect(610, 220, 241, 21))
        self.le_GoneFromObject.setObjectName("le_GoneFromObject")
        self.le_WeightObject = QtWidgets.QLineEdit(self.frmINFO)
        self.le_WeightObject.setGeometry(QtCore.QRect(290, 340, 131, 21))
        self.le_WeightObject.setObjectName("le_WeightObject")
        self.le_CarModel = QtWidgets.QLineEdit(self.frmINFO)
        self.le_CarModel.setGeometry(QtCore.QRect(150, 130, 271, 21))
        self.le_CarModel.setObjectName("le_CarModel")
        self.le_VolumeObject = QtWidgets.QLineEdit(self.frmINFO)
        self.le_VolumeObject.setGeometry(QtCore.QRect(290, 370, 131, 21))
        self.le_VolumeObject.setObjectName("le_VolumeObject")
        self.le_VolumePoligon = QtWidgets.QLineEdit(self.frmINFO)
        self.le_VolumePoligon.setGeometry(QtCore.QRect(700, 370, 151, 21))
        self.le_VolumePoligon.setObjectName("le_VolumePoligon")
        self.le_ComeToPoligon = QtWidgets.QLineEdit(self.frmINFO)
        self.le_ComeToPoligon.setGeometry(QtCore.QRect(610, 250, 241, 21))
        self.le_ComeToPoligon.setObjectName("le_ComeToPoligon")
        self.le_Organisation = QtWidgets.QLineEdit(self.frmINFO)
        self.le_Organisation.setGeometry(QtCore.QRect(150, 70, 271, 21))
        self.le_Organisation.setObjectName("le_Organisation")
        self.le_ComeToObject = QtWidgets.QLineEdit(self.frmINFO)
        self.le_ComeToObject.setGeometry(QtCore.QRect(610, 190, 241, 21))
        self.le_ComeToObject.setObjectName("le_ComeToObject")
        self.le_WeightPoligon = QtWidgets.QLineEdit(self.frmINFO)
        self.le_WeightPoligon.setGeometry(QtCore.QRect(700, 340, 151, 21))
        self.le_WeightPoligon.setObjectName("le_WeightPoligon")
        self.le_ZakazNumber = QtWidgets.QLineEdit(self.frmINFO)
        self.le_ZakazNumber.setGeometry(QtCore.QRect(200, 190, 221, 21))
        self.le_ZakazNumber.setObjectName("le_ZakazNumber")
        self.le_DriveOverTime = QtWidgets.QLineEdit(self.frmINFO)
        self.le_DriveOverTime.setGeometry(QtCore.QRect(610, 280, 241, 21))
        self.le_DriveOverTime.setObjectName("le_DriveOverTime")
        self.le_ZakazState = QtWidgets.QLineEdit(self.frmINFO)
        self.le_ZakazState.setGeometry(QtCore.QRect(200, 250, 221, 21))
        self.le_ZakazState.setObjectName("le_ZakazState")
        self.le_GRZNumber = QtWidgets.QLineEdit(self.frmINFO)
        self.le_GRZNumber.setGeometry(QtCore.QRect(150, 100, 271, 21))
        self.le_GRZNumber.setObjectName("le_GRZNumber")
        self.le_ZakazDate = QtWidgets.QLineEdit(self.frmINFO)
        self.le_ZakazDate.setGeometry(QtCore.QRect(200, 220, 221, 21))
        self.le_ZakazDate.setObjectName("le_ZakazDate")
        self.btnFilterSave = QtWidgets.QPushButton(self.frmINFO)
        self.btnFilterSave.setGeometry(QtCore.QRect(780, 30, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnFilterSave.setFont(font)
        self.btnFilterSave.setText("")
        self.btnFilterSave.setIconSize(QtCore.QSize(25, 25))
        self.btnFilterSave.setObjectName("btnFilterSave")
        self.btnFilterPrint = QtWidgets.QPushButton(self.frmINFO)
        self.btnFilterPrint.setGeometry(QtCore.QRect(820, 30, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnFilterPrint.setFont(font)
        self.btnFilterPrint.setText("")
        self.btnFilterPrint.setIconSize(QtCore.QSize(25, 25))
        self.btnFilterPrint.setObjectName("btnFilterPrint")
        self.label_69 = QtWidgets.QLabel(self.frmINFO)
        self.label_69.setGeometry(QtCore.QRect(40, 280, 151, 21))
        self.label_69.setObjectName("label_69")
        self.le_ZakazDate_2 = QtWidgets.QLineEdit(self.frmINFO)
        self.le_ZakazDate_2.setGeometry(QtCore.QRect(200, 280, 221, 21))
        self.le_ZakazDate_2.setObjectName("le_ZakazDate_2")
        self.btnFilterPrintSet = QtWidgets.QPushButton(self.frmINFO)
        self.btnFilterPrintSet.setGeometry(QtCore.QRect(820, 30, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnFilterPrintSet.setFont(font)
        self.btnFilterPrintSet.setText("")
        self.btnFilterPrintSet.setIconSize(QtCore.QSize(25, 25))
        self.btnFilterPrintSet.setObjectName("btnFilterPrintSet")
        self.le_frmKPPIN = QtWidgets.QLabel(self.frmINFO)
        self.le_frmKPPIN.setEnabled(False)
        self.le_frmKPPIN.setGeometry(QtCore.QRect(460, 480, 410, 410))
        self.le_frmKPPIN.setObjectName("le_frmKPPIN")
        self.le_frmKPPOUT = QtWidgets.QLabel(self.frmINFO)
        self.le_frmKPPOUT.setEnabled(False)
        self.le_frmKPPOUT.setGeometry(QtCore.QRect(20, 480, 410, 410))
        self.le_frmKPPOUT.setObjectName("le_frmKPPOUT")
        self.line_9 = QtWidgets.QFrame(self.frmINFO)
        self.line_9.setGeometry(QtCore.QRect(300, 460, 291, 3))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.label_62 = QtWidgets.QLabel(self.frmINFO)
        self.label_62.setGeometry(QtCore.QRect(300, 433, 291, 25))
        self.label_62.setObjectName("label_62")
        self.lblMainBoxCams_2.raise_()
        self.label_56.raise_()
        self.label_57.raise_()
        self.label_59.raise_()
        self.label_60.raise_()
        self.label_61.raise_()
        self.label_64.raise_()
        self.label_65.raise_()
        self.label_67.raise_()
        self.label_68.raise_()
        self.label_70.raise_()
        self.label_71.raise_()
        self.label_73.raise_()
        self.label_80.raise_()
        self.label_82.raise_()
        self.label_84.raise_()
        self.label_86.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.line_8.raise_()
        self.le_GoneFromObject.raise_()
        self.le_WeightObject.raise_()
        self.le_CarModel.raise_()
        self.le_VolumeObject.raise_()
        self.le_VolumePoligon.raise_()
        self.le_ComeToPoligon.raise_()
        self.le_Organisation.raise_()
        self.le_ComeToObject.raise_()
        self.le_WeightPoligon.raise_()
        self.le_ZakazNumber.raise_()
        self.le_DriveOverTime.raise_()
        self.le_ZakazState.raise_()
        self.le_GRZNumber.raise_()
        self.le_ZakazDate.raise_()
        self.btnFilterSave.raise_()
        self.btnFilterPrint.raise_()
        self.label_69.raise_()
        self.le_ZakazDate_2.raise_()
        self.btnFilterPrintSet.raise_()
        self.le_frmKPPIN.raise_()
        self.le_frmKPPOUT.raise_()
        self.line_9.raise_()
        self.label_62.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        # self.runThJournal()
        self.firstCall()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Панель отчёта"))
        self.label_56.setText(_translate("Dialog", "Выехал с обьекта:"))
        self.label_57.setText(_translate("Dialog", "Отчет"))
        self.label_59.setText(_translate("Dialog", "№ ГРЗ ТС:"))
        self.label_60.setText(_translate("Dialog", "Номер талона :"))
        self.label_61.setText(_translate("Dialog", "Время в пути:"))
        self.label_64.setText(_translate("Dialog", "Приехал на обьект:"))
        self.label_65.setText(_translate("Dialog", "Состояние З/Н:"))
        self.label_68.setText(_translate("Dialog", "Дата выдачи талона:"))
        self.label_70.setText(_translate("Dialog", "Масса грунта в ТС на полигоне:"))
        self.label_71.setText(_translate("Dialog", "Организация:"))
        self.label_73.setText(_translate("Dialog", "Обьем грунта в ТС на полигоне:"))
        self.label_80.setText(_translate("Dialog", "Прибыл на полигон:"))
        self.label_82.setText(_translate("Dialog", "Масса грунта в ТС на объекте:"))
        self.label_84.setText(_translate("Dialog", "Обьем грунта в ТС на объекте:"))
        self.label_86.setText(_translate("Dialog", "Модель ТС:"))
        self.label_69.setText(_translate("Dialog", "Дата закрытия З/Н:"))
        self.label_62.setText(_translate("Dialog", "Фотофиксация транспортного средства"))

    def firstCall(self):

        self.lstLight = [[self.lblBack,"background-color: rgb(66,66,66);"],
        [self.frmINFO,"background-color: rgb(242,242,242);"],
        [self.label_56,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_57,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 16pt \"MS Shell Dlg 2\";"],
        [self.label_59,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_60,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_61,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_64,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_65,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_67,"background-color: rgb(242,242,242);\n"
"color: white;\n"
"image: url(" + globalValues.pathStyleImgs + "iconinfo2.png);"],
        [self.label_68,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_70,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_71,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_73,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_80,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_82,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_84,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_86,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.line_5,"background-color: rgb(242,242,242);"],
        [self.line_6,"background-color: rgb(242,242,242);"],
        [self.line_8,"background-color: rgb(242,242,242);"],
        [self.lblMainBoxCams_2,"background-color: rgb(242,242,242);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(205,205,205);"],
        [self.le_GoneFromObject,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.le_WeightObject,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.le_CarModel,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.le_VolumeObject,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.le_VolumePoligon,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.le_ComeToPoligon,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.le_Organisation,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.le_ComeToObject,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.le_WeightPoligon,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.le_ZakazNumber,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.le_DriveOverTime,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.le_ZakazState,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.le_GRZNumber,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.le_ZakazDate,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.btnFilterSave,"QPushButton:!hover {background-color: rgb(227,227,227);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border:1px solid rgb(135,135,135);\n"
"image: url(" + globalValues.pathStyleImgs + "iconsave9.png);}\n"
"QPushButton:hover {background-color: rgb(84,122,181);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(135,135,135);\n"
"image: url(" + globalValues.pathStyleImgs + "iconsave10.png);}\n"
"QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(135,135,135);\n"
"image: url(" + globalValues.pathStyleImgs + "iconsave10.png);};"],
        [self.btnFilterPrint,"QPushButton:!hover {background-color: rgb(227,227,227);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border:1px solid rgb(135,135,135);\n"
"image: url(" + globalValues.pathStyleImgs + "iconprint9.png);}\n"
"QPushButton:hover {background-color: rgb(84,122,181);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(135,135,135);\n"
"image: url(" + globalValues.pathStyleImgs + "iconprint10.png);}\n"
"QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(135,135,135);\n"
"image: url(" + globalValues.pathStyleImgs + "iconprint10.png);};"],
        [self.label_69,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_ZakazDate_2,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.btnFilterPrintSet,"QPushButton:!hover {background-color: rgb(227,227,227);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border:1px solid rgb(135,135,135);\n"
"image: url(" + globalValues.pathStyleImgs + "iconprintset9.png);}\n"
"QPushButton:hover {background-color: rgb(84,122,181);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(135,135,135);\n"
"image: url(" + globalValues.pathStyleImgs + "iconprintset10.png);}\n"
"QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(135,135,135);\n"
"image: url(" + globalValues.pathStyleImgs + "iconprintset10.png);};"],
        [self.le_frmKPPIN,"background-color: rgb(235,235,235);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(150,150,150);\n"
"image: url(" + globalValues.pathStyleImgs + "iconframe380grey.png);"],
        [self.le_frmKPPOUT,"background-color: rgb(235,235,235);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(150,150,150);\n"
"image: url(" + globalValues.pathStyleImgs + "iconframe380grey.png);"],
        [self.line_9,"background-color: rgb(242,242,242);"],
        [self.label_62,"background-color: rgb(242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"]]

        self.lstDark = [[self.lblBack,"background-color: rgb(66,66,66);"],
        [self.frmINFO,"background-color: rgb(62,62,62);"],
        [self.label_56,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_57,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 16pt \"MS Shell Dlg 2\";"],
        [self.label_59,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_60,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_61,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_64,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_65,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_67,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"image: url(" + globalValues.pathStyleImgs + "iconinfo2.png);"],
        [self.label_68,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_70,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_71,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_73,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_80,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_82,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_84,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_86,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.line_5,"background-color: rgb(66,66,66);\n"
"color: white;"],
        [self.line_6,"background-color: rgb(75,75,75);\n"
"color: white;"],
        [self.line_8,"background-color: rgb(75,75,75);\n"
"color: white;"],
        [self.lblMainBoxCams_2,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"border-radius: 10px;\n"
"font: 10pt \"MS Shell Dlg 2\";"],
        [self.le_GoneFromObject,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_WeightObject,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_CarModel,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_VolumeObject,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_VolumePoligon,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_ComeToPoligon,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_Organisation,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_ComeToObject,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_WeightPoligon,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_ZakazNumber,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_DriveOverTime,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_ZakazState,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_GRZNumber,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_ZakazDate,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.btnFilterSave,"QPushButton:!hover {background-color: rgb(89,89,89);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border:1px solid rgb(135,135,135);\n"
"image: url(" + globalValues.pathStyleImgs + "iconsave10.png);}\n"
"QPushButton:hover {background-color: rgb(84,122,181);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(135,135,135);\n"
"image: url(" + globalValues.pathStyleImgs + "iconsave10.png);}\n"
"QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(135,135,135);\n"
"image: url(" + globalValues.pathStyleImgs + "iconsave10.png);};"],
        [self.btnFilterPrint,"QPushButton:!hover {background-color: rgb(89,89,89);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border:1px solid rgb(135,135,135);\n"
"image: url(" + globalValues.pathStyleImgs + "iconprint10.png);}\n"
"QPushButton:hover {background-color: rgb(84,122,181);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(135,135,135);\n"
"image: url(" + globalValues.pathStyleImgs + "iconprint10.png);}\n"
"QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(135,135,135);\n"
"image: url(" + globalValues.pathStyleImgs + "iconprint10.png);};"],
        [self.label_69,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_ZakazDate_2,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.btnFilterPrintSet,"QPushButton:!hover {background-color: rgb(89,89,89);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border:1px solid rgb(135,135,135);\n"
"image: url(" + globalValues.pathStyleImgs + "iconprintset10.png);}\n"
"QPushButton:hover {background-color: rgb(84,122,181);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(135,135,135);\n"
"image: url(" + globalValues.pathStyleImgs + "iconprintset10.png);}\n"
"QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(135,135,135);\n"
"image: url(" + globalValues.pathStyleImgs + "iconprintset10.png);};"],
        [self.le_frmKPPIN,"background-color: rgb(0,0,0);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(42,42,42);\n"
"image: url(" + globalValues.pathStyleImgs + "iconframe380.png);"],
        [self.le_frmKPPOUT,"background-color: rgb(0,0,0);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(42,42,42);\n"
"image: url(" + globalValues.pathStyleImgs + "iconframe380.png);"],
        [self.line_9,"background-color: rgb(66,66,66);\n"
"color: white;"],
        [self.label_62,"background-color: rgb(242);\n"
"color: rgb(255,255,255);\n"
"font: 12pt \"MS Shell Dlg 2\";"]]

        self.lengthLight = len(self.lstLight)
        self.lengthDark = len(self.lstDark)

        self.changeCOLORMainPanelGrunt()

        self.btnFilterSave.clicked.connect(self.saveReport)
        self.btnFilterPrint.clicked.connect(self.printData)

        self.btnFilterPrintSet.hide()
        self.checkFolderLongPath(globalValues.pathReports)

        self.le_CarModel.setEnabled(False)
        self.le_GRZNumber.setEnabled(False)
        self.le_Organisation.setEnabled(False)
        self.le_ZakazNumber.setEnabled(False)
        self.le_VolumePoligon.setEnabled(False)
        self.le_VolumeObject.setEnabled(False)
        self.le_WeightPoligon.setEnabled(False)
        self.le_WeightObject.setEnabled(False)
        self.le_DriveOverTime.setEnabled(False)
        self.le_ComeToPoligon.setEnabled(False)
        self.le_GoneFromObject.setEnabled(False)
        self.le_ComeToObject.setEnabled(False)
        self.le_ZakazState.setEnabled(False)
        self.le_ZakazDate.setEnabled(False)
        self.le_ZakazDate_2.setEnabled(False)

        self.le_frmKPPOUT.setEnabled(True)
        self.le_frmKPPIN.setEnabled(True)

    def changeColor(self, object, str):
            object.setStyleSheet(str)

    def changeCOLORMainPanelGrunt(self):

        delta = int((0.3 / self.lengthDark) * 1000)

        if (globalValues.colorForm == 1):

            for i in range(self.lengthLight):
                startTime = round(time.time() * 1000)
                while True:
                    obj = self.lstLight[i][0]
                    style = self.lstLight[i][1]
                    self.changeColor(obj, style)
                    # print('changeLight!')
                    if (abs(round(time.time() * 1000) - startTime) > delta):
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
                    if (abs(round(time.time() * 1000) - startTime) > delta):
                        break

    def saveReport(self):
        file_path = globalValues.pathReports + '/'
        num_rep = self.le_ZakazNumber.text()
        name_comp = self.le_Organisation.text()
        number_grz = self.le_GRZNumber.text()
        model_ts = self.le_CarModel.text()
        number_order = self.le_ZakazNumber.text()
        date_order = self.le_ZakazDate.text()
        st_order = self.le_ZakazState.text()
        date_in_object = self.le_ComeToObject.text()
        time_in_object = self.le_ComeToObject.text()
        date_out_object = self.le_GoneFromObject.text()
        time_out_object = self.le_GoneFromObject.text()
        date_in_poly = self.le_ComeToPoligon.text()
        time_in_poly = self.le_ComeToPoligon.text()
        time_in_road = self.le_DriveOverTime.text()
        weight_obj = self.le_WeightObject.text()
        weight_poly = self.le_WeightPoligon.text()
        vol_obj = self.le_VolumeObject.text()
        vol_poly = self.le_VolumePoligon.text()

        pathImgWeight = ''
        pathImgScan = ''

        print(number_order)
        print(globalValues.pathWeightImg)

        rep = self.checkAndPathImgsForReport(number_order, globalValues.pathWeightImg)
        print(rep)
        if rep[0]:
            pathImgWeight = rep[1]
            pathImgScan = rep[2]


        self.createReport(file_path, number_order, name_comp, number_grz, model_ts, number_order, date_order, date_order, st_order, date_in_object, time_in_object, date_out_object, time_out_object, date_in_poly, time_in_poly, time_in_road, weight_obj, vol_obj, weight_poly, vol_poly, pathImgWeight, pathImgScan)

    def createReport(self, file_PATH, RepNum, OrgName, GRZ, CarModel, TalonNum, TalonDate, ZNDate, ZNState, DateObjCome, TimeObjCome, DateObjGone, TimeObjGone, DatePolyCome, TimePolyCome, TimeInRoad, WeightObj, VolObj, WeightPoly, VolPoly, pathImgGRZ, pathImgGRUNT):
        try:
            # Формируем локальные переменные из переданных в функцию для дальнейшей вставки в пдф
            strRepNum = "Отчет #" + str(RepNum)
            strOrgName = "Организация:   " + str(OrgName)
            # strGRZNum = "Номер ГРЗ ТС:  " + str(GRZ[0]) + str(GRZ[1]) + str(GRZ[2]) + str(GRZ[3]) + str(GRZ[4]) + str(GRZ[5]) + str(GRZ[6]) + " " + str(GRZ[7]) + str(GRZ[8]) + str(GRZ[9])
            strGRZNum = "Номер ГРЗ ТС:  " + str(GRZ[0 : 6]) + " " + str(GRZ[6 : len(GRZ)])
            strCarModel = "Модель ТС:       " + str(CarModel)
            strTalonNum = "Номер талона:             " + str(TalonNum)
            strTalonDate = "Дата выдачи талона:  " + str(TalonDate)
            strZNState = "Состояние З/Н:            " + str(ZNState)
            strZNDate = "Дата закрытия З/Н:     " + str(ZNDate)
            strTimeObjCome = "Приехал на обьект:     " + str(DateObjCome) + " / " + str(TimeObjCome)
            strTimeObjGone = "Выехал с обьекта:       " + str(DateObjGone) + " / " + str(TimeObjGone)
            strTimePolyCome = "Приехал на полигон:   " + str(DatePolyCome) + " / " + str(TimePolyCome)
            strTimeInRoad = "Время в пути:               " + str(TimeInRoad)
            strWeightObj = "Масса грунта на обьекте:     " + str(WeightObj)
            strVolObj = "Объем грунта на обьекте:    " + str(VolObj)
            strWeightPoly = "Масса грунта на полигоне:   " + str(WeightPoly)
            strVolPoly = "Объем грунта на полигоне:  " + str(VolPoly)
            strFrameGRZ = "Фотофиксация ГРЗ ТС"
            strFrameGRUNT = "Фотофиксация ГРУНТ"
            strRepDate = "Дата создания отчета: " + str(date.today().day) + "." + str(date.today().month) + "." + str(date.today().year) + "г."

            # Заполнение страницы
            pdf = FPDF()
            pdf.add_page()
            pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
            pdf.set_font('DejaVu', '', 14)
            pdf.cell(200, 10, txt=strRepNum, ln=1, align="C")
            pdf.line(86, 18, 134, 18)
            pdf.set_font('DejaVu', '', 10)
            pdf.cell(70, 2, txt="", ln=1, align="L")
            pdf.cell(70, 5, txt=strOrgName, ln=1, align="L")
            pdf.cell(70, 5, txt=strGRZNum, ln=1, align="L")
            pdf.cell(70, 5, txt=strCarModel, ln=1, align="L")
            pdf.cell(70, 2, txt="", ln=1, align="L")
            pdf.line(11, 38, 198, 38)
            pdf.cell(70, 5, txt=strTalonNum, ln=1, align="L")
            pdf.cell(70, 5, txt=strTalonDate, ln=1, align="L")
            pdf.cell(70, 5, txt=strZNState, ln=1, align="L")
            pdf.cell(70, 5, txt=strZNDate, ln=1, align="L")
            pdf.cell(70, 5, txt=strTimeObjCome, ln=1, align="L")
            pdf.cell(70, 5, txt=strTimeObjGone, ln=1, align="L")
            pdf.cell(70, 5, txt=strTimePolyCome, ln=1, align="L")
            pdf.cell(70, 5, txt=strTimeInRoad, ln=1, align="L")
            pdf.cell(70, 2, txt="", ln=1, align="L")
            pdf.line(11, 80, 198, 80)
            pdf.cell(70, 5, txt=strWeightObj, ln=1, align="L")
            pdf.cell(70, 5, txt=strVolObj, ln=1, align="L")
            pdf.cell(70, 5, txt=strWeightPoly, ln=1, align="L")
            pdf.cell(70, 5, txt=strVolPoly, ln=1, align="L")
            pdf.line(11, 102, 198, 102)
            if (os.path.exists(pathImgGRZ)):
                pdf.image(pathImgGRZ, x=45, y=110, w=130)
            if (os.path.exists(pathImgGRUNT)):
                pdf.image(pathImgGRUNT, x=75, y=191, w=70)
            pdf.cell(200, 2, txt="", ln=1, align="C")
            pdf.cell(200, 8, txt=strFrameGRZ, ln=1, align="C")
            pdf.cell(200, 73, txt="", ln=1, align="C")
            pdf.cell(200, 8, txt=strFrameGRUNT, ln=1, align="C")
            pdf.cell(200, 83, txt="", ln=1, align="C")
            pdf.cell(190, 1, txt=strRepDate, ln=1, align="R")

            # Делаем имя файла и сохраняем
            filename = str(file_PATH) + str(RepNum) + "_" + str(date.today()) + ".pdf"
            pdf.output(filename)
            self.pathFileCur = filename
            # self.pFile_PARTH = file_PATH
            # self.pFile_NAME = str(RepNum) + "_" + str(date.today()) + ".pdf"
            time.sleep(0.3)
            if (os.path.exists(filename)):
                # print(filename)
                os.system(filename)
            self.btnFilterPrint.setEnabled(True)

            strDataToTS = 'Выполнено сохранение З/Н #' + str(RepNum)
            globalValues.writeEventToDBJournalMain('Отчёт', strDataToTS)

            return True
        except Exception as ex:
            globalValues.writeLogData('Функция создания отчёта в пдф', str(ex))
            uiMes = Ui_mes_box()
            uiMes.lblStrInfo.setText('Произошла ошибка при создании отчёта!')
            uiMes.btnOK.hide()
            if (globalValues.colorForm == 1):
                uiMes.label_iconques.setStyleSheet("background-color: rgb(235,235,235);\n"
                                                   "image: url(" + globalValues.pathStyleImgs + "icnAtt.png);")
            else:
                uiMes.label_iconques.setStyleSheet("background-color: rgb(75,75,75);\n"
                                                   "image: url(" + globalValues.pathStyleImgs + "icnAtt.png);")
            uiMes.btnCancel.setText('Продолжить')
            uiMes.exec_()
            return False

    def printData(self):
        self.printReport(self.pathFileCur)

    def printReport(self, pathFile):
        try:
            # PPrinter = ping3.ping(DefaultPrinter_IP)
            # if (str(PPrinter) != 'None'):
                  #формируем полное имя файла (путь каталога+имя, оба параметра получаем из функции создания отчета через глобал параметры)
                #скрипт печати
            check_file = 'pdf' in pathFile
            if (os.path.exists(pathFile) and check_file):
                # win32api.ShellExecute(
                #     0,
                #     "print",
                #     pathFile,
                #     '/d:"%s"' % win32print.GetDefaultPrinter(),
                #     ".",
                #     0
                # )
                PPrinter = ""

                strData = str(pathFile)
                strDataToTS = 'Выполнена печать З/Н(' + strData + ')'
                globalValues.writeEventToDBJournalMain('Отчёт', strDataToTS)

                print("PrinterCheckOK!!!")
            # else:
            #     print("PrinterCheck FALSE!!!")
                return True
        except Exception as ex:
            globalValues.writeLogData('Функция печати файла отчёта', str(ex))
            globalValues.writeLogData('Функция создания отчёта в пдф', str(ex))
            uiMes = Ui_mes_box()
            uiMes.lblStrInfo.setText('Произошла ошибка при печати отчёта!')
            uiMes.btnOK.hide()
            if (globalValues.colorForm == 1):
                uiMes.label_iconques.setStyleSheet("background-color: rgb(235,235,235);\n"
                                                   "image: url(" + globalValues.pathStyleImgs + "icnAtt.png);")
            else:
                uiMes.label_iconques.setStyleSheet("background-color: rgb(75,75,75);\n"
                                                   "image: url(" + globalValues.pathStyleImgs + "icnAtt.png);")
            uiMes.btnCancel.setText('Продолжить')
            uiMes.exec_()
            return False

    def checkFolderLongPath(self, pathFolder):
        try:
            i = 0
            listPath = []
            for element in pathFolder:
                if (element == '/' and i != 0):
                    listPath.append(pathFolder[0:i])
                i += 1
            # listPath = pathFolder.split('/')
            # listPath.pop(0)
            listPath.append(pathFolder)
            for elPath in listPath:
                if (os.path.exists(elPath) == False):
                    try:
                        os.mkdir(elPath)
                    except Exception as ex:
                        globalValues.writeLogData('Функция проверки и создания папки хранилища', str(ex))

            if (len(listPath) > 0):
                return True
            else:
                return False
        except Exception as ex:
            globalValues.writeLogData('Функция проверки ссылки на папку хранилища', str(ex))
            return False

    def checkAndPathImgsForReport(self, numOrder, pathImg):
        try:
            lengthPath = len(pathImg)
            pathFile = ''
            isWeight = False
            isScan = False
            pathImgWeight = ''
            pathImgScan = ''

            for name in glob.glob(pathImg + '/*.jpg'):
                pathFile = name
                name = name[lengthPath:len(name)]
                checkOrder = str(numOrder) in name
                checkWeight = 'weight' in name
                checkScan = 'scan' in name
                if (checkOrder and checkWeight):
                    pathImgWeight = pathFile
                    isWeight = True
                if (checkOrder and checkScan):
                    pathImgScan = pathFile
                    isScan = True
                if (isScan and isWeight):
                    return True, pathImgWeight, pathImgScan

            if (isWeight or isScan):
                return True, pathImgWeight, pathImgScan
            else:
                return False, pathImgWeight, pathImgScan
        except Exception as ex:
            globalValues.writeLogData('Функция проверки картинок для отчёта', str(ex))

if __name__ == "__main__":

    # app = QtWidgets.QApplication(sys.argv)

    uiJournal = Ui_panel_report()
    uiJournal.show()
    sys.exit(app.exec_())
