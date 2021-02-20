from PyQt5.QtGui import QPixmap


import os
import subprocess

# def system_call(args, cwd="."):
#     print("Running '{}' in '{}'".format(str(args), cwd))
#     subprocess.call(args, cwd=cwd)
#     pass

def fix_image_files(path):
    for path, dirs, files in os.walk(os.path.abspath(path)):
        # sys.stdout.write('.')
        for file in files:
            print(file)
            # dir += '/'
            subprocess.call("mogrify /home/sergey/123/imgStrg/" + str(file))
            # subprol("find. - name \"*.png\" - type f - print0 | xargs - 0 pngcrush_1_8_8_w64.exe - n - q > pngError.txt 2 > & 1")


fix_image_files('/home/sergey/123/imgStrg/')