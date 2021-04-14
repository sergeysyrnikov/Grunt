import pathlib
import serial
import logging
import time

logging.basicConfig(level=logging.DEBUG)

data_weight = {'weight_max_meas': 5000, 'weight_val': 5000, 'weight_delta':500}

#func working with Weight
def weight(queue_, port_weight, data):
        iter = 0
        time_start = time.time()
        check_start = True
        check_measure = False
        while True:
            if (check_start):
                try:
                    lst_ports = port_weight.split(' ')
                    port_weight = pathlib.Path.joinpath('/dev/ttyS', lst_ports[1])
                    logging.debug('Port weight: %s' % port_weight)

                    ser_weight = serial.Serial(
                        port=port_weight,
                        baudrate=9600,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=0)

                    logging.debug('Port weight opened!')

                    line = []

                    val_weight = ''
                    int_val_weight_cur = 0
                    int_val_weight_old = ''
                    int_val_weight = 0
                    count_iter = 0
                    count_iter_def_back = 0
                    str_grz_cur = ''
                    check_write_val = True
                    time_start = round(time.time())
                    check_start = True
                    check_change_sema = False
                    is_change_sema_def = False
                    check_measure = True


                    while True:

                        #measure current value from weight
                        try:
                            for c in ser_weight.read():

                                h = hex(c)
                                line.append(h)

                                if h == '0xa':
                                    count_line = len(line)
                                    if (line[0] == '0x77') and (count_line == 14):
                                        val_weight = ''
                                        val_wdg = 0
                                        for element in line:
                                            if (val_wdg > 2 and val_wdg < 10):
                                                str_el = str(element)
                                                str_el = str_el[3]
                                                # print('checking str_el: ' + str_el)
                                                val_weight = val_weight + str_el
                                                # print('checking strValueData: ' + val_weight)
                                                if (val_wdg == 9):
                                                    for dataElement in val_weight:
                                                        if (dataElement == '0'):
                                                            val_weight = val_weight[1::]
                                                        else:
                                                            break
                                                    if (line[2] == '0x2d' and val_weight != ''):
                                                        val_weight = ('-' + val_weight)

                                            val_wdg += 1
                                        if (val_weight == ''):
                                            val_weight = '0'
                                        int_val_weight = int(val_weight)
                                        int_val_weight_cur = int_val_weight
                                        if (int_val_weight_cur > data['weight_max_meas'] and int_val_weight_cur == int_val_weight_old):
                                            count_iter += 1
                                        else:
                                            if (int_val_weight_cur != int_val_weight_old and int_val_weight_cur > data['weight_max_meas']):
                                                if (count_iter > 0):
                                                    count_iter -= 1
                                            else:
                                                count_iter = 0
                                                check_write_val = True

                                        if (int_val_weight_cur == int_val_weight_old and int_val_weight_cur <= data['weight_val']):
                                            count_iter_def_back += 1
                                        else:
                                            if (int_val_weight_cur != int_val_weight_old and int_val_weight_cur <= data['weight_val']):
                                                if (count_iter_def_back > 0):
                                                    count_iter_def_back -= 1
                                            else:
                                                count_iter_def_back = 0

                                        int_val_weight_old = int_val_weight_cur

                                    line = []
                                    break
                        except (Exception, ValueError, IndexError) as ex:
                            logging.debug('Error: %s' % ex)

                        #starting measuring value
                        if (int_val_weight_cur > data['weight_max_meas'] and check_measure and count_iter > 20):
                            is_change_sema_def = True
                            count_iter_def_back = 0
                            queue_.put('measure')
                            check_measure = False
                            logging.debug('Starting process measuring!')

                        #Writing delta value weight defore start cycle
                        if (count_iter_def_back > 500):
                            count_iter_def_back = 0
                            data['weight_delta'] = int_val_weight_cur
                            logging.debug('Current delta: %skg.' % int_val_weight_cur)
                            if (is_change_sema_def):
                                is_change_sema_def = False
                                queue_.put('default')

                        #Writing value from weight
                        if (count_iter > 400 and check_write_val):
                            check_change_sema = True
                            count_iter = 0
                            check_write_val = False
                            intValueWithDelta = int(int_val_weight - data['weight_delta'])
                            strValueWithDelta = str(intValueWithDelta)

                            print('WritingDelta' + str(strValueWithDelta))

                            queue_.put('weight_ready')
                            time.sleep(0.001)

                        #Writing value in DB and change semaphore
                        if (int_val_weight_cur < data['weight_val'] and check_change_sema):
                            queue_.put('default')
                            check_measure = True
                            check_change_sema = False
                            logging.debug('Save current value: %skg.' % int_val_weight_cur)


                except (Exception, SystemError, SystemExit)  as ex:
                    if ser_weight.is_open():
                        ser_weight.close()

                time_start = round(time.time())
                check_start = False

            if (abs(round(time.time() - time_start)) >= 2):
                iter += 1
                check_start = True
                if (iter >= 5):
                    break

            time.sleep(0.04)
