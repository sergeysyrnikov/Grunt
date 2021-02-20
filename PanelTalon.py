from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt
import threading
import time
import sys
import globalValues
# import win32api
# import win32print
# import pdf2image
from PIL import Image
from pathlib import Path
from fpdf import FPDF
from datetime import datetime, date
import os
from panelMesBox import Ui_mes_box

app = QtWidgets.QApplication(sys.argv)

globalValues.colorForm = 0

class Ui_Talon(QDialog):

    lstLight = [[]]
    lstDark = [[]]
    lengthLight = 0
    lengthDark = 0
    delta = 40
    num = 0

    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("Dialog")
        self.setFixedSize(340, 470)
        self.lblBack = QtWidgets.QLabel(self)
        self.lblBack.setGeometry(QtCore.QRect(0, 0, 341, 471))
        self.lblBack.setText("")
        self.lblBack.setObjectName("lblBack")
        self.frmTalon = QtWidgets.QFrame(self)
        self.frmTalon.setGeometry(QtCore.QRect(0, 0, 341, 471))
        self.frmTalon.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmTalon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmTalon.setObjectName("frmTalon")
        self.label_57 = QtWidgets.QLabel(self.frmTalon)
        self.label_57.setGeometry(QtCore.QRect(100, 18, 91, 25))
        self.label_57.setObjectName("label_57")
        self.label_59 = QtWidgets.QLabel(self.frmTalon)
        self.label_59.setGeometry(QtCore.QRect(20, 100, 81, 21))
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.frmTalon)
        self.label_60.setGeometry(QtCore.QRect(20, 190, 131, 21))
        self.label_60.setObjectName("label_60")
        self.label_67 = QtWidgets.QLabel(self.frmTalon)
        self.label_67.setGeometry(QtCore.QRect(65, 18, 28, 28))
        self.label_67.setText("")
        self.label_67.setObjectName("label_67")
        self.label_68 = QtWidgets.QLabel(self.frmTalon)
        self.label_68.setGeometry(QtCore.QRect(20, 220, 131, 21))
        self.label_68.setObjectName("label_68")
        self.label_71 = QtWidgets.QLabel(self.frmTalon)
        self.label_71.setGeometry(QtCore.QRect(20, 70, 101, 21))
        self.label_71.setObjectName("label_71")
        self.label_86 = QtWidgets.QLabel(self.frmTalon)
        self.label_86.setGeometry(QtCore.QRect(20, 130, 91, 21))
        self.label_86.setObjectName("label_86")
        self.line_5 = QtWidgets.QFrame(self.frmTalon)
        self.line_5.setGeometry(QtCore.QRect(98, 50, 160, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.frmTalon)
        self.line_6.setGeometry(QtCore.QRect(20, 170, 300, 3))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.le_CarModel = QtWidgets.QLineEdit(self.frmTalon)
        self.le_CarModel.setGeometry(QtCore.QRect(130, 130, 191, 21))
        self.le_CarModel.setObjectName("le_CarModel")
        self.le_Organisation = QtWidgets.QLineEdit(self.frmTalon)
        self.le_Organisation.setGeometry(QtCore.QRect(130, 70, 191, 21))
        self.le_Organisation.setText("")
        self.le_Organisation.setObjectName("le_Organisation")
        self.le_TakeGruntLocation = QtWidgets.QLineEdit(self.frmTalon)
        self.le_TakeGruntLocation.setGeometry(QtCore.QRect(160, 190, 161, 21))
        self.le_TakeGruntLocation.setObjectName("le_TakeGruntLocation")
        self.le_GRZNumber = QtWidgets.QLineEdit(self.frmTalon)
        self.le_GRZNumber.setGeometry(QtCore.QRect(130, 100, 191, 21))
        self.le_GRZNumber.setObjectName("le_GRZNumber")
        self.le_TimeCome = QtWidgets.QLineEdit(self.frmTalon)
        self.le_TimeCome.setGeometry(QtCore.QRect(160, 220, 161, 21))
        self.le_TimeCome.setObjectName("le_TimeCome")
        self.btnTalonPrint = QtWidgets.QPushButton(self.frmTalon)
        self.btnTalonPrint.setGeometry(QtCore.QRect(290, 15, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnTalonPrint.setFont(font)
        self.btnTalonPrint.setText("")
        self.btnTalonPrint.setIconSize(QtCore.QSize(25, 25))
        self.btnTalonPrint.setObjectName("btnTalonPrint")
        self.le_TalonNum = QtWidgets.QLineEdit(self.frmTalon)
        self.le_TalonNum.setGeometry(QtCore.QRect(190, 20, 71, 21))
        self.le_TalonNum.setText("")
        self.le_TalonNum.setObjectName("le_TalonNum")
        self.le_OffGruntLocation = QtWidgets.QLineEdit(self.frmTalon)
        self.le_OffGruntLocation.setGeometry(QtCore.QRect(160, 370, 161, 21))
        self.le_OffGruntLocation.setText("")
        self.le_OffGruntLocation.setObjectName("le_OffGruntLocation")
        self.label_69 = QtWidgets.QLabel(self.frmTalon)
        self.label_69.setGeometry(QtCore.QRect(20, 370, 131, 21))
        self.label_69.setObjectName("label_69")
        self.le_TalonDate = QtWidgets.QLineEdit(self.frmTalon)
        self.le_TalonDate.setGeometry(QtCore.QRect(160, 430, 161, 21))
        self.le_TalonDate.setObjectName("le_TalonDate")
        self.label_61 = QtWidgets.QLabel(self.frmTalon)
        self.label_61.setGeometry(QtCore.QRect(20, 430, 131, 21))
        self.label_61.setObjectName("label_61")
        self.line_7 = QtWidgets.QFrame(self.frmTalon)
        self.line_7.setGeometry(QtCore.QRect(20, 350, 300, 3))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.frmTalon)
        self.line_8.setGeometry(QtCore.QRect(20, 410, 300, 3))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.le_TimeGone = QtWidgets.QLineEdit(self.frmTalon)
        self.le_TimeGone.setGeometry(QtCore.QRect(160, 250, 161, 21))
        self.le_TimeGone.setObjectName("le_TimeGone")
        self.label_70 = QtWidgets.QLabel(self.frmTalon)
        self.label_70.setGeometry(QtCore.QRect(20, 250, 131, 21))
        self.label_70.setObjectName("label_70")
        self.le_Weight = QtWidgets.QLineEdit(self.frmTalon)
        self.le_Weight.setGeometry(QtCore.QRect(160, 280, 161, 21))
        self.le_Weight.setObjectName("le_Weight")
        self.label_72 = QtWidgets.QLabel(self.frmTalon)
        self.label_72.setGeometry(QtCore.QRect(20, 280, 131, 21))
        self.label_72.setObjectName("label_72")
        self.le_Volume = QtWidgets.QLineEdit(self.frmTalon)
        self.le_Volume.setGeometry(QtCore.QRect(160, 310, 161, 21))
        self.le_Volume.setObjectName("le_Volume")
        self.label_73 = QtWidgets.QLabel(self.frmTalon)
        self.label_73.setGeometry(QtCore.QRect(20, 310, 136, 21))
        self.label_73.setObjectName("label_73")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.firstCall()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Панель талона"))
        self.label_57.setText(_translate("Dialog", "Талон №"))
        self.label_59.setText(_translate("Dialog", "№ ГРЗ ТС:"))
        self.label_60.setText(_translate("Dialog", "Место погрузки:"))
        self.label_68.setText(_translate("Dialog", "Время прибытия:"))
        self.label_71.setText(_translate("Dialog", "Организация:"))
        self.label_86.setText(_translate("Dialog", "Модель ТС:"))
        self.label_69.setText(_translate("Dialog", "Место разгрузки:"))
        self.label_61.setText(_translate("Dialog", "Дата:"))
        self.label_70.setText(_translate("Dialog", "Время выезда:"))
        self.label_72.setText(_translate("Dialog", "Масса грунта, кг:"))
        self.label_73.setText(_translate("Dialog", "Объем грунта, м3:"))

    def firstCall(self):

        self.lstLight = [[self.lblBack,"background-color: rgb(66,66,66);"],
        [self.frmTalon,"background-color: rgb(242,242,242);"],
        [self.label_57,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 16pt \"MS Shell Dlg 2\";"],
        [self.label_59,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_60,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_67,"background-color: rgb(242,242,242);\n"
"color: white;\n"
"image: url(" + globalValues.pathStyleImgs + "iconinfo2.png);"],
        [self.label_68,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_71,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_86,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.line_5,"background-color: rgb(242,242,242);"],
        [self.line_6,"background-color: rgb(242,242,242);"],
        [self.le_CarModel,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_Organisation,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_TakeGruntLocation,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_GRZNumber,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_TimeCome,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.btnTalonPrint,"QPushButton:!hover {background-color: rgb(227,227,227);\n"
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
        [self.le_TalonNum,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"border: none;\n"
"font: 16pt \"MS Shell Dlg 2\";"],
        [self.le_OffGruntLocation,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_69,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_TalonDate,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_61,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.line_7,"background-color: rgb(242,242,242);"],
        [self.line_8,"background-color: rgb(242,242,242);"],
        [self.le_TimeGone,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_70,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_Weight,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_72,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_Volume,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_73,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";"]]

        self.lstDark = [[self.lblBack,"background-color: rgb(66,66,66);"],
        [self.frmTalon,"background-color: rgb(66,66,66);"],
        [self.label_57,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 16pt \"MS Shell Dlg 2\";"],
        [self.label_59,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_60,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_67,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"image: url(" + globalValues.pathStyleImgs + "iconinfo2.png);"],
        [self.label_68,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_71,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_86,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.line_5,"background-color: rgb(66,66,66);\n"
"color: white;"],
        [self.line_6,"background-color: rgb(75,75,75);\n"
"color: white;"],
        [self.le_CarModel,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_Organisation,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_TakeGruntLocation,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_GRZNumber,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_TimeCome,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.btnTalonPrint,"QPushButton:!hover {background-color: rgb(89,89,89);\n"
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
        [self.le_TalonNum,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"border: none;\n"
"font: 16pt \"MS Shell Dlg 2\";"],
        [self.le_OffGruntLocation,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_69,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_TalonDate,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_61,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.line_7,"background-color: rgb(75,75,75);\n"
"color: white;"],
        [self.line_8,"background-color: rgb(75,75,75);\n"
"color: white;"],
        [self.le_TimeGone,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_70,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_Weight,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_72,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.le_Volume,"background-color: rgb(89,89,89);\n"
"color: white;\n"
"border-radius: 3px;\n"
"font: 12pt \"MS Shell Dlg 2\";"],
        [self.label_73,"background-color: rgb(66,66,66);\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";"]]

        self.lengthLight = len(self.lstLight)
        self.lengthDark = len(self.lstDark)

        self.changeCOLORMainPanelGrunt()

        self.le_TalonDate.setAlignment(Qt.AlignCenter)
        self.le_TalonNum.setAlignment(Qt.AlignCenter)
        self.le_TakeGruntLocation.setAlignment(Qt.AlignCenter)
        self.le_CarModel.setAlignment(Qt.AlignCenter)
        self.le_GRZNumber.setAlignment(Qt.AlignCenter)
        self.le_Organisation.setAlignment(Qt.AlignCenter)
        self.le_OffGruntLocation.setAlignment(Qt.AlignCenter)
        self.le_TimeCome.setAlignment(Qt.AlignCenter)
        self.le_TimeGone.setAlignment(Qt.AlignCenter)
        self.le_Volume.setAlignment(Qt.AlignCenter)
        self.le_Weight.setAlignment(Qt.AlignCenter)

        self.le_TalonDate.setEnabled(False)
        self.le_TalonNum.setEnabled(False)
        self.le_TakeGruntLocation.setEnabled(False)
        self.le_CarModel.setEnabled(False)
        self.le_GRZNumber.setEnabled(False)
        self.le_Organisation.setEnabled(False)
        self.le_OffGruntLocation.setEnabled(False)
        self.le_TimeCome.setEnabled(False)
        self.le_TimeGone.setEnabled(False)
        self.le_Volume.setEnabled(False)
        self.le_Weight.setEnabled(False)

        self.btnTalonPrint.clicked.connect(self.printTalon)

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

    def printTalon(self):
        try:
            talon_num = self.le_TalonNum.text()
            company = self.le_Organisation.text()
            grz = self.le_GRZNumber.text()
            car_model = self.le_CarModel.text()
            name_object = self.le_TakeGruntLocation.text()
            time_in = self.le_TimeCome.text()
            time_out = self.le_TimeGone.text()
            weight = self.le_Weight.text()
            volume = self.le_Volume.text()
            polygon = self.le_OffGruntLocation.text()

            self.checkFolderLongPath(globalValues.pathTalon)

            self.printCurTalon(globalValues.pathTalon, talon_num, company, grz, car_model, name_object, time_in, time_out, weight, volume, polygon)
        except Exception as ex:
            globalValues.writeLogData('Функция печати талона', str(ex))

    def printCurTalon(self, file_PARTH, TalonNum, OrgName, GRZ, CarModel, StartLoc, ComeTime, GoneTime, GruntWeight, GruntVolume, DestLoc):
        try:
            # Формируем локальные переменные из переданных в функцию для дальнейшей вставки в пдф
            strTalonNum = "Талон #" + str(TalonNum)
            strOrgName = "Организация:       " + str(OrgName)
            lenGRZ = len(GRZ)
            if (len(GRZ) > 6):
                strGRZNum = "Номер ГРЗ ТС:      " + str(GRZ[0:6]) + " " + str(GRZ[6:len(GRZ)])
            strCarModel = "Модель ТС:           " + str(CarModel)
            strStartLoc = "Место погрузки:   " + str(StartLoc)
            strComeTime = "Время прибытия: " + str(ComeTime)
            strGoneTime = "Время выезда:     " + str(GoneTime)
            strGruntWeight = "Масса грунта:      " + str(GruntWeight)
            strGruntVolume = "Объем грунта:     " + str(GruntVolume)
            strDestLoc = "Место разгрузки: " + str(DestLoc)
            strTalonDate = "Дата:                     " + str(date.today().day) + "." + str(date.today().month) + "." + str(date.today().year) + "г."

            # Заполнение страницы
            pdf = FPDF()
            pdf.add_page()
            pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
            pdf.set_font('DejaVu', '', 14)
            pdf.cell(82, 5, txt=strTalonNum, ln=1, align="C")
            pdf.line(32, 15, 70, 15)
            pdf.set_font('DejaVu', '', 10)
            pdf.cell(70, 6, txt="", ln=1, align="L")
            pdf.cell(70, 6, txt=strOrgName, ln=1, align="L")
            pdf.cell(70, 6, txt=strGRZNum, ln=1, align="L")
            pdf.cell(70, 6, txt=strCarModel, ln=1, align="L")
            pdf.cell(70, 4, txt="", ln=1, align="L")
            pdf.line(11, 41, 89, 41)
            pdf.cell(70, 6, txt=strStartLoc, ln=1, align="L")
            pdf.cell(70, 6, txt=strComeTime, ln=1, align="L")
            pdf.cell(70, 6, txt=strGoneTime, ln=1, align="L")
            pdf.cell(70, 6, txt=strGruntWeight, ln=1, align="L")
            pdf.cell(70, 6, txt=strGruntVolume, ln=1, align="L")
            pdf.cell(70, 4, txt="", ln=1, align="L")
            pdf.line(11, 75, 89, 75)
            pdf.cell(70, 6, txt=strDestLoc, ln=1, align="L")
            pdf.cell(70, 4, txt="", ln=1, align="L")
            pdf.line(11, 85, 89, 85)
            pdf.cell(70, 6, txt=strTalonDate, ln=1, align="L")
            pdf.set_line_width(0.5)
            pdf.set_fill_color(0, 255, 0)
            pdf.rect(6, 5, 89, 95)


            # Делаем имя файла и сохраняем в лог
            filename = str(file_PARTH) + str(TalonNum) + "_" + str(date.today()) + ".pdf"
            pdf.output(filename)

            pFile_PARTH = file_PARTH
            pFile_NAME = str(TalonNum) + "_" + str(date.today()) + ".pdf"
            ppFile_NAME = str(TalonNum) + "_" + str(date.today())
            # print("MKTalonPDF ones OK!!!")
        except Exception as ex:
            # print("MKTalonPDF FALSE!!!")
            globalValues.writeLogData('Сохранение талона в пдф', str(ex))
            uiMes = Ui_mes_box()
            uiMes.lblStrInfo.setText('Произошла ошибка при сохранении отчёта!')
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

        #конвертим пдф в пнг
        try:
            JpgFile_Parth = str(file_PARTH) + str(ppFile_NAME) + ".png"
            talonPDF = pdf2image.convert_from_path(filename, 500)
            for page in talonPDF:
                page.save(JpgFile_Parth, 'PNG')

            imgfile = Path(JpgFile_Parth)
            img = Image.open(imgfile)
            width = img.size[0]
            height = img.size[1]
            img3 = img.crop((0, 0, width - 440, height - 770))
            img3.save(JpgFile_Parth)
            os.remove(filename)

            #создаем новый пдф и пихаем туда 3 обрезанных пнг талона
            pdfnew = FPDF()
            pdfnew.add_page()
            pdfnew.image(str(JpgFile_Parth), x=20, y=10, w=150)
            pdfnew.image(str(JpgFile_Parth), x=110, y=10, w=150)
            pdfnew.image(str(JpgFile_Parth), x=20, y=120, w=150)
            pdfnew.output(filename)


            strDataToTS = 'Выполнено сохранение талона #' + str(TalonNum)
            globalValues.writeEventToDBJournalMain('Талон', strDataToTS)

            os.remove(JpgFile_Parth)

            #печатаем файл
            PPrinter = "this"
            if (str(PPrinter) != 'None'):
                filename = str(pFile_PARTH) + str(pFile_NAME)  #формируем полное имя файла (путь каталога+имя, оба параметра получаем из функции создания отчета через глобал параметры)

                #скрипт печати
                # win32api.ShellExecute(
                #     0,
                #     "print",
                #     filename,
                #     '/d:"%s"' % win32print.GetDefaultPrinter(),
                #     ".",
                #     0
                # )

                os.startfile(filename, "print")

                strDataToTS = 'Выполнена печать талона #' + str(TalonNum)
                globalValues.writeEventToDBJournalMain('Талон', strDataToTS)

        except Exception as ex:
            globalValues.writeLogData('Функция печати талона', str(ex))
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

if __name__ == "__main__":
    uiTalon = Ui_Talon()
    uiTalon.show()
    sys.exit(app.exec_())
