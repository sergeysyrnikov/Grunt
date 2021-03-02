from PyQt5.QtWidgets import QApplication, QLabel, QFrame, QDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QCoreApplication, QMetaObject, QRect
import time
import sys
import globalValues

globalValues.colorForm = 1

app = QApplication(sys.argv)

class Ui_about_system_menu(QDialog):

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
        self.resize(1000, 309)
        self.setStyleSheet("")
        self.label = QLabel(self)
        self.label.setGeometry(QRect(370, -5, 295, 47))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lblIconJournal = QLabel(self)
        self.lblIconJournal.setGeometry(QRect(340, 8, 23, 23))
        self.lblIconJournal.setText("")
        self.lblIconJournal.setObjectName("lblIconJournal")
        self.line = QFrame(self)
        self.line.setGeometry(QRect(342, 31, 318, 8))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_134 = QLabel(self)
        self.label_134.setGeometry(QRect(13, 53, 991, 251))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_134.setFont(font)
        self.label_134.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_134.setObjectName("label_134")
        self.lblBack = QLabel(self)
        self.lblBack.setGeometry(QRect(0, 0, 1000, 311))
        self.lblBack.setText("")
        self.lblBack.setObjectName("lblBack")
        self.lblBack.raise_()
        self.label_134.raise_()
        self.label.raise_()
        self.lblIconJournal.raise_()
        self.line.raise_()

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)
        # self.runThJournal()
        self.firstCall()

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Панель справки"))
        self.label.setText(_translate("Dialog", "Справка \"Панель управления\""))
        self.label_134.setText(_translate("Dialog", "    Меню панели управления имеет 4 кнопки управления: \"Журнал событий\", \"Журнал ЗН Т/С\", \"Добавить З/Н\", \"База ТС\". \n"
                                          "  1. Журнал событий. \n"
                                          "      Журнал событий хранит всю информацию о произошедших событиях в системе в табличном виде. \n"
                                          "  2. Журнал З/Н ТС. \n"
                                          "      При нажатии на данную кнопку открывается журнал З/Н ТС. В данном журнале в табличном виде представлены все произведенные рейсы транспортными\n"
                                          "      дублируется в журнале З/Н ТС в более подбробном виде. Заказ-наряды содержат всю подробную информацию о совершенном рейсе ТС, а также\n"
                                          "      видеофрагменты распознавания данного ТС на объекте строительства. \n"
                                          "  3. Добавить З/Н. \n"
                                          "      Данная кнопка позволяет оператору вручную добавить заказ-наряд в систему, в случае, если при въезде на объект строительства номер ГРЗ ТС был\n"
                                          "      распознан ошибочно. В штатном режиме все ЗН добавляются автоматически. \n"
                                          "  4. База ТС. \n"
                                          "      При нажатии на данную кнопку откроется меню базы данных ТС системы. В данном меню в табличном виде отображен автопарк ТС распознаваемых\n"
                                          "      системой. Только те ТС, которые внесены в данную базу будут распознаваться системой и автоматически регистрировать заказ-наряды. Данная база ТС\n"
                                          "      должна содержать полный список ТС, совершающих работы по вывозу грунта с объекта строительства."))

    def firstCall(self):

        self.lstLight = [[self.label,"background-color: rgb(242,242,242);\n"
        "color: black;\n"
        "border-radius: 5px;"],
                [self.lblIconJournal,"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));\n"
        "image: url(" + globalValues.pathStyleImgs + "iconworkpanel1.png);"],
                [self.label_134,"background-color: rgb(242,242,242);\n"
        "color: black;\n"
        "font: 10pt \"Arial\";"],
                [self.lblBack,"background-color: rgb(242,242,242);\n"
        "gridline-color: rgb(20, 18, 57);"]]
        self.lstDark = [[self.label,"background-color: rgb(66,66,66);\n"
        "color: rgb(255,255,255);\n"
        "border-radius: 5px;"],
                [self.lblIconJournal,"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));\n"
        "image: url(" + globalValues.pathStyleImgs + "iconworkpanel1.png);"],
                [self.label_134,"background-color: rgb(66,66,66);\n"
        "color: white;\n"
        "font: 10pt \"Arial\";"],
                [self.lblBack,"background-color: rgb(66,66,66);\n"
        "gridline-color: rgb(20, 18, 57);"]]


        self.lengthLight = len(self.lstLight)
        self.lengthDark = len(self.lstDark)

        self.changeCOLORMainPanelGrunt(0.1)

        globalValues.writeEventToDBJournalMain('Панель управления', 'Выполнено открытие справки панели управления')

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
    # app = QApplication(sys.argv)
    uiJournal = Ui_about_system_menu()

    uiJournal.show()
    # uiJournal.thChangeCOLORJournal()
    # app.exec_()
    sys.exit(app.exec_())
