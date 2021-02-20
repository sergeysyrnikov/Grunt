from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import time
import sys
import globalValues
import os
from panelMesBox import Ui_mes_box

app = QtWidgets.QApplication(sys.argv)

globalValues.colorForm = 1

class Ui_panRtspCams(QDialog):

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
        self.resize(619, 532)
        self.le_rtsp0 = QtWidgets.QLineEdit(self)
        self.le_rtsp0.setGeometry(QtCore.QRect(10, 10, 601, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.le_rtsp0.setFont(font)
        self.le_rtsp0.setText("")
        self.le_rtsp0.setObjectName("le_rtsp0")
        self.btn_Save = QtWidgets.QPushButton(self)
        self.btn_Save.setGeometry(QtCore.QRect(510, 490, 101, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_Save.setFont(font)
        self.btn_Save.setObjectName("btn_Save")
        self.le_rtsp1 = QtWidgets.QLineEdit(self)
        self.le_rtsp1.setGeometry(QtCore.QRect(10, 50, 601, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.le_rtsp1.setFont(font)
        self.le_rtsp1.setText("")
        self.le_rtsp1.setObjectName("le_rtsp1")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, 621, 532))
        self.label.setText("")
        self.label.setObjectName("label")
        self.le_rtsp2 = QtWidgets.QLineEdit(self)
        self.le_rtsp2.setGeometry(QtCore.QRect(10, 90, 601, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.le_rtsp2.setFont(font)
        self.le_rtsp2.setText("")
        self.le_rtsp2.setObjectName("le_rtsp2")
        self.le_rtsp3 = QtWidgets.QLineEdit(self)
        self.le_rtsp3.setGeometry(QtCore.QRect(10, 130, 601, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.le_rtsp3.setFont(font)
        self.le_rtsp3.setText("")
        self.le_rtsp4 = QtWidgets.QLineEdit(self)
        self.le_rtsp4.setGeometry(QtCore.QRect(10, 170, 601, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.le_rtsp4.setFont(font)
        self.le_rtsp4.setText("")
        self.le_rtsp5 = QtWidgets.QLineEdit(self)
        self.le_rtsp5.setGeometry(QtCore.QRect(10, 210, 601, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.le_rtsp5.setFont(font)
        self.le_rtsp5.setText("")
        self.le_rtsp5.setObjectName("le_rtsp3")
        self.le_rtsp6 = QtWidgets.QLineEdit(self)
        self.le_rtsp6.setGeometry(QtCore.QRect(10, 250, 601, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.le_rtsp6.setFont(font)
        self.le_rtsp6.setText("")
        self.le_rtsp6.setObjectName("le_rtsp3")
        self.le_rtsp7 = QtWidgets.QLineEdit(self)
        self.le_rtsp7.setGeometry(QtCore.QRect(10, 290, 601, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.le_rtsp7.setFont(font)
        self.le_rtsp7.setText("")
        self.le_rtsp7.setObjectName("le_rtsp3")
        self.le_rtsp8 = QtWidgets.QLineEdit(self)
        self.le_rtsp8.setGeometry(QtCore.QRect(10, 330, 601, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.le_rtsp8.setFont(font)
        self.le_rtsp8.setText("")
        self.le_rtsp8.setObjectName("le_rtsp3")
        self.le_rtsp9 = QtWidgets.QLineEdit(self)
        self.le_rtsp9.setGeometry(QtCore.QRect(10, 370, 601, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.le_rtsp9.setFont(font)
        self.le_rtsp9.setText("")
        self.le_rtsp9.setObjectName("le_rtsp3")
        self.le_rtsp10 = QtWidgets.QLineEdit(self)
        self.le_rtsp10.setGeometry(QtCore.QRect(10, 410, 601, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.le_rtsp10.setFont(font)
        self.le_rtsp10.setText("")
        self.le_rtsp10.setObjectName("le_rtsp3")
        self.le_rtsp11 = QtWidgets.QLineEdit(self)
        self.le_rtsp11.setGeometry(QtCore.QRect(10, 450, 601, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.le_rtsp11.setFont(font)
        self.le_rtsp11.setText("")
        self.le_rtsp11.setObjectName("le_rtsp3")
        self.label.raise_()
        self.le_rtsp1.raise_()
        self.btn_Save.raise_()
        self.le_rtsp0.raise_()
        self.le_rtsp2.raise_()
        self.le_rtsp3.raise_()
        self.le_rtsp4.raise_()
        self.le_rtsp5.raise_()
        self.le_rtsp6.raise_()
        self.le_rtsp7.raise_()
        self.le_rtsp8.raise_()
        self.le_rtsp9.raise_()
        self.le_rtsp10.raise_()
        self.le_rtsp11.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        # self.runThJournal()
        self.firstCall()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Панель rtsp"))
        self.btn_Save.setText(_translate("Dialog", "Сохранить"))

    def firstCall(self):

        self.le_rtsp0.setPlaceholderText('Введите ртсп для 1-го канала(вторичный)')
        self.le_rtsp1.setPlaceholderText('Введите ртсп для 2-го канала(вторичный)')
        self.le_rtsp2.setPlaceholderText('Введите ртсп для 3-го канала(вторичный)')
        self.le_rtsp3.setPlaceholderText('Введите ртсп для 4-го канала(вторичный)')
        self.le_rtsp4.setPlaceholderText('Введите ртсп для 5-го канала(вторичный)')
        self.le_rtsp5.setPlaceholderText('Введите ртсп для 6-го канала(вторичный)')
        self.le_rtsp6.setPlaceholderText('Введите ртсп для 7-го канала(первичный)')
        self.le_rtsp7.setPlaceholderText('Введите ртсп для 8-го канала(первичный)')
        self.le_rtsp8.setPlaceholderText('Введите ртсп для 9-го канала(первичный)')
        self.le_rtsp9.setPlaceholderText('Введите ртсп для 10-го канала(первичный)')
        self.le_rtsp10.setPlaceholderText('Введите ртсп для 11-го канала(первичный)')
        self.le_rtsp11.setPlaceholderText('Введите ртсп для 12-го канала(первичный)')


        self.lstLight =  [[self.le_rtsp0,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.btn_Save,"QPushButton:!hover {background-color: rgb(227,227,227);\n"
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
        [self.le_rtsp1,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.label,"background-color: rgb(242,242,242);"],
        [self.le_rtsp2,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.le_rtsp3,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"border: 1px solid rgb(150,150,150);"],
        [self.le_rtsp4, "background-color: rgb(255,255,255);\n"
                                          "color: rgb(0,0,0);\n"
                                          "border-radius:3px;\n"
                                          "border: 1px solid rgb(150,150,150);"],
        [self.le_rtsp6, "background-color: rgb(255,255,255);\n"
                                          "color: rgb(0,0,0);\n"
                                          "border-radius:3px;\n"
                                          "border: 1px solid rgb(150,150,150);"],
        [self.le_rtsp7, "background-color: rgb(255,255,255);\n"
                                          "color: rgb(0,0,0);\n"
                                          "border-radius:3px;\n"
                                          "border: 1px solid rgb(150,150,150);"],
        [self.le_rtsp8, "background-color: rgb(255,255,255);\n"
                                          "color: rgb(0,0,0);\n"
                                          "border-radius:3px;\n"
                                          "border: 1px solid rgb(150,150,150);"],
        [self.le_rtsp9, "background-color: rgb(255,255,255);\n"
                                          "color: rgb(0,0,0);\n"
                                          "border-radius:3px;\n"
                                          "border: 1px solid rgb(150,150,150);"],
        [self.le_rtsp10, "background-color: rgb(255,255,255);\n"
                                          "color: rgb(0,0,0);\n"
                                          "border-radius:3px;\n"
                                          "border: 1px solid rgb(150,150,150);"],
        [self.le_rtsp11, "background-color: rgb(255,255,255);\n"
                                          "color: rgb(0,0,0);\n"
                                          "border-radius:3px;\n"
                                          "border: 1px solid rgb(150,150,150);"],

        [self.le_rtsp5, "background-color: rgb(255,255,255);\n"
                                          "color: rgb(0,0,0);\n"
                                          "border-radius:3px;\n"
                                          "border: 1px solid rgb(150,150,150);"]]

        self.lstDark = [[self.le_rtsp0,"background-color: rgb(42, 42, 42);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3px;"],
        [self.btn_Save,"QPushButton:!hover {background-color: rgb(89,89,89);\n"
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
        [self.le_rtsp1,"background-color: rgb(42, 42, 42);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3px;"],
        [self.label,"background-color: rgb(62,62,62);"],
        [self.le_rtsp2,"background-color: rgb(42, 42, 42);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3px;"],
        [self.le_rtsp3,"background-color: rgb(42, 42, 42);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3px;"],
        [self.le_rtsp4, "background-color: rgb(42, 42, 42);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 3px;"],
        [self.le_rtsp6, "background-color: rgb(42, 42, 42);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 3px;"],
        [self.le_rtsp7, "background-color: rgb(42, 42, 42);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 3px;"],
        [self.le_rtsp8, "background-color: rgb(42, 42, 42);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 3px;"],
        [self.le_rtsp9, "background-color: rgb(42, 42, 42);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 3px;"],
        [self.le_rtsp10, "background-color: rgb(42, 42, 42);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 3px;"],
        [self.le_rtsp11, "background-color: rgb(42, 42, 42);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 3px;"],
        [self.le_rtsp5, "background-color: rgb(42, 42, 42);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 3px;"]]

        self.lengthLight = len(self.lstLight)
        self.lengthDark = len(self.lstDark)

        self.changeCOLORMainPanelGrunt(0.1)

        self.btn_Save.clicked.connect(self.saveRtspLinks)

        checkFile = False

        try:
            pathFileRtsp = globalValues.pathDefaultData + r'\Sinaps\dataRtsp.txt'
            print(pathFileRtsp)
            if (os.path.exists(pathFileRtsp)):
                f = open(pathFileRtsp, 'r')
                dataRead = f.read()
                print(dataRead)
                f.close()
                if (dataRead != ''):
                    checkFile = True
                    lstData = dataRead.split('\n')
                    print(lstData)
                    self.le_rtsp0.setText(lstData[0])
                    self.le_rtsp1.setText(lstData[1])
                    self.le_rtsp2.setText(lstData[2])
                    self.le_rtsp3.setText(lstData[3])
                    self.le_rtsp4.setText(lstData[4])
                    self.le_rtsp5.setText(lstData[5])
                    self.le_rtsp6.setText(lstData[6])
                    self.le_rtsp7.setText(lstData[7])
                    self.le_rtsp8.setText(lstData[8])
                    self.le_rtsp9.setText(lstData[9])
                    self.le_rtsp10.setText(lstData[10])
                    self.le_rtsp11.setText(lstData[11])
        except Exception as ex:
            globalValues.writeLogData('Чтение данных из файла rtsp', str(ex))

        if (checkFile == False):
            self.le_rtsp0.setText('rtsp://login:pwd@strIP:554/cam/realmonitor?channel=1&subtype=1')
            self.le_rtsp1.setText('rtsp://login:pwd@strIP:554/cam/realmonitor?channel=1&subtype=1')
            self.le_rtsp2.setText('rtsp://login:pwd@strIP:554/cam/realmonitor?channel=1&subtype=1')
            self.le_rtsp3.setText('rtsp://login:pwd@strIP:554/cam/realmonitor?channel=1&subtype=1')
            self.le_rtsp4.setText('rtsp://login:pwd@strIP:554/cam/realmonitor?channel=1&subtype=1')
            self.le_rtsp5.setText('rtsp://login:pwd@strIP:554/cam/realmonitor?channel=1&subtype=1')

    def changeColor(self, object, str):
            object.setStyleSheet(str)

    def changeCOLORMainPanelGrunt(self, timeChangeColor):

        delta = int((timeChangeColor / self.lengthDark) * 1000)

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

    def saveRtspLinks(self):
        try:
            try:
                    pathFileRtsp = globalValues.pathDefaultData + r'\Sinaps\dataRtsp.txt'
                    rtsp = []
                    rtsp.append(self.le_rtsp0.text())
                    rtsp.append(self.le_rtsp1.text())
                    rtsp.append(self.le_rtsp2.text())
                    rtsp.append(self.le_rtsp3.text())
                    rtsp.append(self.le_rtsp4.text())
                    rtsp.append(self.le_rtsp5.text())
                    rtsp.append(self.le_rtsp6.text())
                    rtsp.append(self.le_rtsp7.text())
                    rtsp.append(self.le_rtsp8.text())
                    rtsp.append(self.le_rtsp9.text())
                    rtsp.append(self.le_rtsp10.text())
                    rtsp.append(self.le_rtsp11.text())

                    if (rtsp[0] != '' and rtsp[1] != '' and rtsp[2] != '' and rtsp[3] != '' and rtsp[4] != '' and rtsp[5] != '' and rtsp[6] != '' and rtsp[7] != '' and rtsp[8] != '' and rtsp[9] != '' and rtsp[10] != '' and rtsp[11] != ''):
                        f = open(pathFileRtsp, 'w')
                        dataAll = rtsp[0] + '\n' + rtsp[1] + '\n' + rtsp[2] + '\n' + rtsp[3] + '\n' + rtsp[4] + '\n' + rtsp[5] + '\n' + rtsp[6] + '\n' + rtsp[7] + '\n' + rtsp[8] + '\n' + rtsp[9] + '\n' + rtsp[10] + '\n' + rtsp[11]
                        for i in range(6):
                            globalValues.rtspMainLink[i] = rtsp[i]
                        f.write(dataAll)
                        f.close()
                        self.close()
                    else:
                        uiMes = Ui_mes_box()
                        uiMes.lblStrInfo.setText('Некорректно заполнены поля данных!')
                        uiMes.btnOK.hide()
                        if (globalValues.colorForm == 1):
                            uiMes.label_iconques.setStyleSheet("background-color: rgb(235,235,235);\n"
                                                               "image: url(" + globalValues.pathStyleImgs + "icnAtt.png);")
                        else:
                            uiMes.label_iconques.setStyleSheet("background-color: rgb(75,75,75);\n"
                                                               "image: url(" + globalValues.pathStyleImgs + "icnAtt.png);")
                        uiMes.btnCancel.setText('Продолжить')
                        uiMes.exec_()
            except Exception as ex:
                globalValues.writeLogData('Запись данных в файл rtsp', str(ex))
        except Exception as ex:
            globalValues.writeLogData('Функция сохранения rtsp links', str(ex))

if __name__ == "__main__":
    uiPanRtsp = Ui_panRtspCams()
    uiPanRtsp.show()
    sys.exit(app.exec_())
