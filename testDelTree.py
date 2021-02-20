import os
import globalValues

pathRm = '/usr/local/Sinaps/Storage/*'
passwd = '34ubitav\n'
print("sudo rm -r " + str(pathRm))
command = "rm -r " + str(pathRm)
# command = 'ls'
print(command)
os.system(command)


# p = os.system('echo %s|sudo -S %s' % (passwd, command))