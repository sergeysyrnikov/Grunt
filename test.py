import pathlib

port_weight = 'tty1'

print(pathlib.Path().joinpath('/dev/ttyS', port_weight))

print(port_weight)