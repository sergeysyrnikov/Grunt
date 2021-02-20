from PyQt5 import QtCore, QtGui, QtWidgets
import globalValues
import time

class Ui_AboutSysMenu(QtWidgets.QDialog):

    lstLight = [[]]
    lstDark = [[]]
    lengthLight = 0
    lengthDark = 0

    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
            self.setObjectName("Dialog")
            self.setFixedSize(1003, 665)
            self.setStyleSheet("")
            self.label = QtWidgets.QLabel(self)
            self.label.setGeometry(QtCore.QRect(370, -5, 295, 47))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(14)
            font.setBold(True)
            font.setWeight(75)
            self.label.setFont(font)
            self.label.setObjectName("label")
            self.lblIconJournal = QtWidgets.QLabel(self)
            self.lblIconJournal.setGeometry(QtCore.QRect(340, 8, 23, 23))
            self.lblIconJournal.setText("")
            self.lblIconJournal.setObjectName("lblIconJournal")
            self.line = QtWidgets.QFrame(self)
            self.line.setGeometry(QtCore.QRect(342, 31, 315, 8))
            self.line.setFrameShape(QtWidgets.QFrame.HLine)
            self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line.setObjectName("line")
            self.label_50 = QtWidgets.QLabel(self)
            self.label_50.setGeometry(QtCore.QRect(20, 60, 966, 611))
            self.label_50.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            self.label_50.setObjectName("label_50")
            self.lblBack = QtWidgets.QLabel(self)
            self.lblBack.setGeometry(QtCore.QRect(0, 0, 1003, 671))
            self.lblBack.setText("")
            self.lblBack.setObjectName("lblBack")
            self.lblBack.raise_()
            self.label_50.raise_()
            self.label.raise_()
            self.lblIconJournal.raise_()
            self.line.raise_()

            self.retranslateUi()
            QtCore.QMetaObject.connectSlotsByName(self)
            # self.runThJournal()
            self.firstCall()

    def retranslateUi(self):
            _translate = QtCore.QCoreApplication.translate
            self.setWindowTitle(_translate("Dialog", "Панель справки"))
            self.label.setText(_translate("Dialog", "Справка \"Настройки системы\""))
            self.label_50.setText(_translate("Dialog",
                                             "    Меню панели управления имеет 8 кнопок. Ниже представлено краткое описание функций, которые выполняют данные элементы управления.\n"
                                             " 1. Видеонаблюдение.\n"
                                             "    При нажатии на данную кнопку открывается меню управления видеокамерами.В данном меню отображены видеокамеры, которые подключены к истеме. \n"
                                             " Пользователь имеет возможность добавлять/удалять видеокамеры, также редактировать сетевые настройки, просматривать видеопоток с выбранной \n"
                                             " камеры.\n"
                                             " 2. Весовой контроль.\n"
                                             "    При нажатии на данную кнопку открывается меню управления весового комплекса, интегрированного в систему. Данный комплекс подсоединен к \n"
                                             " системе посредством двух USB-COM-портов - один для подключения весов, второй для подключения светофоров. В меню пользователь может выбрать\n"
                                             " номера портов для подключения весов и светофоров. Также в нижней части меню графически отображеноы текущие показания весов в режиме реального \n"
                                             " времени и отображены текущие состояние светофоров, которые также меняются  режиме реального времени.\n"
                                             " 3. Контроль доступа.\n"
                                             "    При нажатии на данную кнопку открывается меню управления шлагбаумом. Управление шлагбаумом в автоматичемком и ручном режиме осуществляется\n"
                                             " посредством отправки управляющих команд на контроллер MOXA. Данно меню управления позволяет по необходимости изменить сетевые настройки для \n"
                                             " связи с контроллером управления шлагбаумом. Также в данном меню отображено текущее состояние шлагбаума (открыт/закрыт) и выведен видеопоток с \n"
                                             " камеры  видеонаблюдения на въезде для визуального наблюдения за шлагбаумом.\n"
                                             " 4. Базы данных.\n"
                                             "    При нажатии на данную кнопку открывается меню управления локальными базами данных. Для работы системы используются две локальные базы \n"
                                             " данных SQL, работа с которыми осуществляется при помощи СУРБД MySQL и PostgreSQL. В меню управления базами данных пользователь может \n"
                                             " отредактировать настройки,  которые система использует для подключения в локальным базам данных.\n"
                                             " 5. Статус системы.\n"
                                             "    При нажатии на данную кнопку открывается меню, в котором в графической форме отображены все функциональные узлы системы и их соответствующий \n"
                                             " текущий статус. Зеленый круг напротив того или иного узла означает, что он подключен к системе и функционирует корректно. Красный круг напротив \n"
                                             " того или иного узла означает, что в данный момент он не подключен к системе (не отвечает).\n"
                                             " 6. Отслеживание ТС.\n"
                                             "    При нажатии на данную кнопку открывается меню настройки отслеживания транспортных средств. В данном меню пользователь может указать URL-адрес\n"
                                             " агрегатора-ГЛОНАСС, к которому прекреплено каждое ТС заведенное в систему. В результате, чтобы узнать текущее географическое положение ТС, нужно\n"
                                             " в главном журнале навести курсор компьютерной мыши на необходимую запись с требуемым ГРЗ(искомого ТС) и два раза нажать на эту ячейку левой \n"
                                             " кнопкой мыши. В результате откроется web-браузер, в котором автоматически отобразиться где данное ТС находится в данный момент.\n"
                                             " 7. Режим работы ПО.\n"
                                             "    При нажатии на данную кнопку откроется меню выбора режима работы системы. В системе предусмотрено два режима работы - автоматический и ручной.\n"
                                             " В автоматическом режиме обработка данных с всех узлов системы и управления всеми узлами системы производится автоматическо согласно заложенным\n"
                                             " алгоритмам. Если в системе произошел сбой или требуется вмешательство оператора (на пример для корректироваки измеряемого значения массы ТС), то\n"
                                             " в системе предусмотрен ручной режим работы. В данном на главном экране ПО появляются инструменты мониторинга и управления весовым комплексом и \n"
                                             " шлагбаумом, а также дополнительные кнопки, при помощи которых оператор может вручную менять состояние светофоров, а также открывать/закрывать\n"
                                             " шлагбаум. \n"
                                             " 8. Справка.\n"
                                             "   При нажатии на данную кнопку открывается окно, в котором представлено описание работы элементов управления из меню \"Настройки системы\".\n"
                                             ""))

    def firstCall(self):

            self.lstLight = [[self.label, "background-color: rgb(242,242,242);"],
                             [self.lblIconJournal,
                              "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));\n"
                              "image: url(" + globalValues.pathStyleImgs + "iconworkpanel1.png);"],
                             [self.label_50, "background-color: rgb(242,242,242);\n"
                                             "font: 10pt \"Arial\";"],
                             [self.lblBack, "background-color: rgb(242,242,242);"]]
            self.lstDark = [[self.label, "background-color: rgb(66,66,66);\n"
                                         "color: white;"],
                            [self.lblIconJournal,
                             "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));\n"
                             "image: url(" + globalValues.pathStyleImgs + "iconworkpanel1.png);"],
                            [self.label_50, "background-color: rgb(66,66,66);\n"
                                            "color:white;\n"
                                            "font: 10pt \"Arial\";"],
                            [self.lblBack, "background-color: rgb(66,66,66);"]]

            self.lengthLight = len(self.lstLight)
            self.lengthDark = len(self.lstDark)

            self.changeCOLORMainPanelGrunt(0.1)

            globalValues.writeEventToDBJournalMain('Настройки системы', 'Выполнено открытие справки настройки системы')

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
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_AboutSysMenu()
    ui.show()
    sys.exit(app.exec_())
