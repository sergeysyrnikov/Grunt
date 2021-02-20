from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import globalValues
import threading
from time import sleep
import pymysql
import datetime
import time
from panelMesBox import Ui_mes_box

# globalValues.colorForm = 0

class Ui_Journal(QtWidgets.QDialog):

    # con = pymysql.connections

    globalValues.checkUpdateTblJournal = True
    stopUpdateTblJournal = False

    changeCount = False
    curCount = 0
    listItem = []

    lstLight = [[]]
    lstDark = [[]]
    lengthLight = 0
    lengthDark = 0

    checkSearchEls = False

    firstCallChangeScroll = True

    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("Dialog")
        self.setFixedSize(1090, 1005)
        self.setStyleSheet("")
        self.labelnameForm = QtWidgets.QLabel(self)
        self.labelnameForm.setGeometry(QtCore.QRect(480, -5, 161, 47))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelnameForm.setFont(font)
        self.labelnameForm.setObjectName("labelnameForm")
        self.lblIconJournal = QtWidgets.QLabel(self)
        self.lblIconJournal.setGeometry(QtCore.QRect(450, 8, 23, 23))
        self.lblIconJournal.setText("")
        self.lblIconJournal.setObjectName("lblIconJournal")
        self.line1 = QtWidgets.QFrame(self)
        self.line1.setGeometry(QtCore.QRect(450, 33, 195, 16))
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        self.label_front1 = QtWidgets.QLabel(self)
        self.label_front1.setGeometry(QtCore.QRect(10, 53, 1071, 940))
        self.label_front1.setText("")
        self.label_front1.setObjectName("label_front1")
        self.label_front3 = QtWidgets.QLabel(self)
        self.label_front3.setGeometry(QtCore.QRect(18, 144, 1055, 841))
        self.label_front3.setText("")
        self.label_front3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_front3.setObjectName("label_front3")
        self.tblJournal = QtWidgets.QTableWidget(self)
        self.tblJournal.setGeometry(QtCore.QRect(26, 155, 1030, 821))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblJournal.sizePolicy().hasHeightForWidth())
        self.tblJournal.verticalScrollBar().hide()
        # self.tblJournal.setSizePolicy(sizePolicy)
        # self.tblJournal.setInputMethodHints(QtCore.Qt.ImhDate)
        self.tblJournal.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tblJournal.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tblJournal.setObjectName("tblJournal")
        self.tblJournal.setColumnCount(4)
        self.tblJournal.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblJournal.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblJournal.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblJournal.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblJournal.setHorizontalHeaderItem(3, item)
        # self.tblJournal.horizontalHeader().setCascadingSectionResizes(False)
        # self.tblJournal.horizontalHeader().setDefaultSectionSize(257)
        # self.tblJournal.horizontalHeader().setMinimumSectionSize(31)
        # self.tblJournal.horizontalHeader().setStretchLastSection(False)
        self.label_filtertype = QtWidgets.QLabel(self)
        self.label_filtertype.setGeometry(QtCore.QRect(30, 100, 111, 31))
        self.label_filtertype.setObjectName("label_filtertype")
        self.comboFilter = QtWidgets.QComboBox(self)
        self.comboFilter.setGeometry(QtCore.QRect(150, 100, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboFilter.setFont(font)
        self.comboFilter.setObjectName("comboFilter")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.btnFilter = QtWidgets.QPushButton(self)
        self.btnFilter.setGeometry(QtCore.QRect(740, 100, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnFilter.setFont(font)
        self.btnFilter.setObjectName("btnFilter")
        self.label_front2 = QtWidgets.QLabel(self)
        self.label_front2.setGeometry(QtCore.QRect(18, 60, 1055, 80))
        self.label_front2.setText("")
        self.label_front2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_front2.setObjectName("label_front2")
        self.frmDateRng = QtWidgets.QFrame(self)
        self.frmDateRng.setGeometry(QtCore.QRect(240, 99, 471, 31))
        self.frmDateRng.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmDateRng.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmDateRng.setObjectName("frmDateRng")
        self.label_DateRng = QtWidgets.QLabel(self.frmDateRng)
        self.label_DateRng.setGeometry(QtCore.QRect(10, 5, 71, 21))
        self.label_DateRng.setObjectName("label_DateRng")
        self.label_dateAt = QtWidgets.QLabel(self.frmDateRng)
        self.label_dateAt.setGeometry(QtCore.QRect(93, 5, 24, 21))
        self.label_dateAt.setObjectName("label_dateAt")
        self.DTEditRngAt = QtWidgets.QDateTimeEdit(self.frmDateRng)
        self.DTEditRngAt.setGeometry(QtCore.QRect(120, 0, 146, 31))
        self.DTEditRngAt.setObjectName("DTEditRngAt")
        self.DTEditRngTo = QtWidgets.QDateTimeEdit(self.frmDateRng)
        self.DTEditRngTo.setGeometry(QtCore.QRect(310, 0, 146, 31))
        self.DTEditRngTo.setObjectName("DTEditRngTo")
        self.label_DateTo = QtWidgets.QLabel(self.frmDateRng)
        self.label_DateTo.setGeometry(QtCore.QRect(280, 5, 24, 21))
        self.label_DateTo.setObjectName("label_DateTo")
        self.label_iconfilter = QtWidgets.QLabel(self)
        self.label_iconfilter.setGeometry(QtCore.QRect(22, 67, 30, 30))
        self.label_iconfilter.setText("")
        self.label_iconfilter.setObjectName("label_iconfilter")
        self.frmDateFix = QtWidgets.QFrame(self)
        self.frmDateFix.setGeometry(QtCore.QRect(240, 99, 471, 31))
        self.frmDateFix.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmDateFix.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmDateFix.setObjectName("frmDateFix")
        self.label_DateFix = QtWidgets.QLabel(self.frmDateFix)
        self.label_DateFix.setGeometry(QtCore.QRect(10, 5, 51, 21))
        self.label_DateFix.setObjectName("label_DateFix")
        self.DTEitFix = QtWidgets.QDateTimeEdit(self.frmDateFix)
        self.DTEitFix.setGeometry(QtCore.QRect(70, 0, 146, 31))
        self.DTEitFix.setObjectName("DTEitFix")
        self.btnFilterDel = QtWidgets.QPushButton(self)
        self.btnFilterDel.setGeometry(QtCore.QRect(930, 100, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnFilterDel.setFont(font)
        self.btnFilterDel.setIconSize(QtCore.QSize(25, 25))
        self.btnFilterDel.setObjectName("btnFilterDel")
        self.btnFilterRefresh = QtWidgets.QPushButton(self)
        self.btnFilterRefresh.setGeometry(QtCore.QRect(1030, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnFilterRefresh.setFont(font)
        self.btnFilterRefresh.setText("")
        self.btnFilterRefresh.setIconSize(QtCore.QSize(25, 25))
        self.btnFilterRefresh.setObjectName("btnFilterRefresh")
        self.lblBack = QtWidgets.QLabel(self)
        self.lblBack.setGeometry(QtCore.QRect(0, 0, 1091, 1005))
        self.lblBack.setText("")
        self.lblBack.setObjectName("lblBack")
        self.verticalScrollBar = QtWidgets.QScrollBar(self)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1055, 178, 10, 798))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.lblBack.raise_()
        self.label_front1.raise_()
        self.label_front2.raise_()
        self.label_front3.raise_()
        self.labelnameForm.raise_()
        self.lblIconJournal.raise_()
        self.line1.raise_()
        self.tblJournal.raise_()
        self.label_filtertype.raise_()
        self.comboFilter.raise_()
        self.btnFilter.raise_()
        self.label_iconfilter.raise_()
        self.btnFilterDel.raise_()
        self.btnFilterRefresh.raise_()
        self.frmDateFix.raise_()
        self.frmDateRng.raise_()
        self.verticalScrollBar.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        # self.runThJournal()
        self.firstSet()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Панель журнала"))
        self.labelnameForm.setText(_translate("Dialog", "Журнал событий"))
        self.tblJournal.setSortingEnabled(True)
        item = self.tblJournal.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Дата"))
        item = self.tblJournal.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Время"))
        item = self.tblJournal.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Объект"))
        item = self.tblJournal.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Событие"))
        self.label_filtertype.setText(_translate("Dialog", "Тип фильтра:"))
        self.comboFilter.setItemText(0, _translate("Dialog", "Нет"))
        self.comboFilter.setItemText(1, _translate("Dialog", "Дата"))
        self.comboFilter.setItemText(2, _translate("Dialog", "Период"))
        self.btnFilter.setText(_translate("Dialog", "    Применить фильтр"))
        self.label_DateRng.setText(_translate("Dialog", "Период:"))
        self.label_dateAt.setText(_translate("Dialog", "От"))
        self.label_DateTo.setText(_translate("Dialog", "До"))
        self.label_iconfilter.setToolTip(_translate("Dialog", "Фильтр для поиска"))
        self.label_DateFix.setText(_translate("Dialog", "Дата :"))
        self.btnFilterDel.setText(_translate("Dialog", "    Удалить"))

    def firstSet(self):

        self.tblJournal.setFont(QtGui.QFont("Arial", 9, QtGui.QFont.Bold))
        self.DTEitFix.setFont(QtGui.QFont("MS Shell Dlg 2", 11))
        self.DTEditRngTo.setFont(QtGui.QFont("MS Shell Dlg 2", 11))
        self.DTEditRngAt.setFont(QtGui.QFont("MS Shell Dlg 2", 11))

        self.lstLight = [[self.labelnameForm, "background-color: rgb(252,252,252);\n"
                                              "color: rgb(0,0,0);\n"
                                              "border-radius: 5px;"],
                         [self.lblIconJournal,
                          "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));\n"
                          "image: url(" + globalValues.pathStyleImgs + "iconworkpanel1.png);"],
                         [self.line1, "background-color: rgb(252,252,252);\n"
                                      "gridline-color: rgb(20, 18, 57);"],
                         [self.label_front1, "background-color: rgb(242,242,242);\n"
                                             "border-radius: 10px;\n"
                                             "border: 1px solid rgb(205,205,205);"],
                         [self.label_front3, "background-color: rgb(235,235,235);\n"
                                             "border-radius: 10px;\n"
                                             "border: 1px solid rgb(150,150,150);\n"
                                             "font: 10pt \"MS Shell Dlg 2\";"],
                         [self.tblJournal, "QTableWidget {background-color: rgb(235,235,235);\n"
                                           "border: 1px solid rgb(150,150,150);\n"
                                           "gridline-color: rgb(89,89,89);\n"
                                           "border-radius:5px;\n"
                                           "border-bottom-right-radius: 0px;\n"
                                           "color:black;}\n"
                                           "QLineEdit {background-color: white;}\n"
                                           "QHeaderView::section {\n"
                                           "gridline-color: rgb(89,89,89);\n"
                                           "background-color: rgb(142,187,208);\n"
                                           "color: black;};\n"
                                           ""],
                         [self.label_filtertype, "background-color: rgb(235,235,235);\n"
                                                 "color: rgb(0,0,0);\n"
                                                 "font: 12pt \"MS Shell Dlg 2\";"],
                         [self.comboFilter, "background-color: rgb(227,227,227);\n"
                                            "color: black;\n"
                                            "border-radius: 3px;\n"
                                            "border: 1px solid rgb(135,135,135);"],
                         [self.btnFilter, "QPushButton:!hover {background-color: rgb(227,227,227);\n"
                                          "color: rgb(0,0,0);\n"
                                          "border-radius:3px;\n"
                                          "border:1px solid rgb(135,135,135);\n"
                                          "image: url(" + globalValues.pathStyleImgs + "iconsearch12grey.png);}\n"
                                          "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-radius:3px;\n"
                                          "border:1px solid rgb(63,63,63);\n"
                                          "image: url(" + globalValues.pathStyleImgs + "iconsearch12.png);}\n"
                                          "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-radius:3px;\n"
                                          "border:1px solid rgb(63,63,63);\n"
                                          "image: url(" + globalValues.pathStyleImgs + "iconsearch12.png);};"],
                         [self.label_front2, "background-color: rgb(235,235,235);\n"
                                             "border-radius: 10px;\n"
                                             "border: 1px solid rgb(150,150,150);\n"
                                             "font: 10pt \"MS Shell Dlg 2\";"],
                         [self.frmDateRng, "background-color: rgb(235,235,235);"],
                         [self.label_DateRng, "background-color: rgb(235,235,235);\n"
                                              "color: rgb(0,0,0);\n"
                                              "font: 12pt \"MS Shell Dlg 2\";"],
                         [self.label_dateAt, "background-color: rgb(235,235,235);\n"
                                             "color: rgb(0,0,0);\n"
                                             "font: 12pt \"MS Shell Dlg 2\";"],
                         [self.DTEditRngAt, "background-color: rgb(227,227,227);\n"
                                            "color: black;\n"
                                            "border-radius: 3px;\n"
                                            "border: 1px solid rgb(135,135,135);\n"
                                            "font: 11pt \"MS Shell Dlg 2\";"],
                         [self.DTEditRngTo, "background-color: rgb(227,227,227);\n"
                                            "color: black;\n"
                                            "border-radius: 3px;\n"
                                            "border: 1px solid rgb(135,135,135);\n"
                                            "font: 11pt \"MS Shell Dlg 2\";"],
                         [self.label_DateTo, "background-color: rgb(235,235,235);\n"
                                             "color: rgb(0,0,0);\n"
                                             "font: 12pt \"MS Shell Dlg 2\";"],
                         [self.label_iconfilter, "background-color: rgb(235,235,235);\n"
                                                 "image: url(" + globalValues.pathStyleImgs + "iconfilter2.png);"],
                         [self.frmDateFix, "background-color: rgb(235,235,235);"],
                         [self.label_DateFix, "background-color: rgb(235,235,235);\n"
                                              "color: rgb(0,0,0);\n"
                                              "font: 12pt \"MS Shell Dlg 2\";"],
                         [self.DTEitFix, "background-color: rgb(227,227,227);\n"
                                         "color: black;\n"
                                         "border-radius: 3px;\n"
                                         "border: 1px solid rgb(135,135,135);\n"
                                         "font: 11pt \"MS Shell Dlg 2\";"],
                         [self.btnFilterDel, "QPushButton:!hover {background-color: rgb(227,227,227);\n"
                                             "color: rgb(0,0,0);\n"
                                             "border-radius:3px;\n"
                                             "border:1px solid rgb(135,135,135);\n"
                                             "image: url(" + globalValues.pathStyleImgs + "iconfilterdel5grey.png);}\n"
                                             "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "border-radius:3px;\n"
                                             "border:1px solid rgb(63,63,63);\n"
                                             "image: url(" + globalValues.pathStyleImgs + "iconfilterdel5.png);}\n"
                                             "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "border-radius:3px;\n"
                                             "border:1px solid rgb(63,63,63);\n"
                                             "image: url(" + globalValues.pathStyleImgs + "iconfilterdel5.png);};"],
                         [self.btnFilterRefresh, "QPushButton:!hover {background-color: rgb(227,227,227);\n"
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
                         [self.lblBack, "background-color: rgb(252,252,252);\n"
                                        "gridline-color: rgb(20, 18, 57);"],
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
                        [self.line1, "background-color: rgb(62,62,62);\n"
                                     "gridline-color: rgb(20, 18, 57);"],
                        [self.label_front1, "background-color: rgb(66,66,66);\n"
                                            "border-radius: 10px;"],
                        [self.label_front3, "background-color: rgb(75,75,75);\n"
                                            "color: white;\n"
                                            "border-radius: 10px;\n"
                                            "font: 10pt \"MS Shell Dlg 2\";"],
                        [self.tblJournal, "QTableWidget {background-color: rgb(42,42,42);\n"
                                          "border: 1px solid rgb(63,63,63);\n"
                                          "gridline-color: rgb(89,89,89);\n"
                                          "border-radius:5px;\n"
                                          "border-bottom-right-radius: 0px;\n"
                                          "color:white;}\n"
                                          "QLineEdit {background-color: white;}\n"
                                          "QHeaderView::section {\n"
                                          "gridline-color: rgb(89,89,89);\n"
                                          "background-color: rgb(50,75,115);};\n"
                                          ""],
                        [self.label_filtertype, "background-color: rgb(75,75,75);\n"
                                                "color: rgb(255,255,255);\n"
                                                "font: 12pt \"MS Shell Dlg 2\";"],
                        [self.comboFilter, "background-color: rgb(89,89,89);\n"
                                           "color: white;"],
                        [self.btnFilter, "QPushButton:!hover {background-color: rgb(89,89,89);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius:3px;\n"
                                         "border:1px solid rgb(63,63,63);\n"
                                         "image: url(" + globalValues.pathStyleImgs + "iconsearch12.png);}\n"
                                         "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius:3px;\n"
                                         "border:1px solid rgb(63,63,63);\n"
                                         "image: url(" + globalValues.pathStyleImgs + "iconsearch12.png);}\n"
                                         "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius:3px;\n"
                                         "border:1px solid rgb(63,63,63);\n"
                                         "image: url(" + globalValues.pathStyleImgs + "iconsearch12.png);};"],
                        [self.label_front2, "background-color: rgb(75,75,75);\n"
                                            "color: white;\n"
                                            "border-radius: 10px;\n"
                                            "font: 10pt \"MS Shell Dlg 2\";"],
                        [self.frmDateRng, "background-color: rgb(75, 75, 75);"],
                        [self.label_DateRng, "background-color: rgb(75,75,75);\n"
                                             "color: rgb(255,255,255);\n"
                                             "font: 12pt \"MS Shell Dlg 2\";"],
                        [self.label_dateAt, "background-color: rgb(75,75,75);\n"
                                            "color: rgb(255,255,255);\n"
                                            "font: 12pt \"MS Shell Dlg 2\";"],
                        [self.DTEditRngAt, "background-color: rgb(89,89,89);\n"
                                           "color: rgb(255,255,255);\n"
                                           "font: 11pt \"MS Shell Dlg 2\";"],
                        [self.DTEditRngTo, "background-color: rgb(89,89,89);\n"
                                           "color: rgb(255,255,255);\n"
                                           "font: 11pt \"MS Shell Dlg 2\";"],
                        [self.label_DateTo, "background-color: rgb(75,75,75);\n"
                                            "color: rgb(255,255,255);\n"
                                            "font: 12pt \"MS Shell Dlg 2\";"],
                        [self.label_iconfilter, "background-color: rgb(75,75,75);\n"
                                                "image: url(" + globalValues.pathStyleImgs + "iconfilter2.png);"],
                        [self.frmDateFix, "background-color: rgb(75, 75, 75);"],
                        [self.label_DateFix, "background-color: rgb(75,75,75);\n"
                                             "color: rgb(255,255,255);\n"
                                             "font: 12pt \"MS Shell Dlg 2\";"],
                        [self.DTEitFix, "background-color: rgb(89,89,89);\n"
                                        "color: rgb(255,255,255);\n"
                                        "font: 11pt \"MS Shell Dlg 2\";"],
                        [self.btnFilterDel, "QPushButton:!hover {background-color: rgb(89,89,89);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius:3px;\n"
                                            "border:1px solid rgb(63,63,63);\n"
                                            "image: url(" + globalValues.pathStyleImgs + "iconfilterdel5.png);}\n"
                                            "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius:3px;\n"
                                            "border:1px solid rgb(63,63,63);\n"
                                            "image: url(" + globalValues.pathStyleImgs + "iconfilterdel5.png);}\n"
                                            "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius:3px;\n"
                                            "border:1px solid rgb(63,63,63);\n"
                                            "image: url(" + globalValues.pathStyleImgs + "iconfilterdel5.png);};"],
                        [self.btnFilterRefresh, "QPushButton:!hover {background-color: rgb(89,89,89);\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "border-radius:3px;\n"
                                                "border:1px solid rgb(63,63,63);\n"
                                                "image: url(" + globalValues.pathStyleImgs + "iconrefresh.png);}\n"
                                                "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "border-radius:3px;\n"
                                                "border:1px solid rgb(63,63,63);\n"
                                                "image: url(" + globalValues.pathStyleImgs + "iconrefresh.png);}\n"
                                                "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "border-radius:3px;\n"
                                                "border:1px solid rgb(63,63,63);\n"
                                                "image: url(" + globalValues.pathStyleImgs + "iconrefresh.png);};"],
                        [self.lblBack, "background-color: rgb(62,62,62);\n"
                                       "gridline-color: rgb(20, 18, 57);"],
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

        globalValues.stopUpdateTblJournal = False

        self.tblJournal.setColumnCount(4)
        self.tblJournal.setColumnWidth(0, 120)
        self.tblJournal.setColumnWidth(1, 120)
        self.tblJournal.setColumnWidth(2, 160)
        self.tblJournal.setColumnWidth(3, 628)
        myQHeaderView = self.tblJournal.horizontalHeader()
        myQHeaderView.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        myQHeaderView.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        myQHeaderView.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        myQHeaderView.setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)
        # myQHeaderView.setStretchLastSection(False)
        self.tblJournal.setHorizontalHeader(myQHeaderView)
        self.tblJournal.verticalHeader().hide()
        self.tblJournal.horizontalScrollBar().hide()


        self.tblJournal.verticalHeader().setVisible(False)
        self.changeStCb()

        # time.sleep(30)

        self.comboFilter.currentIndexChanged.connect(self.changeStCb)

        self.btnFilterRefresh.clicked.connect(self.refreshTbl)

        dateToday = datetime.date.today().strftime('%d.%m.%Y')
        str_date_today = str(dateToday)
        cur_time = datetime.datetime.time(datetime.datetime.now())
        str_cur_time = str(cur_time)
        len_cur_time = len(str_cur_time)
        str_cur_time = str_cur_time[0: (len_cur_time - 10)]
        date_time_at = str_date_today + " " + '00:00'
        date_time_to = str_date_today + " " + str_cur_time
        dateCur = str_date_today
        datetimeTo = QtCore.QDateTime.fromString(date_time_to, 'd.M.yyyy hh:mm')
        datetimeAt = QtCore.QDateTime.fromString(date_time_at, 'd.M.yyyy hh:mm')
        date = QtCore.QDateTime.fromString(dateCur, 'd.M.yyyy')
        self.DTEditRngTo.setDateTime(datetimeTo)
        self.DTEditRngAt.setDateTime(datetimeAt)
        self.DTEitFix.setDateTime(date)

        self.btnFilter.clicked.connect(self.searchEls)
        self.btnFilterDel.clicked.connect(self.removeJournal)
        self.verticalScrollBar.valueChanged.connect(self.sync_func)
        self.updateTable()

        self.tblJournal.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

    def sync_func(self):
        self.tblJournal.verticalScrollBar().setValue(self.verticalScrollBar.value())

    def changeColor(self, object, str):
            object.setStyleSheet(str)

    def changeCOLORMainPanelGrunt(self):

        delta = int((0.1 / self.lengthDark) * 1000)

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

    def refreshTbl(self):
        try:
            globalValues.checkUpdateTblJournal = True
            self.stopUpdateTblJournal = False
            self.updateTable()
            globalValues.writeEventToDBJournalMain('Журнал', 'Выполнено обновление таблицы журнала')
            globalValues.checkUpdateTblJournal = True
        except Exception as ex:
            globalValues.writeLogData('Функция обновления таблицы журнала', str(ex))

    def searchEls(self):
        try:
            dataCb = self.comboFilter.currentIndex()

            print(dataCb)

            if (dataCb == 1):
                self.checkSearchEls = True
                globalValues.checkUpdateTblJournal = True
                globalValues.testVal = True
                self.updateTable()
                print('startingUpdateTbl!!!')

                dataDate = self.DTEitFix.text()
                dataDate = dataDate[0 : 10]

                try:
                            countItems = self.tblJournal.rowCount()
                            if (countItems == ''):
                                countItems = 0

                            countItems = int(countItems)
                            dataCount = countItems

                            # print(countItems)
                            self.listItem = []
                            for i in range(countItems - 1, -1,  -1):
                                # print(i)
                                # print(countItems)
                                # print(self.tblJournal.item(i, 0).text() )
                                dataItem = str(self.tblJournal.item(i, 0).text())
                                if (dataItem == ''):
                                    dataItem = ' '
                                is_data_in_db = dataDate in dataItem
                                if (is_data_in_db == False):
                                    dataCount -= 1
                                    self.listItem.append(i)
                                    self.tblJournal.removeRow(i)
                                    # self.tblJournal.clearSpans()

                            # self.tblJournal.setRowCount(dataCount)
                            # self.tblJournal.updateGeometry()
                            self.curCount = dataCount
                            self.changeCount = True

                except Exception as ex:
                    globalValues.writeLogData('Поиск по дате в таблице журналирования событий', str(ex))

            elif (dataCb == 2):
                # print('checkingTimes')
                self.checkSearchEls = True
                globalValues.checkUpdateTblJournal = True
                self.updateTable()
                # sleep(0.2)
                # self.stopUpdateTblJournal = True
                dataDateAt = self.DTEditRngAt.text()
                lenDateAt = len(dataDateAt)
                dataTimeAt = dataDateAt[11 : lenDateAt]
                if (len(dataTimeAt) == 4):
                    dataTimeAt = '0' + dataTimeAt
                dataDateAt = dataDateAt[0:10]


                # print(dataDateAt + 'Time: ' + dataTimeAt)

                dataDateTo = self.DTEditRngTo.text()
                lenDateTo = len(dataDateTo)
                dataTimeTo = dataDateTo[11: lenDateTo]
                if (len(dataTimeTo) == 4):
                    dataTimeTo = '0' + dataTimeTo
                dataDateTo = dataDateTo[0:10]

                startTimeVal = self.valueTimeToIntSearch(dataTimeAt)
                endTimeVal = self.valueTimeToIntSearch(dataTimeTo)

                try:
                    self.listItem = []
                    countItems = self.tblJournal.rowCount()
                    # print('numberCounts: ')
                    # print(countItems)
                    if (countItems == ''):
                        countItems = 0

                    countItems = int(countItems)

                    # print(countItems)

                    for i in range(countItems - 1, -1, -1):
                        # print(i)
                        # print(countItems)
                        # print(self.tblJournal.item(i, 0).text())
                        dataItem = str(self.tblJournal.item(i, 0).text())
                        dataTimeItem = str(self.tblJournal.item(i, 1).text())
                        if (dataItem == ''):
                            dataItem = '0'


                        if self.checkDataTime(dataItem, dataDateAt, dataDateTo, startTimeVal, endTimeVal, dataTimeItem):
                            self.tblJournal.removeRow(i)
                        # # is_dataAt_in_db = dataDateAt in dataItem
                        # # is_dataTo_in_db = dataDateTo in dataItem
                        # if (valMonthAt == valMonthTo and valYearAt == valYearTo):
                        #     if (valDateAt <= valDateEl <= valDateTo):
                        #         dataTimeItem = str(self.tblJournal.item(i, 1).text())
                        #         timeElTbl = self.valueTimeToIntTbl(dataTimeItem)
                        #         # print('CurTime: ' + str(timeElTbl))
                        #         # print(startTimeVal)
                        #         # print(endTimeVal)
                        #         if (valDateEl == valDateAt):
                        #             if (timeElTbl < startTimeVal):
                        #                 self.tblJournal.removeRow(i)
                        #                 # self.listItem.append(i)
                        #         if (valDateEl == valDateTo):
                        #             if (timeElTbl> endTimeVal):
                        #                 self.tblJournal.removeRow(i)
                        #                 # self.listItem.append(i)
                        #
                        # elif (valMonthAt != valMonthTo and valYearAt == valYearTo):
                        #     if ((valDateAt <= valDateEl and valMonthEl == valMonthAt) or (valDateEl <= valDateTo and valMonthEl == valMonthTo) or (valMonthAt != valMonthEl and valMonthTo != valMonthEl)):
                        #         dataTimeItem = str(self.tblJournal.item(i, 1).text())
                        #         timeElTbl = self.valueTimeToIntTbl(dataTimeItem)
                        #         # print('CurTime: ' + str(timeElTbl))
                        #         # print(startTimeVal)
                        #         # print(endTimeVal)
                        #         if (valDateEl == valDateAt and valMonthEl == valMonthAt):
                        #             if (timeElTbl < startTimeVal):
                        #                 self.tblJournal.removeRow(i)
                        #                 # self.listItem.append(i)
                        #         if (valDateEl == valDateTo and valMonthEl == valMonthTo):
                        #             if (timeElTbl> endTimeVal):
                        #                 self.tblJournal.removeRow(i)
                        #
                        # elif (valYearAt != valYearTo):
                        #     if (valDateAt <= valDateEl <= valDateTo):
                        #         dataTimeItem = str(self.tblJournal.item(i, 1).text())
                        #         timeElTbl = self.valueTimeToIntTbl(dataTimeItem)
                        #         # print('CurTime: ' + str(timeElTbl))
                        #         # print(startTimeVal)
                        #         # print(endTimeVal)
                        #         if (valDateEl == valDateAt):
                        #             if (timeElTbl < startTimeVal):
                        #                 self.tblJournal.removeRow(i)
                        #                 # self.listItem.append(i)
                        #         if (valDateEl == valDateTo):
                        #             if (timeElTbl> endTimeVal):
                        #                 self.tblJournal.removeRow(i)
                        #                 # self.listItem.append(i)
                        #
                        # else:

                    self.changeCount = True

                except Exception as ex:
                    print('Error!')
                    globalValues.writeLogData('Поиск по дате и времени в таблице журналирования событий', str(ex))

            elif (dataCb == 0):
                globalValues.checkUpdateTblJournal = True
                self.updateTable()
        except Exception as ex:
            globalValues.writeLogData('Функция поиска', str(ex))

    def updateTable(self):

        try:

            if globalValues.debug:
                con = pymysql.connect(host='localhost',
                                      port=3306,
                                      user='sergey',
                                      passwd='34ubitav',
                                      db=globalValues.dbMySqlName)
            else:
                con = pymysql.connect(host=globalValues.my_sql_localhost,
                                      port=globalValues.my_sql_port,
                                      user=globalValues.my_sql_name,
                                      passwd=globalValues.my_sql_password,
                                      db=globalValues.dbMySqlName)

            cur = con.cursor()

            try:

                countRowsOld = 0

                start_time = round(time.time())

                if True:

                    # if (globalValues.stopAll or globalValues.stopUpdateTblJournal):
                    #     print('checkExit!')
                        # break

                    if (self.changeCount):
                        self.changeCount = False
                        # print('ChangeCount')
                        # print(self.curCount)

                        # countItems = self.tblJournal.rowCount()
                        # if (countItems == ''):
                        #     countItems = 0
                        #
                        # countItems = int(countItems)

                        # for index in self.listItem:
                        #     self.tblJournal.removeRow(index)

                        # self.tblJournal.setRowCount(self.curCount)
                        self.tblJournal.updateGeometry()
                        self.stopUpdateTblJournal = True
                        # break

                    if True:
                        start_time = round(time.time())
                        # print('updateTblIsWorking!!!')
                        # print(globalValues.stopUpdateTblJournal)
                        if True:
                        # with con:
                            cur.execute("SELECT * FROM " + globalValues.tblsDB[0])

                            rows = cur.fetchall()

                            countRows = 0

                            for row in rows:
                                countRows += 1

                            # print(countRows)

                            if ((countRows != 0 and countRows != countRowsOld) or (globalValues.checkUpdateTblJournal)):
                                self.tblJournal.setRowCount(0)
                                globalValues.checkUpdateTblJournal = False
                                valWdg = 0
                                # print('111111111111111')

                                for row in reversed(rows):
                                    # print(str(row[1]))
                                    # print(i)
                                    self.tblJournal.insertRow(valWdg)
                                    item = QtWidgets.QTableWidgetItem(str(row[1]))
                                    item.setTextAlignment(Qt.AlignCenter)
                                    if(globalValues.colorForm == 1):
                                        item.setForeground(QtGui.QBrush(Qt.black))
                                    else:
                                        item.setForeground(QtGui.QBrush(Qt.white))
                                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                    self.tblJournal.setItem(valWdg, 0, item)

                                    item = QtWidgets.QTableWidgetItem(str(row[2]))
                                    item.setTextAlignment(Qt.AlignCenter)
                                    if (globalValues.colorForm == 1):
                                        item.setForeground(QtGui.QBrush(Qt.black))
                                    else:
                                        item.setForeground(QtGui.QBrush(Qt.white))
                                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                    self.tblJournal.setItem(valWdg, 1, item)

                                    item = QtWidgets.QTableWidgetItem(str(row[3]))
                                    item.setTextAlignment(Qt.AlignCenter)
                                    if (globalValues.colorForm == 1):
                                        item.setForeground(QtGui.QBrush(Qt.black))
                                    else:
                                        item.setForeground(QtGui.QBrush(Qt.white))
                                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                    self.tblJournal.setItem(valWdg, 2, item)

                                    item = QtWidgets.QTableWidgetItem(str(row[4]))
                                    item.setTextAlignment(Qt.AlignCenter)
                                    if (globalValues.colorForm == 1):
                                        item.setForeground(QtGui.QBrush(Qt.black))
                                    else:
                                        item.setForeground(QtGui.QBrush(Qt.white))
                                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                    self.tblJournal.setItem(valWdg, 3, item)
                                    valWdg += 1

                                th_scroll = threading.Thread(target=self.thChangeScroll, args=(True, ))
                                th_scroll.start()

                                # print(valWdg)
                                countRowsOld = countRows

                if self.checkSearchEls:
                    self.checkSearchEls = False
                else:
                    self.tblJournal.setRowCount(500)

            except Exception as ex:
                globalValues.writeLogData('Поток обновления панели журнала', str(ex))

            cur.close()
            con.close()
        except Exception as ex:
            globalValues.writeLogData('Поток обновления панели журнала', str(ex))
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

            # my_thread.join()

    def changeStCb(self):
        try:
            dataCb = self.comboFilter.currentIndex()
            if (dataCb == 1):
                self.frmDateRng.hide()
                self.frmDateFix.show()
            elif (dataCb == 2):
                self.frmDateFix.hide()
                self.frmDateRng.show()
            elif (dataCb == 0):
                self.frmDateFix.hide()
                self.frmDateRng.hide()

        except Exception as ex:
            globalValues.writeLogData('Функция смены фильра поиска панели журнала', str(ex))

    def valueTimeToIntSearch(self, strTime):
        strTime = strTime + '00'
        strTime = strTime.replace(':', '')
        return(int(strTime))

    def valueTimeToIntTbl(self, strTime):
        strTime = strTime
        strTime = strTime.replace(':', '')
        return(int(strTime))

    def closeEvent(self, event):
        print('closePanel!!!')
        globalValues.stopUpdateTblJournal = True
        # sleep(5)
        self.close()

    def removeJournal(self):
        try:
            if globalValues.debug:
                con = pymysql.connect(host='localhost',
                                      port=3306,
                                      user='sergey',
                                      passwd='34ubitav',
                                      db=globalValues.dbMySqlName)
            else:
                con = pymysql.connect(host=globalValues.my_sql_localhost,
                                      port=globalValues.my_sql_port,
                                      user=globalValues.my_sql_name,
                                      passwd=globalValues.my_sql_password,
                                      db=globalValues.dbMySqlName)

            cur = con.cursor()

            try:

                # with con:
                if True:
                    cur.execute('SELECT id FROM ' + globalValues.tblsDB[0])
                    rows = cur.fetchall()

                    for row in rows:
                        query = ("DELETE FROM " + globalValues.tblsDB[0] + " where id = (%s)")
                        cur.execute(query, str(row[0]))
                        con.commit()

                    strDataToTS = 'Выполнено удаление записей'
                    globalValues.writeEventToDBJournalMain('Журнал событий', strDataToTS)

            except Exception as ex:
                globalValues.writeLogData('Функция удаления данных таблицы журнала', str(ex))

            cur.close()
            con.close()
            self.updateTable()
        except Exception as ex:
            globalValues.writeLogData('Функция удаления данных журнала', str(ex))

    def thChangeScroll(self, check):
        try:

            num_delta = 200
            if (self.firstCallChangeScroll):
                self.firstCallChangeScroll = False
                num_delta = 350

            # print('Delta: ' + str(num_delta))

            start_time = round(time.time() * 100)
            while True:
                numRows = self.tblJournal.verticalScrollBar().maximum()
                delta = round(abs(time.time() * 100) - start_time)

                print(num_delta)

                if numRows != 0:
                    print('changeBarScroll!!!' + str(numRows))
                    time.sleep(0.6)
                    self.verticalScrollBar.setMaximum(self.tblJournal.verticalScrollBar().maximum())
                    break
                # print('checkingScroll!!!: ' + str(numRows))

                if delta > num_delta:
                    if (check):
                        # print('changeScrollTimer')
                        self.verticalScrollBar.setMaximum(self.tblJournal.verticalScrollBar().maximum())
                    break

                time.sleep(0.1)

                if (globalValues.stopAll):
                    break
        except Exception as ex:
            globalValues.writeLogData('Поток обработки изменения скролла', str(ex))

    def checkDataTime(self, timeEl, timeAt, timeTo, startTimeVal, endTimeVal, dataTimeItem):
        try:
            valDateAt = int(timeAt[0:2])
            valMonthAt = int(timeAt[3:5])
            valYearAt = int(timeAt[6:10])

            valDateTo = int(timeTo[0:2])
            valMonthTo = int(timeTo[3:5])
            valYearTo = int(timeTo[6:10])

            valDateEl = int(timeEl[0:2])
            valMonthEl = int(timeEl[3:5])
            valYearEl = int(timeEl[6:10])

            if (valMonthAt == valMonthTo and valYearAt == valYearTo):
                print('changeDay')
                if (valDateAt <= valDateEl <= valDateTo):
                    timeElTbl = self.valueTimeToIntTbl(dataTimeItem)

                    if (valDateEl == valDateAt):
                        if (timeElTbl < startTimeVal):
                            return True
                    if (valDateEl == valDateTo):
                        if (timeElTbl > endTimeVal):
                            return True

                    return False
                return True
            elif (valMonthAt != valMonthTo and valYearAt == valYearTo):
                print('changeMonth')
                if ((valDateAt <= valDateEl and valMonthEl == valMonthAt) or (valDateEl <= valDateTo and valMonthEl == valMonthTo) or (valMonthAt < valMonthEl < valMonthTo)):
                    timeElTbl = self.valueTimeToIntTbl(dataTimeItem)

                    if (valDateEl == valDateAt and valMonthEl == valMonthAt):
                        if (timeElTbl < startTimeVal):
                            return True
                            # self.listItem.append(i)
                    if (valDateEl == valDateTo and valMonthEl == valMonthTo):
                        if (timeElTbl > endTimeVal):
                            return True

                    return False
                return True
            elif (valYearAt != valYearTo):
                print('changeYear')
                timeElTbl = self.valueTimeToIntTbl(dataTimeItem)

                if ((valYearEl == valYearAt and valMonthEl > valMonthAt) or (
                        valYearEl == valYearTo and valMonthEl < valMonthTo) or (valYearAt < valYearEl < valYearTo) or (
                        valYearEl == valYearAt and valMonthEl == valMonthAt and valDateEl >= valDateAt) or (
                        valYearEl == valYearTo and valMonthEl == valMonthTo and valDateEl <= valDateTo)):

                    if (valDateEl == valDateAt and valMonthEl == valMonthAt and valYearEl == valYearAt):
                        if (timeElTbl < startTimeVal):
                            return True
                    if (valDateEl == valDateTo and valMonthEl == valMonthTo and valYearEl == valYearTo):
                        if (timeElTbl > endTimeVal):
                            return True

                    return False

                return True
            else:
                print('NotCase!')
                return False

        except Exception as ex:
            globalValues.writeLogData('Функция проверки записи датаэдита', str(ex))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Journal()
    ui.show()
    sys.exit(app.exec_())
