import serial
import logging
import time

logging.basicConfig(level=logging.DEBUG)

#func working with semaphore
def semaphore(queue_, port_sema):
    iter = 0
    time_start = 0
    check_start = True

    while True:
        if (check_start):
            try:
                lst_ports = port_sema.split(' ')
                port_sema = '/dev/ttyS' + lst_ports[1]

                ser_traffic = serial.Serial(
                    port=port_sema,
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=0)

                logging.debug('Opening sema port: %s.' % port_sema)

                values_default_checking = bytearray([0x40, 0x31, 0x30, 0x41, 0x31, 0x0D])
                values_default_data_green_default_in = bytearray([0x40, 0x31, 0x30, 0x30, 0x33, 0x30, 0x34, 0x0D])
                values_default_traffic_light_green_out = bytearray([0x40, 0x31, 0x30, 0x30, 0x34, 0x30, 0x35, 0x0D])
                values_default_traffic_light_all_red = bytearray([0x40, 0x31, 0x30, 0x30, 0x38, 0x30, 0x39, 0x0D])
                values = values_default_data_green_default_in

                millis = int(round(time.time() * 1000))
                val_iter = 0
                line = []
                lineNew = []
                time_get_data_traffic = round(time.time())
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
                        lineNew.append(h)
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

            except (Exception, SystemError, SystemExit) as ex:
                if ser_traffic.is_open():
                    ser_traffic.close()
                logging.debug('Error: %s.' % ex)


            time_start = round(time.time() * 100)
            check_start = False

        if (abs(round(time.time()*100 - time_start) >= 500)):
            iter += 1
            check_start = True
            if (iter >= 5):
                break

        time.sleep(0.04)


