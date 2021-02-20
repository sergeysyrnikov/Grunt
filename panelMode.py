from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

import globalValues
import time


class Ui_select_st_working(QDialog):

    checkClickOk = False
    stWorkingCb = ''

    lstLight = [[]]
    lstDark = [[]]
    lengthLight = 0
    lengthDark = 0

    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("Dialog")
        self.setFixedSize(250, 128)
        self.setStyleSheet("")
        self.btnAutoSt = QtWidgets.QPushButton(self)
        self.btnAutoSt.setGeometry(QtCore.QRect(26, 92, 90, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnAutoSt.setFont(font)
        self.btnAutoSt.setObjectName("btnAcc")
        self.btnCancel = QtWidgets.QPushButton(self)
        self.btnCancel.setGeometry(QtCore.QRect(136, 92, 90, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName("btnCnsl")
        self.label_txt = QtWidgets.QLabel(self)
        self.label_txt.setGeometry(QtCore.QRect(56, 11, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_txt.setFont(font)
        self.label_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.label_txt.setObjectName("label_txt")
        self.label_icon = QtWidgets.QLabel(self)
        self.label_icon.setGeometry(QtCore.QRect(10, 9, 25, 25))
        self.label_icon.setText("")
        self.label_icon.setObjectName("label_icon")
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(66, 53, 120, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lblBack = QtWidgets.QLabel(self)
        self.lblBack.setGeometry(QtCore.QRect(0, 0, 250, 128))
        self.lblBack.setText("")
        self.lblBack.setObjectName("lblBack")
        self.lblBack.raise_()
        self.btnAutoSt.raise_()
        self.btnCancel.raise_()
        self.label_txt.raise_()
        self.label_icon.raise_()
        self.comboBox.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        # self.runThJournal()
        self.firstSets()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Панель ПО"))
        self.btnAutoSt.setText(_translate("Dialog", "Да"))
        self.btnCancel.setText(_translate("Dialog", "Нет"))
        self.label_txt.setText(_translate("Dialog", "Режим работы ПО"))
        self.comboBox.setItemText(0, _translate("Dialog", "Автоматический"))
        self.comboBox.setItemText(1, _translate("Dialog", "Ручной"))

    def firstSets(self):

        self.lstLight = [[self.btnAutoSt, "QPushButton:!hover {background-color: rgb(227,227,227);\n"
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
                         [self.label_txt, "background-color: rgb(235,235,235);\n"
                                          "color: rgb(0,0,0);"],
                         [self.label_icon, "background-color: rgb(242,242,242);\n"
                                           "image: url(" + globalValues.pathStyleImgs + "iconset1.png);"],
                         [self.comboBox, "background-color: rgb(255,255,255);\n"
                                         "color: rgb(0,0,0);\n"
                                         "border-radius:3px;\n"
                                         "border: 1px solid rgb(150,150,150);"],
                         [self.lblBack, "background-color: rgb(235,235,235);"]]
        self.lstDark = [[self.btnAutoSt, "QPushButton:!hover {background-color: rgb(89,89,89);\n"
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
                        [self.label_txt, "background-color: rgb(75,75,75);\n"
                                         "color: rgb(255,255,255);"],
                        [self.label_icon, "background-color: rgb(75,75,75);\n"
                                          "image: url(" + globalValues.pathStyleImgs + "iconset1.png);"],
                        [self.comboBox, "color: white;\n"
                                        "background-color: rgb(89,89,89);"],
                        [self.lblBack, "background-color: rgb(75,75,75);"]]

        self.lengthLight = len(self.lstLight)
        self.lengthDark = len(self.lstDark)

        self.changeCOLORMainPanelGrunt()

        self.btnAutoSt.clicked.connect(self.clickOk)
        self.btnCancel.clicked.connect(self.clickCancel)

    def clickOk(self):
        self.checkClickOk = True
        self.stWorkingCb = self.comboBox.currentText()
        self.close()

    def clickCancel(self):
        self.checkClickOk = False
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
                                    print('changeLight!')
                                    if (abs(round(time.time()*100) - startTime) > delta):
                                            break

            elif (globalValues.colorForm == 0):
                    startTime = round(time.time() * 100)
                    for i in range(self.lengthDark):
                            while True:
                                    obj = self.lstDark[i][0]
                                    style = self.lstDark[i][1]
                                    self.changeColor(obj, style)
                                    print('changeDark!')
                                    if (abs(round(time.time()*100) - startTime) > delta):
                                            break


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    uiHand = Ui_select_st_working()
    uiHand.show()
    sys.exit(app.exec_())
