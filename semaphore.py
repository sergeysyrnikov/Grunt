import pathlib
import serial
import logging
import time

logging.basicConfig(level=logging.DEBUG)

def semaphore(self, input_queue, port_sema):
        iter = 0
        time_start = 0
        check_start = True

        while True:
            if (check_start):
                try:
                        port_traffic = str(port_sema)

                        lstPorts = port_traffic.split(' ')
                        port_traffic = '/dev/ttyS' + lstPorts[1]
                        print(port_traffic)

                        ser_traffic = serial.Serial(
                            port=port_traffic, \
                            baudrate=9600, \
                            parity=serial.PARITY_NONE, \
                            stopbits=serial.STOPBITS_ONE, \
                            bytesize=serial.EIGHTBITS, \
                            timeout=0)

                        check_default = True
                        check_default_traffic_left = False
                        check_default_traffic_right = False

                        self.is_good_start_traffic = False

                        Debug = globalValues.debugPorts

                        globalValues.check_sema_1_in = 0
                        globalValues.check_sema_1_out = 0
                        globalValues.check_sema_2_in = 0
                        globalValues.check_sema_2_out = 0

                        values_default_checking = bytearray([0x40, 0x31, 0x30, 0x41, 0x31, 0x0D])
                        values_default_data_green_default_in = bytearray([0x40, 0x31, 0x30, 0x30, 0x33, 0x30, 0x34, 0x0D])
                        values_default_traffic_light_green_out = bytearray([0x40, 0x31, 0x30, 0x30, 0x34, 0x30, 0x35, 0x0D])
                        values_default_traffic_light_all_red = bytearray([0x40, 0x31, 0x30, 0x30, 0x38, 0x30, 0x39, 0x0D])

                        values = values_default_data_green_default_in

                        millisStart = int(round(time.time() * 1000))
                        millis = int(round(time.time() * 1000))

                        value_iter = 0

                        line = []

                        time_finish = 0
                        check_finish = False

                        lineNew = []

                        time_get_data_traffic = round(time.time())
                        time_start = round(time.time())
                        check_start = True
                        data_queue = ''

                        while True:

                            if (globalValues.stopAll):
                                    print('EndComTraffic!')
                                    break

                            if ((int(round(time.time() * 1000)) - millis) > 50):
                                if ((value_iter % 2) == 1):
                                    millis = int(round(time.time() * 1000))
                                    ser_traffic.write(values)
                                else:
                                    millis = int(round(time.time() * 1000))
                                    ser_traffic.write(values_default_checking)

                            for c in ser_traffic.read():
                                h = hex(c)
                                line.append(h)
                                lineNew.append(h)
                                countLine = len(line)
                                # may be h = 0xd or 0x0D
                                if h == '0xd':
                                    countLine = len(line)
                                    # may be '0x3E'
                                    # and (countLine == 8)
                                    if (line[0] == '0x3e'):
                                        time_get_data_traffic = round(time.time())

                                    line = []

                            #Debug
                            if (Debug == False):
                                    if (abs(round(time.time()) - time_get_data_traffic) >= 7):
                                        self.cbTraff.setEnabled(True)
                                        self.btnOpenPorts.show()

                                        globalValues.writeEventToDBJournalMain('Весы', 'Не удалось установить соединение с контроллером светофоров')
                                        ser_traffic.flush()
                                        ser_traffic.close()
                                        # self.setFixedSize(360, 200)
                                        # self.btnOpenPorts.show()
                                        # self.lblStTraffImg.setPixmap(QtGui.QPixmap(pathImgRedCom))
                                        self.lblStTraffImg.setStyleSheet('QLabel:!hover { image: url(' + pathImgRed + '); background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));};')
                                        self.lblStWeightAndSema.setStyleSheet(
                                            'QLabel:!hover {background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));\n'
                                            'image: url(' + pathImgRedCom + ');};')

                                        currentIndexTab = self.advices.currentIndex()
                                        self.advices.setCurrentIndex(0)
                                        self.advices.setCurrentIndex(currentIndexTab)
                                        if (iter == 0):
                                            self.error_traffic_signal.emit()
                                        self.is_good_start_traffic = False
                                        print('NotConnectTraffic!')
                                        break


                            if (abs(round(time.time()) - time_start) >= 6 and check_start):
                                check_start = False
                                self.cbTraff.setEnabled(False)
                                globalValues.writeEventToDBJournalMain('Весы', 'Успешно выполнено соединение с контроллером светофоров')
                                self.is_good_start_traffic = True

                                if (self.is_good_start_weight):
                                    self.btnOpenPorts.hide()
                                    print('goodWorkingWeight!')
                                    self.lblStWeightAndSema.setStyleSheet(
                                        'QLabel:!hover {background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));\n'
                                        'image: url(' + pathImgGreenCom + ');};')
                                self.lblStTraffImg.setStyleSheet('QLabel:!hover {background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));\n'
                            'image: url(' + pathImgGreen + ');};')

                                currentIndexTab = self.advices.currentIndex()
                                self.advices.setCurrentIndex(0)
                                self.advices.setCurrentIndex(currentIndexTab)

                                self.is_good_con_traffic.emit()

                            value_iter += 1

                            if (self.is_good_start_traffic):

                                if (values == values_default_traffic_light_green_out):
                                    globalValues.check_sema_1_in = 2
                                    globalValues.check_sema_1_out = 1
                                    globalValues.check_sema_2_in = 2
                                    globalValues.check_sema_2_out = 1
                                else:
                                    if (values == values_default_traffic_light_all_red):
                                        globalValues.check_sema_1_in = 1
                                        globalValues.check_sema_1_out = 1
                                        globalValues.check_sema_2_in = 1
                                        globalValues.check_sema_2_out = 1
                                    else:
                                        if (values == values_default_data_green_default_in):
                                            globalValues.check_sema_1_in = 1
                                            globalValues.check_sema_1_out = 2
                                            globalValues.check_sema_2_in = 1
                                            globalValues.check_sema_2_out = 2
                                        else:
                                            globalValues.check_sema_1_in = 0
                                            globalValues.check_sema_1_out = 0
                                            globalValues.check_sema_2_in = 0
                                            globalValues.check_sema_2_out = 0

                            trafWeightReady = False
                            trafMeasure = False
                            trafDefault = False

                            if (globalValues.startHandSt):
                                if (globalValues.trafWeightReady):
                                    globalValues.trafWeightReady = False
                                    values = values_default_traffic_light_green_out
                                    print('changeSemaGreenIn')
                                    globalValues.writeEventToDBJournalMain('Светофоры', 'Переключены светофоры в режим выезд ТС')

                                if (globalValues.trafMeasure):
                                    globalValues.trafMeasure = False
                                    values = values_default_traffic_light_all_red
                                    print('changeSemaAllRed')
                                    globalValues.writeEventToDBJournalMain('Светофоры','Переключены светофоры в режим запрет движения ТС')

                                if (globalValues.trafDefault):
                                    globalValues.trafDefault = False
                                    values = values_default_data_green_default_in
                                    print('changeSemaGreenOut')
                                    globalValues.writeEventToDBJournalMain('Светофоры','Переключены светофоры в режим въезд ТС')

                            else:

                                    if (q.empty() == False):
                                        data_queue = input_queue.get()


                                    if (str(data_queue) == 'weight_ready'):
                                        values = values_default_traffic_light_green_out
                                        data_queue = ''
                                        globalValues.writeEventToDBJournalMain('Светофоры','Переключены светофоры в режим выезд ТС')

                                    if (str(data_queue) == 'measure'):
                                        values = values_default_traffic_light_all_red
                                        globalValues.writeEventToDBJournalMain('Светофоры','Переключены светофоры в режим запрет движения ТС')
                                        data_queue = ''

                                    if (str(data_queue) == 'default'):
                                        values = values_default_data_green_default_in
                                        data_queue = ''
                                        globalValues.writeEventToDBJournalMain('Светофоры','Переключены светофоры в режим въезд ТС')
                                        print('checking Default!!!')

                        print('ExitThreadTraffic!')

                except Exception as ex:
                    globalValues.writeLogData('Поток обработки данных со светофоров', str(ex))
                    ser_traffic.close()
                    self.btnOpenPorts.show()
                    self.cbTraff.setEnabled(True)
                    self.lblStTraffImg.setStyleSheet(
                        'QLabel:!hover { image: url(' + pathImgRed + '); background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));};')
                    self.lblStWeightAndSema.setStyleSheet(
                        'QLabel:!hover {background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));\n'
                        'image: url(' + pathImgRedCom + ');};')

                    currentIndexTab = self.advices.currentIndex()
                    self.advices.setCurrentIndex(0)
                    self.advices.setCurrentIndex(currentIndexTab)
                    self.is_good_start_traffic = False
                    time.sleep(1)

                time_start = round(time.time() * 100)
                check_start = False

            if (globalValues.stopAll or globalValues.stopComPortTraffic):
                print('endTraffic!!!')
                break

            if (abs(round(time.time()*100 - time_start) > 500)):
                iter += 1
                check_start = True
                if (iter >= 5):
                    break

            time.sleep(0.1)


