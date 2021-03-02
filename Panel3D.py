from PyQt5.QtWidgets import QApplication, QLabel, QFrame, QDialog, QPushButton, QScrollBar, QTreeWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QCoreApplication, QMetaObject, QRect
import globalValues
import glob
import os
import threading
import time

# import traceback
# import numpy as np
# import scipy.ndimage as ndimage
# import cv2
# from panelMesBox import Ui_mes_box
# import matplotlib.pyplot as plt
# from matplotlib.pyplot import imread
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import animation
# import mayavi.mlab as mlab
# import matplotlib.cm as cm
# from panelCreate3D import create_3d

class Ui_PanelCreateModel(QDialog):

    oldName = ''
    pathCurImg = ''
    firstCallChangeScroll = True

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.setFixedSize(1920, 940)
        self.frmArchive = QFrame(self)
        self.frmArchive.setGeometry(QRect(0, 0, 1920, 1011))
        self.frmArchive.setFrameShape(QFrame.StyledPanel)
        self.frmArchive.setFrameShadow(QFrame.Raised)
        self.frmArchive.setObjectName("frmArchive")
        self.btnBackToMain = QPushButton(self.frmArchive)
        self.btnBackToMain.setGeometry(QRect(1519, 910, 401, 31))
        font = QFont()
        font.setPointSize(10)
        self.btnBackToMain.setFont(font)
        self.btnBackToMain.setStyleSheet("QPushButton:!hover {background-color: rgb(66,66,66);\n"
            "border-radius: 0px;\n"
            "border-bottom-right-radius: 3px;\n"
            "color: rgb(255, 255, 255);\n"
            "border-bottom: 2px solid rgb(42,42,42);\n"
            "border-right: 2px solid rgb(42,42,42);\n"
            "border-top: 2px solid rgb(42,42,42);}\n"
            "\n"
            "QPushButton:hover {background-color: rgb(84,122,181);\n"
            "border-radius: 0px;\n"
            "border-bottom-right-radius: 3px;\n"
            "color: rgb(255, 255, 255);\n"
            "border-bottom: 2px solid rgb(42,42,42);\n"
            "border-right: 2px solid rgb(42,42,42);\n"
            "border-top: 2px solid rgb(42,42,42);}\n"
            "\n"
            "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
            "border-radius: 0px;\n"
            "border-bottom-right-radius: 3px;\n"
            "color: rgb(255, 255, 255);\n"
            "border-bottom: 2px solid rgb(42,42,42);\n"
            "border-right: 2px solid rgb(42,42,42);\n"
            "border-top: 2px solid rgb(42,42,42);}")
        self.btnBackToMain.setObjectName("btnBackToMain")
        self.label_6 = QLabel(self.frmArchive)
        self.label_6.setGeometry(QRect(1670, 5, 111, 21))
        self.label_6.setStyleSheet("background-color: rgb(42,42,42);\n"
            "color: white;\n"
            "font: 11pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QLabel(self.frmArchive)
        self.label_7.setGeometry(QRect(1516, 0, 411, 31))
        self.label_7.setStyleSheet("background-color: rgb(42,42,42);\n"
            "border-radius: 5px;\n"
            "border: 2px solid rgb(42,42,42);\n"
            "border-left-color: rgb(75,75,75);\n"
            "border-bottom-right-radius: 0px;\n"
            "border-top-left-radius: 0px;\n"
            "border-bottom-left-radius: 0px;\n"
            "border-bottom: 1px;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.vScrollArch = QScrollBar(self.frmArchive)
        self.vScrollArch.setGeometry(QRect(1910, 30, 10, 881))
        self.vScrollArch.setStyleSheet("QScrollBar:vertical {\n"
            "border: 1px solid rgb(63,63,63);\n"
            " background: rgb(63,63,63);\n"
            "width:10px;\n"
            "margin: 0px 0px 0px 0px;\n"
            "}\n"
            "QScrollBar::add-page:vertical {background: rgb(89,89,89);}\n"
            "QScrollBar::sub-page:vertical {background: rgb(89,89,89);}\n"
            "QScrollBar::handle:vertical {\n"
            "background: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop: 0 rgb(50,75,115), stop: 0.5 rgb(50,75,115), stop:1 rgb(50,75,115));\n"
            "min-height: 0px;\n"
            "}\n"
            "QScrollBar::add-line:vertical {\n"
            " background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 rgb(50,75,115), stop: 0.5 rgb(50,75,115),  stop:1 rgb(50,75,115));\n"
            "height: 0px;\n"
            "subcontrol-position: bottom;\n"
            "subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:vertical {\n"
            "background: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop: 0  rgb(50,75,115), stop: 0.5 rgb(50,75,115),  stop:1 rgb(50,75,115));\n"
            "height: 0 px;\n"
            "subcontrol-position: top;\n"
            "subcontrol-origin: margin;\n"
            "}")
        self.vScrollArch.setOrientation(Qt.Vertical)
        self.vScrollArch.setObjectName("vScrollArch")
        self.line = QFrame(self.frmArchive)
        self.line.setGeometry(QRect(1521, 30, 388, 2))
        self.line.setStyleSheet("background-color: rgb(42,42,42);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.treeArchive = QTreeWidget(self.frmArchive)
        self.treeArchive.setGeometry(QRect(1519, 6, 392, 904))
        self.treeArchive.setStyleSheet("QTreeWidget {\n"
            "background-color: rgb(42,42,42);\n"
            "border-radius: 5px;\n"
            "border-top-left-radius : 0px;\n"
            "border-bottom-left-radius: 0px;\n"
            "border: 2px solid rgb(42,42,42);\n"
            "border-left: 0px solid rgb(42,42,42);\n"
            "border-top-right-radius: 0px;\n"
            "border-bottom-right-radius: 0px;\n"
            "border-bottom: 4px solid rgb(42,42,42);\n"
            "color: white;\n"
            "font: 11pt \"MS Shell Dlg 2\";\n"
            "padding-left: 7px;\n"
            "}\n"
            "\n"
            "QTreeWidget::item {\n"
            "margin: 2px;\n"
            "};")
        self.treeArchive.setObjectName("treeArchive")
        self.label = QLabel(self.frmArchive)
        self.label.setGeometry(QRect(0, 0, 1519, 941))
        self.label.setStyleSheet("background-color: rgb(75,75,75);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.btnBackToMain.raise_()
        self.treeArchive.raise_()
        self.label_7.raise_()
        self.label_6.raise_()
        self.line.raise_()
        self.vScrollArch.raise_()
        self.label.raise_()

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)
        self.firstSets()

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Панель создания 3д модели"))
        self.btnBackToMain.setText(_translate("Dialog", "Построить 3Д модель"))
        self.label_6.setText(_translate("Dialog", "Список файлов"))
        self.treeArchive.headerItem().setText(0, _translate("Dialog", "Arch"))

    def firstSets(self):
        self.treeArchive.verticalScrollBar().hide()
        self.vScrollArch.valueChanged.connect(self.sync_func)
        pathCur = globalValues.pathScanImgs
        self.checkFolderLongPath(pathCur)
        self.readAndPasteTreeImgs(pathCur)
        self.treeArchive.itemClicked.connect(self.openImg)
        self.btnBackToMain.clicked.connect(self.open3DModel)

    def checkFolderLongPath(self, pathFolder):
        try:
            i = 0
            listPath = []
            for element in pathFolder:
                if (element == '/' and i != 0):
                    listPath.append(pathFolder[0:i])
                i += 1
            listPath.append(pathFolder)

            # print(listPath)

            for elPath in listPath:
                if (os.path.exists(elPath) == False):
                    try:
                        os.mkdir(elPath)
                    except Exception as ex:
                        globalValues.writeLogData('Функция проверки и создания папки хранилища', str(ex))

        except Exception as ex:
            globalValues.writeLogData('Функция проверки ссылки на папку хранилища', str(ex))

    def readAndPasteTreeImgs(self, path):
        try:
            print(path)
            lengthPath = len(path)
            self.treeArchive.clear()
            for name in glob.glob(path + '/*.jpg'):
                name = name[lengthPath+1:len(name)]
                item = QTreeWidgetItem()
                item.setText(0, name)
                self.treeArchive.addTopLevelItem(item)

            th_chg_scrl = threading.Thread(target=self.thChangeScroll, args=(True,))
            th_chg_scrl.start()
        except Exception as ex:
            globalValues.writeLogData('Функция считывания данных картинок из папки', str(ex))

    def openImg(self):
        try:
            data = self.treeArchive.currentItem().text(0)
            print(data)
            if (data != self.oldName):
                pathImg = globalValues.pathScanImgs + '/' + data
                img = QPixmap(pathImg)
                k = 940/img.height()
                img = img.scaled(int(k*img.width()), 940)
                self.label.setPixmap(img)
                self.updateGeometry()
                self.pathCurImg = pathImg

            self.oldName = data
        except Exception as ex:
            globalValues.writeLogData('Функция вставки картинки', str(ex))

    def open3DModel(self):
        try:
            if (self.pathCurImg != ''):
                print('checking!')
            #     path_adapt= ''
            #     imageFile = self.pathCurImg
            #     img = cv2.imread(imageFile)
            #     img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            #     lstPath = self.pathCurImg.split('/')
            #     print('qwery')
            #     print(lstPath)
            #     strData = str(lstPath[len(lstPath) - 1])
            #     lengthStr = len(strData)
            #     strData = strData[0:lengthStr-4] + '_adapt' + strData[lengthStr-4:lengthStr]
            #     lstPath[len(lstPath) - 1] = strData
            #     i = 0
            #     for el in lstPath:
            #         i += 1
            #         path_adapt += el
            #         if (i != len(lstPath)):
            #             path_adapt += '/'
            #     cv2.imwrite(path_adapt, img)
            #     time.sleep(0.3)
            #
            #     # img = img.
            #     # mat = img[15:220, 85:190]
            #     img = cv2.imread(path_adapt)
            #     mat = img
            #     mat = mat[:, :, 0]  # get the first channel
            #     # print(mat)
            #     rows, cols = mat.shape
            #     xv, yv = np.meshgrid(range(cols), range(rows)[::1])
            #     # xv ,yv = np.mgrid[-1:1:0.001, -1:1:0.001]
            #     z0 = xv ** 3 + yv ** 4
            #
            #     k = 0
            #     for el in mat:
            #         z = 0
            #         for elVal in el:
            #             if (elVal > 168):
            #                 print(elVal)
            #                 mat[k][z] = 168
            #             z += 1
            #         k += 1
            #
            #     blurred = ndimage.gaussian_filter(mat, sigma=(4, 4), order=0)
            #
            #     print(blurred)
            #
            #     w = np.arctan(blurred / 100)
            #     print(w)
            #
            #     s = mlab.mesh(xv, yv, blurred, scalars=w)
            #
            #     alpha = 30  # degrees
            #     mlab.view(azimuth=0, elevation=90, roll=-90 + alpha)
            #
            #     # dataX = ''
            #     # dataY = ''
            #     # dataZ = ''
            #     # for el in xv:
            #     #     dataX += str(el)
            #     # for el in yv:
            #     #     dataY += str(el)
            #     # for el in blurred:
            #     #     dataZ += str(el)
            #     # print(dataX)
            #     #
            #     # f = open('E:/exampleList.txt', 'w')
            #     # data = 'ExampleListX: \r\n' + dataX + '\r\n' + 'ExampleListY: \r\n' + dataY + '\r\n' + 'ExampleListZ: \r\n' + dataZ + '\r\n'
            #     # print(data)
            #     # f.write(data)
            #     #
            #     # f.close()
            #
            #     mlab.show()
            #
            #     self.readAndPasteTreeImgs(globalValues.pathScanImgs)
            #
            # else:
            #     uiMes = Ui_mes_box()
            #     uiMes.lblStrInfo.setText('Не выбрана картинка!')
            #     uiMes.btnOK.hide()
            #     if (globalValues.colorForm == 1):
            #         uiMes.label_iconques.setStyleSheet("background-color: rgb(235,235,235);\n"
            #                                            "image: url(" + globalValues.pathStyleImgs + "icnAtt.png);")
            #     else:
            #         uiMes.label_iconques.setStyleSheet("background-color: rgb(75,75,75);\n"
            #                                            "image: url(" + globalValues.pathStyleImgs + "icnAtt.png);")
            #     uiMes.btnCancel.setText('Продолжить')
            #     uiMes.exec_()

        except Exception as ex:
            globalValues.writeLogData('Функция создания 3д модели', str(ex))

    def sync_func(self):
        self.treeArchive.verticalScrollBar().setValue(self.vScrollArch.value())

    def thChangeScroll(self, check):
        try:

            num_delta = 200
            if (self.firstCallChangeScroll):
                self.firstCallChangeScroll = False
                num_delta = 350

            # print('Delta: ' + str(num_delta))

            start_time = round(time.time() * 100)
            while True:
                numRows = self.treeArchive.verticalScrollBar().maximum()
                delta = round(abs(time.time() * 100) - start_time)

                # print(num_delta)

                if numRows != 0:
                    print('changeBarScroll!!!' + str(numRows))
                    time.sleep(0.2)
                    self.vScrollArch.setMaximum(self.treeArchive.verticalScrollBar().maximum())
                    break
                # print('checkingScroll!!!: ' + str(numRows))

                if delta > num_delta:
                    if (check):
                        # print('changeScrollTimer')
                        self.vScrollArch.setMaximum(self.treeArchive.verticalScrollBar().maximum())
                    break

                time.sleep(0.1)

                if (globalValues.stopAll):
                    break
        except Exception as ex:
            globalValues.writeLogData('Поток обработки изменения скролла', str(ex))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Ui_PanelCreateModel()
    ui.show()
    sys.exit(app.exec_())
