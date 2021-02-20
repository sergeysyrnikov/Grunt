import cv2
import time
import os
import globalValues
import datetime
import threading
# import ping3
import requests
import subprocess
import shutil
from multiprocessing import Process
import glob
from PyQt5 import QtGui
# import vlc
import gc


class WorkingWithVideo:

    listBadCams = []
    listCheckIP = []
    listCheckRtsp = []
    isListCams = []
    listNameChls = []
    listNumChl = []
    pathFolderWritingCamDate = ''
    pathWriteEventsFolderDate = ''
    pathImgEventsFolderDate = ''
    pathFileEvent = ''

    pathWriteEvents = ''

    numberStartImg = 0
    numberEndImg = 0
    numImgSub = 0

    firstCheckStrg = True

    def covertingVideo(self, pathWriteFile, pathCreateFile):
        try:
            self.checkFolderPath(self.pathFolderWritingCamDate, False)
            print(pathWriteFile)
            print(pathCreateFile)
            strCommand = 'ffmpeg -i ' + pathWriteFile + ' -q:v 10 -vcodec libx264 -threads 2 ' + pathCreateFile
            os.system(strCommand)
            while True:
                if (os.path.exists(pathCreateFile)):
                    os.remove(pathWriteFile)
                    # print(abs(round(time.time()) - start_time))
                    break
                if (globalValues.stopAll):
                    break
        except Exception as ex:
            strDataInLog = 'Поток сжатия видеофайла в h264 путь: ' + str(pathCreateFile)
            globalValues.writeLogData(strDataInLog, str(ex))

    def copyFileandRemoveOld(self, pathOld, pathNew, strIP):
        try:
            self.checkFolderPath(self.pathFolderWritingCamDate, False)
            start_time = round(time.time())
            k = 0
            while True:
                if (os.path.exists(pathOld) and k == 0):
                    os.system('cp ' + pathOld + ' ' + pathNew)
                    # shutil.copyfile(pathOld, pathNew)
                    print('WritingFile Ip: ' + strIP)
                    k += 1

                if (abs(round(time.time()) - start_time) > 10):
                    if (os.path.exists(pathOld)):
                        os.remove(pathOld)
                    break

        except Exception as ex:
            globalValues.writeLogData('Функция копирования файлов ' + strIP, str(ex))

    # def thMainLoopWriterCamWithCompress(self, strIP, rtsp_link, delta):
    #     try:
    #         curDateOld = ''
    #         curIPOld = ''
    #         g = 0
    #         while True:
    #             try:
    #                 if (globalValsSBV.stopAll):
    #                     break
    #                 # if (0 <= i <= 2):
    #
    #                 # print(pathDefFolder)
    #
    #                 pathCamFolderWrite = pathDefFolder + '/' + strIP
    #                 cap = cv2.VideoCapture(rtsp_link, cv2.CAP_FFMPEG)
    #                 if (cap.isOpened()):
    #                     self.checkFolderPath(pathCamFolderWrite, True)
    #                     # print('CreateFolderCam!')
    #
    #                     cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    #                     frame_width = int(cap.get(3))
    #                     frame_height = int(cap.get(4))
    #                     # print(frame_width)
    #                     # print(frame_height)
    #
    #                     prev = time.time()
    #                     frame_rate = 24
    #                     z = 0
    #                     x = 0
    #
    #                     while True:
    #                         curDate = self.strCurDate()
    #                         if (curDate != curDateOld):
    #                             self.pathFolderWritingCamDate = pathStorage + '/' + curDate
    #                             self.checkFolderPath(self.pathFolderWritingCamDate, False)
    #                         curDateOld = curDate
    #
    #                         if (globalValsSBV.stopAll):
    #                             break
    #                         listFoldersInStorage = os.listdir(pathStorage)
    #                         k = 0
    #                         listFoldersGood = []
    #                         for elList in listFoldersInStorage:
    #                             x = '.' in elList
    #                             if (x and len(elList) == 10):
    #                                 listFoldersGood.append(elList)
    #                                 k += 1
    #                             if (k > 14):
    #                                 listValEl = []
    #                                 for el in listFoldersGood:
    #                                     el = el.replace('.', '')
    #                                     valEl = int(el)
    #                                     listValEl.append(valEl)
    #                                 i = 0
    #                                 z = 0
    #                                 valMin = 999999999
    #                                 for elVal in listValEl:
    #                                     if (elVal < valMin):
    #                                         i = z
    #                                         valMin = elVal
    #                                     z += 1
    #
    #                                 # print(valMin)
    #                                 # print(i)
    #                                 pathRmDir = pathStorage + '/' + listFoldersGood[i]
    #                                 try:
    #                                     shutil.rmtree(pathRmDir)
    #                                 except Exception as ex:
    #                                     globalValsSBV.writeLogData('Удаление старых записей', str(ex))
    #                                 break
    #
    #                         k = 0
    #
    #                         pathFileWrite = pathCamFolderWrite + '/' + self.strCurTime() + '.mp4'
    #
    #                         z += 1
    #                         out = cv2.VideoWriter(pathFileWrite, cv2.VideoWriter_fourcc(*"mp4v"), 15.9,
    #                                               (frame_width, frame_height))
    #                         # out = cv2.VideoWriter(pathFileWrite, 0x00000021, 15.9,
    #                         #                       (frame_width, frame_height))
    #                         start_time_wr = self.strCurTime()
    #                         time_start = round(time.time())
    #
    #                         if (cap.isOpened()):
    #                             g = 0
    #                             x = 0
    #                             while (True):
    #                                 if (globalValsSBV.stopAll):
    #                                     break
    #                                 ret, frame = cap.read()
    #                                 out.write(frame)
    #                                 # nameImg = 'E:/frame/' + str(k) + '.jpg'
    #                                 # cv2.imwrite(nameImg, frame)
    #                                 # cv2.imshow('frame', frame)
    #                                 k += 1
    #                                 # if cv2.waitKey(1) & 0xFF == ord('q'):
    #                                 #         break
    #                                 # print(round(time.time()))
    #                                 # print(abs(round(time.time()) - time_start))
    #                                 if (abs(round(time.time()) - time_start) >= delta):
    #                                         break
    #
    #
    #                             out.release()
    #
    #                             end_time_wr = self.strCurTime()
    #
    #                             # if (0 <= i <= 2):
    #
    #                             # curDate = strCurDate()
    #                             self.pathFolderWritingCamDate = pathStorage + '/' + curDate
    #                             pathFolderTheCam = self.pathFolderWritingCamDate + '/' + strIP
    #                             self.checkFolderPath(pathFolderTheCam, False)
    #
    #                             nameFileCreate = start_time_wr + '-' + end_time_wr
    #                             pathFileCreate = pathFolderTheCam + '/' + nameFileCreate + '.mp4'
    #
    #
    #                             # strPathNew = nameFileCreate + '.mp4'
    #                             th_convert_video = threading.Thread(target=self.covertingVideo,
    #                                                                 args=(pathFileWrite, pathFileCreate,))
    #                             th_convert_video.start()
    #                         else:
    #                             x += 1
    #                         if (x > 5):
    #                             dataInLog = 'Ошибка открытия камеры: ' + strIP
    #                             globalValsSBV.writeLogData(dataInLog, ' ')
    #                             break
    #
    #                 if (g > 2):
    #                     globalValsSBV.writeLogData('Ошибка потока, запись камеры остановлена ', strIP)
    #                     break
    #
    #                 g += 1
    #
    #                 cap.release()
    #
    #             except Exception as ex:
    #                 globalValsSBV.writeLogData('Функция записи видеопотока', str(ex))
    #
    #     except Exception as ex:
    #         globalValsSBV.writeLogData('Функция записи видео', str(ex))

    def thMainLoopWriterCam(self, strIP, rtsp_link, delta, pathStorage, pathDefFolderCam, valGlobal, nameChannel, numCam):

        try:
            checkGoodWrite = True
            curDateOld = ''
            curIPOld = ''
            g = 0
            time_start_pr = 0
            start_time_wr = ''
            end_time_wr = ''
            checkWriteFileEvent = False
            pathFileEvent = ''

            globalValues.numEvent[numCam] = 0

            self.numImgSub = 0

            firstNumImg = False

            print('sergio123')
            print(nameChannel)
            print(valGlobal)

            pathWriteEvents = globalValues.curDisk + '/ACMK/VideoEvents/' + nameChannel

            print(pathWriteEvents)

            # pathImgEvents = globalValues.curDisk + ':/ACMK/КартинкиСобытий/' + nameChannel

            pathStorage = pathStorage + '/' + nameChannel

            while True:

                try:
                    globalValues.checkCamStrg[numCam] = False
                    print('ChangeCamSt: ' + str(globalValues.checkCamStrg))
                    print('NumberDayToSave' + str(globalValues.numberFolderDateSave))
                    if (globalValues.stopAll or globalValues.stopStrg):
                        break

                    pathCamFolderWrite = pathDefFolderCam + '/' + strIP
                    pathCamFolderImgWrt = pathDefFolderCam + '/' + strIP + '/imagesBefore'
                    # print('startCheckingCam!!!')
                    print('RtspLink: ' + rtsp_link)
                    cap = cv2.VideoCapture(rtsp_link)
                    # print('endCheckingCam!!!')

                    cap.set(cv2.CAP_PROP_BUFFERSIZE, 3)
                    if (cap.isOpened()):
                        g = 0
                        print('checkingTrueCam!' + str(numCam))
                        globalValues.checkCamStrg[numCam] = True
                        # print(globalValues.checkCamStrg)
                        # cap.set(cv2.CAP_PROP_BUFFERSIZE, 5)

                        globalValues.writeLogDataTh('Камера открыта:', strIP, strIP)

                        self.checkFolderPath(pathCamFolderWrite, True)
                        self.checkFolderPath(pathCamFolderImgWrt, True)
                        self.checkFolderLongPath(pathWriteEvents)
                        # self.checkFolderLongPath(pathImgEvents)
                        self.checkFolderLongPath(pathStorage)

                        numberImg = 0

                        prev = time.time()
                        frame_rate = 24
                        z = 0
                        x = 0
                        checkOut = False

                        start_time_wrt_frm = round(time.time() * 100)

                        shutil.rmtree(pathCamFolderImgWrt)

                        # listPathElFrm = os.listdir(pathCamFolderImgWrt)
                        # for el in listPathElFrm:
                        #     os.remove('rm -r ' + pathCamFolderImgWrt + '/' + str(el))
                        #     # print(pathCamFolderImgWrt + '\\' + el)

                        while True:

                            if (globalValues.stopAll or globalValues.stopStrg):
                                break

                            if (checkGoodWrite):
                                k = 0
                                z += 1

                                if (cap.isOpened()):
                                    x = 0
                                    g = 0


                            numCheckWrt = 0
                            start_time_check = round(time.time() * 100)
                            numberImgOld = 0
                            numberImgStop = 0
                            numEventFrm = 0


                            checkDelOld = False

                            while True:
                                if (globalValues.stopAll or globalValues.stopStrg):
                                    break

                                curDate = self.strCurDate()

                                if (curDate != curDateOld):
                                    self.pathFolderWritingCamDate = pathStorage + '/' + curDate
                                    self.checkFolderPath(self.pathFolderWritingCamDate, False)
                                    pathWriteEventsFolderDate = pathWriteEvents + '/' + curDate
                                    self.checkFolderPath(pathWriteEventsFolderDate, False)
                                    # self.pathImgEventsFolderDate = pathImgEvents + '/' + curDate
                                    # self.checkFolderPath(self.pathImgEventsFolderDate, False)


                                curDateOld = curDate

                                if (checkGoodWrite):
                                    print('CheckingStrg!!!')
                                    print(pathStorage)
                                    print(globalValues.numberFolderDateSave)
                                    self.checkStrgAndRmv(pathStorage, strIP)

                                    frame_width = int(cap.get(3))
                                    frame_height = int(cap.get(4))

                                    pathFileWrite = pathCamFolderWrite + '/' + self.strCurTime() + '.mp4'
                                    # checkFolderLongPath(pathCamFolderWrite)

                                    out = cv2.VideoWriter(pathFileWrite, cv2.VideoWriter_fourcc(*"mp4v"), 15.9,
                                                          (frame_width, frame_height))

                                    out.set(cv2.CAP_PROP_BUFFERSIZE, 3)

                                    checkGoodWrite = False
                                    time_start_pr = round(time.time())
                                    start_time_wr = self.strCurTime()

                                z = 0
                                frame_rate = 16
                                delta_time = 0

                                start_time_clear_cache = round(time.time()*100)

                                while True:
                                            if (globalValues.stopAll or globalValues.stopStrg):
                                                 break

                                            ret, frame = cap.read()

                                            # frameNew = frame
                                            # time.sleep(0.035)
                                            # print(ret)

                                            # time_elapsed = time.time() - prev
                                            #
                                            # if time_elapsed > 1. / frame_rate:
                                            #     prev = time.time()

                                            if ret == True:

                                                suc_video, frame_video = cap.read()
                                                if suc_video:
                                                    out.write(frame)
                                                    out.write(frame_video)
                                                else:
                                                    out.write(frame)

                                                x = 0
                                                g = 0

                                                # curTime = self.strCurTimeMs()
                                                #
                                                # nameImg = pathCamFolderImgWrt + '/' + curTime + '.png'

                                                if (globalValues.debugStrg == False):

                                                    curTime = self.strCurTimeMs()

                                                    # print(globalValsSBV.numEvent[valGlobal])
                                                    if (globalValues.numEvent[valGlobal] == 1 and checkDelOld):
                                                            print('checkingGlobalEvent: ' + str(valGlobal) + str(globalValues.numEvent))
                                                            firstNumImg = True
                                                            self.numberStartImg = 0
                                                            globalValues.numEvent[valGlobal] = 2
                                                            checkDelOld = False
                                                            start_time_wrt_frm = round(time.time() * 100)

                                                            curDate = self.strCurDate()

                                                            if (curDate != curDateOld):
                                                                pathWriteEventsFolderDate = pathWriteEvents + '/' + curDate
                                                                self.checkFolderPath(pathWriteEventsFolderDate, False)
                                                                # self.pathImgEventsFolderDate = pathImgEvents + '/' + curDate
                                                                # self.checkFolderPath(self.pathImgEventsFolderDate, False)

                                                            # pathImgEventCur = self.pathImgEventsFolderDate + '/' + curTime[0:8] + '.bmp'
                                                            #
                                                            # # print('SaveImgFrm!!! : ' + str(pathImgEventCur))
                                                            # # print(frame)
                                                            #
                                                            # rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                                                            # h, w, ch = rgbImage.shape
                                                            # bytesPerLine = ch * w
                                                            # imgQt = QtGui.QImage(rgbImage.data, w, h, bytesPerLine,
                                                            #                QtGui.QImage.Format_RGB888)
                                                            # # pixCam = QtGui.QPixmap(imgQt)
                                                            # imgQt.save(pathImgEventCur)
                                                            # global pathFileEvent
                                                            pathFileEvent = pathWriteEventsFolderDate + '/' + globalValues.numTalonVideo + '_' + globalValues.numGRZVideo + '.mp4'

                                                            print('StartingEvent!!!')
                                                            print(pathFileEvent)
                                                            globalValues.numThreadVideo += 1
                                                            count = 0
                                                            for filename in glob.glob(pathCamFolderImgWrt + '/*.jpg'):
                                                                count += 1
                                                            self.numImgSub = count
                                                            print('NumberSub: ' + str(self.numImgSub))

                                                            strDataInJournal = 'Выполнен запуск формирования записи события канала ' + nameChannel
                                                            globalValues.writeEventToDBJournalMain('Камеры', strDataInJournal)

                                                    else:
                                                        if (globalValues.numEvent[valGlobal] == 1 and checkDelOld == False):

                                                                if (curDate != curDateOld):
                                                                    pathWriteEventsFolderDate = pathWriteEvents + '/' + curDate
                                                                    self.checkFolderPath(pathWriteEventsFolderDate, False)

                                                                pathFileEvent = pathWriteEventsFolderDate + '/' + globalValues.numTalonVideo + '_' + globalValues.numGRZVideo + '.mp4'

                                                                checkWriteFileEvent = True
                                                                globalValues.numThreadVideo += 1


                                                                # curDate = self.strCurDate()
                                                                #
                                                                # if (curDate != curDateOld):
                                                                #     self.pathImgEventsFolderDate = self.pathImgEvents + '/' + curDate
                                                                #     self.checkFolderPath(self.pathImgEventsFolderDate, False)
                                                                #
                                                                # pathImgEventCur = self.pathImgEventsFolderDate + '/' + curTime[0:8] + '.bmp'
                                                                #
                                                                # rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                                                                # h, w, ch = rgbImage.shape
                                                                # bytesPerLine = ch * w
                                                                # imgQt = QtGui.QImage(rgbImage.data, w, h, bytesPerLine,
                                                                #                      QtGui.QImage.Format_RGB888)
                                                                # # pixCam = QtGui.QPixmap(imgQt)
                                                                # imgQt.save(pathImgEventCur)

                                                                print('SecondStart!!!')

                                                    nameImg = pathCamFolderImgWrt + '/' + curTime + '.jpg'

                                                    suc_img, frame_img = cap.read()

                                                    if suc_img:
                                                        cv2.imwrite(nameImg, frame_img)

                                                        numberImg += 1

                                                        if (checkDelOld):
                                                            # print('CheckingDel!!!')
                                                            for el in glob.glob(pathCamFolderImgWrt + '/*.jpg'):
                                                                os.remove(os.path.join(pathCamFolderImgWrt, el))
                                                                break

                                                    else:
                                                        cv2.imwrite(nameImg, frame)
                                                        print('checking!!!')
                                                        numberImg += 1

                                                        if (checkDelOld):
                                                            # print('CheckingDel!!!')
                                                            for el in glob.glob(pathCamFolderImgWrt + '/*.jpg'):
                                                                os.remove(os.path.join(pathCamFolderImgWrt, el))
                                                                break

                                                    if (abs (round(time.time()*100) - start_time_wrt_frm) >= (globalValues.timeWriteEvent*100 - delta_time) or checkWriteFileEvent):

                                                        start_time_delta = round(time.time() * 100)

                                                        if (globalValues.numEvent[valGlobal] == 0):
                                                            checkDelOld = True

                                                        listPathElFrm = []
                                                        for filename in glob.glob(pathCamFolderImgWrt + '/*.jpg'):
                                                            listPathElFrm.append(os.path.join(pathCamFolderImgWrt, filename))

                                                        listPathElFrm.sort(key=self.sortByLength)

                                                        newListFrms = []

                                                        countList = len(listPathElFrm)


                                                        if (globalValues.numEvent[valGlobal] == 2 or checkWriteFileEvent):
                                                            globalValues.listPathVideoCreate = []

                                                            if (checkWriteFileEvent):
                                                                globalValues.numEvent[valGlobal] = 2
                                                                if (firstNumImg):
                                                                    firstNumImg = False
                                                                    print('Number imgs to Save: ' + str(countList))
                                                                    for i in range(0, countList, 1):
                                                                        globalValues.listPathVideoCreate.append(listPathElFrm[i])
                                                                    self.numberStartImg = countList
                                                                    self.numImgSub = int((self.numberStartImg + self.numImgSub)/2)
                                                                    print('NumberSub: ' + str(self.numImgSub))
                                                                else:
                                                                    print('Number start: ' + str(self.numberStartImg))
                                                                    print(countList)
                                                                    for i in range(self.numImgSub, countList, 1):
                                                                        globalValues.listPathVideoCreate.append(listPathElFrm[i])

                                                                    self.numImgSub =int((self.numberStartImg + countList)/2)
                                                                    self.numberStartImg = countList



                                                            else:
                                                                if (self.numberStartImg != 0):
                                                                    for i in range(self.numImgSub, countList, 1):
                                                                        globalValues.listPathVideoCreate.append(listPathElFrm[i])
                                                                    self.numImgSub = int((self.numberStartImg + countList) / 2)
                                                                    self.numberStartImg = countList
                                                                else:
                                                                    for i in range(0, countList, 1):
                                                                        globalValues.listPathVideoCreate.append(listPathElFrm[i])

                                                            print(len(globalValues.listPathVideoCreate))

                                                            pathWriteEventsFolderDate = pathWriteEvents + '/' + curDate
                                                            self.checkFolderPath(pathWriteEventsFolderDate, False)

                                                            print('fwefwefewf')
                                                            print(pathWriteEvents)

                                                            print(rtsp_link)
                                                            print(nameChannel)
                                                            print(valGlobal)
                                                            # global pathFileEvent
                                                            # global pathFileEvent
                                                            pathFileEventNew = pathFileEvent
                                                            print(pathFileEventNew)
                                                            th_create_video = threading.Thread(target=self.createVideoEvent, args=(strIP, pathFileEventNew, globalValues.listPathVideoCreate, valGlobal, ))
                                                            th_create_video.start()

                                                            if (checkWriteFileEvent):
                                                                curTime = self.strCurTimeMs()

                                                                curDate = self.strCurDate()

                                                                if (curDate != curDateOld):
                                                                    self.pathWriteEventsFolderDate = self.pathWriteEvents + '/' + curDate
                                                                    self.checkFolderPath(self.pathWriteEventsFolderDate, False)
                                                                pathFileEvent = pathWriteEventsFolderDate + '/' + globalValues.numTalonVideo + '_' + globalValues.numGRZVideo + '.mp4'

                                                            print('startingthread!!!')

                                                            # numCheckWrt = 0
                                                            #
                                                            # img_array = []
                                                            #
                                                            # for filename in listPathElFrm:
                                                            #     img = cv2.imread(filename)
                                                            #     height, width, layers = img.shape
                                                            #     size = (width, height)
                                                            #     img_array.append(img)
                                                            #
                                                            # out_video = cv2.VideoWriter(globalValsSBV.pathToSaveFile, cv2.VideoWriter_fourcc(*'mp4v'), 15.9, size)
                                                            #
                                                            # for i in range(len(img_array)):
                                                            #     out_video.write(img_array[i])
                                                            #
                                                            # out_video.release()
                                                            #
                                                            # print('SaveVideoEvent')
                                                            #
                                                            # for i in range(numberImgOld):
                                                            #     if (os.path.exists(listPathElFrm[i])):
                                                            #         os.remove(listPathElFrm[i])
                                                            #         countList -= 1
                                                            #
                                                            # numberImg = countList


                                                        numberImgOld = numberImg

                                                        print('CountList: ' + str(countList))
                                                        print('NumberImgs: ' + str(numberImg))
                                                        if (countList != numberImg and countList > (numberImg + 50) and globalValues.numEvent[valGlobal] == 0):
                                                            valRng = abs(countList - numberImg)
                                                            for i in range(valRng):
                                                                path = listPathElFrm[i]
                                                                if (os.path.exists(path)):
                                                                    os.remove(path)

                                                        numberImg = 0
                                                        delta_time = abs(round(time.time() * 100) - start_time_delta)
                                                        print('DeltaTime: ' + str(delta_time))
                                                        checkWriteFileEvent = False
                                                        start_time_wrt_frm = round(time.time()*100)

                                            if (ret == False):
                                                z += 1

                                            else:
                                                z = 0
                                                start_time_check = round(time.time() * 100)

                                            if (z > 0):
                                                print('ExitCam!!!!')
                                                # print(abs(round(time.time()*100) - start_time_check))
                                                break

                                            if (abs(round(time.time()) - time_start_pr) >= delta):
                                                # print(delta)
                                                checkGoodWrite = True
                                                break

                                            if (abs(round(time.time()*100) - start_time_clear_cache) > 15000):
                                                # caching.clear_cache()
                                                gc.collect()
                                                # print('Checking Clear!!!')
                                                start_time_clear_cache = round(time.time()*100)

                                if (checkGoodWrite):

                                    out.release()

                                    end_time_wr = self.strCurTime()

                                    self.pathFolderWritingCamDate = pathStorage + '/' + curDate
                                    pathFolderTheCam = self.pathFolderWritingCamDate
                                    self.checkFolderPath(pathFolderTheCam, False)

                                    nameFileCreate = start_time_wr + '-' + end_time_wr
                                    pathFileCreate = pathFolderTheCam + '/' + nameFileCreate + '.mp4'

                                    th_convert_video = threading.Thread(target=self.copyFileandRemoveOld, args=(pathFileWrite, pathFileCreate, strIP,))

                                    th_convert_video.start()

                                    if (cap.isOpened() == False):
                                        break

                                if (abs(round(time.time()*100) - start_time_check) > 0 and checkGoodWrite == False):
                                    dataInLog = 'Ошибка записи видео в камеру: '
                                    globalValues.writeLogDataTh(dataInLog, strIP, strIP)
                                    checkOut = True
                                    break

                                x += 1

                            if (checkOut):
                                break

                    else:
                        globalValues.writeLogDataTh('Ошибка подключения к камере' + strIP, '. Попытка: ' + str(g), strIP)
                    if (g > 5):
                        globalValues.writeLogDataTh('Ошибка потока, камера недоступна, запись остановлена: ', strIP, strIP)
                        # time.sleep(2)
                        break

                    g += 1

                    cap.release()

                except Exception as ex:
                    globalValues.writeLogDataTh('Функция записи видеопотока' + strIP, str(ex), strIP)
                    globalValues.checkCamStrg[numCam] = False

            strDataInJournal = 'Выполнена остановка записи канала ' + nameChannel
            globalValues.writeEventToDBJournalMain('Камеры', strDataInJournal)

        except Exception as ex:
            globalValues.writeLogDataTh('Функция записи видео' + strIP, str(ex), strIP)
            globalValues.checkCamStrg[numCam] = False

    def ping(self, host):
        """
        Returns True if host (str) responds to a ping request.
        Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
        """

        # Option for the number of packets as a function of
        param = '-c'

        # Building the command. Ex: "ping -c 1 google.com"
        command = ['ping', param, '1', host]

        return subprocess.call(command) == 0

    def checkCamInNetwork(self, strIps):
                checkGoodIp = False
                # strIp = '192.168.0.88'
                strIpHTTP = 'http://' + strIps
                # print(strIpHTTP)
                start_time = round(time.time())
                try:
                    dataPing = self.ping(strIps)
                except Exception as ex:
                    return checkGoodIp
                if (str(dataPing) == 'False'):
                    checkGoodIp = False
                    return checkGoodIp
                    # print(abs(round(time.time()) - start_time))
                else:
                    try:
                        # print('goodping')
                        data = requests.head(strIpHTTP, verify=False, timeout=4)

                        checkGoodIp = True
                        # print('Good opening: ' + strIps)
                        return checkGoodIp
                        # print(abs(round(time.time()) - start_time))
                    except Exception as ex:
                        checkGoodIp = False
                        return checkGoodIp
                        # print(abs(round(time.time()) - start_time))

    def thPingIps(self, strIP, rtsp, name_chl, num_chl):
        if (self.checkCamInNetwork(strIP)):
            self.listCheckIP.append(strIP)
            self.listCheckRtsp.append(rtsp)
            self.listNameChls.append(name_chl)
            self.listNumChl.append(num_chl)
            self.isListCams.append(True)
        else:
            self.isListCams.append(False)
            self.listBadCams.append(strIP)

    def runThreads(self, poolIps, poolRtsp, delta, pathStorage, pathDefFolder, listNameChannels, lstNum):
        try:
            k = 0
            for curIP in poolIps:
                nameChannel = listNameChannels[k]
                curRtsp = poolRtsp[k]
                numCam = lstNum[k]
                valGlobal = numCam
                th_main = threading.Thread(target=self.thMainLoopWriterCam,
                                           args=(curIP, curRtsp, delta, pathStorage, pathDefFolder, valGlobal, nameChannel, numCam, ))
                th_main.start()

                time.sleep(0.5)
                k += 1

        except Exception as ex:
            globalValues.writeLogData('Запуск камер для записи видеопотоков', str(ex))

    def strCurTime(self):
        str_cur_time = str(datetime.datetime.time(datetime.datetime.now()))
        len_cur_time = len(str_cur_time)
        str_cur_time = str_cur_time[0: (len_cur_time - 7)]
        str_cur_time = str_cur_time.replace(':', '.')
        return str_cur_time

    def strCurTimeMs(self):
        str_cur_time = str(datetime.datetime.time(datetime.datetime.now()))
        len_cur_time = len(str_cur_time)
        str_cur_time = str_cur_time[0: (len_cur_time - 3)]
        str_cur_time = str_cur_time.replace(':', '.')
        return str_cur_time

    def strCurDate(self):
        dateToday = datetime.date.today().strftime('%d.%m.%Y')
        str_date_today = str(dateToday)
        return str_date_today

    def checkFolderLongPath(self, pathFolder):
        try:
            i = 0
            listPath = []
            for element in pathFolder:
                if (element == '/' and i != 0):
                    listPath.append(pathFolder[0:i])
                i += 1
            # listPath = pathFolder.split('/')
            # listPath.pop(0)
            listPath.append(pathFolder)

            print(listPath)

            for elPath in listPath:
                if (os.path.exists(elPath) == False):
                    try:
                        os.mkdir(elPath)
                    except Exception as ex:
                        globalValues.writeLogData('Функция проверки и создания папки хранилища', str(ex))

        except Exception as ex:
            globalValues.writeLogData('Функция проверки ссылки на папку хранилища', str(ex))

    def checkFolderPath(self, pathFolder, isHide):
        try:

            if (os.path.exists(pathFolder) == False):
                try:
                    os.mkdir(pathFolder)
                    # if (isHide):
                    #     subprocess.call(['attrib', '+H', pathFolder])
                    return False
                except Exception as ex:
                    globalValues.writeLogData('Функция проверки и создания папки хранилища', str(ex))
            else:
                return True

        except Exception as ex:
            globalValues.writeLogData('Функция проверки ссылки на текущую папку записи', str(ex))

    def sortByLength(self, inputStr):
        return len(inputStr)

    def createVideoEvent(self, strIP, pathFile, listPathImgs, valGlobal):
        try:

            img_array = []

            for filename in listPathImgs:
                img = cv2.imread(filename)
                height, width, layers = img.shape
                size = (width, height)
                img_array.append(img)

            print(len(img_array))


            out_video = cv2.VideoWriter(pathFile, cv2.VideoWriter_fourcc(*'mp4v'), 15.9, size)

            out_video.set(cv2.CAP_PROP_BUFFERSIZE, 3)

            for i in range(len(img_array)):
                out_video.write(img_array[i])

            out_video.release()

            print('SaveVideoEvent')

            globalValues.numThreadVideo -= 1

            print('NumberThread: ' + str(globalValues.numThreadVideo))

            if (globalValues.numThreadVideo <= 0):
                globalValues.numEvent[valGlobal] = 0
                self.numImgSub = 0
                self.numberStartImg = 0

        except Exception as ex:
            globalValues.writeLogDataTh('Функция создания видео в отдельном потоке', str(ex), strIP)
            globalValues.numEvent[valGlobal] = 0

    def checkStrgAndRmv(self, pathStrg, strIP):

        try:

            strDate = self.strCurDate()
            # print(strDate)
            # print(pathStrg)
            # print(self.firstCheckStrg)
            if (strDate != globalValues.curDate or self.firstCheckStrg):

                # print('qweqweqwewqe')
                self.firstCheckStrg = False

                lstFldrInStrg = os.listdir(pathStrg)
                # print(lstFldrInStrg)
                k = 0


                # print(len(lstFldrInStrg))
                lstFldrs = []
                for elList in lstFldrInStrg:
                    x = '.' in elList
                    # print(elList)
                    if (x and len(elList) == 10):
                        lstFldrs.append(elList)
                        k += 1
                    # print(k)
                print(lstFldrs)
                # print(k)
                if (k > globalValues.numberFolderDateSave):
                        listValEl = []
                        # print('asd')
                        date = []
                        month = []
                        year = []
                        for el in lstFldrs:
                            el = el.replace('.', '')
                            date.append(int(el[0:2]))
                            month.append(int(el[2:4]))
                            year.append(int(el[4:8]))
                        i = 0
                        # print(date)
                        # print(month)
                        # print(year)
                        minDate = 999
                        minMonth = 999
                        minYear = 999999
                        z = []
                        for el in year:
                            if (el == minYear):
                                z.append(i)
                            else:
                                if (el < minYear):
                                    z = []
                                    minYear = el
                                    z.append(i)
                            i += 1
                        # print(minYear)
                        # print(z)
                        lst = []
                        dateNew = []
                        for iter in z:
                            lst.append(month[iter])
                            dateNew.append(date[iter])
                        # print(lst)

                        z = []
                        i = 0
                        l = 0
                        for el in lst:
                            if (el == minMonth):
                                z.append(i)
                            else:
                                if (el < minMonth and i == 0):
                                    l = i
                                if (el < minMonth):
                                    z = []
                                    minMonth = el
                                    z.append(i)
                            i += 1
                        lst = []
                        # print(lstFldrs)
                        # print(z)
                        for iter in z:
                            lst.append(dateNew[iter])
                        # print(minMonth)
                        # print(lst)

                        z = []
                        i = 0
                        k = 0
                        for el in lst:
                            if (el == minDate):
                                z.append(i)
                            else:
                                if (el < minDate):
                                    z = []
                                    minDate = el
                                    z.append(i)
                                    k = i
                            i += 1

                        strDate = str(minDate)
                        if (len(strDate) < 2):
                            strDate = '0' + strDate
                        strMonth = str(minMonth)
                        if (len(strMonth) < 2):
                            strMonth = '0' + strMonth
                        strYear = str(minYear)
                        if (len(strYear) < 2):
                            strYear = '0' + strYear

                        nameFldr = strDate + '.' + strMonth + '.' + strYear

                        # print(nameFldr)

                        pathRmDir = pathStrg + '/' + nameFldr

                        print('PathDataDel: ', pathRmDir)

                        try:
                            shutil.rmtree(pathRmDir)
                            globalValues.curDate = strDate
                        except Exception as ex:
                            globalValues.writeLogDataTh('Удаление старых записей', str(ex), strIP)


        except Exception as ex:
            globalValues.writeLogData('Функция проверки и удаления данных архивка', str(ex))

    def delEmptyFldr(self, pathFldr):
        try:
            checkFldr = True

            lstPath = []
            lstPath.append(pathFldr)
            i = 0

            pathDefault = pathFldr

            while checkFldr:
                lstData = lstPath
                lstPath = []
                # if (i != 0):
                #     lstPath = []
                lengthFldr = len(lstData)
                # print(lengthFldr)
                if (lengthFldr == 0):
                    break
                for el in lstData:
                    if (os.path.isfile(el) == False):
                        lstDataIn = os.listdir(el)
                        if (len(lstDataIn) == 0):
                            shutil.rmtree(el)
                        for el_in in lstDataIn:
                            lstPath.append(el + '/' + el_in)
                # print(lstPath)
                # print(lengthFldr)

                i += 1
                # break

        except Exception as ex:
            globalValues.writeLogData('Функция удаления папок без файлов', str(ex))

# rtsp_link_beward = 'rtsp://admin:admin@strIP:554/av0_1'
# rtsp_link_novicam = 'rtsp://strIP:554/user=admin&password=admin&channel=1&stream=0.sdp'
# rtsp_link_axis = 'rtsp://root:root@strIP/axis-media/media.amp'
# rtsp_link_beward_ip_cam = 'rtsp://admin:admin123@strIP:554'
# sleepOpenCam = 0

def startingWritingCams(pathStorage, pathDefFolder, delta, listRtsp, listIp, lstNameChl, listNum):

    try:
        obVideo = WorkingWithVideo()

        obVideo.checkFolderPath(pathDefFolder, True)
        globalValues.curPathFolderToWrite = pathDefFolder

        #rm Files in defFolder
        listPath = os.listdir(pathDefFolder)
        for el in listPath:
            pathRm = os.path.join(pathDefFolder, el)
            if (os.path.isfile(pathRm)):
                os.remove(pathRm)
            else:
                try:
                    passwd = globalValues.passwdLogin
                    print('checkPathDel: ', pathRm)
                    os.system('rm -r ' + pathRm + '/')
                    # shutil.rmtree(pathRm)
                except Exception as ex:
                    globalValues.writeLogData('Функция удаления дефолтных данных записи', str(ex))
        #create Folder to Write
        # curDate = obVideo.strCurDate()
        # pathFolder = pathStorage + '/' + curDate
        # obVideo.checkFolderPath(pathFolder, False)

        obVideo.listNumChl = []
        obVideo.listNameChls = []
        obVideo.listCheckIP = []
        obVideo.listCheckRtsp = []

        m = 0
        for curIP in listIp:
            th_ping_ip = threading.Thread(target=obVideo.thPingIps, args=(curIP, listRtsp[m], lstNameChl[m], listNum[m]))
            th_ping_ip.start()
            m += 1

        start_time = round(time.time() * 100)
        countListIP = len(listIp)
        while True:

            if (len(obVideo.isListCams) == countListIP):
                print('Exit!!!')
                break

            if (abs(round(time.time() * 100) - start_time) > 400):
                break

        if (len(obVideo.listCheckIP) != 0):

            # numCams = 4
            listIP_end = obVideo.listCheckIP
            listRtsp_end = obVideo.listCheckRtsp
            listNameChl_end = obVideo.listNameChls
            listNumChl_end = obVideo.listNumChl


            lengthList = len(listIP_end)
            # allProcess = []

            pathCheck = globalValues.curDisk + '/ACMK/VideoEvents'
            if (os.path.exists(pathCheck)):
                obVideo.delEmptyFldr(pathCheck)

            z = 0
            try:
                # for j in range(lengthList):
                    # if ((j % numCams == 0 and j != 0) or (j == lengthList - 1)):
                    #     poolIPs = []
                    #     poolRtsp = []
                    #     if (j == lengthList - 1):
                    #         stopVal = len(listIP)
                    #     else:
                    #         stopVal = j
                    #     print(z)
                    #     print(stopVal)
                    #     for i in range(z, stopVal, 1):
                    #         poolIPs.append(listIP[i])
                    #         poolRtsp.append(listRtsp[i])
                    #     z = j
                        print('startStrgThread!!!')
                        print(delta)
                        print(pathStorage)
                        print(listIP_end)
                        print(listRtsp_end)
                        print(listNameChl_end)
                        print(listNumChl_end)
                        # process = Process(target=obVideo.runThreads, args=(poolIPs, poolRtsp, delta, pathStorage, pathDefFolder, lstNameChl, listNum, ))
                        # allProcess.append(process)
                        # process.start()
                        th_cams = threading.Thread(target=obVideo.runThreads, args=(listIP_end, listRtsp_end, delta, pathStorage, pathDefFolder, listNameChl_end, listNumChl_end, ))
                        th_cams.start()

                # for p in allProcess:
                #     p.join()
            except Exception as ex:
                globalValues.writeLogData('Функция создания процессов', str(ex))

    except Exception as ex:
        globalValues.writeLogData('Функция запуска записи камер', str(ex))


# if __name__== '__main__':
    # listRtsp = ['rtsp://192.168.1.88:554/user=admin&password=admin&channel=1&stream=0.sdp']
    # listIp = ['192.168.1.88']
    #
    # pathDefFolder = globalValsSBV.curDisk + ':/Sinaps'
    # delta = globalValsSBV.deltaWriting
    # pathStorage = globalValsSBV.curDisk + ':/Storage'
    #
    # startingWritingCams(pathStorage, pathDefFolder, delta, listRtsp, listIp)












