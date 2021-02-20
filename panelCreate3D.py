import globalValues
import glob
import os
import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.pyplot import imread
from mpl_toolkits.mplot3d import Axes3D
import scipy.ndimage as ndimage
# from matplotlib import animation
import cv2
# import mayavi.mlab as mlab
# import matplotlib.cm as cm
import time
from panelMesBox import Ui_mes_box
from PyQt5.QtWidgets import QDialog
import threading

class create_3d(QDialog):

    pathCurImg = ''

    def __init__(self, pathImg):
        super().__init__()
        self.pathCurImg = pathImg

    def createModel(self):
        try:
            if (self.pathCurImg != ''):
                path_adapt= ''
                imageFile = self.pathCurImg
                img = cv2.imread(imageFile)
                img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                lstPath = self.pathCurImg.split('/')
                print('qwery')
                print(lstPath)
                strData = str(lstPath[len(lstPath) - 1])
                lengthStr = len(strData)
                strData = strData[0:lengthStr-4] + '_adapt' + strData[lengthStr-4:lengthStr]
                lstPath[len(lstPath) - 1] = strData
                i = 0
                for el in lstPath:
                    i += 1
                    path_adapt += el
                    if (i != len(lstPath)):
                        path_adapt += '/'
                cv2.imwrite(path_adapt, img)
                time.sleep(0.3)

                # img = img.
                # mat = img[15:220, 85:190]
                img = cv2.imread(path_adapt)
                mat = img
                mat = mat[:, :, 0]  # get the first channel
                # print(mat)
                rows, cols = mat.shape
                xv, yv = np.meshgrid(range(cols), range(rows)[::1])
                # xv ,yv = np.mgrid[-1:1:0.001, -1:1:0.001]
                z0 = xv ** 3 + yv ** 4

                k = 0
                for el in mat:
                    z = 0
                    for elVal in el:
                        if (elVal > 168):
                            print(elVal)
                            mat[k][z] = 168
                        z += 1
                    k += 1

                blurred = ndimage.gaussian_filter(mat, sigma=(4, 4), order=0)

                print(blurred)

                w = np.arctan(blurred / 100)
                print(w)

                # s = mlab.mesh(xv, yv, blurred, scalars=w)
                #
                # alpha = 30  # degrees
                # mlab.view(azimuth=0, elevation=90, roll=-90 + alpha)

                f = open('E:/exampleList.txt', 'w')
                data = 'ExampleListX: \r\n' + xv + '\r\n' + 'ExampleListY: \r\n' + yv + '\r\n' + 'ExampleListZ: \r\n' + blurred +'\r\n'
                f.write(data)
                f.close()
                # mlab.show()

                self.readAndPasteTreeImgs(globalValues.pathScanImgs)

            else:
                uiMes = Ui_mes_box()
                uiMes.lblStrInfo.setText('Не выбрана картинка!')
                uiMes.btnOK.hide()
                if (globalValues.colorForm == 1):
                    uiMes.label_iconques.setStyleSheet("background-color: rgb(235,235,235);\n"
                                                       "image: url(" + globalValues.pathStyleImgs + "icnAtt.png);")
                else:
                    uiMes.label_iconques.setStyleSheet("background-color: rgb(75,75,75);\n"
                                                       "image: url(" + globalValues.pathStyleImgs + "icnAtt.png);")
                uiMes.btnCancel.setText('Продолжить')
                uiMes.exec_()

        except Exception as ex:
            globalValues.writeLogData('Функция создания 3д модели', str(ex))
