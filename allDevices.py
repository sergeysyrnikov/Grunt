import serial
import logging
import time
from queue import LifoQueue
import threading
import pathlib

from serial.serialutil import SerialException

logging.basicConfig(level=logging.DEBUG)

q = LifoQueue()

data_weight = {'weight_max_meas': 5000, 'weight_val': 5000, 'weight_delta':500}
data_ports = {'ports': ['tty1', 'tty2']}

#func working with semaphore
def semaphore(queue_, port_sema):

    iter = 0
    time_start = 0
    check_start = True
    ser_traffic = serial.Serial()

    while True:

        if (check_start):
            try:
                port_sema = str(pathlib.Path().joinpath('/dev/ttyS',  port_sema))

                ser_traffic = serial.Serial(
                    port=port_sema,
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=0)

                logging.debug('Opening sema port: %s.' % port_sema)

                #values for control controller_oven_discretes
                values_default_checking = bytearray([0x40, 0x31, 0x30, 0x41, 0x31, 0x0D])
                values_default_data_green_default_in = bytearray([0x40, 0x31, 0x30, 0x30, 0x33, 0x30, 0x34, 0x0D])
                values_default_traffic_light_green_out = bytearray([0x40, 0x31, 0x30, 0x30, 0x34, 0x30, 0x35, 0x0D])
                values_default_traffic_light_all_red = bytearray([0x40, 0x31, 0x30, 0x30, 0x38, 0x30, 0x39, 0x0D])
                values = values_default_data_green_default_in

                millis = int(round(time.time() * 1000))
                val_iter = 0
                line = []
                time_start = round(time.time())
                check_start = True
                data_queue = ''

                while True:

                    #writing current bytearray to port
                    if ((int(round(time.time() * 1000)) - millis) > 50):
                        if ((val_iter % 2) == 1):
                            millis = int(round(time.time() * 1000))
                            ser_traffic.write(values)
                        else:
                            millis = int(round(time.time() * 1000))
                            ser_traffic.write(values_default_checking)

                    #reading data from sema_port
                    for c in ser_traffic.read():
                        h = hex(c)
                        line.append(h)
                        # lineNew.append(h)
                        # countLine = len(line)
                        # may be h = 0xd or 0x0D
                        if h == '0xd':
                            # countLine = len(line)
                            # may be '0x3E'
                            # and (countLine == 8)
                            if (line[0] == '0x3e'):
                                time_get_data_traffic = round(time.time())

                            line = []

                    if not queue_.empty():
                        data_queue = queue_.get()

                        if data_queue == 'weight_ready':
                            values = values_default_traffic_light_green_out
                            logging.debug('Change semaphore state to %s.' % data_queue)
                            data_queue = ''

                        elif data_queue == 'measure':
                            values = values_default_traffic_light_all_red
                            logging.debug('Change semaphore state to %s.' % data_queue)
                            data_queue = ''

                        elif data_queue == 'default':
                            values = values_default_data_green_default_in
                            logging.debug('Change semaphore state to %s.' % data_queue)
                            data_queue = ''

                    val_iter += 1

                    #old values states semaphore

                    # if (is_good_start_traffic):

                    #     if (values == values_default_traffic_light_green_out):
                    #         globalValues.check_sema_1_in = 2
                    #         globalValues.check_sema_1_out = 1
                    #         globalValues.check_sema_2_in = 2
                    #         globalValues.check_sema_2_out = 1
                    #     else:
                    #         if (values == values_default_traffic_light_all_red):
                    #             globalValues.check_sema_1_in = 1
                    #             globalValues.check_sema_1_out = 1
                    #             globalValues.check_sema_2_in = 1
                    #             globalValues.check_sema_2_out = 1
                    #         else:
                    #             if (values == values_default_data_green_default_in):
                    #                 globalValues.check_sema_1_in = 1
                    #                 globalValues.check_sema_1_out = 2
                    #                 globalValues.check_sema_2_in = 1
                    #                 globalValues.check_sema_2_out = 2
                    #             else:
                    #                 globalValues.check_sema_1_in = 0
                    #                 globalValues.check_sema_1_out = 0
                    #                 globalValues.check_sema_2_in = 0
                    #                 globalValues.check_sema_2_out = 0

            except (Exception, SystemError, SystemExit, SerialException) as ex:
                if ser_traffic.is_open:
                    ser_traffic.close()
                logging.debug('Error semaphore: %s.' % ex)


            time_start = round(time.time() * 100)
            check_start = False

        if (abs(round(time.time()*100 - time_start) >= 500)):
            iter += 1
            check_start = True
            if (iter >= 5):
                break

        time.sleep(0.04)

#func working with Weight
def weight(queue_, port_weight, data):
    iter = 0
    time_start = time.time()
    check_start = True
    check_measure = False
    ser_weight = serial.Serial()

    while True:
        if (check_start):
            try:
                port_weight = str(pathlib.Path().joinpath('/dev/ttyS', port_weight))
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


            except (Exception, SystemError, SystemExit, SerialException)  as ex:
                if ser_weight.is_open:
                    ser_weight.close()
                logging.debug('Error weight: %s.' % ex)

            time_start = round(time.time())
            check_start = False

        if (abs(round(time.time() - time_start)) >= 5):
            iter += 1
            check_start = True
            if (iter >= 5):
                break

        time.sleep(0.04)


th_weight = threading.Thread(target=weight, args=(q, data_ports['ports'][0], data_weight, ), daemon=True)
th_sema = threading.Thread(target=semaphore, args=(q, data_ports['ports'][1], ), daemon=True)
th_weight.start()
th_sema.start()

start_time = time.time()
while True:

    logging.debug('Thread weight: %s.' % th_weight.is_alive())
    logging.debug('Thread sema: %s.' % th_sema.is_alive())
    if not th_weight.is_alive():
        th_weight = threading.Thread(target=weight, args=(q, data_ports['ports'][0], data_weight, ), daemon=True)
        th_weight.start()
        logging.debug('Thread %s starting again.' % th_weight)
    if not th_sema.is_alive():
        th_sema = threading.Thread(target=semaphore, args=(q, data_ports['ports'][1], ), daemon=True)
        th_sema.start()
        logging.debug('Thread %s starting again.' % th_sema)

    if abs(time.time() - start_time) > 180:
        break
    time.sleep(1)
