import serial.tools.list_ports

list = serial.tools.list_ports.comports()

print('ComPorts: ', list)



connected = []
for element in list:
            dataEl = str(element.device)
            dataLst = dataEl.split('S')
            dataEl = 'Com ' + str(dataLst[1])
            connected.append(dataEl)
            print('ComPortsName: ', dataEl)

print(connected)
