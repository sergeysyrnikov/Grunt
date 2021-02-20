from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import time
import sys
import globalValues

app = QtWidgets.QApplication(sys.argv)


class Ui_systemMenu(QDialog):

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
        self.setFixedSize(1003, 390)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(331, -5, 341, 47))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lblIconJournal = QtWidgets.QLabel(self)
        self.lblIconJournal.setGeometry(QtCore.QRect(301, 8, 23, 23))
        self.lblIconJournal.setText("")
        self.lblIconJournal.setObjectName("lblIconJournal")
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(303, 35, 370, 2))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_50 = QtWidgets.QLabel(self)
        self.label_50.setGeometry(QtCore.QRect(35, 60, 961, 321))
        self.label_50.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_50.setObjectName("label_50")
        self.lblBack = QtWidgets.QLabel(self)
        self.lblBack.setGeometry(QtCore.QRect(0, 0, 1003, 391))
        self.lblBack.setObjectName("lblBack")
        self.label_51 = QtWidgets.QLabel(self)
        self.label_51.setGeometry(QtCore.QRect(10, 95, 30, 30))
        self.label_51.setText("")
        self.label_51.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self)
        self.label_52.setGeometry(QtCore.QRect(10, 159, 30, 30))
        self.label_52.setText("")
        self.label_52.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self)
        self.label_53.setGeometry(QtCore.QRect(10, 220, 30, 30))
        self.label_53.setText("")
        self.label_53.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self)
        self.label_54.setGeometry(QtCore.QRect(10, 300, 30, 30))
        self.label_54.setText("")
        self.label_54.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_54.setObjectName("label_54")
        self.lblBack.raise_()
        self.label_50.raise_()
        self.label.raise_()
        self.lblIconJournal.raise_()
        self.line.raise_()
        self.label_51.raise_()
        self.label_52.raise_()
        self.label_53.raise_()
        self.label_54.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        # self.runThJournal()
        self.firstCall()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Панель справки системного меню"))
        self.label.setText(_translate("Dialog", "Справка \"Панель настройки камер\""))
        self.label_50.setText(_translate("Dialog", "      Панель настройки камер содержит 4 элемента управления:\n\n\n"
                                                   "  1. Архив.\n"
                                                   "      При нажатии на данную кнопку откроется меню настройки видеоархива системы.\n\n\n"
                                                   "  2. Добавление видеокамеры.\n"
                                                   "      При нажатии данной кнопки откроется меню добавления новой камеры в систему.\n\n\n"
                                                   "  3. Удаление камеры.\n"
                                                   "      При нажатии на данную кнопку откроется меню удаления видеокамеры из системы. Для того, чтобы удалить видеокамеру из системы необходимо\n"
                                                   "      выбрать нужную видеокамеру из списка, расположенного с левой стороны панели, а затем нажать кнопку \"удалить\".\n\n\n"
                                                   "  4. Редактирование камеры.\n"
                                                   "      При нажатии на данную кнопку откроется меню редактирования настроек видеокамеры. Для того, чтобы воспользоваться данным элементом управления\n"
                                                   "      необходимо выбрать нужную видеокамер из списка, затем нажать кнопку \"редактировать\"."))
        self.lblBack.setText(_translate("Dialog", "`"))

    def firstCall(self):

        self.lstLight = [[self.label,"background-color: rgb(242,242,242);"],
        [self.lblIconJournal,"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));\n"
"image: url(" + globalValues.pathStyleImgs + "iconworkpanel1.png);"],
        [self.label_50,"background-color: rgb(242,242,242);\n"
"font: 10pt \"Arial\";"],
        [self.lblBack,"background-color: rgb(242,242,242);"],
        [self.label_51,"background-color: rgb(242,242,242); \n"
"color: rgb(255,255,255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(63,63,63);\n"
"image: url(" + globalValues.pathStyleImgs + "iconarchset2.png);"],
        [self.label_52,"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(9, 131, 25, 255), stop:1 rgba(9, 185, 32, 255));\n"
"color: rgb(255,255,255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(63,63,63);\n"
"image: url(" + globalValues.pathStyleImgs + "iconpluscam3.png);"],
        [self.label_53,"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(223, 0, 0, 255), stop:1 rgba(255, 100, 100, 255));\n"
"color: rgb(255,255,255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(63,63,63);\n"
"image: url(" + globalValues.pathStyleImgs + "iconminuscam.png);"],
        [self.label_54,"background-color:  qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(89, 89, 89, 255), stop:1 rgba(143, 141, 141, 255));\n"
"color: rgb(255,255,255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(63,63,63);\n"
"image: url(" + globalValues.pathStyleImgs + "iconprintset10.png);"]]
        self.lstDark = [[self.label,"background-color: rgb(66,66,66);\n"
"color: white;"],
        [self.lblIconJournal,"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));\n"
"image: url(" + globalValues.pathStyleImgs + "iconworkpanel1.png);"],
        [self.label_50,"background-color: rgb(66,66,66);\n"
"color:white;\n"
"font: 10pt \"Arial\";"],
        [self.lblBack,"background-color: rgb(66,66,66);"],
        [self.label_51,"background-color: rgb(242,242,242); \n"
"color: rgb(255,255,255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(63,63,63);\n"
"image: url(" + globalValues.pathStyleImgs + "iconarchset2.png);"],
        [self.label_52,"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(9, 131, 25, 255), stop:1 rgba(9, 185, 32, 255));\n"
"color: rgb(255,255,255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(63,63,63);\n"
"image: url(" + globalValues.pathStyleImgs + "iconpluscam3.png);"],
        [self.label_53,"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(223, 0, 0, 255), stop:1 rgba(255, 100, 100, 255));\n"
"color: rgb(255,255,255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(63,63,63);\n"
"image: url(" + globalValues.pathStyleImgs + "iconminuscam.png);"],
        [self.label_54,"background-color:  qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(89, 89, 89, 255), stop:1 rgba(143, 141, 141, 255));\n"
"color: rgb(255,255,255);\n"
"border-radius:3px;\n"
"border:1px solid rgb(63,63,63);\n"
"image: url(" + globalValues.pathStyleImgs + "iconprintset10.png);"]]

        self.lengthLight = len(self.lstLight)
        self.lengthDark = len(self.lstDark)

        self.changeCOLORMainPanelGrunt(0.1)

        globalValues.writeEventToDBJournalMain('Камеры', 'Выполнено открытие справки \"панель настройки камер\"')

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


if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    uiJournal = Ui_systemMenu()

    uiJournal.show()
    # uiJournal.thChangeCOLORJournal()
    # app.exec_()
    sys.exit(app.exec_())
