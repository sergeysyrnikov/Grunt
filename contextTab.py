from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QPushButton, QFrame
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QCoreApplication, QMetaObject, QRect, pyqtSignal, QEvent
import sys
import time
import globalValues
# import threading
# import os
# import pyautogui
# import subprocess
# import win32api
# import win32con

class Ui_ContextTable(QDialog):

    signalClickPyMouse = pyqtSignal()

    defCon = 99

    lstLight = [[]]
    lstDark = [[]]
    lengthLight = 0
    lengthDark = 0

    def __init__(self):
        # self.screenImgDisplay()
        super().__init__()
        self.runUiContextTab()

    def runUiContextTab(self):
        self.setObjectName("ContextTable")
        self.setFixedSize(1920, 1080)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setModal(True)
        self.setAutoFillBackground(False)
        self.label_setscreen = QLabel(self)
        self.label_setscreen.setGeometry(QRect(0, 0, 1920, 1080))
        pathImg = globalValues.curDisk + '/Sinaps/screenShot.png'
        # pathImg = pathImg.replace('\\', '/')
        print(pathImg)
        print('image: url(\'' + pathImg + '\');')
        self.label_setscreen.setStyleSheet("image: url(" + pathImg + ");")
        self.label_setscreen.setObjectName("label_setscreen")

        self.label_gradient = QLabel(self)
        self.label_gradient.setGeometry(QRect(0, 0, 1920, 1080))
        # self.label_gradient.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 211), stop:1 rgba(0, 0, 0, 210));")
        self.label_gradient.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.label_gradient.setObjectName("label_gradient")

        self.frmConBtn = QFrame(self)
        self.frmConBtn.setGeometry(QRect(110, 80, 161, 121))

        self.frmConBtn.setFrameShape(QFrame.StyledPanel)
        self.frmConBtn.setFrameShadow(QFrame.Raised)
        self.frmConBtn.setObjectName("frmConBtn")
        self.btnConDef = QPushButton(self.frmConBtn)
        self.btnConDef.setGeometry(QRect(0, 88, 161, 31))
        font = QFont()
        font.setPointSize(12)
        self.btnConDef.setFont(font)

        self.btnConDef.setObjectName("btnConDef")
        self.btnConSave = QPushButton(self.frmConBtn)
        self.btnConSave.setGeometry(QRect(0, 30, 161, 31))
        font = QFont()
        font.setPointSize(12)
        self.btnConSave.setFont(font)

        self.btnConSave.setObjectName("btnConSave")
        self.btnConEdit = QPushButton(self.frmConBtn)
        self.btnConEdit.setGeometry(QRect(0, 0, 161, 31))
        font = QFont()
        font.setPointSize(12)
        self.btnConEdit.setFont(font)

        self.btnConEdit.setObjectName("btnConEdit")
        self.btnConDel = QPushButton(self.frmConBtn)
        self.btnConDel.setGeometry(QRect(0, 60, 161, 31))
        font = QFont()
        font.setPointSize(12)
        self.btnConDel.setFont(font)

        self.btnConDel.setObjectName("btnConDel")

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)


        self.firstSets()

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("ContextTable", "Dialog"))
        self.btnConDef.setText(_translate("ContextTable", "По умолчанию"))
        self.btnConSave.setText(_translate("ContextTable", "Сохранить"))
        self.btnConEdit.setText(_translate("ContextTable", "Редактировать"))
        self.btnConDel.setText(_translate("ContextTable", "Удалить З/Н"))

    def firstSets(self):

        self.lstLight = [[self.btnConDel,"QPushButton:!hover {background-color: rgb(227,227,227);\n"
                                         "color: rgb(0,0,0);\n"
                                         "border:1px solid rgb(135,135,135);\n"
                                         "border-top-color: rgb(135,135,135);\n"
                                         "border-left-color: rgb(135,135,135);\n"
                                         "border-right-color:rgb(135,135,135);}\n"
                                         "\n"
                                         "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border:1px solid rgb(135,135,135);\n"
                                         "border-top-color: rgb(135,135,135);\n"
                                         "border-left-color: rgb(135,135,135);\n"
                                         "border-right-color:rgb(135,135,135);}\n"
                                         "\n"
                                         "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border:1px solid rgb(135,135,135);\n"
                                         "border:1px solid rgb(135,135,135);\n"
                                         "border-top-color: rgb(135,135,135);\n"
                                         "border-left-color: rgb(135,135,135);\n"
                                         "border-right-color:rgb(135,135,135);};"],
            [self.btnConEdit,"QPushButton:!hover {background-color: rgb(227,227,227);\n"
                                          "color: rgb(0,0,0);\n"
                                          "border:1px solid rgb(135,135,135);\n"
                                          "border-top-color: rgb(135,135,135);\n"
                                          "border-left-color: rgb(135,135,135);\n"
                                          "border-right-color:rgb(135,135,135);}\n"
                                          "\n"
                                          "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border:1px solid rgb(135,135,135);\n"
                                          "border-top-color: rgb(135,135,135);\n"
                                          "border-left-color: rgb(135,135,135);\n"
                                          "border-right-color:rgb(135,135,135);}\n"
                                          "\n"
                                          "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border:1px solid rgb(135,135,135);\n"
                                          "border:1px solid rgb(135,135,135);\n"
                                          "border-top-color: rgb(135,135,135);\n"
                                          "border-left-color: rgb(135,135,135);\n"
                                          "border-right-color:rgb(135,135,135);};"],
            [self.btnConSave,"QPushButton:!hover {background-color: rgb(227,227,227);\n"
                                          "color: rgb(0,0,0);\n"
                                          "border:1px solid rgb(135,135,135);\n"
                                          "border-top-color: rgb(135,135,135);\n"
                                          "border-left-color: rgb(135,135,135);\n"
                                          "border-right-color:rgb(135,135,135);}\n"
                                          "\n"
                                          "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border:1px solid rgb(135,135,135);\n"
                                          "border-top-color: rgb(135,135,135);\n"
                                          "border-left-color: rgb(135,135,135);\n"
                                          "border-right-color:rgb(135,135,135);}\n"
                                          "\n"
                                          "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border:1px solid rgb(135,135,135);\n"
                                          "border:1px solid rgb(135,135,135);\n"
                                          "border-top-color: rgb(135,135,135);\n"
                                          "border-left-color: rgb(135,135,135);\n"
                                          "border-right-color:rgb(135,135,135);};"],
            [self.btnConDef,"QPushButton:!hover {background-color: rgb(227,227,227);\n"
                                         "color: rgb(0,0,0);\n"
                                         "border:1px solid rgb(135,135,135);\n"
                                         "border-top-color: rgb(135,135,135);\n"
                                         "border-left-color: rgb(135,135,135);\n"
                                         "border-right-color:rgb(135,135,135);}\n"
                                         "\n"
                                         "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border:1px solid rgb(135,135,135);\n"
                                         "border-top-color: rgb(135,135,135);\n"
                                         "border-left-color: rgb(135,135,135);\n"
                                         "border-right-color:rgb(135,135,135);}\n"
                                         "\n"
                                         "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border:1px solid rgb(135,135,135);\n"
                                         "border:1px solid rgb(135,135,135);\n"
                                         "border-top-color: rgb(135,135,135);\n"
                                         "border-left-color: rgb(135,135,135);\n"
                                         "border-right-color:rgb(135,135,135);};"],
            [self.frmConBtn,"background-color: rgb(252,252,252);\n"
                                         "border: 0px;"]]
        self.lstDark = [[self.btnConDel,"QPushButton:!hover {background-color: rgb(89,89,89);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border:1px solid rgb(63,63,63);\n"
                                         "border-left-color: black;\n"
                                         "border-right-color: black}\n"
                                         "\n"
                                         "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border:1px solid rgb(63,63,63);\n"
                                         "border-left-color: black;\n"
                                         "border-right-color: black}\n"
                                         "\n"
                                         "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border:1px solid rgb(63,63,63);\n"
                                         "border-left-color: black;\n"
                                         "border-right-color: black};"],
            [self.btnConEdit,"QPushButton:!hover {background-color: rgb(89,89,89);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border:1px solid rgb(63,63,63);\n"
                                          "border-top-color: black;\n"
                                          "border-left-color: black;\n"
                                          "border-right-color: black;}\n"
                                          "\n"
                                          "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border:1px solid rgb(63,63,63);\n"
                                          "border-top-color: black;\n"
                                          "border-left-color: black;\n"
                                          "border-right-color: black;}\n"
                                          "\n"
                                          "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border:1px solid rgb(63,63,63);\n"
                                          "border-top-color: black;\n"
                                          "border-left-color: black;\n"
                                          "border-right-color: black;};"],
            [self.btnConSave,"QPushButton:!hover {background-color: rgb(89,89,89);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border:1px solid rgb(63,63,63);\n"
                                          "border-bottom-color: black;\n"
                                          "border-left-color: black;\n"
                                          "border-right-color: black}\n"
                                          "\n"
                                          "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border:1px solid rgb(63,63,63);\n"
                                          "border-bottom-color: black;\n"
                                          "border-left-color: black;\n"
                                          "border-right-color: black}\n"
                                          "\n"
                                          "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border:1px solid rgb(63,63,63);\n"
                                          "border-bottom-color: black;\n"
                                          "border-left-color: black;\n"
                                          "border-right-color: black};"],
            [self.btnConDef,"QPushButton:!hover {background-color: rgb(89,89,89);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border:1px solid rgb(63,63,63);\n"
                                         "border-bottom-color: black;\n"
                                         "border-left-color: black;\n"
                                         "border-right-color: black;}\n"
                                         "\n"
                                         "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border:1px solid rgb(63,63,63);\n"
                                         "border-bottom-color: black;\n"
                                         "border-left-color: black;\n"
                                         "border-right-color: black;}\n"
                                         "\n"
                                         "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border:1px solid rgb(63,63,63);\n"
                                         "border-bottom-color: black;\n"
                                         "border-left-color: black;\n"
                                         "border-right-color: black;};"],
            [self.frmConBtn,"background-color: rgb(89,89,89);\n"
                                         "border: 0px;"]]

        self.lengthLight = len(self.lstLight)
        self.lengthDark = len(self.lstDark)

        self.changeCOLORMainPanelGrunt()

        self.btnConEdit.clicked.connect(self.editTblMain)
        self.btnConSave.clicked.connect(self.saveTblMain)
        self.btnConDel.clicked.connect(self.delTblMain)
        self.btnConDef.clicked.connect(self.editElDef)
        self.btnConEdit.installEventFilter(self)
        self.btnConSave.installEventFilter(self)
        self.btnConDel.installEventFilter(self)
        self.btnConDef.installEventFilter(self)
        self.installEventFilter(self)

    def changeColor(self, object, str):
            object.setStyleSheet(str)

    def changeCOLORMainPanelGrunt(self):

            delta = 10

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

    # def screenImgDisplay(self):
    #     pathImg = globalValues.curDisk + '/Sinaps/screenShot.png'
    #     try:
    #         if(os.path.exists(pathImg)):
    #             os.remove(pathImg)
    #         app = QApplication(sys.argv)
    #         QScreen.grabWindow(app.primaryScreen(), QApplication.desktop().winId()).save(pathImg, 'png')
    #         # screen = pyautogui.screenshot(pathImg)
    #         # subprocess.call(['attrib', '+H', pathImg])
    #     except Exception as ex:
    #         print(ex)
    #
    #         globalValues.writeLogData('Функция создания скриншота рабочего стола', str(ex))

    def generateMenu(self):
        print('Inchecking!!!')
    #
    def editTblMain(self):
        # print('checkingEdit')
        self.defCon = 1
        self.close()

        # self.hide()

    def saveTblMain(self):
        # print('checkingSave')
        self.defCon = 2
        self.close()
        # self.hide()

    def delTblMain(self):
        # print('checkingDel')
        self.defCon = 3
        self.close()
        # self.hide()

    def editElDef(self):
        self.defCon = 4
        self.close()

    def eventFilter(self, source, event):
        try:

            checkEventBtn = False
            if ((source is self.btnConEdit) or (source is self.btnConSave) or (source is self.btnConDel) or (source is self.btnConDef)):
                checkEventBtn = True

            if ((source is self.btnConEdit) and event.type() == QEvent.MouseButtonPress and
                    event.buttons() == Qt.LeftButton):
                globalValues.checkEditMode = True


            if (event.type() == QEvent.MouseButtonPress and
                    event.buttons() == Qt.LeftButton and
                    checkEventBtn):
                    print('checkingBtnClick')

            if (event.type() == QEvent.MouseButtonPress and
                    event.buttons() == Qt.LeftButton and
                    checkEventBtn == False):
                print('Checkqwe:', globalValues.checkEditMode)
                if (globalValues.checkEditMode == False):
                    print('check!')
                    globalValues.checkEditTbl = False
                self.close()

            return super(Ui_ContextTable, self).eventFilter(source, event)

        except Exception as ex:
            globalValues.writeLogData('Функция обработки событий в контекстном окне', str(ex))

    # def startClickPython(self):
    #     my_thread = threading.Thread(target=self.signalClickPy)
    #     my_thread.start()
    #
    # def signalClickPy(self):
    #
    #     try:
    #         t = 0
    #         i = 1
    #         while i != 0:
    #             # print(win32api.GetKeyState(win32con.VK_LBUTTON))
    #             if (globalValues.stopAll):
    #                 break
    #             if win32api.GetKeyState(win32con.VK_LBUTTON) < 0:
    #                 win32api.GetCursorPos()
    #                 t = 1
    #             else:
    #                 if t == 1:  # Если отпускается кнопка то выходим
    #                     print('EndingProcess!!!')
    #                     i = 0
    #         print('check1')
    #         time.sleep(0.1)
    #         self.close()
    #         # self.signalClickPyMouse.emit()
    #         print('FinishContext!')
    #
    #     except Exception as ex:
    #         globalValues.writeLogData('Поток обработки события клика мыши', str(ex))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Ui_ContextTable()
    ui.show()
    sys.exit(app.exec_())
