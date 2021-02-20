from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import globalValues
import time

# globalValues.colorForm = 1

class Ui_NetworkCam(QDialog):

    checkSaveBtn = False

    lstLight = [[]]
    lstDark = [[]]
    lengthLight = 0
    lengthDark = 0

    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("Dialog")
        self.setFixedSize(410, 290)
        self.btnAddNewCam = QtWidgets.QPushButton(self)
        self.btnAddNewCam.setGeometry(QtCore.QRect(220, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnAddNewCam.setFont(font)
        self.btnAddNewCam.setObjectName("btnAddNewCam")
        self.lblFront3 = QtWidgets.QLabel(self)
        self.lblFront3.setGeometry(QtCore.QRect(5, 5, 401, 361))
        self.lblFront3.setText("")
        self.lblFront3.setObjectName("lblFront3")
        self.lblFront4 = QtWidgets.QLabel(self)
        self.lblFront4.setGeometry(QtCore.QRect(0, 0, 410, 291))
        self.lblFront4.setText("")
        self.lblFront4.setObjectName("lblFront4")
        self.label_icon = QtWidgets.QLabel(self)
        self.label_icon.setGeometry(QtCore.QRect(10, 10, 35, 35))
        self.label_icon.setText("")
        self.label_icon.setObjectName("label_icon")
        self.leNewCamName = QtWidgets.QLineEdit(self)
        self.leNewCamName.setGeometry(QtCore.QRect(190, 63, 141, 20))
        self.leNewCamName.setText("")
        self.leNewCamName.setObjectName("leNewCamName")
        self.label_NameCam = QtWidgets.QLabel(self)
        self.label_NameCam.setEnabled(False)
        self.label_NameCam.setGeometry(QtCore.QRect(70, 65, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_NameCam.setFont(font)
        self.label_NameCam.setObjectName("label_NameCam")
        self.leNewCamIP = QtWidgets.QLineEdit(self)
        self.leNewCamIP.setGeometry(QtCore.QRect(190, 98, 141, 20))
        self.leNewCamIP.setText("")
        self.leNewCamIP.setObjectName("leNewCamIP")
        self.label_ChnName = QtWidgets.QLabel(self)
        self.label_ChnName.setEnabled(False)
        self.label_ChnName.setGeometry(QtCore.QRect(70, 135, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ChnName.setFont(font)
        self.label_ChnName.setObjectName("label_ChnName")
        self.label_ipCam = QtWidgets.QLabel(self)
        self.label_ipCam.setEnabled(False)
        self.label_ipCam.setGeometry(QtCore.QRect(70, 100, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ipCam.setFont(font)
        self.label_ipCam.setObjectName("label_ipCam")
        self.label_gateCam_2 = QtWidgets.QLabel(self)
        self.label_gateCam_2.setEnabled(False)
        self.label_gateCam_2.setGeometry(QtCore.QRect(70, 172, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_gateCam_2.setFont(font)
        self.label_gateCam_2.setObjectName("label_gateCam_2")
        self.label_ChnName_2 = QtWidgets.QLabel(self)
        self.label_ChnName_2.setEnabled(False)
        self.label_ChnName_2.setGeometry(QtCore.QRect(70, 207, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ChnName_2.setFont(font)
        self.label_ChnName_2.setObjectName("label_ChnName_2")
        self.leNewCamPass = QtWidgets.QLineEdit(self)
        self.leNewCamPass.setGeometry(QtCore.QRect(190, 170, 141, 20))
        self.leNewCamPass.setText("")
        self.leNewCamPass.setObjectName("leNewCamPass")
        self.leNewCamLogin = QtWidgets.QLineEdit(self)
        self.leNewCamLogin.setGeometry(QtCore.QRect(190, 135, 141, 20))
        self.leNewCamLogin.setText("")
        self.leNewCamLogin.setObjectName("leNewCamLogin")
        self.comboNewCamChlName = QtWidgets.QComboBox(self)
        self.comboNewCamChlName.setGeometry(QtCore.QRect(190, 205, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboNewCamChlName.setFont(font)
        self.comboNewCamChlName.setObjectName("comboNewCamChlName")
        self.line1 = QtWidgets.QFrame(self)
        self.line1.setGeometry(QtCore.QRect(128, 29, 155, 20))
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        self.labelNewCam = QtWidgets.QLabel(self)
        self.labelNewCam.setGeometry(QtCore.QRect(128, 10, 155, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelNewCam.setFont(font)
        self.labelNewCam.setObjectName("labelNewCam")
        self.lblFront3.raise_()
        self.lblFront4.raise_()
        self.btnAddNewCam.raise_()
        self.label_icon.raise_()
        self.leNewCamName.raise_()
        self.label_NameCam.raise_()
        self.leNewCamIP.raise_()
        self.label_ChnName.raise_()
        self.label_ipCam.raise_()
        self.label_gateCam_2.raise_()
        self.label_ChnName_2.raise_()
        self.leNewCamPass.raise_()
        self.leNewCamLogin.raise_()
        self.comboNewCamChlName.raise_()
        self.line1.raise_()
        self.labelNewCam.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        # self.runThJournal()
        self.firstStart()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Панель сетевых настроек"))
        self.btnAddNewCam.setText(_translate("Dialog", "Сохранить"))
        self.label_NameCam.setText(_translate("Dialog", "Имя :"))
        self.label_ChnName.setText(_translate("Dialog", "Логин :"))
        self.label_ipCam.setText(_translate("Dialog", "ip адрес :"))
        self.label_gateCam_2.setText(_translate("Dialog", "Пароль :"))
        self.label_ChnName_2.setText(_translate("Dialog", "Название канала :"))
        self.labelNewCam.setText(_translate("Dialog", "Добавление камеры"))

    def firstStart(self):

        self.lstLight = [[self, "background-color: rgb(66,66,66);"],
                         [self.btnAddNewCam, "QPushButton:!hover {background-color: rgb(227,227,227);\n"
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
                         [self.lblFront3, "background-color: rgb(62,62,62);\n"
                                          "border-radius: 10px;"],
                         [self.lblFront4, "background-color: rgb(242,242,242);"],
                         [self.label_icon, "background-color: rgb(242,242,242);\n"
                                           "image: url(" + globalValues.pathStyleImgs + "iconaddnewcam1.png);"],
                         [self.line1, "background-color: rgb(242,242,242);"],
                         [self.labelNewCam, "background-color: rgb(242,242,242);\n"
                                            "color: rgb(0,0,0);\n"
                                            "border-radius: 5px;"],
                         [self.leNewCamName, "background-color: rgb(255,255,255);\n"
                                             "color: rgb(0,0,0);\n"
                                             "border-radius:3px;\n"
                                             "border: 1px solid rgb(150,150,150);"],
                         [self.label_NameCam, "background-color: rgb(242,242,242);\n"
                                              "color: rgb(0,0,0);"],
                         [self.leNewCamIP, "background-color: rgb(255,255,255);\n"
                                           "color: rgb(0,0,0);\n"
                                           "border-radius:3px;\n"
                                           "border: 1px solid rgb(150,150,150);"],
                         [self.label_ChnName, "background-color: rgb(242,242,242);\n"
                                              "color: rgb(0,0,0);"],
                         [self.label_ipCam, "background-color: rgb(242,242,242);\n"
                                            "color: rgb(0,0,0);"],
                         [self.label_gateCam_2, "background-color: rgb(242,242,242);\n"
                                                "color: rgb(0,0,0);"],
                         [self.label_ChnName_2, "background-color: rgb(242,242,242);\n"
                                                "color: rgb(0,0,0);"],
                         [self.leNewCamPass, "background-color: rgb(255,255,255);\n"
                                             "color: rgb(0,0,0);\n"
                                             "border-radius:3px;\n"
                                             "border: 1px solid rgb(150,150,150);"],
                         [self.leNewCamLogin, "background-color: rgb(255,255,255);\n"
                                              "color: rgb(0,0,0);\n"
                                              "border-radius:3px;\n"
                                              "border: 1px solid rgb(150,150,150);"],
                         [self.comboNewCamChlName, "background-color: rgb(255,255,255);\n"
                                                   "color: rgb(0,0,0);\n"
                                                   "border-radius:3px;\n"
                                                   "border: 1px solid rgb(150,150,150);"]]

        self.lstDark = [[self, "background-color: rgb(66,66,66);"],
                        [self.btnAddNewCam, "QPushButton:!hover {background-color: rgb(89,89,89);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius:4px;\n"
                                            "border:1px solid rgb(63,63,63);}\n"
                                            "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius:4px;\n"
                                            "border:1px solid rgb(63,63,63);}\n"
                                            "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius:4px;\n"
                                            "border:1px solid rgb(63,63,63);};"],
                        [self.lblFront3, "background-color: rgb(62,62,62);\n"
                                         "border-radius: 10px;"],
                        [self.lblFront4, "background-color: rgb(75,75,75);\n"
                                         "border-radius: 10px;"],
                        [self.label_icon, "background-color: rgb(75,75,75);\n"
                                          "image: url(" + globalValues.pathStyleImgs + "iconaddnewcam1.png);"],
                        [self.leNewCamName, "background-color: white;\n"
                                            "border-radius:3px;"],
                        [self.label_NameCam, "background-color: rgb(75,75,75);\n"
                                             "color: white;"],
                        [self.leNewCamIP, "background-color: white;\n"
                                          "border-radius:3px;"],
                        [self.label_ChnName, "background-color: rgb(75,75,75);\n"
                                             "color: white;"],
                        [self.label_ipCam, "background-color: rgb(75,75,75);\n"
                                           "color: white;"],
                        [self.label_gateCam_2, "background-color: rgb(75,75,75);\n"
                                               "color: white;"],
                        [self.label_ChnName_2, "background-color: rgb(75,75,75);\n"
                                               "color: white;"],
                        [self.leNewCamPass, "background-color: white;\n"
                                            "border-radius:3px;"],
                        [self.leNewCamLogin, "background-color: white;\n"
                                             "border-radius:3px;"],
                        [self.comboNewCamChlName, "background-color: rgb(255,255,255);\n"
                                                  "color: rgb(0,0,0);\n"
                                                  "border-radius:3px;"],
                        [self.line1, "background-color: rgb(75,75,75);"],
                        [self.labelNewCam, "background-color: rgb(75,75,75);\n"
                                           "color: rgb(255,255,255);\n"
                                           "border-radius: 5px;"]]

        self.lengthLight = len(self.lstLight)
        self.lengthDark = len(self.lstDark)

        self.changeCOLORMainPanelGrunt()

        # self.leNewCamName.setText('NoviCam')
        # self.leNewCamIP.setText('192.168.0.88')
        self.comboNewCamChlName.addItem('Камера въезд КПП')
        self.comboNewCamChlName.addItem('Камера выезд КПП')
        self.comboNewCamChlName.addItem('Камера въезд Весы')
        self.comboNewCamChlName.addItem('Камера выезд Весы')
        self.comboNewCamChlName.addItem('Сканер ВК1')
        self.comboNewCamChlName.addItem('Сканер ВК2')
        # self.leNewCamLogin.setText('admin')
        self.leNewCamPass.setEchoMode(QtWidgets.QLineEdit.Password)
        # self.leNewCamPass.setText('admin')

        self.btnAddNewCam.clicked.connect(self.savePanelBtn)

    def closeEvent(self, event):
        self.close()

    def savePanelBtn(self):
        self.checkSaveBtn = True
        self.close()

    def changeColor(self, object, str):
            object.setStyleSheet(str)

    def changeCOLORMainPanelGrunt(self):

            delta = 50

            if (globalValues.colorForm == 1):
                    startTime = round(time.time() * 100)
                    for i in range(self.lengthLight):
                            while True:
                                    obj = self.lstLight[i][0]
                                    style = self.lstLight[i][1]
                                    self.changeColor(obj, style)
                                    # print('changeLight!')
                                    if (abs(round(time.time()*100) - startTime) > delta):
                                            break

            elif (globalValues.colorForm == 0):
                    startTime = round(time.time() * 100)
                    for i in range(self.lengthDark):
                            while True:
                                    obj = self.lstDark[i][0]
                                    style = self.lstDark[i][1]
                                    self.changeColor(obj, style)
                                    # print('changeDark!')
                                    if (abs(round(time.time()*100) - startTime) > delta):
                                            break

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_NetworkCam()
    ui.exec_()
    sys.exit(app.exec_())
