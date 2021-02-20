from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import time
import sys
import globalValues
import os
from panelMesBox import Ui_mes_box
import writeCams as wrtCams
import threading
# from tkinter import Tk
# from tkinter.filedialog import askdirectory

app = QtWidgets.QApplication(sys.argv)

globalValues.colorForm = 0

class Ui_Storage(QDialog):

    lstLight = [[]]
    lstDark = [[]]
    lengthLight = 0
    lengthDark = 0
    delta = 40
    num = 0

    pathFldr = ''

    def __init__(self):
        super().__init__()
        self.runStorageUi()

    def runStorageUi(self):
        self.setObjectName("Form")
        self.setFixedSize(510, 273)
        self.lblBack = QtWidgets.QLabel(self)
        self.lblBack.setGeometry(QtCore.QRect(0, 0, 510, 273))
        self.lblBack.setText("")
        self.lblBack.setObjectName("lblBack")
        self.le_Catalog = QtWidgets.QLineEdit(self)
        self.le_Catalog.setGeometry(QtCore.QRect(220, 140, 251, 21))
        self.le_Catalog.setObjectName("le_Catalog")
        self.label_66 = QtWidgets.QLabel(self)
        self.label_66.setGeometry(QtCore.QRect(20, 140, 171, 21))
        self.label_66.setObjectName("label_66")
        self.label_72 = QtWidgets.QLabel(self)
        self.label_72.setGeometry(QtCore.QRect(20, 170, 181, 21))
        self.label_72.setObjectName("label_72")
        self.label_74 = QtWidgets.QLabel(self)
        self.label_74.setGeometry(QtCore.QRect(20, 50, 211, 21))
        self.label_74.setObjectName("label_74")
        self.le_ArchState = QtWidgets.QLineEdit(self)
        self.le_ArchState.setGeometry(QtCore.QRect(230, 50, 121, 21))
        self.le_ArchState.setText("")
        self.le_ArchState.setObjectName("le_ArchState")
        self.btnArchCatalog = QtWidgets.QPushButton(self)
        self.btnArchCatalog.setGeometry(QtCore.QRect(470, 140, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnArchCatalog.setFont(font)
        self.btnArchCatalog.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/iconrefresh2323.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnArchCatalog.setIcon(icon)
        self.btnArchCatalog.setIconSize(QtCore.QSize(25, 25))
        self.btnArchCatalog.setObjectName("btnArchCatalog")
        self.line_7 = QtWidgets.QFrame(self)
        self.line_7.setGeometry(QtCore.QRect(20, 120, 470, 3))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_75 = QtWidgets.QLabel(self)
        self.label_75.setGeometry(QtCore.QRect(20, 80, 211, 21))
        self.label_75.setObjectName("label_75")
        self.le_ArchVol = QtWidgets.QLineEdit(self)
        self.le_ArchVol.setGeometry(QtCore.QRect(230, 80, 130, 20))
        self.le_ArchVol.setText("")
        self.le_ArchVol.setObjectName("le_ArchVol")
        self.btnArchStart = QtWidgets.QPushButton(self)
        self.btnArchStart.setGeometry(QtCore.QRect(240, 230, 121, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnArchStart.setFont(font)
        self.btnArchStart.setObjectName("btnArchStart")
        self.btnArchStop = QtWidgets.QPushButton(self)
        self.btnArchStop.setGeometry(QtCore.QRect(370, 230, 121, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnArchStop.setFont(font)
        self.btnArchStop.setObjectName("btnArchStop")
        self.line_10 = QtWidgets.QFrame(self)
        self.line_10.setGeometry(QtCore.QRect(190, 37, 135, 3))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.label_58 = QtWidgets.QLabel(self)
        self.label_58.setGeometry(QtCore.QRect(190, 10, 141, 25))
        self.label_58.setObjectName("label_58")
        self.cb_ArchLiveTime = QtWidgets.QComboBox(self)
        self.cb_ArchLiveTime.setGeometry(QtCore.QRect(220, 170, 61, 22))
        self.cb_ArchLiveTime.setObjectName("cb_ArchLiveTime")
        self.le_Catalog_5 = QtWidgets.QLineEdit(self)
        self.le_Catalog_5.setGeometry(QtCore.QRect(230, 200, 31, 21))
        self.le_Catalog_5.setText("")
        self.le_Catalog_5.setObjectName("le_Catalog_5")
        self.label_76 = QtWidgets.QLabel(self)
        self.label_76.setGeometry(QtCore.QRect(20, 200, 191, 21))
        self.label_76.setObjectName("label_76")
        self.label_78 = QtWidgets.QLabel(self)
        self.label_78.setGeometry(QtCore.QRect(232, 200, 21, 21))
        self.label_78.setObjectName("label_78")
        self.le_ArchActiveCam = QtWidgets.QLineEdit(self)
        self.le_ArchActiveCam.setGeometry(QtCore.QRect(220, 200, 50, 21))
        self.le_ArchActiveCam.setText("")
        self.le_ArchActiveCam.setObjectName("le_ArchActiveCam")
        self.label_78.raise_()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        # self.runThJournal()
        self.firstCall()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Панель настройки архива"))
        self.label_66.setText(_translate("Form", "Расположение архива:"))
        self.label_72.setText(_translate("Form", "Время хранения:, дней:"))
        self.label_74.setText(_translate("Form", "Текущее состояние архива:"))
        self.label_75.setText(_translate("Form", "Текущий обьем архива, Гб:"))
        self.btnArchStart.setText(_translate("Form", "Запустить"))
        self.btnArchStop.setText(_translate("Form", "Остановить"))
        self.label_58.setText(_translate("Form", "Настройки архива"))
        self.label_76.setText(_translate("Form", "Кол-во доступных камер:"))
        self.label_78.setText(_translate("Form", "/4"))

    def firstCall(self):

        # self.le_ArchVol.setText('serhio')

        self.lstLight = [[self.lblBack, "background-color: rgb(235,235,235);"],
                         [self.le_Catalog, "background-color: rgb(255,255,255);\n"
                                           "color: rgb(0,0,0);\n"
                                           "font: 12pt \"MS Shell Dlg 2\";\n"
                                           "border-radius:3px;\n"
                                           "border: 1px solid rgb(150,150,150);\n"
                                           "border-top-right-radius: 0px;\n"
                                           "border-bottom-right-radius: 0px;"],
                         [self.label_66, "background-color: rgb(235,235,235);\n"
                                         "color: rgb(0,0,0);\n"
                                         "font: 12pt \"MS Shell Dlg 2\";"],
                         [self.label_72, "background-color: rgb(235,235,235);\n"
                                         "color: rgb(0,0,0);\n"
                                         "font: 12pt \"MS Shell Dlg 2\";"],
                         [self.label_74, "background-color: rgb(235,235,235);\n"
                                         "color: rgb(0,0,0);\n"
                                         "font: 12pt \"MS Shell Dlg 2\";"],
                         [self.le_ArchState, "background-color: rgb(235,235,235);\n"
                                             "border: none;\n"
                                             "color: rgb(0,0,0);\n"
                                             "font: 12pt \"MS Shell Dlg 2\";"],
                         [self.btnArchCatalog, "QPushButton:!hover {background-color: rgb(227,227,227);\n"
                                               "color: rgb(0,0,0);\n"
                                               "border-radius:3px;\n"
                                               "border:1px solid rgb(135,135,135);\n"
                                               "border-top-left-radius: 0px;\n"
                                               "border-bottom-left-radius: 0px;\n"
                                               "image: url(" + globalValues.pathStyleImgs + "iconopencatgrey.png);}\n"
                                               "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "border-radius:3px;\n"
                                               "border:1px solid rgb(135,135,135);\n"
                                               "border-top-left-radius: 0px;\n"
                                               "border-bottom-left-radius: 0px;\n"
                                               "image: url(" + globalValues.pathStyleImgs + "iconopencatgrey.png);}\n"
                                               "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "border-radius:3px;\n"
                                               "border:1px solid rgb(135,135,135);\n"
                                               "border-top-left-radius: 0px;\n"
                                               "border-bottom-left-radius: 0px;\n"
                                               "image: url(" + globalValues.pathStyleImgs + "iconopencatgrey.png);};"],
                         [self.line_7, "background-color: rgb(242,242,242);"],
                         [self.label_75, "background-color: rgb(235,235,235);\n"
                                         "color: rgb(0,0,0);\n"
                                         "font: 12pt \"MS Shell Dlg 2\";"],
                         [self.le_ArchVol, "background-color: rgb(235,235,235);\n"
                                           "border: none;\n"
                                           "color: rgb(0,0,0);\n"],
                         [self.btnArchStart, "QPushButton:!hover {background-color: rgb(227,227,227);\n"
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
                         [self.btnArchStop, "QPushButton:!hover {background-color: rgb(227,227,227);\n"
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
                         [self.line_10, "background-color: rgb(242,242,242);"],
                         [self.label_58, "background-color: rgb(235,235,235);\n"
                                         "color: rgb(0,0,0);\n"
                                         "font: 12pt \"MS Shell Dlg 2\";"],
                         [self.cb_ArchLiveTime, "background-color: rgb(227,227,227);\n"
                                                "color: black;\n"
                                                "border-radius: 3px;\n"
                                                "border: 1px solid rgb(135,135,135);"],
                         [self.le_Catalog_5, "background-color: rgb(235,235,235);\n"
                                             "border: none;\n"
                                             "color: rgb(0,0,0);\n"
                                             "font: 12pt \"MS Shell Dlg 2\";"],
                         [self.label_76, "background-color: rgb(235,235,235);\n"
                                         "color: rgb(0,0,0);\n"
                                         "font: 12pt \"MS Shell Dlg 2\";"],
                         [self.label_78, "background-color: rgb(235,235,235);\n"
                                         "color: rgb(0,0,0);\n"
                                         "font: 12pt \"MS Shell Dlg 2\";"],
                         [self.le_ArchActiveCam, "background-color: rgb(235,235,235);\n"
                                                 "border: none;\n"
                                                 "color: rgb(0,0,0);\n"
                                                 "font: 12pt \"MS Shell Dlg 2\";"]]

        self.lstDark = [[self.lblBack, "background-color: rgb(75,75,75);\n"
                                       "color: rgb(255,255,255);\n"
                                       "font: 12pt \"MS Shell Dlg 2\";"],
                        [self.le_Catalog, "background-color: rgb(42, 42, 42);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "font: 12pt \"MS Shell Dlg 2\";\n"
                                          "border-radius: 3px;"],
                        [self.label_66, "background-color: rgb(75,75,75);\n"
                                        "color: rgb(255,255,255);\n"
                                        "font: 12pt \"MS Shell Dlg 2\";"],
                        [self.label_72, "background-color: rgb(75,75,75);\n"
                                        "color: rgb(255,255,255);\n"
                                        "font: 12pt \"MS Shell Dlg 2\";"],
                        [self.label_74, "background-color: rgb(75,75,75);\n"
                                        "color: rgb(255,255,255);\n"
                                        "font: 12pt \"MS Shell Dlg 2\";"],
                        [self.le_ArchState, "background-color: rgb(75,75,75);\n"
                                            "border: none;\n"
                                            "color: rgb(255,255,255);\n"
                                            "font: 12pt \"MS Shell Dlg 2\";"],
                        [self.btnArchCatalog, "QPushButton:!hover {background-color: rgb(63,63,63);\n"
                                              "color: rgb(0,0,0);\n"
                                              "border-radius:3px;\n"
                                              "border-top-left-radius: 0px;\n"
                                              "border-bottom-left-radius: 0px;\n"
                                              "border:1px solid rgb(42,42,42);\n"
                                              "image: url(" + globalValues.pathStyleImgs + "iconopencatgrey.png);}\n"
                                              "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "border-radius:3px;\n"
                                              "border-top-left-radius: 0px;\n"
                                              "border-bottom-left-radius: 0px;\n"
                                              "border:1px solid rgb(135,135,135);\n"
                                              "image: url(" + globalValues.pathStyleImgs + "iconopencatgrey.png);}\n"
                                              "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "border-radius:3px;\n"
                                              "border-top-left-radius: 0px;\n"
                                              "border-bottom-left-radius: 0px;\n"
                                              "border:1px solid rgb(135,135,135);\n"
                                              "image: url(" + globalValues.pathStyleImgs + "iconopencatgrey.png);};"],
                        [self.line_7, "background-color: rgb(75,75,75);"],
                        [self.label_75, "background-color: rgb(75,75,75);\n"
                                        "color: rgb(255,255,255);\n"
                                        "font: 12pt \"MS Shell Dlg 2\";"],
                        [self.le_ArchVol, "background-color: rgb(75,75,75);\n"
                                          "border: none;\n"
                                          "color: rgb(255,255,255);\n"],
                        [self.btnArchStart, "QPushButton:!hover {background-color: rgb(89,89,89);\n"
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
                        [self.btnArchStop, "QPushButton:!hover {background-color: rgb(89,89,89);\n"
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
                        [self.line_10, "background-color: rgb(75,75,75);"],
                        [self.label_58, "background-color: rgb(75,75,75);\n"
                                        "color: rgb(255,255,255);\n"
                                        "font: 12pt \"MS Shell Dlg 2\";"],
                        [self.cb_ArchLiveTime, "background-color: rgb(89,89,89);\n"
                                               "color: white;\n"
                                               "border-radius: 3px;\n"
                                               "border: 1px solid rgb(63,63,63)"],
                        [self.le_Catalog_5, "background-color: rgb(235,235,235);\n"
                                            "border: none;\n"
                                            "color: rgb(0,0,0);\n"
                                            "font: 12pt \"MS Shell Dlg 2\";"],
                        [self.label_76, "background-color: rgb(75,75,75);\n"
                                        "color: rgb(255,255,255);\n"
                                        "font: 12pt \"MS Shell Dlg 2\";"],
                        [self.label_78, "background-color: rgb(75,75,75);\n"
                                        "color: rgb(255,255,255);\n"
                                        "font: 12pt \"MS Shell Dlg 2\";"],
                        [self.le_ArchActiveCam, "background-color: rgb(75,75,75);\n"
                                                "border: none;\n"
                                                "color: rgb(255,255,255);\n"
                                                "font: 12pt \"MS Shell Dlg 2\";"]]

        self.lengthLight = len(self.lstLight)
        self.lengthDark = len(self.lstDark)


        numCam = 0
        for el in globalValues.camsSt:
            if (el == True):
                numCam += 1

        self.le_ArchActiveCam.setEnabled(False)
        self.le_ArchActiveCam.setText(str(numCam))

        self.changeCOLORMainPanelGrunt(0.15)

        self.le_ArchState.setEnabled(False)
        self.le_ArchVol.setEnabled(False)

        if (globalValues.stateStorage):
            if (globalValues.colorForm == 0):
                self.le_ArchState.setStyleSheet(
                    "background-color: rgb(75,75,75); border: none; color: rgb(16, 140, 16); font: 12pt \"MS Shell Dlg 2\";")
            else:
                self.le_ArchState.setStyleSheet(
                    "background-color: rgb(235, 235, 235); border: none; color: rgb(84, 161, 100); font: 12pt \"MS Shell Dlg 2\";")
            self.le_ArchState.setText('запущен')
        else:
            if (globalValues.colorForm == 0):
                self.le_ArchState.setStyleSheet(
                    "background-color: rgb(75,75,75); border: none; color: rgb(215, 26, 26); font: 12pt \"MS Shell Dlg 2\";")
            else:
                self.le_ArchState.setStyleSheet(
                    "background-color: rgb(235, 235, 235); border: none; color: rgb(214, 104, 104); font: 12pt \"MS Shell Dlg 2\";")
            self.le_ArchState.setText('не запущен')


        # self.le_ArchActiveCam.setText('4')
        self.cb_ArchLiveTime.setFont(QtGui.QFont("Arial", 10))
        for i in range(7):
            i += 1
            self.cb_ArchLiveTime.addItem(str(i))

        self.le_Catalog.setText(globalValues.pathStrg)

        # self.size()

        self.btnArchCatalog.clicked.connect(self.selectFolderToWrite)
        self.btnArchStart.clicked.connect(self.startWritingCam)
        self.btnArchStop.clicked.connect(self.stopRecCams)

        try:
            pathData = globalValues.pathDefFldr + '/dataStrg.txt'
            if (os.path.exists(pathData)):
                file_strg = open(pathData, 'r')
                dataAll = file_strg.read()
                dataLst = dataAll.split()
                print('DataPathStorage: ', dataLst)
                self.cb_ArchLiveTime.setCurrentText(dataLst[2])

                self.le_Catalog.setText(str(dataLst[0]))

                thNew = threading.Thread(target=self.sizeFolderStorage, args=(str(dataLst[0]), ))
                thNew.start()
                # self.sizeFolderStorage(str(dataLst[0]))

        except Exception as ex:
            globalValues.writeLogData('Считывание данных о лимите хранения данных', str(ex))

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

    def selectFolderToWrite(self):
        try:

            self.pathFldr = ''

            # time.sleep(0.25)

            pathFolderCur = QtWidgets.QFileDialog.getExistingDirectory(None, 'Панель выбора папки архива', self.pathFldr, QtWidgets.QFileDialog.ShowDirsOnly)
            # pathFolderCur = askdirectory(title='Панель выбора папки архива')

            self.pathFldr = pathFolderCur

            # self.le_Catalog.setFont(QtGui.QFont("Arial", 11))
            self.le_Catalog.setText(pathFolderCur)
            pathStorage = self.le_Catalog.text()
            # thNew = threading.Thread(target=self.sizeFolderStorage, args=(pathStorage, ))
            # thNew.start()

            total_size = 0
            for dirpath, dirnames, filenames in os.walk(pathStorage):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    # skip if it is symbolic link
                    if not os.path.islink(fp):
                        total_size += os.path.getsize(fp)

            size = int(total_size)

            sizeNew = round(size / 1024 / 1024)

            print(sizeNew)

            strData = str(sizeNew) + ' MB.'
            print(strData)

            self.le_ArchVol.setEnabled(True)
            self.le_ArchVol.setText(strData)

            # thNew.join()

        except Exception as ex:
            globalValues.writeLogData('Функция выбора папки архива', str(ex))

    # def size(self):

    def sizeFolderStorage(self, pathFolderStorage):
        try:
            # pathFiles = []
            # dirFolder = []
            # data = []
            #
            # start_time = round(time.time() * 100)
            # pathFolder = [pathFolderStorage]
            # path_folder = []
            # checkFolder = False
            # while True:
            #     i = 0
            #     checkFolder = False
            #     for path in pathFolder:
            #         curPath = path
            #         data = os.listdir(path)
            #         if (i == 0):
            #             pathFolder = []
            #         for el in data:
            #             pathCur = curPath + '/' + el
            #             if (os.path.isfile(pathCur)):
            #                 pathFiles.append(pathCur)
            #             else:
            #                 path_folder.append(pathCur)
            #                 pathFolder.append(pathCur)
            #                 checkFolder = True
            #
            #         i += 1
            #
            #     if checkFolder == False:
            #         break
            #
            #     if (abs(round(time.time() * 100) - start_time) > 200 and len(pathFolder) == 0):
            #         break
            #     if (globalValues.stopAll):
            #         break
            #     time.sleep(0.1)

            # countFolders = len(path_folder)
            # countFiles = len(pathFiles)

            # size = 0
            # for el in pathFiles:
            #     sizeCur = os.path.getsize(el)
            #
            #     size += sizeCur

            print('CheckMem:', pathFolderStorage)

            total_size = 0
            for dirpath, dirnames, filenames in os.walk(pathFolderStorage):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    # skip if it is symbolic link
                    if not os.path.islink(fp):
                        total_size += os.path.getsize(fp)

            size = int(total_size)



            print(size)

            sizeNew = round(size / 1024 / 1024)

            print(sizeNew)

            strData = str(sizeNew) + ' MB.'
            print(strData)



            self.le_ArchVol.setEnabled(True)
            globalValues.sizeStrg = strData
            # self.setData(strData)
            # sys.exit()

            time.sleep(0.25)
            self.le_ArchVol.setText(globalValues.sizeStrg)
            time.sleep(0.25)

            print('1234')
            sys.exit()



        except Exception as ex:
            globalValues.writeLogData('Функция считывания данных о папке', str(ex))
            # return 'error'

    def startWritingCam(self):
        try:
            globalValues.stopStrg = False
            time.sleep(0.1)
            pathFolder = self.le_Catalog.text()

            globalValues.pathStrg = pathFolder

            checkFolder = False

            checkPath = '/' in pathFolder

            dataDays = self.cb_ArchLiveTime.currentText()
            if (dataDays != ''):
                globalValues.numberFolderDateSave = int(dataDays)
            else:
                globalValues.numberFolderDateSave = 3

            try:
                pathData = globalValues.pathDefFldr + '/dataStrg.txt'
                file_strg = open(pathData, 'w')
                dataAll = str(globalValues.pathStrg) + ' 0 ' + str(globalValues.numberFolderDateSave)
                file_strg.write(dataAll)
                file_strg.close()
            except Exception as ex:
                globalValues.writeLogData('Функция записи состояния архива в файл', str(ex))

            if (self.checkFolderLongPath(pathFolder) and pathFolder != '' and checkPath):
                if (os.path.isfile(pathFolder) == False and os.path.exists(pathFolder)):
                    checkFolder = True

                    if (int(self.le_ArchActiveCam.text()) > 0):

                        print('checkingChnl: ')
                        print(globalValues.lstGoodCams)
                        listRtsp = []
                        listIp = []
                        listChnl = []
                        listNum = []
                        pathDefFolder = globalValues.diskForTimeFiles
                        delta = globalValues.deltaWriting
                        name_channel = ''
                        for i in range(4):
                            if (globalValues.lstGoodCams[i]):
                                if (globalValues.listRtsp[i] != ''):
                                    listRtsp.append(globalValues.listRtsp[i])
                                    listIp.append(globalValues.listIp[i])
                                    if (i == 0):
                                        name_channel = 'КппВъезд'
                                    elif (i == 1):
                                        name_channel = 'КппВыезд'
                                    elif (i == 2):
                                        name_channel = 'ВесыВъезд'
                                    elif (i == 3):
                                        name_channel = 'ВесыВыезд'
                                    else:
                                        name_channel = 'КаналЗаписи'
                                    listChnl.append(name_channel)
                                    listNum.append(i)
                        print(listRtsp)
                        print(listIp)
                        print(listChnl)
                        print(listNum)

                        th_start_writing_cams = threading.Thread(target=wrtCams.startingWritingCams, args=(pathFolder, pathDefFolder, delta, listRtsp, listIp, listChnl, listNum, ))
                        th_start_writing_cams.start()
                        globalValues.stateStorage = True

                        strChls = ''
                        for el in listChnl:
                            strChls += el + ', '
                        if (strChls != ''):
                            lengthStr = len(strChls)
                            strChls = strChls[0:lengthStr - 2]

                        strDataToTS = 'Выполнен запуск записи архива(' + strChls + ')'
                        globalValues.writeEventToDBJournalMain('Камеры', strDataToTS)

                        try:
                            pathData = globalValues.pathDefFldr + '/dataStrg.txt'
                            file_strg = open(pathData, 'w')
                            dataAll = str(globalValues.pathStrg) + ' 1 ' + str(globalValues.numberFolderDateSave)
                            file_strg.write(dataAll)
                            file_strg.close()
                        except Exception as ex:
                            globalValues.writeLogData('Функция записи состояния архива в файл', str(ex))

                        if (globalValues.colorForm == 0):
                            self.le_ArchState.setStyleSheet(
                                "background-color: rgb(75,75,75); border: none; color: rgb(16, 140, 16); font: 12pt \"MS Shell Dlg 2\";")
                        else:
                            self.le_ArchState.setStyleSheet(
                                "background-color: rgb(235, 235, 235); border: none; color: rgb(84, 161, 100); font: 12pt \"MS Shell Dlg 2\";")
                        self.le_ArchState.setText('запущен')

                    else:
                        uiMes = Ui_mes_box()
                        uiMes.lblStrInfo.setText('Нет доступных камер!')
                        uiMes.btnOK.hide()
                        if (globalValues.colorForm == 1):
                            uiMes.label_iconques.setStyleSheet("background-color: rgb(235,235,235);\n"
                                                               "image: url(" + globalValues.pathStyleImgs + "icnAtt.png);")
                        else:
                            uiMes.label_iconques.setStyleSheet("background-color: rgb(75,75,75);\n"
                                                               "image: url(" + globalValues.pathStyleImgs + "icnAtt.png);")
                        uiMes.btnCancel.setText('Продолжить')
                        uiMes.exec()


                else:
                    checkFolder = False
            else:
                checkFolder = False

            print(os.path.exists(pathFolder))

            if (checkFolder == False):
                uiMes = Ui_mes_box()
                uiMes.lblStrInfo.setText('Расположение архива задано некорректно!')
                uiMes.btnOK.hide()
                if (globalValues.colorForm == 1):
                    uiMes.label_iconques.setStyleSheet("background-color: rgb(235,235,235);\n"
                                                       "image: url(" + globalValues.pathStyleImgs + "icnAtt.png);")
                else:
                    uiMes.label_iconques.setStyleSheet("background-color: rgb(75,75,75);\n"
                                                       "image: url(" + globalValues.pathStyleImgs + "icnAtt.png);")
                uiMes.btnCancel.setText('Продолжить')
                uiMes.exec()

        except Exception as ex:
            globalValues.writeLogData('Функция запуска записи в архив', str(ex))
            uiMes = Ui_mes_box()
            uiMes.lblStrInfo.setText('Расположение архива задано некорректно!')
            uiMes.btnOK.hide()
            if (globalValues.colorForm == 1):
                uiMes.label_iconques.setStyleSheet("background-color: rgb(235,235,235);\n"
                                                   "image: url(" + globalValues.pathStyleImgs + "icnAtt.png);")
            else:
                uiMes.label_iconques.setStyleSheet("background-color: rgb(75,75,75);\n"
                                                   "image: url(" + globalValues.pathStyleImgs + "icnAtt.png);")
            uiMes.btnCancel.setText('Продолжить')
            uiMes.exec()

    def checkFolderLongPath(self, pathFolder):
        try:
            # i = 0
            # listPath = []
            # for element in pathFolder:
            #     if (element == '/'):
            #         listPath.append(pathFolder[0:i])
            #     i += 1
            listPath = pathFolder.split('/')
            listPath.pop(0)
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

    def stopRecCams(self):

        try:
            globalValues.stopStrg = True
            globalValues.stateStorage = False

            strDataToTS = 'Выполнена остановка записи архива'
            globalValues.writeEventToDBJournalMain('Камеры', strDataToTS)

            try:
                pathData = globalValues.pathDefFldr + '/dataStrg.txt'
                file_strg = open(pathData, 'w')
                dataAll = str(globalValues.pathStrg) + ' 0 ' + str(globalValues.numberFolderDateSave)
                file_strg.write(dataAll)
                file_strg.close()
            except Exception as ex:
                globalValues.writeLogData('Функция записи состояния архива в файл', str(ex))

            if (globalValues.colorForm == 0):
                self.le_ArchState.setStyleSheet(
                    "background-color: rgb(75,75,75); border: none; color: rgb(215, 26, 26); font: 12pt \"MS Shell Dlg 2\";")
            else:
                self.le_ArchState.setStyleSheet(
                    "background-color: rgb(235, 235, 235); border: none; color: rgb(214, 104, 104); font: 12pt \"MS Shell Dlg 2\";")
            self.le_ArchState.setText('не запущен')
        except Exception as ex:
            globalValues.writeLogData('Функция остановки записи архива', str(ex))

if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Storage()
    ui.show()
    sys.exit(app.exec_())
