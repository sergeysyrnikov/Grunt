from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import threading
import time
import sys
import globalValues
import pymysql
import datetime
from panelMesBox import Ui_mes_box

app = QtWidgets.QApplication(sys.argv)

class Ui_AddZakaz(QDialog):

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
        self.setFixedSize(390, 200)
        self.btnAddNewZakaz = QtWidgets.QPushButton(self)
        self.btnAddNewZakaz.setGeometry(QtCore.QRect(240, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnAddNewZakaz.setFont(font)
        self.btnAddNewZakaz.setObjectName("btnAddNewZakaz")
        self.lblFront4 = QtWidgets.QLabel(self)
        self.lblFront4.setGeometry(QtCore.QRect(0, 0, 391, 199))
        self.lblFront4.setText("")
        self.lblFront4.setObjectName("lblFront4")
        self.leNewZakaz = QtWidgets.QLineEdit(self)
        self.leNewZakaz.setGeometry(QtCore.QRect(180, 60, 141, 30))
        self.leNewZakaz.setText("")
        self.leNewZakaz.setObjectName("leNewCamZakaz")
        self.label_NameCam = QtWidgets.QLabel(self)
        self.label_NameCam.setEnabled(False)
        self.label_NameCam.setGeometry(QtCore.QRect(60, 67, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_NameCam.setFont(font)
        self.label_NameCam.setObjectName("label_NameCam")
        self.line1 = QtWidgets.QFrame(self)
        self.line1.setGeometry(QtCore.QRect(105, 29, 177, 20))
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        self.labelNewCam = QtWidgets.QLabel(self)
        self.labelNewCam.setGeometry(QtCore.QRect(105, 10, 181, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelNewCam.setFont(font)
        self.labelNewCam.setObjectName("labelNewCam")
        self.label_NameCam_2 = QtWidgets.QLabel(self)
        self.label_NameCam_2.setEnabled(False)
        self.label_NameCam_2.setGeometry(QtCore.QRect(47, 125, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_NameCam_2.setFont(font)
        self.label_NameCam_2.setObjectName("label_NameCam_2")
        self.label_NameCam_3 = QtWidgets.QLabel(self)
        self.label_NameCam_3.setEnabled(False)
        self.label_NameCam_3.setGeometry(QtCore.QRect(47, 110, 331, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_NameCam_3.setFont(font)
        self.label_NameCam_3.setObjectName("label_NameCam_3")
        self.label_67 = QtWidgets.QLabel(self)
        self.label_67.setGeometry(QtCore.QRect(14, 110, 31, 31))
        self.label_67.setText("")
        self.label_67.setObjectName("label_67")
        self.lblFront4.raise_()
        self.btnAddNewZakaz.raise_()
        self.leNewZakaz.raise_()
        self.label_NameCam.raise_()
        self.line1.raise_()
        self.labelNewCam.raise_()
        self.label_NameCam_2.raise_()
        self.label_NameCam_3.raise_()
        self.label_67.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        # self.runThJournal()
        self.firstCall()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Панель добавления З/Н"))
        self.btnAddNewZakaz.setText(_translate("Dialog", "Добавить З/Н"))
        self.leNewZakaz.setToolTip(_translate("Dialog", "Пример: A123BB777"))
        self.label_NameCam.setText(_translate("Dialog", "Номер ГРЗ ТС:"))
        self.labelNewCam.setText(_translate("Dialog", "Добавление нового З/Н"))
        self.label_NameCam_2.setText(_translate("Dialog", "Пример ввода ГРЗ ТС: А123ВВ 777, Е456ХХ 99"))
        self.label_NameCam_3.setText(_translate("Dialog", "Номер следедует вводить только латинскими буквами!"))

    def firstCall(self):

        self.lstLight = [[self,"background-color: rgb(66,66,66);"],
        [self.btnAddNewZakaz,"QPushButton:!hover {background-color: rgb(227,227,227);\n"
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
        [self.lblFront4,"background-color: rgb(242,242,242);"],
        [self.leNewZakaz,"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius:3px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border: 1px solid rgb(150,150,150);"],
        [self.label_NameCam,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;"],
        [self.line1,"background-color: rgb(242,242,242);"],
        [self.labelNewCam,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;"],
        [self.label_67,"background-color: rgb(242,242,242);\n"
"color: white;\n"
"image: url(" + globalValues.pathStyleImgs + "iconinfo2.png);"],
        [self.label_NameCam_2,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;"],
        [self.label_NameCam_3,"background-color: rgb(242,242,242);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;"]]

        self.lstDark = [[self,"background-color: rgb(66,66,66);"],
        [self.btnAddNewZakaz,"QPushButton:!hover {background-color: rgb(89,89,89);\n"
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
        [self.lblFront4,"background-color: rgb(75,75,75);\n"
"border-radius: 10px;"],
        [self.leNewZakaz,"background-color: white;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"                         
"border-radius:3px;"],
        [self.label_NameCam,"background-color: rgb(75,75,75);\n"
"color: white;"],
        [self.line1,"background-color: rgb(75,75,75);"],
        [self.labelNewCam,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.label_NameCam_2,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.label_NameCam_3,"background-color: rgb(75,75,75);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;"],
        [self.label_67,"background-color: rgb(75,75,75);\n"
"color: white;\n"
"image: url(" + globalValues.pathStyleImgs + "iconinfo2.png);"]]

        self.lengthLight = len(self.lstLight)
        self.lengthDark = len(self.lstDark)
        self.changeCOLORMainPanelGrunt()

        self.btnAddNewZakaz.clicked.connect(self.addZakaz)

    def changeColor(self, object, str):
            object.setStyleSheet(str)

    def changeCOLORMainPanelGrunt(self):

            delta = int((0.15/self.lengthDark)*1000)


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

    def addZakaz(self):
        try:

            dataSearch = self.leNewZakaz.text()

            if (len(dataSearch) < 6):
                uiMes = Ui_mes_box()
                uiMes.lblStrInfo.setText('Введён некорректный ГРЗ!')
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
            print('sqwdwdw')

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


            except Exception as ex:
                globalValues.writeLogData('Подключение к БД панель создания З/Н', str(ex))
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

            cur = con.cursor()

            try:
                # with con:
                if True:
                    cur.execute("SELECT * FROM " + globalValues.tblsDB[6])
                    rows = cur.fetchall()
                    countRows = 0

                    str_grz = ''
                    car_name = ''
                    date_work = ''
                    name_company = ''
                    car_model = ''


                    dataSearch = dataSearch.lower()
                    is_search = False

                    for row in rows:
                        is_search = dataSearch in str(row[4]).lower()
                        if is_search:
                            str_grz = str(row[4]).upper()
                            car_name = str(row[2])
                            name_company = str(row[1])
                            car_model = str(row[3])
                            break

                    print(is_search)

                    try:
                        if is_search:
                            # with con:
                            if True:
                                    cur.execute("SELECT number_order FROM " + globalValues.tblsDB[1])
                                    rows = cur.fetchall()

                                    number_order = 100001
                                    print(len(rows))
                                    if (len(rows) != 0):
                                        for row in reversed(rows):
                                            try:
                                                number_order = str(int(row[0]) + 1)
                                            except Exception as ex:
                                                globalValues.writeLogData('Присвоение нового номера талона', str(ex))
                                            break
                                    print(number_order)
                                    print(str_grz)
                                    print(car_name)
                                    print(name_company)
                                    print(car_model)
                                    dateToday = datetime.date.today().strftime('%d.%m.%Y')
                                    date_work = str(dateToday)
                                    print(date_work)
                                    str_time = self.strCurTime()

                                    query = ("INSERT INTO " + globalValues.tblsDB[1] + " (number_order, number_grz, date, time_entry, state_order) VALUES ( %s, %s, %s, %s, \'выполняется\')")
                                    cur.execute(query, (number_order, str_grz, date_work, str_time))
                                    con.commit()

                                    query = ("INSERT INTO " + globalValues.tblsDB[2] + " (car_name, number_order, date_work, name_company, car_model, car_grz) VALUES (%s, %s, %s, %s, %s, %s)")
                                    cur.execute(query, (car_name, number_order, date_work, name_company, car_model, str_grz))
                                    con.commit()

                                    sqlMy = "INSERT INTO " + globalValues.tblsDB[4] + " (url) VALUES (%s)"
                                    cur.execute(sqlMy, ('https://hosting.wialon.com/'))
                                    con.commit()

                                    query = ("INSERT INTO " + globalValues.tblsDB[5] + " (weight) VALUES ( \'не измерена\')")
                                    cur.execute(query)
                                    con.commit()

                                    strDataToTS = 'Выполнено создание нового ЗН(' + str(number_order) + ', ' + str(str_grz) + ')'
                                    globalValues.writeEventToDBJournalMain('Панель управления', strDataToTS)

                        else:
                            uiMes = Ui_mes_box()
                            uiMes.lblStrInfo.setText('Введён некорректный ГРЗ!')
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
                    except Exception as ex:
                        globalValues.writeLogData('Создание нового З/Н в ручном режиме', str(ex))
            except Exception as ex:
                globalValues.writeLogData('Проверка ГРЗ в бд панель добавления З/Н', str(ex))

            cur.close()
            con.close()

            if (is_search):
                self.close()

        except Exception as ex:
            globalValues.writeLogData('Функция добавления З/Н панель добавления З/Н', str(ex))

    def strCurTime(self):
        str_cur_time = str(datetime.datetime.time(datetime.datetime.now()))
        len_cur_time = len(str_cur_time)
        str_cur_time = str_cur_time[0: (len_cur_time - 7)]
        str_cur_time = str_cur_time.replace(':', '.')
        return str_cur_time

if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    uiAddZakaz = Ui_AddZakaz()
    uiAddZakaz.show()
    sys.exit(app.exec_())
