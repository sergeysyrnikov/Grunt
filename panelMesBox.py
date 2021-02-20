
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import globalValues
import time

# globalValues.colorForm = 1

class Ui_mes_box(QDialog):

    checkCont = False

    lstLight = [[]]
    lstDark = [[]]
    lengthLight = 0
    lengthDark = 0

    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("Dialog")
        self.setFixedSize(347, 117)
        self.setStyleSheet("")
        self.btnOK = QtWidgets.QPushButton(self)
        self.btnOK.setGeometry(QtCore.QRect(135, 77, 90, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnOK.setFont(font)
        self.btnOK.setObjectName("btnOK")
        self.btnCancel = QtWidgets.QPushButton(self)
        self.btnCancel.setGeometry(QtCore.QRect(236, 77, 90, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName("btnCnsl")
        self.lblBack = QtWidgets.QLabel(self)
        self.lblBack.setGeometry(QtCore.QRect(0, 0, 347, 117))
        self.lblBack.setText("")
        self.lblBack.setObjectName("lblBack")
        self.lblStrInfo = QtWidgets.QLabel(self)
        self.lblStrInfo.setGeometry(QtCore.QRect(25, 42, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblStrInfo.setFont(font)
        self.lblStrInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStrInfo.setObjectName("labeltxt")
        self.label_iconques = QtWidgets.QLabel(self)
        self.label_iconques.setGeometry(QtCore.QRect(10, 11, 25, 25))
        self.label_iconques.setText("")
        self.label_iconques.setObjectName("label_iconques")
        self.lblBack.raise_()
        self.btnOK.raise_()
        self.btnCancel.raise_()
        self.lblStrInfo.raise_()
        self.label_iconques.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        # self.runThJournal()
        self.firstSets()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Панель сообщений"))
        self.btnOK.setText(_translate("Dialog", "Да"))
        self.btnCancel.setText(_translate("Dialog", "Нет"))
        # self.labeltxt.setText(_translate("Dialog", "123"))

    def firstSets(self):

        self.lstLight = [[self.btnOK, "QPushButton:!hover {background-color: rgb(227,227,227);\n"
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
                         [self.btnCancel, "QPushButton:!hover {background-color: rgb(227,227,227);\n"
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
                         [self.lblStrInfo, "background-color: rgb(242,242,242);\n"
                                         "color: rgb(0,0,0);"],
                         [self.label_iconques, "background-color: rgb(242,242,242);\n"
                                               "image: url(" + globalValues.pathStyleImgs + "iconatten.png);"],
                         [self.lblBack, "background-color: rgb(242,242,242);"]]
        self.lstDark = [[self.btnOK, "QPushButton:!hover {background-color: rgb(89,89,89);\n"
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
                        [self.btnCancel, "QPushButton:!hover {background-color: rgb(89,89,89);\n"
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
                        [self.lblBack, "background-color: rgb(62,62,62);"],
                        [self.lblStrInfo, "background-color: rgb(62,62,62);\n"
                                        "color: rgb(255,255,255);"],
                        [self.label_iconques, "background-color: rgb(62,62,62);\n"
                                              "image: url(" + globalValues.pathStyleImgs + "iconatten.png);"]]

        self.lengthLight = len(self.lstLight)
        self.lengthDark = len(self.lstDark)

        self.changeCOLORMainPanelGrunt()

        self.btnOK.clicked.connect(self.clickOk)
        self.btnCancel.clicked.connect(self.clickCancel)

    def clickOk(self):
        self.checkCont = True
        self.close()

    def clickCancel(self):
        self.checkCont = False
        self.close()

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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    uiMes = Ui_mes_box()
    uiMes.show()
    sys.exit(app.exec_())
