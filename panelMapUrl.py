from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import time
import sys
import globalValues
import threading
import pymysql
from PyQt5.QtCore import Qt
from panelMesBox import Ui_mes_box


app = QtWidgets.QApplication(sys.argv)

globalValues.colorForm = 0

class Ui_DialogMap(QDialog):

    con = pymysql.connections

    lstLight = [[]]
    lstDark = [[]]
    lengthLight = 0
    lengthDark = 0
    delta = 40
    num = 0

    firstCall = True
    lstUrl = []

    firstCallChangeScroll = True

    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("Dialog")
        self.setFixedSize(700, 938)
        self.setStyleSheet("")
        self.labelnameForm = QtWidgets.QLabel(self)
        self.labelnameForm.setGeometry(QtCore.QRect(210, -5, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelnameForm.setFont(font)
        self.labelnameForm.setObjectName("labelnameForm")
        self.lblIconJournal = QtWidgets.QLabel(self)
        self.lblIconJournal.setGeometry(QtCore.QRect(180, 8, 23, 23))
        self.lblIconJournal.setText("")
        self.lblIconJournal.setObjectName("lblIconJournal")
        self.tblJournalUrl = QtWidgets.QTableWidget(self)
        self.tblJournalUrl.setGeometry(QtCore.QRect(10, 80, 671, 851))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblJournalUrl.sizePolicy().hasHeightForWidth())
        self.tblJournalUrl.setSizePolicy(sizePolicy)
        self.tblJournalUrl.setInputMethodHints(QtCore.Qt.ImhDate)
        self.tblJournalUrl.setObjectName("tblJournalUrl")
        self.tblJournalUrl.setColumnCount(4)
        self.tblJournalUrl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblJournalUrl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblJournalUrl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblJournalUrl.setHorizontalHeaderItem(2, item)
        self.tblJournalUrl.horizontalHeader().setCascadingSectionResizes(False)
        self.tblJournalUrl.horizontalHeader().setDefaultSectionSize(223)
        self.tblJournalUrl.horizontalHeader().setMinimumSectionSize(31)
        self.tblJournalUrl.horizontalHeader().setStretchLastSection(False)
        self.lblBack = QtWidgets.QLabel(self)
        self.lblBack.setGeometry(QtCore.QRect(0, 0, 700, 938))
        self.lblBack.setText("")
        self.lblBack.setObjectName("lblBack")
        self.btnSearchUrl = QtWidgets.QPushButton(self)
        self.btnSearchUrl.setGeometry(QtCore.QRect(420, 40, 102, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnSearchUrl.setFont(font)
        icon = QtGui.QIcon()
        self.btnSearchUrl.setIcon(icon)
        self.btnSearchUrl.setIconSize(QtCore.QSize(25, 25))
        self.btnSearchUrl.setObjectName("btnSearchUrl")
        self.btnRefreshUrl = QtWidgets.QPushButton(self)
        self.btnRefreshUrl.setGeometry(QtCore.QRect(660, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnRefreshUrl.setFont(font)
        self.btnRefreshUrl.setText("")
        icon1 = QtGui.QIcon()
        self.btnRefreshUrl.setIcon(icon1)
        self.btnRefreshUrl.setIconSize(QtCore.QSize(25, 25))
        self.btnRefreshUrl.setObjectName("btnRefreshUrl")
        self.leSearchTblUrl = QtWidgets.QLineEdit(self)
        self.leSearchTblUrl.setGeometry(QtCore.QRect(10, 40, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.leSearchTblUrl.setFont(font)
        self.leSearchTblUrl.setObjectName("leSearchTblUrl")
        self.comboSearchUrl = QtWidgets.QComboBox(self)
        self.comboSearchUrl.setGeometry(QtCore.QRect(350, 40, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboSearchUrl.setFont(font)
        self.comboSearchUrl.setObjectName("comboSearchUrl")
        self.btnSaveUrl = QtWidgets.QPushButton(self)
        self.btnSaveUrl.setGeometry(QtCore.QRect(530, 40, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnSaveUrl.setFont(font)
        self.btnSaveUrl.setIconSize(QtCore.QSize(25, 25))
        self.btnSaveUrl.setObjectName("btnSaveUrl")
        self.verticalScrollBar = QtWidgets.QScrollBar(self)
        self.verticalScrollBar.setGeometry(QtCore.QRect(680, 104, 10, 827))
        self.verticalScrollBar.setMaximum(59)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.lblBack.raise_()
        self.labelnameForm.raise_()
        self.lblIconJournal.raise_()
        self.tblJournalUrl.raise_()
        self.btnSearchUrl.raise_()
        self.btnRefreshUrl.raise_()
        self.leSearchTblUrl.raise_()
        self.comboSearchUrl.raise_()
        self.btnSaveUrl.raise_()
        self.verticalScrollBar.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        # self.runThJournal()
        self.firstCall()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Панель отслеживания ТС"))
        self.labelnameForm.setText(_translate("Dialog", "Настройка отслеживания ТС"))
        self.tblJournalUrl.setSortingEnabled(True)
        item = self.tblJournalUrl.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Номер ГРЗ ТС"))
        item = self.tblJournalUrl.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Номер З/Н"))
        item = self.tblJournalUrl.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Ссылка Агрегатора для отслеживания"))
        self.btnSearchUrl.setText(_translate("Dialog", "      Поиск"))
        # self.leSearchTblUrl.setText(_translate("Dialog", "Поиск"))
        self.btnSaveUrl.setText(_translate("Dialog", "     Сохранить"))

    def firstCall(self):

        self.tblJournalUrl.setFont(QtGui.QFont("Arial", 9, QtGui.QFont.Bold))

        self.leSearchTblUrl.setPlaceholderText('Поиск')

        self.lstLight = [[self.labelnameForm, "background-color: rgb(252,252,252);\n"
                                              "color: rgb(0,0,0);\n"
                                              "border-radius: 5px;"],
                         [self.lblIconJournal,
                          "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));\n"
                          "image: url(" + globalValues.pathStyleImgs + "iconworkpanel1.png);"],
                         [self.tblJournalUrl, "QTableWidget {background-color: rgb(242,242,242);\n"
                                              "border: 1px solid rgb(150,150,150);\n"
                                              "gridline-color: rgb(89,89,89);\n"
                                              "color:black;}\n"
                                              "QLineEdit {background-color: white;}\n"
                                              "QHeaderView::section {\n"
                                              "gridline-color: rgb(89,89,89);\n"
                                              "background-color: rgb(142,187,208);\n"
                                              "color: black;};"],
                         [self.lblBack, "background-color: rgb(252,252,252);\n"
                                        "gridline-color: rgb(20, 18, 57);"],
                         [self.btnSearchUrl, "QPushButton:!hover {background-color: rgb(227,227,227);\n"
                                             "color: rgb(0,0,0);\n"
                                             "border-radius:3px;\n"
                                             "border:1px solid rgb(135,135,135);\n"
                                             "image: url(" + globalValues.pathStyleImgs + "iconsearch8.png);}\n"
                                                                                          "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                                                                          "color: rgb(255, 255, 255);\n"
                                                                                          "border-radius:3px;\n"
                                                                                          "border:1px solid rgb(135,135,135);\n"
                                                                                          "image: url(" + globalValues.pathStyleImgs + "iconsearchwhite.png);}\n"
                                                                                                                                       "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                                                                                                                       "color: rgb(255, 255, 255);\n"
                                                                                                                                       "border-radius:3px;\n"
                                                                                                                                       "border:1px solid rgb(135,135,135);\n"
                                                                                                                                       "image: url(" + globalValues.pathStyleImgs + "iconsearchwhite.png);};"],
                         [self.btnRefreshUrl, "QPushButton:!hover {background-color: rgb(227,227,227);\n"
                                              "color: rgb(0,0,0);\n"
                                              "border-radius:3px;\n"
                                              "border:1px solid rgb(135,135,135);\n"
                                              "image: url(" + globalValues.pathStyleImgs + "iconrefreshgrey.png);}\n"
                                                                                           "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                                                                           "color: rgb(255, 255, 255);\n"
                                                                                           "border-radius:3px;\n"
                                                                                           "border:1px solid rgb(63,63,63);\n"
                                                                                           "image: url(" + globalValues.pathStyleImgs + "iconrefresh.png);}\n"
                                                                                                                                        "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                                                                                                                        "color: rgb(255, 255, 255);\n"
                                                                                                                                        "border-radius:3px;\n"
                                                                                                                                        "border:1px solid rgb(63,63,63);\n"
                                                                                                                                        "image: url(" + globalValues.pathStyleImgs + "iconrefresh.png);};r"],
                         [self.leSearchTblUrl, "background-color: rgb(242,242,242);\n"
                                               "color: rgb(0,0,0);\n"
                                               "border-radius: 3px;\n"
                                               "border: 1px solid rgb(150,150,150);"],
                         [self.comboSearchUrl, "background-color: rgb(227,227,227);\n"
                                               "color: black;\n"
                                               "border-radius: 3px;\n"
                                               "border: 1px solid rgb(135,135,135);"],
                         [self.btnSaveUrl, "QPushButton:!hover {background-color: rgb(227,227,227);\n"
                                           "color: rgb(0,0,0);\n"
                                           "border-radius:3px;\n"
                                           "border:1px solid rgb(135,135,135);\n"
                                           "image: url(" + globalValues.pathStyleImgs + "iconsaveGREY.png);}\n"
                                                                                        "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                                                                        "color: rgb(255, 255, 255);\n"
                                                                                        "border-radius:3px;\n"
                                                                                        "border:1px solid rgb(135,135,135);\n"
                                                                                        "image: url(" + globalValues.pathStyleImgs + "iconsaveWHITE.png);}\n"
                                                                                                                                     "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                                                                                                                     "color: rgb(255, 255, 255);\n"
                                                                                                                                     "border-radius:3px;\n"
                                                                                                                                     "border:1px solid rgb(135,135,135);\n"
                                                                                                                                     "image: url(" + globalValues.pathStyleImgs + "iconsaveWHITE.png);};"],
                         [self.verticalScrollBar, "QScrollBar:vertical {\n"
                                                  "border: 1px solid rgb(89,89,89);\n"
                                                  " background: rgb(255,255,255);\n"
                                                  "width:10px;\n"
                                                  "margin: 0px 0px 0px 0px;\n"
                                                  "}\n"
                                                  "QScrollBar::handle:vertical {\n"
                                                  "background: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop: 0 rgb(142,187,208), stop: 0.5 rgb(142,187,208), stop:1 rgb(142,187,208));\n"
                                                  "min-height: 0px;\n"
                                                  "}\n"
                                                  "QScrollBar::add-line:vertical {\n"
                                                  " background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 rgb(142,187,208), stop: 0.5 rgb(142,187,208),  stop:1 rgb(142,187,208));\n"
                                                  "height: 0px;\n"
                                                  "subcontrol-position: bottom;\n"
                                                  "subcontrol-origin: margin;\n"
                                                  "}\n"
                                                  "QScrollBar::sub-line:vertical {\n"
                                                  "background: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop: 0  rgb(142,187,208), stop: 0.5 rgb(142,187,208),  stop:1 rgb(142,187,208));\n"
                                                  "height: 0 px;\n"
                                                  "subcontrol-position: top;\n"
                                                  "subcontrol-origin: margin;\n"
                                                  "}"]]
        self.lstDark = [[self.labelnameForm, "background-color: rgb(62,62,62);\n"
                                             "color: rgb(255,255,255);\n"
                                             "border-radius: 5px;"],
                        [self.lblIconJournal,
                         "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));\n"
                         "image: url(" + globalValues.pathStyleImgs + "iconworkpanel1.png);"],
                        [self.tblJournalUrl, "QTableWidget {background-color: rgb(42,42,42);\n"
                                             "border: 1px solid rgb(63,63,63);\n"
                                             "gridline-color: rgb(89,89,89);\n"
                                             "color:white;}\n"
                                             "QLineEdit {background-color: white;}\n"
                                             "QHeaderView::section {\n"
                                             "gridline-color: rgb(89,89,89);\n"
                                             "background-color: rgb(50,75,115);};\n"
                                             ""],
                        [self.lblBack, "background-color: rgb(62,62,62);\n"
                                       "gridline-color: rgb(20, 18, 57);"],
                        [self.btnSearchUrl, "QPushButton:!hover {background-color: rgb(89,89,89);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius:3px;\n"
                                            "border:1px solid rgb(63,63,63);\n"
                                            "image: url(" + globalValues.pathStyleImgs + "iconsearchwhite.png);}\n"
                                                                                         "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                                                                         "color: rgb(255, 255, 255);\n"
                                                                                         "border-radius:3px;\n"
                                                                                         "border:1px solid rgb(63,63,63);\n"
                                                                                         "image: url(" + globalValues.pathStyleImgs + "iconsearchwhite.png);}\n"
                                                                                                                                      "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                                                                                                                      "color: rgb(255, 255, 255);\n"
                                                                                                                                      "border-radius:3px;\n"
                                                                                                                                      "border:1px solid rgb(63,63,63);\n"
                                                                                                                                      "image: url(" + globalValues.pathStyleImgs + "iconsearchwhite.png);};"],
                        [self.btnRefreshUrl, "QPushButton:!hover {background-color: rgb(89,89,89);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "border-radius:3px;\n"
                                             "border:1px solid rgb(63,63,63);\n"
                                             "image: url(" + globalValues.pathStyleImgs + "iconrefreshwhite.png);}\n"
                                                                                          "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                                                                          "color: rgb(255, 255, 255);\n"
                                                                                          "border-radius:3px;\n"
                                                                                          "border:1px solid rgb(63,63,63);\n"
                                                                                          "image: url(" + globalValues.pathStyleImgs + "iconrefreshwhite.png);}\n"
                                                                                                                                       "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                                                                                                                       "color: rgb(255, 255, 255);\n"
                                                                                                                                       "border-radius:3px;\n"
                                                                                                                                       "border:1px solid rgb(63,63,63);\n"
                                                                                                                                       "image: url(" + globalValues.pathStyleImgs + "iconrefreshwhite.png);};"],
                        [self.leSearchTblUrl, "background-color: rgb(42, 42, 42);\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "border-radius: 3px;"],
                        [self.comboSearchUrl, "background-color: rgb(89,89,89);\n"
                                              "color: white;\n"
                                              "border-radius: 3px;\n"
                                              "border: 1px solid rgb(63,63,63)"],
                        [self.btnSaveUrl, "QPushButton:!hover {background-color: rgb(89,89,89);\n"
                                          "color: rgb(255,255,255);\n"
                                          "border-radius:3px;\n"
                                          "border:1px solid rgb(63,63,63);\n"
                                          "image: url(" + globalValues.pathStyleImgs + "iconsaveWHITE.png);}\n"
                                                                                       "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                                                                       "color: rgb(255, 255, 255);\n"
                                                                                       "border-radius:3px;\n"
                                                                                       "border:1px solid rgb(135,135,135);\n"
                                                                                       "image: url(" + globalValues.pathStyleImgs + "iconsaveWHITE.png);}\n"
                                                                                                                                    "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                                                                                                                    "color: rgb(255, 255, 255);\n"
                                                                                                                                    "border-radius:3px;\n"
                                                                                                                                    "border:1px solid rgb(135,135,135);\n"
                                                                                                                                    "image: url(" + globalValues.pathStyleImgs + "iconsaveWHITE.png);};"],
                        [self.verticalScrollBar, "QScrollBar:vertical {\n"
                                                 "border: 1px solid rgb(63,63,63);\n"
                                                 " background: rgb(63,63,63);\n"
                                                 "width:10px;\n"
                                                 "margin: 0px 0px 0px 0px;\n"
                                                 "}\n"
                                                 "QScrollBar::add-page:vertical {background: rgb(89,89,89);}\n"
                                                 "QScrollBar::sub-page:vertical {background: rgb(89,89,89);}\n"
                                                 "QScrollBar::handle:vertical {\n"
                                                 "background: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop: 0 rgb(50,75,115), stop: 0.5 rgb(50,75,115), stop:1 rgb(50,75,115));\n"
                                                 "min-height: 0px;\n"
                                                 "}\n"
                                                 "QScrollBar::add-line:vertical {\n"
                                                 " background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 rgb(50,75,115), stop: 0.5 rgb(50,75,115),  stop:1 rgb(50,75,115));\n"
                                                 "height: 0px;\n"
                                                 "subcontrol-position: bottom;\n"
                                                 "subcontrol-origin: margin;\n"
                                                 "}\n"
                                                 "QScrollBar::sub-line:vertical {\n"
                                                 "background: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop: 0  rgb(50,75,115), stop: 0.5 rgb(50,75,115),  stop:1 rgb(50,75,115));\n"
                                                 "height: 0 px;\n"
                                                 "subcontrol-position: top;\n"
                                                 "subcontrol-origin: margin;\n"
                                                 "}"]]

        self.lengthLight = len(self.lstLight)
        self.lengthDark = len(self.lstDark)

        self.changeCOLORMainPanelGrunt()

        self.tblJournalUrl.setColumnWidth(0, 100)
        self.tblJournalUrl.setColumnWidth(1, 80)
        self.tblJournalUrl.setColumnWidth(2, 490)
        self.tblJournalUrl.setColumnWidth(3, 0)
        myQHeaderView = self.tblJournalUrl.horizontalHeader()
        myQHeaderView.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        myQHeaderView.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        myQHeaderView.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        myQHeaderView.setStretchLastSection(False)
        self.tblJournalUrl.verticalHeader().hide()
        self.tblJournalUrl.horizontalScrollBar().hide()
        self.tblJournalUrl.verticalScrollBar().hide()

        self.comboSearchUrl.addItem('Нет')
        self.comboSearchUrl.addItem('ГРЗ')
        self.comboSearchUrl.addItem('З/Н')

        self.btnRefreshUrl.clicked.connect(self.updateTbl)
        self.btnSaveUrl.clicked.connect(self.saveDataDatabase)
        self.btnSearchUrl.clicked.connect(self.searchEls)
        self.verticalScrollBar.valueChanged.connect(self.sync_func)

        self.connectToMySql()
        self.updateTbl()

    def sync_func(self):
        self.tblJournalUrl.verticalScrollBar().setValue(self.verticalScrollBar.value())

    def thChangeScroll(self, check):
        try:

            num_delta = 200
            if (self.firstCallChangeScroll):
                self.firstCallChangeScroll = False
                num_delta = 350

            # print('Delta: ' + str(num_delta))

            start_time = round(time.time() * 100)
            while True:
                numRows = self.tblJournalUrl.verticalScrollBar().maximum()
                delta = round(abs(time.time() * 100) - start_time)

                # print(num_delta)

                if numRows != 0:
                    print('changeBarScroll!!!' + str(numRows))
                    time.sleep(0.2)
                    self.verticalScrollBar.setMaximum(self.tblJournalUrl.verticalScrollBar().maximum())
                    break
                # print('checkingScroll!!!: ' + str(numRows))

                if delta > num_delta:
                    if (check):
                        # print('changeScrollTimer')
                        self.verticalScrollBar.setMaximum(self.tblJournalUrl.verticalScrollBar().maximum())
                    break

                time.sleep(0.1)

                if (globalValues.stopAll):
                    break
        except Exception as ex:
            globalValues.writeLogData('Поток обработки изменения скролла', str(ex))

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

    def saveDataDatabase(self):

        uiMes = Ui_mes_box()
        uiMes.lblStrInfo.setText('Вы уверены, что хотите сохранить изменения?')
        uiMes.btnOK.setText('Да')
        uiMes.btnCancel.setText('Нет')
        uiMes.exec_()
        strID = self.tblJournalUrl.item(0, 3).text()
        print(strID)

        if (uiMes.checkCont):
            try:

                if (self.checkMySql):
                    self.connectToMySql()

                with self.con:
                    cur = self.con.cursor()
                    cur.execute("SELECT * FROM " + globalValues.tblsDB[4])

                    rows = cur.fetchall()

                    strRows = ''
                    countRows = self.tblJournalUrl.rowCount()
                    strData = ''
                    # print(self.lstUrl)
                    for i in range(countRows):
                        dataOrder = self.tblJournalUrl.item(i, 0).text()
                        dataUrl = self.tblJournalUrl.item(i, 2).text()

                        if (dataUrl != self.lstUrl[i]):
                            strData += '#' + dataOrder + '(' + str(i + 1) + '), '

                        strID = self.tblJournalUrl.item(i, 3).text()

                        ID = int(strID)
                        print(dataUrl)

                        query = ("UPDATE " + globalValues.tblsDB[4] + " SET url = (%s) WHERE id= (%s)")
                        cur.execute(query, (dataUrl, ID))
                        self.con.commit()
                    # print(self.lstUrl)
                    # print('checkingDataUrl')
                    # print(strData)
                    if (strData != ''):
                        strData = strData[0:(len(strData) - 2)]
                        strDataToJournal = 'Изменены ссылки для З/Н: ' + strData

                        globalValues.writeEventToDBJournalMain('Отслеживание ТС', strDataToJournal)

                    cur.close()

            except Exception as ex:
                globalValues.writeLogData('Функция сохранения данных панель трэкинга ТС', str(ex))

            self.close()

    def updateTbl(self):

        i = 0

        while True:
            # print('qweqwe')
            try:
                if (self.checkMySql):
                    self.con = pymysql.connect(host=globalValues.my_sql_localhost,
                                               port=globalValues.my_sql_port,
                                               user=globalValues.my_sql_name,
                                               passwd=globalValues.my_sql_password, db=globalValues.dbMySqlName)

                with self.con:
                    cur = self.con.cursor()
                    cur.execute("SELECT number_order, number_grz FROM " + globalValues.tblsDB[1])

                    rows = cur.fetchall()

                    self.tblJournalUrl.setRowCount(0)

                    valWdg = 0

                    countRow = 0
                    for row in rows:
                        countRow += 1

                    for row in reversed(rows):
                        countRow -= 1
                        self.tblJournalUrl.insertRow(valWdg)
                        item = QtWidgets.QTableWidgetItem(str(row[1]))
                        item.setTextAlignment(Qt.AlignCenter)
                        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.tblJournalUrl.setItem(valWdg, 0, item)
                        item = QtWidgets.QTableWidgetItem(str(row[0]))
                        item.setTextAlignment(Qt.AlignCenter)
                        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.tblJournalUrl.setItem(valWdg, 1, item)
                        valWdg += 1



                    cur.execute("SELECT url, id FROM " + globalValues.tblsDB[4])

                    rowsUrl = cur.fetchall()

                    valWdg = 0
                    self.listDataLink = []
                    self.lstUrl = []
                    for row in reversed(rowsUrl):
                        self.listDataLink.append(str(row[0]))
                        item = QtWidgets.QTableWidgetItem(str(row[0]))
                        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                        item.setTextAlignment(Qt.AlignCenter)
                        self.tblJournalUrl.setItem(valWdg, 2, item)
                        item = QtWidgets.QTableWidgetItem(str(row[1]))
                        item.setTextAlignment(Qt.AlignCenter)
                        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.tblJournalUrl.setItem(valWdg, 3, item)
                        valWdg += 1

                        if self.firstCall:
                            self.lstUrl.append(str(row[0]))

                    self.firstCall = False

                    th_scroll = threading.Thread(target=self.thChangeScroll, args=(True, ))
                    th_scroll.start()

                    cur.close()

                    break

            except Exception as ex:
                globalValues.writeLogData('Функция обновления таблицы отслеживания в панели трэкинга ТС', str(ex))
                i += 1

            if (i > 2):
                break

    def refreshTbl(self):
        try:
            # globalValues.checkUpdateTblMap = True
            self.updateTbl()
            globalValues.writeEventToDBJournalMain('Отслеживание', 'Выполнено обновление таблицы отслеживания ТС')
            globalValues.checkUpdateTblJournal = True
        except Exception as ex:
            globalValues.writeLogData('Функция обновления таблицы журнала', str(ex))

    def searchEls(self):
        try:
            print('StartingSearch!!!')
            dataCb = self.comboSearchUrl.currentIndex()

            if (dataCb == 1):

                self.updateTbl()

                dataSearch = self.leSearchTblUrl.text()

                try:
                            countItems = self.tblJournalUrl.rowCount()
                            if (countItems == ''):
                                countItems = 0

                            countItems = int(countItems)

                            for i in range(countItems - 1, -1,  -1):
                                dataItem = str(self.tblJournalUrl.item(i, 0).text())
                                if (dataItem == ''):
                                    dataItem = ' '
                                is_data_in_db = dataSearch in dataItem
                                if (is_data_in_db == False):
                                    self.tblJournalUrl.removeRow(i)


                except Exception as ex:
                    globalValues.writeLogData('Поиск по ГРЗ в таблице отслеживания ТС', str(ex))

            elif (dataCb == 2):
                self.updateTbl()

                dataSearch = self.leSearchTblUrl.text()

                try:
                    countItems = self.tblJournalUrl.rowCount()
                    if (countItems == ''):
                        countItems = 0

                    countItems = int(countItems)

                    for i in range(countItems - 1, -1, -1):
                        dataItem = str(self.tblJournalUrl.item(i, 1).text())
                        if (dataItem == ''):
                            dataItem = ' '
                        is_data_in_db = dataSearch in dataItem
                        if (is_data_in_db == False):
                            self.tblJournalUrl.removeRow(i)


                except Exception as ex:
                    globalValues.writeLogData('Поиск по номеру З/Н в таблице отслеживания ТС', str(ex))

            elif (dataCb == 0):
                self.updateTbl()
        except Exception as ex:
            globalValues.writeLogData('Функция поиска', str(ex))

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
                globalValues.writeLogData('Функция подключения к БД панель трэкинга ТС', str(ex))

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
                globalValues.writeLogData('Функция проверки подключения к бд MySql панель трэкинга ТС', str(ex))


if __name__ == "__main__":
    ui = Ui_DialogMap()
    ui.show()
    sys.exit(app.exec_())
