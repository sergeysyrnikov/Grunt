from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt
import threading
import time
import sys
import globalValues
from PanelAddTS import Ui_add_TS
import pymysql
from panelMesBox import Ui_mes_box
from Panel3D import Ui_PanelCreateModel
from addUser import Ui_addUser

app = QtWidgets.QApplication(sys.argv)

globalValues.colorForm = 0

class Ui_TS_Base(QDialog):

    firstCallChangeScroll = True

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
        self.setFixedSize(1920, 1080)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.FramelessWindowHint)
        self.lblBack = QtWidgets.QLabel(self)
        self.lblBack.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.lblBack.setText("")
        self.lblBack.setObjectName("lblBack")
        self.frmTableDBTS = QtWidgets.QFrame(self)
        self.frmTableDBTS.setGeometry(QtCore.QRect(0, 31, 1920, 1041))
        self.frmTableDBTS.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmTableDBTS.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmTableDBTS.setObjectName("frmTableDBTS")
        self.tblTS = QtWidgets.QTableWidget(self.frmTableDBTS)
        self.tblTS.setGeometry(QtCore.QRect(20, 66, 1874, 965))
        self.tblTS.setObjectName("tblTS")
        self.tblTS.setColumnCount(14)
        self.tblTS.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(84, 122, 181))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblTS.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(84, 122, 181))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblTS.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(84, 122, 181))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblTS.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(84, 122, 181))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblTS.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblTS.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(84, 122, 181))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblTS.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(84, 122, 181))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblTS.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(84, 122, 181))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblTS.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(84, 122, 181))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblTS.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(84, 122, 181))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblTS.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(84, 122, 181))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblTS.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(84, 122, 181))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblTS.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(84, 122, 181))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblTS.setHorizontalHeaderItem(12, item)
        self.tblTS.horizontalHeader().setDefaultSectionSize(144)
        self.tblTS.horizontalHeader().setMinimumSectionSize(39)

        if (globalValues.colorForm == 1):
            self.tblTS.setStyleSheet("QTableWidget {background-color: rgb(235,235,235);\n"
            "border: 1px solid rgb(150,150,150);\n"
            "gridline-color: rgb(89,89,89);\n"
            "border-bottom-left-radius: 5px;\n"
            "border-bottom-right-radius: 0px;\n"
            "color:black;}\n"
            "QLineEdit {background-color: white;}\n"
            "QHeaderView::section {\n"
            "gridline-color: rgb(89,89,89);\n"
            "background-color: rgb(142,187,208);\n"
            "color: black;};")
        else:
            self.tblTS.setStyleSheet("QTableWidget {background-color: rgb(42,42,42);\n"
                         "border: 1px solid rgb(63,63,63);\n"
                         "border-radius:5px;\n"
                         "gridline-color: rgb(89,89,89);\n"
                         "border-bottom-right-radius: 0px;\n"
                         "color:white;}\n"
                         "QLineEdit {background-color: white;}\n"
                         "QHeaderView::section {\n"
                         "gridline-color: rgb(89,89,89);\n"
                         "background-color: rgb(50,75,115);};")
        self.lblMainBoxCams = QtWidgets.QLabel(self.frmTableDBTS)
        self.lblMainBoxCams.setEnabled(False)
        self.lblMainBoxCams.setGeometry(QtCore.QRect(10, 10, 1900, 1030))
        self.lblMainBoxCams.setText("")
        self.lblMainBoxCams.setObjectName("lblMainBoxCams")
        self.btnSearch = QtWidgets.QPushButton(self.frmTableDBTS)
        self.btnSearch.setGeometry(QtCore.QRect(850, 20, 102, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnSearch.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/iconsearch4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSearch.setIcon(icon)
        self.btnSearch.setIconSize(QtCore.QSize(25, 25))
        self.btnSearch.setObjectName("btnSearch")
        self.leSearchTbDBlTS = QtWidgets.QLineEdit(self.frmTableDBTS)
        self.leSearchTbDBlTS.setGeometry(QtCore.QRect(20, 20, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.leSearchTbDBlTS.setFont(font)
        self.leSearchTbDBlTS.setObjectName("leSearchTbDBlTS")
        self.comboSearch = QtWidgets.QComboBox(self.frmTableDBTS)
        self.comboSearch.setGeometry(QtCore.QRect(680, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboSearch.setFont(font)
        self.comboSearch.setObjectName("comboSearch")
        self.comboSearch.addItem("")
        self.comboSearch.addItem("")
        self.comboSearch.addItem("")
        self.comboSearch.addItem("")
        self.comboSearch.addItem("")
        self.btnSrchRefresh = QtWidgets.QPushButton(self.frmTableDBTS)
        self.btnSrchRefresh.setGeometry(QtCore.QRect(960, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnSrchRefresh.setFont(font)
        self.btnSrchRefresh.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/iconrefresh2323.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSrchRefresh.setIcon(icon1)
        self.btnSrchRefresh.setIconSize(QtCore.QSize(25, 25))
        self.btnSrchRefresh.setObjectName("btnSrchRefresh")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.frmTableDBTS)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1893, 90, 10, 941))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.btnAddTS = QtWidgets.QPushButton(self.frmTableDBTS)
        self.btnAddTS.setGeometry(QtCore.QRect(1770, 20, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnAddTS.setFont(font)
        self.btnAddTS.setIcon(icon)
        self.btnAddTS.setIconSize(QtCore.QSize(25, 25))
        self.btnAddTS.setObjectName("btnAddTS")
        self.label_filtertype = QtWidgets.QLabel(self.frmTableDBTS)
        self.label_filtertype.setGeometry(QtCore.QRect(580, 20, 91, 31))
        self.label_filtertype.setObjectName("label_filtertype")
        self.btnDelTS = QtWidgets.QPushButton(self.frmTableDBTS)
        self.btnDelTS.setGeometry(QtCore.QRect(1640, 20, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnDelTS.setFont(font)
        self.btnDelTS.setIcon(icon)
        self.btnDelTS.setIconSize(QtCore.QSize(25, 25))
        self.btnDelTS.setObjectName("btnDelTS")
        self.lblMainBoxCams.raise_()
        self.tblTS.raise_()
        self.btnSearch.raise_()
        self.leSearchTbDBlTS.raise_()
        self.comboSearch.raise_()
        self.btnSrchRefresh.raise_()
        self.verticalScrollBar.raise_()
        self.btnAddTS.raise_()
        self.label_filtertype.raise_()
        self.btnDelTS.raise_()
        self.frmHeadExit = QtWidgets.QFrame(self)
        self.frmHeadExit.setGeometry(QtCore.QRect(0, 0, 1920, 31))
        self.frmHeadExit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmHeadExit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmHeadExit.setObjectName("frmHeadExit")
        self.lblBarClose = QtWidgets.QLabel(self.frmHeadExit)
        self.lblBarClose.setGeometry(QtCore.QRect(25, 0, 1896, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.lblBarClose.setFont(font)
        self.lblBarClose.setObjectName("lblBarClose")
        self.lblIconBarClose = QtWidgets.QLabel(self.frmHeadExit)
        self.lblIconBarClose.setGeometry(QtCore.QRect(2, 0, 20, 30))
        self.lblIconBarClose.setText("")
        self.lblIconBarClose.setObjectName("lblIconBarClose")
        self.btnCloseDBTSform = QtWidgets.QPushButton(self.frmHeadExit)
        self.btnCloseDBTSform.setGeometry(QtCore.QRect(1890, 2, 26, 26))
        self.btnCloseDBTSform.setText("")
        self.btnCloseDBTSform.setObjectName("btnCloseDBTSform")
        self.label = QtWidgets.QLabel(self.frmHeadExit)
        self.label.setGeometry(QtCore.QRect(0, 0, 50, 30))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.lblBarClose.raise_()
        self.lblIconBarClose.raise_()
        self.btnCloseDBTSform.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        # self.runThJournal()
        self.firstCall()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tblTS.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Организация"))
        item = self.tblTS.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Наименование ТС"))
        item = self.tblTS.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Модель ТС"))
        item = self.tblTS.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "№ГРЗ"))
        item = self.tblTS.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Год изг-я"))
        item = self.tblTS.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Эко.класс ЕВРО"))
        item = self.tblTS.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Мощность двиг.,л.с.(кВт)"))
        item = self.tblTS.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Объем двиг.,см3"))
        item = self.tblTS.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "Масса пустой,кг."))
        item = self.tblTS.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "Разр.макс.масса,кг."))
        item = self.tblTS.horizontalHeaderItem(10)
        item.setText(_translate("Dialog", "Грузоподъемность,кг."))
        item = self.tblTS.horizontalHeaderItem(11)
        item.setText(_translate("Dialog", "Вместимость кузова,м3"))
        item = self.tblTS.horizontalHeaderItem(12)
        item.setText(_translate("Dialog", "Колесная ф-ла"))
        self.btnSearch.setText(_translate("Dialog", "      Поиск"))
        # self.leSearchTbDBlTS.setText(_translate("Dialog", "Поиск"))

        self.comboSearch.setItemText(0, _translate("Dialog", "Нет"))
        self.comboSearch.setItemText(1, _translate("Dialog", "Организация"))
        self.comboSearch.setItemText(2, _translate("Dialog", "Наименование ТС"))
        self.comboSearch.setItemText(3, _translate("Dialog", "Модель ТС"))
        self.comboSearch.setItemText(4, _translate("Dialog", "№ ГРЗ"))
        self.btnAddTS.setText(_translate("Dialog", "Добавить ТС"))
        self.label_filtertype.setText(_translate("Dialog", "Тип поиска:"))
        self.btnDelTS.setText(_translate("Dialog", "Удалить ТС"))
        self.lblBarClose.setText(_translate("Dialog", "АСМК-ГРУНТ"))

    def firstCall(self):

        self.leSearchTbDBlTS.setPlaceholderText('Поиск')

        #step x 130

        self.btnCreate3D = QtWidgets.QPushButton(self.frmTableDBTS)
        self.btnCreate3D.setGeometry(QtCore.QRect(1510, 20, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnCreate3D.setFont(font)
        # self.btnCreate3D.setIcon(icon)
        self.btnCreate3D.setIconSize(QtCore.QSize(25, 25))
        self.btnCreate3D.setObjectName("btnCr3D")
        self.btnCreate3D.raise_()
        self.btnCreate3D.setText('Создать 3D')

        self.btnAddUser = QtWidgets.QPushButton(self.frmTableDBTS)
        self.btnAddUser.setGeometry(QtCore.QRect(1380, 20, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnAddUser.setFont(font)
        # self.btnCreate3D.setIcon(icon)
        self.btnAddUser.setIconSize(QtCore.QSize(25, 25))
        self.btnAddUser.setObjectName("btnAddUser")
        self.btnAddUser.raise_()
        self.btnAddUser.setText('Пользователь')

        if (globalValues.curUserName != 'sergey'):
            self.btnAddUser.hide()
            self.btnCreate3D.hide()

        self.lstLight = [[self.lblBack, "background-color: rgb(242,242,242);"],
                         [self.frmTableDBTS, "background-color: rgb(242,242,242);"],
                         [self.tblTS, "QTableWidget {background-color: rgb(235,235,235);\n"
                                      "border: 1px solid rgb(150,150,150);\n"
                                      "gridline-color: rgb(89,89,89);\n"
                                      "border-bottom-left-radius: 5px;\n"
                                      "border-bottom-right-radius: 0px;\n"
                                      "color:black;}\n"
                                      "QLineEdit {background-color: white;}\n"
                                      "QHeaderView::section {\n"
                                      "gridline-color: rgb(89,89,89);\n"
                                      "background-color: rgb(142,187,208);\n"
                                      "color: black;};"],
                         [self.lblMainBoxCams, "background-color: rgb(242,242,242);\n"
                                               "border-radius: 5px;\n"
                                               "border: 2px solid rgb(205,205,205);"],
                         [self.btnSearch, "QPushButton:!hover {background-color: rgb(227,227,227);\n"
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
                         [self.leSearchTbDBlTS, "background-color: rgb(235,235,235);\n"
                                                "color: rgb(0,0,0);\n"
                                                "border-radius: 3px;\n"
                                                "border: 1px solid rgb(150,150,150);"],
                         [self.comboSearch, "background-color: rgb(227,227,227);\n"
                                            "color: black;\n"
                                            "border-radius: 3px;\n"
                                            "border: 1px solid rgb(135,135,135);"],
                         [self.btnSrchRefresh, "QPushButton:!hover {background-color: rgb(227,227,227);\n"
                                               "color: rgb(0,0,0);\n"
                                               "border-radius:3px;\n"
                                               "border:1px solid rgb(135,135,135);\n"
                                               "image: url(" + globalValues.pathStyleImgs + "iconrefreshgrey.png);}\n"
                                               "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "border-radius:3px;\n"
                                               "border:1px solid rgb(135,135,135);\n"
                                               "image: url(" + globalValues.pathStyleImgs + "iconrefreshwhite.png);}\n"
                                               "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "border-radius:3px;\n"
                                               "border:1px solid rgb(135,135,135);\n"
                                               "image: url(" + globalValues.pathStyleImgs + "iconrefreshwhite.png);};"],
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
                                                  "}"],
                         [self.btnAddTS, "QPushButton:!hover {background-color: rgb(227,227,227);\n"
                                         "color: rgb(0,0,0);\n"
                                         "border-radius:3px;\n"
                                         "border:1px solid rgb(135,135,135);}\n"
                                         "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius:3px;\n"
                                         "border:1px solid rgb(135,135,135);}\n"
                                         "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius:3px;\n"
                                         "border:1px solid rgb(135,135,135);};"],
                         [self.btnCreate3D, "QPushButton:!hover {background-color: rgb(227,227,227);\n"
                                         "color: rgb(0,0,0);\n"
                                         "border-radius:3px;\n"
                                         "border:1px solid rgb(135,135,135);}\n"
                                         "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius:3px;\n"
                                         "border:1px solid rgb(135,135,135);}\n"
                                         "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius:3px;\n"
                                         "border:1px solid rgb(135,135,135);};"],
                         [self.btnAddUser, "QPushButton:!hover {background-color: rgb(227,227,227);\n"
                                            "color: rgb(0,0,0);\n"
                                            "border-radius:3px;\n"
                                            "border:1px solid rgb(135,135,135);}\n"
                                            "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius:3px;\n"
                                            "border:1px solid rgb(135,135,135);}\n"
                                            "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius:3px;\n"
                                            "border:1px solid rgb(135,135,135);};"],
                         [self.label_filtertype, "background-color: rgb(242,242,242);\n"
                                                 "color: rgb(0,0,0);\n"
                                                 "font: 12pt \"MS Shell Dlg 2\";"],
                         [self.btnDelTS, "QPushButton:!hover {background-color: rgb(227,227,227);\n"
                                         "color: rgb(0,0,0);\n"
                                         "border-radius:3px;\n"
                                         "border:1px solid rgb(135,135,135);}\n"
                                         "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius:3px;\n"
                                         "border:1px solid rgb(135,135,135);}\n"
                                         "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius:3px;\n"
                                         "border:1px solid rgb(135,135,135);};"],
                         [self.frmHeadExit, "background-color: rgb(205,205,205);"],
                         [self.lblBarClose, "background-color: rgb(255,255,255);\n"
                                            "color: rgb(0,0,0);\n"
                                            ""],
                         [self.lblIconBarClose, "background-color: rgb(255,255,255);\n"
                                                "image: url(" + globalValues.pathStyleImgs + "sinaps1717.png);"],
                         [self.btnCloseDBTSform, "QPushButton:!hover{ background-color: rgb(255,255,255);\n"
                                                 "border-radius: 5px;\n"
                                                 "image: url(" + globalValues.pathStyleImgs + "iconextbl1919.png);}\n"
                                                 "QPushButton:hover { background-color: rgb(84,122,181);\n"
                                                 "border-radius: 3px;\n"
                                                 "image: url(" + globalValues.pathStyleImgs + "iconext1919.png);}\n"
                                                 "QPushButton:hover:pressed { background-color: rgb(50,75,115);\n"
                                                 "border-radius: 3px;\n"
                                                 "image: url(" + globalValues.pathStyleImgs + "iconext1919.png);};\n"
                                                 ""],
                         [self.label, "background-color: rgb(255,255,255);"]]

        self.lstDark = [[self.lblBack, "background-color: rgb(66,66,66);\n"
                                       "color: white;"],
                        [self.frmTableDBTS, "background-color: rgb(66,66,66);\n"
                                            "color: white;"],
                        [self.tblTS, "QTableWidget {background-color: rgb(42,42,42);\n"
                                     "border: 1px solid rgb(63,63,63);\n"
                                     "border-radius:5px;\n"
                                     "gridline-color: rgb(89,89,89);\n"
                                     "border-bottom-right-radius: 0px;\n"
                                     "color:white;}\n"
                                     "QLineEdit {background-color: white;}\n"
                                     "QHeaderView::section {\n"
                                     "gridline-color: rgb(89,89,89);\n"
                                     "background-color: rgb(50,75,115);};"],
                        [self.lblMainBoxCams, "background-color: rgb(62,62,62);\n"
                                              "border-radius: 10px;"],
                        [self.btnSearch, "QPushButton:!hover {background-color: rgb(89,89,89);\n"
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
                        [self.leSearchTbDBlTS, "background-color: rgb(42, 42, 42);\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "border-radius: 3px;"],
                        [self.comboSearch, "background-color: rgb(89,89,89);\n"
                                           "color: white;\n"
                                           "border-radius: 3px;\n"
                                           "border: 1px solid rgb(63,63,63)"],
                        [self.btnSrchRefresh, "QPushButton:!hover {background-color: rgb(89,89,89);\n"
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
                                                 "}"],
                        [self.btnAddTS, "QPushButton:!hover {background-color: rgb(89,89,89);\n"
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
                        [self.btnCreate3D, "QPushButton:!hover {background-color: rgb(89,89,89);\n"
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
                        [self.btnAddUser, "QPushButton:!hover {background-color: rgb(89,89,89);\n"
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
                        [self.label_filtertype, "background-color: rgb(62,62,62);\n"
                                                "color: rgb(255,255,255);\n"
                                                "font: 12pt \"MS Shell Dlg 2\";"],
                        [self.btnDelTS, "QPushButton:!hover {background-color: rgb(89,89,89);\n"
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
                        [self.frmHeadExit, "background-color: rgb(205,205,205);"],
                        [self.lblBarClose, "background-color: rgb(255,255,255);\n"
                                           "color: rgb(0,0,0);\n"
                                           ""],
                        [self.lblIconBarClose, "background-color: rgb(255,255,255);\n"
                                               "image: url(" + globalValues.pathStyleImgs + "sinaps1717.png);"],
                        [self.btnCloseDBTSform, "QPushButton:!hover{ background-color: rgb(255,255,255);\n"
                                                "border-radius: 5px;\n"
                                                "image: url(" + globalValues.pathStyleImgs + "iconextbl1919.png);}\n"
                                                "QPushButton:hover { background-color: rgb(84,122,181);\n"
                                                "border-radius: 3px;\n"
                                                "image: url(" + globalValues.pathStyleImgs + "iconext1919.png);}\n"
                                                "QPushButton:hover:pressed { background-color: rgb(50,75,115);\n"
                                                "border-radius: 3px;\n"
                                                "image: url(" + globalValues.pathStyleImgs + "iconext1919.png);};\n"
                                                ""],
                        [self.label, "background-color: rgb(255,255,255);"]]

        self.lengthLight = len(self.lstLight)
        self.lengthDark = len(self.lstDark)

        self.changeCOLORMainPanelGrunt()

        self.btnCloseDBTSform.clicked.connect(self.closeWindow)
        self.btnAddTS.clicked.connect(self.openPanelAddTS)
        self.verticalScrollBar.valueChanged.connect(self.sync_func)

        self.updateTable()
        self.btnSrchRefresh.clicked.connect(self.refreshTbl)
        self.btnDelTS.clicked.connect(self.delDataTS)
        self.btnAddUser.clicked.connect(self.openPanAddUser)

        self.tblTS.verticalHeader().hide()
        self.tblTS.horizontalScrollBar().hide()
        self.tblTS.verticalScrollBar().hide()

        myQHeaderView = self.tblTS.horizontalHeader()
        for i in range(13):
            myQHeaderView.setSectionResizeMode(i, QtWidgets.QHeaderView.Fixed)
        myQHeaderView.setStretchLastSection(False)
        self.tblTS.setHorizontalHeader(myQHeaderView)
        self.tblTS.setColumnWidth(13, 0)
        self.btnSearch.clicked.connect(self.searchEls)
        self.btnCreate3D.clicked.connect(self.openPanCreate3D)

        self.tblTS.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

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

    def closeWindow(self):
        try:
            self.close()
        except Exception as ex:
            globalValues.writeLogData('Функция закрытия панели', str(ex))

    def openPanelAddTS(self):
        try:
            uiAddTS = Ui_add_TS()
            uiAddTS.exec_()
            time.sleep(0.35)
            globalValues.checkUpdateTblTS = True
            print('checking!!!!')
            globalValues.checkEditTbl = False
            globalValues.checkPoolTS = True
            globalValues.refreshTblMain = True
            self.updateTable()

        except Exception as ex:
            globalValues.writeLogData('Панель добавления нового ТС', str(ex))

    def sync_func(self):
        self.tblTS.verticalScrollBar().setValue(self.verticalScrollBar.value())

    def thChangeScroll(self, check):
        try:

            num_delta = 200
            if (self.firstCallChangeScroll):
                self.firstCallChangeScroll = False
                num_delta = 350

            # print('Delta: ' + str(num_delta))

            start_time = round(time.time() * 100)
            while True:
                numRows = self.tblTS.verticalScrollBar().maximum()
                delta = round(abs(time.time() * 100) - start_time)

                # print(num_delta)

                if numRows != 0:
                    print('changeBarScroll!!!' + str(numRows))
                    time.sleep(0.2)
                    self.verticalScrollBar.setMaximum(self.tblTS.verticalScrollBar().maximum())
                    break
                # print('checkingScroll!!!: ' + str(numRows))

                if delta > num_delta:
                    if (check):
                        # print('changeScrollTimer')
                        self.verticalScrollBar.setMaximum(self.tblTS.verticalScrollBar().maximum())
                    break

                time.sleep(0.1)

                if (globalValues.stopAll):
                    break
        except Exception as ex:
            globalValues.writeLogData('Поток обработки изменения скролла, панель ТС', str(ex))

    def refreshTbl(self):
        try:
            globalValues.checkUpdateTblTS = True
            self.updateTable()
            globalValues.writeEventToDBJournalMain('Журнал', 'Выполнено обновление таблицы ТС')
        except Exception as ex:
            globalValues.writeLogData('Функция обновления таблицы ТС', str(ex))

    def searchEls(self):
        try:
            dataCb = self.comboSearch.currentIndex()

            if (dataCb == 0):
                globalValues.checkUpdateTblTS = True
                self.updateTable()

            elif (dataCb == 1):

                self.updateTable()

                dataSearch = self.leSearchTbDBlTS.text()

                try:
                            countItems = self.tblTS.rowCount()
                            if (countItems == ''):
                                countItems = 0

                            countItems = int(countItems)

                            for i in range(countItems - 1, -1,  -1):
                                dataItem = str(self.tblTS.item(i, 0).text())
                                if (dataItem == ''):
                                    dataItem = ' '
                                is_data_in_db = dataSearch in dataItem
                                if (is_data_in_db == False):
                                    self.tblTS.removeRow(i)


                except Exception as ex:
                    globalValues.writeLogData('Поиск по организации в таблице панели ТС', str(ex))

            elif (dataCb == 2):

                self.updateTable()

                dataSearch = self.leSearchTbDBlTS.text()

                try:

                    countItems = self.tblTS.rowCount()

                    if (countItems == ''):
                        countItems = 0

                    countItems = int(countItems)

                    for i in range(countItems - 1, -1, -1):

                        dataItem = str(self.tblTS.item(i, 1).text())

                        if (dataItem == ''):
                            dataItem = ' '

                        is_data_in_db = dataSearch in dataItem

                        if (is_data_in_db == False):
                            self.tblTS.removeRow(i)



                except Exception as ex:

                    globalValues.writeLogData('Поиск по наименовании ТС в таблице панели ТС', str(ex))

            elif (dataCb == 3):

                self.updateTable()

                dataSearch = self.leSearchTbDBlTS.text()

                try:
                            countItems = self.tblTS.rowCount()
                            if (countItems == ''):
                                countItems = 0

                            countItems = int(countItems)

                            for i in range(countItems - 1, -1,  -1):
                                dataItem = str(self.tblTS.item(i, 2).text())
                                if (dataItem == ''):
                                    dataItem = ' '
                                is_data_in_db = dataSearch in dataItem
                                if (is_data_in_db == False):
                                    self.tblTS.removeRow(i)


                except Exception as ex:
                    globalValues.writeLogData('Поиск по модели ТС в таблице панели ТС', str(ex))

            elif (dataCb == 4):

                self.updateTable()

                dataSearch = self.leSearchTbDBlTS.text()

                try:
                            countItems = self.tblTS.rowCount()
                            if (countItems == ''):
                                countItems = 0

                            countItems = int(countItems)

                            for i in range(countItems - 1, -1,  -1):
                                dataItem = str(self.tblTS.item(i, 3).text())
                                if (dataItem == ''):
                                    dataItem = ' '
                                is_data_in_db = dataSearch in dataItem
                                if (is_data_in_db == False):
                                    self.tblTS.removeRow(i)


                except Exception as ex:
                    globalValues.writeLogData('Поиск по номеру ГРЗ ТС в таблице панели ТС', str(ex))

            else:
                globalValues.checkUpdateTblTS = True
                self.updateTable()

        except Exception as ex:
            globalValues.writeLogData('Функция поиска панели ТС', str(ex))

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

                        print('updateTblIsWorking!!!')
                        # print(globalValues.stopUpdateTblJournal)
                        # with con:
                        if True:
                            cur.execute("SELECT * FROM " + globalValues.tblsDB[6])

                            rows = cur.fetchall()

                            countRows = 0

                            for row in rows:
                                countRows += 1

                            print(countRows)

                            if ((countRows != 0 and countRows != countRowsOld) or (globalValues.checkUpdateTblTS)):
                                self.tblTS.setRowCount(0)
                                globalValues.checkUpdateTblTS = False
                                valWdg = 0

                                for row in reversed(rows):
                                    print(str(row[1]))
                                    # print(i)
                                    self.tblTS.insertRow(valWdg)
                                    item = QtWidgets.QTableWidgetItem(str(row[1]))
                                    item.setTextAlignment(Qt.AlignCenter)
                                    if(globalValues.colorForm == 1):
                                        item.setForeground(QtGui.QBrush(Qt.black))
                                    else:
                                        item.setForeground(QtGui.QBrush(Qt.white))
                                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                    self.tblTS.setItem(valWdg, 0, item)

                                    item = QtWidgets.QTableWidgetItem(str(row[2]))
                                    item.setTextAlignment(Qt.AlignCenter)
                                    if (globalValues.colorForm == 1):
                                        item.setForeground(QtGui.QBrush(Qt.black))
                                    else:
                                        item.setForeground(QtGui.QBrush(Qt.white))
                                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                    self.tblTS.setItem(valWdg, 1, item)

                                    item = QtWidgets.QTableWidgetItem(str(row[3]))
                                    item.setTextAlignment(Qt.AlignCenter)
                                    if (globalValues.colorForm == 1):
                                        item.setForeground(QtGui.QBrush(Qt.black))
                                    else:
                                        item.setForeground(QtGui.QBrush(Qt.white))
                                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                    self.tblTS.setItem(valWdg, 2, item)

                                    item = QtWidgets.QTableWidgetItem(str(row[4]))
                                    item.setTextAlignment(Qt.AlignCenter)
                                    if (globalValues.colorForm == 1):
                                        item.setForeground(QtGui.QBrush(Qt.black))
                                    else:
                                        item.setForeground(QtGui.QBrush(Qt.white))
                                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                    self.tblTS.setItem(valWdg, 3, item)

                                    item = QtWidgets.QTableWidgetItem(str(row[5]))
                                    item.setTextAlignment(Qt.AlignCenter)
                                    if (globalValues.colorForm == 1):
                                        item.setForeground(QtGui.QBrush(Qt.black))
                                    else:
                                        item.setForeground(QtGui.QBrush(Qt.white))
                                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                    self.tblTS.setItem(valWdg, 4, item)

                                    item = QtWidgets.QTableWidgetItem(str(row[6]))
                                    item.setTextAlignment(Qt.AlignCenter)
                                    if (globalValues.colorForm == 1):
                                        item.setForeground(QtGui.QBrush(Qt.black))
                                    else:
                                        item.setForeground(QtGui.QBrush(Qt.white))
                                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                    self.tblTS.setItem(valWdg, 5, item)

                                    item = QtWidgets.QTableWidgetItem(str(row[7]) + '(' + str(row[8]) + ')')
                                    item.setTextAlignment(Qt.AlignCenter)
                                    if (globalValues.colorForm == 1):
                                        item.setForeground(QtGui.QBrush(Qt.black))
                                    else:
                                        item.setForeground(QtGui.QBrush(Qt.white))
                                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                    self.tblTS.setItem(valWdg, 6, item)

                                    item = QtWidgets.QTableWidgetItem(str(row[9]))
                                    item.setTextAlignment(Qt.AlignCenter)
                                    if (globalValues.colorForm == 1):
                                        item.setForeground(QtGui.QBrush(Qt.black))
                                    else:
                                        item.setForeground(QtGui.QBrush(Qt.white))
                                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                    self.tblTS.setItem(valWdg, 7, item)

                                    item = QtWidgets.QTableWidgetItem(str(row[10]))
                                    item.setTextAlignment(Qt.AlignCenter)
                                    if (globalValues.colorForm == 1):
                                        item.setForeground(QtGui.QBrush(Qt.black))
                                    else:
                                        item.setForeground(QtGui.QBrush(Qt.white))
                                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                    self.tblTS.setItem(valWdg, 8, item)

                                    item = QtWidgets.QTableWidgetItem(str(row[11]))
                                    item.setTextAlignment(Qt.AlignCenter)
                                    if (globalValues.colorForm == 1):
                                        item.setForeground(QtGui.QBrush(Qt.black))
                                    else:
                                        item.setForeground(QtGui.QBrush(Qt.white))
                                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                    self.tblTS.setItem(valWdg, 9, item)

                                    item = QtWidgets.QTableWidgetItem(str(row[12]))
                                    item.setTextAlignment(Qt.AlignCenter)
                                    if (globalValues.colorForm == 1):
                                        item.setForeground(QtGui.QBrush(Qt.black))
                                    else:
                                        item.setForeground(QtGui.QBrush(Qt.white))
                                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                    self.tblTS.setItem(valWdg, 10, item)

                                    item = QtWidgets.QTableWidgetItem(str(row[13]))
                                    item.setTextAlignment(Qt.AlignCenter)
                                    if (globalValues.colorForm == 1):
                                        item.setForeground(QtGui.QBrush(Qt.black))
                                    else:
                                        item.setForeground(QtGui.QBrush(Qt.white))
                                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                    self.tblTS.setItem(valWdg, 11, item)

                                    item = QtWidgets.QTableWidgetItem(str(row[14]))
                                    item.setTextAlignment(Qt.AlignCenter)
                                    if (globalValues.colorForm == 1):
                                        item.setForeground(QtGui.QBrush(Qt.black))
                                    else:
                                        item.setForeground(QtGui.QBrush(Qt.white))
                                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                    self.tblTS.setItem(valWdg, 12, item)

                                    item = QtWidgets.QTableWidgetItem(str(row[0]))
                                    self.tblTS.setItem(valWdg, 13, item)

                                    valWdg += 1

                                print(valWdg)
                                countRowsOld = countRows

                                strDataToTS = 'Выполнено обновление таблицы'
                                globalValues.writeEventToDBJournalMain('База ТС', strDataToTS)

                        th_scroll = threading.Thread(target=self.thChangeScroll, args=(True,))
                        th_scroll.start()

            except Exception as ex:
                globalValues.writeLogData('Поток обновления панели ТС', str(ex))

            cur.close()
            con.close()
        except Exception as ex:
            globalValues.writeLogData('Поток обновления панели ТС', str(ex))
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

    def delDataTS(self):
        try:
            my_thread_del_row_tbl_main = threading.Thread(target=self.startDelElsTbl)
            my_thread_del_row_tbl_main.start()

        except Exception as ex:
            globalValues.writeLogData('Функция удаления записи ТС из БД MySql', str(ex))

    def startDelElsTbl(self):

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

                    indexRow = self.tblTS.currentRow()

                    dataGRZ = self.tblTS.item(indexRow, 3).text()

                    # with con:
                    if True:
                            numberId = int(self.tblTS.item(indexRow, 13).text())
                            query = ("DELETE FROM " + globalValues.tblsDB[6] + " where id = (%s)")
                            cur.execute(query, numberId)
                            con.commit()

                    strDataInJournal = 'Выполнено удаление записи ТС: ' + dataGRZ
                    globalValues.writeEventToDBJournalMain('База ТС', strDataInJournal)

                    cur.close()
                    con.close()

                    self.refreshTbl()

            except Exception as ex:
                    globalValues.writeLogData('Функция удаления записи ТС из БД MySql', str(ex))

    def openPanCreate3D(self):
        try:
            self.uiPan3D = Ui_PanelCreateModel()
            self.uiPan3D.show()
        except Exception as ex:
            globalValues.writeLogData('Функция открытия панели с базой для создания моделей', str(ex))

    def openPanAddUser(self):
        try:
            uiAddUser = Ui_addUser()
            uiAddUser.exec_()
        except Exception as ex:
            globalValues.writeLogData('Функция добавления нового пользователя в систему ', str(ex))

if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    uiJournal = Ui_TS_Base()

    uiJournal.show()
    sys.exit(app.exec_())
