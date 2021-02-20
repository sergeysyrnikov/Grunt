import pyrealsense2 as rs
import numpy as np
import cv2
import time
# import mayavi.mlab as mlab
# import scipy.ndimage as ndimage
import globalValues
import scipy.spatial as ss
# import pylab
import os
import datetime

class MeasureVol:

    pathImgRedCom = globalValues.pathImage + 'iconredkrug4141.png'

    pathImgGreenCom = globalValues.pathImage + 'icongreenkrug4141.png'

    pipeline = rs.pipeline()  # <- Объект pipeline содержит методы для взаимодействия с потоком

    global profile

    statusCam = 99

    # def __init__(self):
    #     super().__init__()
        # self.initCam()
        # self.runCam()

    def runCam(self, obj, btn):
        try:
            i = 0
            time_start = round(time.time() * 100)
            while i < 1:

                if (globalValues.stopAll):
                    break

                if (abs(round(time.time() * 100) - time_start) > 250):

                    try:

                        btn.setEnabled(False)
                        globalValues.stateScaner = False

                        print('StartRS!')
                        pipeline = rs.pipeline()  # <- Объект pipeline содержит методы для взаимодействия с потоком
                        config = rs.config()  # <- Дополнительный объект для хранения настроек потока
                        colorizer = rs.colorizer()  # <- Пригодится для отрисовки цветной карты глубины

                        # Инициализируем модель
                        # model = cv.dnn.readNetFromTensorflow("E:/RS/model.pb", "graph.pbtxt")

                        # Resnet50v1
                        # model = cv.dnn.readNetFromTensorflow("E:/neuroForRS/resnet50/model.pb", "E:/neuroForRS/resnet50/graph.pbtxt")

                        # v2_coco
                        # model = cv.dnn.readNetFromTensorflow("E:/neuroForRS/v2_coco/model.pb", "E:/neuroForRS/v2_coco/graph.pbtxt")

                        # v2_coco_2
                        # model = cv.dnn.readNetFromTensorflow("E:/neuroForRS/v2_coco_2/model.pb", "E:/neuroForRS/v2_coco_2/graph.pbtxt")
                        config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
                        global profile
                        profile = self.pipeline.start(config)

                        print('YesGood!!!')

                        time.sleep(0.25)

                        start_time = round(time.time() * 100)
                        check = True
                        # check = False

                        num_circle = 0


                        height_frm = 0
                        width_frm = 0
                        checkExit = False

                        is_measure_vol = False

                        globalValues.delta_time = 0

                        # print('123123')

                        globalValues.stateScaner = True

                        obj.setStyleSheet(
                            'QLabel:!hover {background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));\n'
                            'image: url(' + self.pathImgGreenCom + ');};')

                        btn.setEnabled(False)

                        while True:
                            # Ждем захват фреймов для "цвета" и "глубины"
                            frames = self.pipeline.wait_for_frames()
                            depth_frame = frames.get_depth_frame()
                            # color_frame = frames.get_color_frame()
                            # if not depth_frame or not color_frame:
                            if not depth_frame:
                                continue

                            # Конвертируем фреймы в numpy-массивы
                            depth_image = np.asanyarray(depth_frame.get_data())
                            # color_image = np.asanyarray(color_frame.get_data())

                            # Обнаружение объектов
                            # model.setInput(cv.dnn.blobFromImage(color_image, size=(300, 300), swapRB=True, crop=False))
                            # pred = model.forward()
                            # draw_predictions(pred, color_image, depth_image)

                            # Переводим изображение глубины в цвет
                            colorized_depth = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

                            # Выйти при нажатии 'ESC' или 'q'
                            key = cv2.waitKey(1) & 0xFF

                            if ((key == 27) or (key == ord('q')) or globalValues.stopAll):
                                cv2.destroyAllWindows()
                                self.pipeline.stop()
                                break

                            if checkExit:
                                cv2.destroyAllWindows()
                                self.pipeline.stop()
                                break

                            if (abs(round(time.time() * 100) - start_time) > 500 and globalValues.is_read_depth):

                                num_circle += 1

                                zv = depth_image

                                if (num_circle == 1):

                                    depth_sum = []

                                    height_frm = len(depth_image)
                                    width_frm = 0
                                    for el in depth_image:
                                        width_frm = len(el)
                                        # print(el)
                                        break
                                    for i in range(height_frm):
                                        lst_ = []
                                        for j in range(width_frm):
                                            lst_.append(0)
                                        depth_sum.append(lst_)

                                val_ = 0

                                for i in range(height_frm):
                                    for j in range(width_frm):

                                        if (zv[i][j] > globalValues.maxDist):
                                            zv[i][j] = val_

                                        if (globalValues.deltaFrame < i < height_frm - globalValues.deltaFrame) and (
                                                globalValues.deltaFrame < j < width_frm - globalValues.deltaFrame):
                                            if (zv[i][j] < 100):
                                                zv[i][j] = val_

                                        val_ = zv[i][j]

                                depth_sum = depth_sum + zv

                                if (num_circle >= globalValues.numberFrameForDepth):

                                    lst_x = []
                                    lst_y = []
                                    i = 0
                                    for i in range(height_frm):
                                        data = []
                                        k = 0
                                        for j in range(width_frm):
                                            data.append(k)
                                            k += 1
                                        lst_x.append(data)

                                    xv = lst_x

                                    k = 0
                                    for i in range(height_frm):
                                        data = []
                                        for j in range(width_frm):
                                            data.append(k)
                                        lst_y.append(data)
                                        k += 1

                                    yv = lst_y

                                    depth_sum = depth_sum / globalValues.numberFrameForDepth

                                    print('GoodCreateDepth!')
                                    # print('TimeInWork: ' + str(abs(round(time.time() * 100) - start_time - 500)))

                                    # blurred = ndimage.gaussian_filter(depth_image, sigma=(3, 3), order=0)
                                    #
                                    # print(blurred)
                                    #
                                    # w = np.arctan(mat / 100)
                                    # print(w)

                                    # Построение 3D модели

                                    # s = mlab.mesh(xv, yv, depth_sum)

                                    # alpha = 30  # degrees
                                    # mlab.view(azimuth=0, elevation=90, roll=-90 + alpha)

                                    # mlab.show()

                                    pathFolder = globalValues.pathNpArr + self.strCurDate() + '/'
                                    self.checkFolderLongPath(pathFolder)

                                    nameNpzAll = ''

                                    if (globalValues.debugVolume):
                                        nameNpzAll = pathFolder + self.strCurTime() + '.npz'
                                    else:
                                        nameNpzAll = pathFolder + str(globalValues.curTalon) + '_all.npz'

                                    np.savez_compressed(nameNpzAll, xv=xv, yv=yv, zv=depth_sum)

                                    check = False

                                    start_time = round(time.time() * 100)

                                    # cv2.imwrite(globalValues.nameImgGrunt, colorized_depth)

                                    # checkExit = True

                                    num_circle = 0

                                    is_measure_vol = True

                            if is_measure_vol:

                                pathImg = ''
                                nameNpz = ''

                                pathFolder = globalValues.pathNpArr + self.strCurDate() + '/'
                                self.checkFolderLongPath(pathFolder)

                                if (globalValues.debugVolume):
                                    pathImg = pathFolder + self.strCurTime() + '.png'
                                    nameNpz = pathFolder + self.strCurTime()
                                else:
                                    pathImg = pathFolder + str(globalValues.curTalon) + '.png'
                                    nameNpz = pathFolder + str(globalValues.curTalon)

                                depth_area = self.findRect(depth_sum, colorized_depth, globalValues.disMeasure - globalValues.deltaDis,
                                                      globalValues.disMeasure + globalValues.deltaDis, pathImg)

                                self.createBox(depth_area, nameNpz)

                                is_measure_vol = False

                                globalValues.is_read_depth = False

                        print('Ending thread measuring!')

                    except Exception as ex:
                        globalValues.writeLogData('Создание карты глубины', str(ex))

                    time_start = round(time.time() * 100)

                    i += 1

                time.sleep(0.15)

            print('Not connection cam RS!')

            globalValues.stateScaner = False

            obj.setStyleSheet(
                                        'QLabel:!hover {background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));\n'
                                        'image: url(' + self.pathImgRedCom + ');};')

            btn.setEnabled(True)

            self.pipeline.stop()



            globalValues.delta_time = 0
        except Exception as ex:
            print('StopChecking!')
            globalValues.writeLogData('Не удаётся подключиться к камере глубины. ', str(ex))

    def findRect(self, depth, img, min_val, max_val, pathImg):
        try:
            # data = np.load(globalValues.nameNpz, allow_pickle=False)
            #
            # depth = data['zv']
            z = 0
            z_col = 0
            height = len(depth)
            width = 0
            # print(height)

            num_y = []
            num_x = []
            str_data_y = ''
            str_data_x = ''
            num_true_x = 0

            for i in depth:
                arr = []
                z_col = 0
                arr.append(z)
                num_true = 0
                for j in i:
                    width = len(i)

                    str_data_y += str(z) + ' : ' + str(j) + '\n'
                    # print(z)
                    if ((min_val < j < max_val) and (
                            globalValues.deltaFrame < z < int(height) - globalValues.deltaFrame)):
                        num_true += 1
                    z_col += 1
                if (num_true > globalValues.numRepeat):
                    arr.append(num_true)
                    num_y.append(arr)
                z += 1

            k_ = 0
            for i in range(z_col):
                num_true_x = 0
                arr = []
                arr.append(k_)
                for j in range(z):

                    str_data_x += str(k_) + ' : ' + str(depth[j][i]) + '\n'

                    if ((min_val < depth[j][i] < max_val) and (
                            globalValues.deltaFrameX < i < int(width) - globalValues.deltaFrameX)):
                        num_true_x += 1
                if (num_true_x > globalValues.numRepeat_x):
                    arr.append(num_true_x)
                    num_x.append(arr)
                k_ += 1

            # f = open('data_x.txt', 'w')
            # f.write(str_data_x)
            # f.close()
            #
            # f = open('data_y.txt', 'w')
            # f.write(str_data_y)
            # f.close()

            # print(len(num_y))
            y_down = num_y[len(num_y) - 1][0]
            y_high = num_y[0][0]
            x_right = num_x[len(num_x) - 1][0]
            x_left = num_x[0][0]

            frame = img

            cv2.line(frame, (0, y_high), (640, y_high), (0, 0, 255), 2)

            cv2.line(frame, (x_left, 0), (x_left, 480), (0, 0, 255), 2)
            cv2.line(frame, (x_right, 0), (x_right, 480), (0, 0, 255), 2)

            # height_pix = abs(y_high - y_down)
            width_pix = abs(x_right - x_left)

            # print(height_pix)
            print(width_pix)

            coef_width = width_pix / globalValues.width_obj

            print('Coeff: ' + str(coef_width))

            y_down = int(y_high + (globalValues.height_obj * coef_width))

            cv2.line(frame, (0, y_down), (640, y_down), (0, 0, 255), 2)


            cv2.imwrite(pathImg, frame)

            # frame_line = cv2.imread('img.png')

            # k = 20
            # while (k < height):
            #     cv2.line(frame_line, (0, k), (width, k), (0, 0, 255), 2)
            #     cv2.putText(frame_line, str(k), (10, k - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 255), 1)
            #     k += 20
            #
            # k = 30
            # while (k < width):
            #     cv2.line(frame_line, (k, 0), (k, height), (0, 0, 255), 2)
            #     cv2.putText(frame_line, str(k), (k + 5, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (0, 255, 255), 1)
            #     k += 30
            #
            # cv2.imwrite('imgLinesAll.png', frame_line)

            # height_pix = abs(y_high - y_down)

            # print(y_high)
            # print(y_down)
            # print(x_left)
            # print(x_right)

            depth_box_arr = []

            for i in range(y_high, y_down, 1):
                arr = []
                for j in range(x_left, x_right, 1):
                    arr.append(depth[i][j])
                depth_box_arr.append(arr)

            length_x = len(depth_box_arr)
            for el in depth_box_arr:
                length_y = len(el)
                break
            return depth_box_arr

        except Exception as ex:
            globalValues.writeLogData('Функция поиска контура', str(ex))

    def createBox(self, depth, nameNpz):
        try:

            width = 0
            for el in depth:
                width = len(el)
                break
            height = len(depth)

            print('Width_start: ' + str(width))
            print('Height_start: ' + str(height))

            delta = globalValues.delta_find_edge

            delta_search = globalValues.delta_search

            delta_depth = globalValues.delta_depth

            val_y_high = 0

            for i in range(0, delta_search):
                for j in range(delta, width - delta, 1):
                    if (depth[i][j] > (globalValues.disMeasure + delta_depth) or depth[i][j] < (
                            globalValues.disMeasure - delta_depth)):
                        if (i >= val_y_high):
                            val_y_high = i

            val_down_y = height
            for i in range(height - 1, height - delta_search, -1):

                for j in range(delta, width - delta, 1):
                    # print(j)
                    if (depth[i][j] > (globalValues.disMeasure + delta_depth) or depth[i][j] < (
                            globalValues.disMeasure - delta_depth)):
                        # print('sergio: ' + str(depth[i][j]))
                        if i <= val_down_y:
                            val_down_y = i

            depth_new = []

            for i in range(val_y_high, val_down_y):
                arr = []
                for j in range(width):
                    arr.append(depth[i][j])
                depth_new.append(arr)
            #

            height = len(depth_new)

            for el in depth_new:
                width = len(el)
                break

            val_left_x = 0
            for j in range(0, delta_search):
                for i in range(0, height):
                    if (depth_new[i][j] > (globalValues.disMeasure + delta_depth) or depth_new[i][j] < (
                            globalValues.disMeasure - delta_depth)):
                        # print('Num I: ' + str(i) + ', ' + 'CurDepth: ' + str(depth_new[j][i]))
                        if j >= val_left_x:
                            val_left_x = j
            #
            val_right_x = width
            for j in range(width - 1, width - delta_search, -1):
                for i in range(0, height):
                    if (depth_new[i][j] > (globalValues.disMeasure + delta_depth) or depth_new[i][j] < (
                            globalValues.disMeasure - delta_depth)):
                        if j <= val_right_x:
                            val_right_x = j

            # print(len_xv)
            # print(len_yv)
            # print('Left_x_max: ' + str(val_y_high))
            # print('Right_x_max: ' + str(val_down_y))
            # print('Height_y_max: ' + str(val_left_x))
            # print('Low_y_max: ' + str(val_right_x))

            depth_new = []

            for i in range(val_y_high + 1, val_down_y - 1):
                arr = []
                for j in range(val_left_x + 1, val_right_x - 1):
                    arr.append(depth[i][j])
                depth_new.append(arr)

            height = len(depth_new)
            for el in depth_new:
                width = len(el)
                break

            # width = abs(val_down_y - val_y_high)

            # depth_new = []
            # for j in range(height):
            #     arr = []
            #     for i in range(val_y_high, val_down_y):
            #         arr.append(depth[j][i])
            #     depth_new.append(arr)

            # z = 0
            # for i in depth_new:
            #     z_col = 0
            #     for j in i:
            #         # print(j)
            #         # depth[z][z_col] = abs(j*100)
            #         z_col += 1
            #     z += 1
            # получение высоты/ширины фрейма

            # mat = depth
            #
            # width_frm = 0
            # height_frm = 0
            # z = 0
            # for el in mat:
            #     if z == 0:
            #         width_frm = len(el)
            #     # print('Line: ' + str(el))
            #     z += 1
            #
            # height_frm = z

            # print('Height: ' + str(z))

            # компенсация локальных экстремумов
            # i = 0
            # j = 0
            # for j in range(width_frm):
            #     for i in range(height_frm):
            #         if mat[i][j] == 0:
            #             mat[i][j] = mat[i - 1][j - 1]

            # создание 3д модели
            lst_x = []
            lst_y = []
            i = 0
            for i in range(height):
                data = []
                k = 0
                for j in range(width):
                    data.append(k)
                    k += 1
                lst_x.append(data)

            xv = lst_x

            k = 0
            for i in range(height):
                data = []
                for j in range(width):
                    data.append(k)
                lst_y.append(data)
                k += 1

            yv = lst_y

            # blurred = ndimage.gaussian_filter(mat, sigma=(4, 4), order=0)

            # print(blurred)

            # w = np.arctan(mat / 100)
            # print(w)

            # print(len(xv))
            # print(xv[0])

            # print(len(yv))
            # print(yv[0])

            # print(len(depth))
            # print(depth[0])

            arr_box = []
            for i in range(height):
                # arr = []
                for j in range(width):
                    arr_coord = []
                    arr_coord.append(xv[i][j])
                    arr_coord.append(yv[i][j])
                    arr_coord.append(depth_new[i][j])
                    arr_box.append(arr_coord)

            # if globalValues.is_empty:
            #     np.savez_compressed('grunt/dataForVolumeEmpty.npz', depth=arr_box)
            # else:
            #     np.savez_compressed('grunt/dataForVolumeLoad.npz', depth=arr_box)

            # print(arr_empty)

            val_0 = height / globalValues.height_obj
            val_1 = width / globalValues.width_obj
            val_aver = (val_0 + val_1) / 2
            val_aver = round(val_aver, 4)

            # Measure volume convex Hull
            points = arr_box

            # print(arr_box)

            # print(arr_box.shape)

            # print(points)

            volume = 0

            if globalValues.is_convex_hull:
                hull = ss.ConvexHull(points)
                volume = round(hull.volume / (1000 * val_aver * val_aver * 10000), 4)
                print('CurVolume: ' + str(volume))
            else:
                np.savez_compressed('timeMod.npz', depth=arr_box)
                time.sleep(0.25)
                data = np.load('timeMod.npz')
                arr_in = data['depth']
                volume = self.measureVol(arr_in, width, val_aver)
                print('CurVolume: ' + str(volume))

            # if globalValues.is_vertical_area:
            #     print('Vertical area measuring volume!')

            if globalValues.is_empty:
                pathNpz = nameNpz + '_empty.npz'
                pathNew = nameNpz + '_serhio.npz'
                np.savez_compressed(pathNpz, depth=arr_box, volume=volume)
                np.savez_compressed(pathNew, depth=depth_new, xv=xv, yv=yv)
            else:
                pathNpz = nameNpz + '_load.npz'
                pathNew = nameNpz + '_serhio.npz'
                np.savez_compressed(pathNpz, depth=arr_box, volume=volume)
                np.savez_compressed(pathNew, depth=depth_new, xv=xv, yv=yv)

            print('Ending measuring!')

            # s = mlab.mesh(xv, yv, depth_new)

            # alpha = 30  # degrees
            # mlab.view(azimuth=0, elevation=90, roll=-90 + alpha)

            # print('Width_end: ' + str(width))
            # print('Height_end: ' + str(height))

            # mlab.show()

            # np.savez_compressed('box_0.npz', depth=depth_new)
            # np.savez_compressed('box_1.npz', depth= depth_new)

        except Exception as ex:
            globalValues.writeLogData('Функция формирования окончательной модели и вычисление объёма', str(ex))

    def measureVol(self, arr, width, val_aver):

        try:
            lst = arr.shape
            height = lst[0]
            col = 0
            sum_all = 0

            while col < height - width:
                col = col + width
                arr_el = arr[col:col + width]

                # print(arr_el)

                cols = [0, 2]

                arr_el = arr_el[:, cols]
                # points = arr_el

                pp = arr_el
                # compute centroid
                # cent=(sum([p[0] for p in pp])/len(pp), sum([p[1] for p in pp])/len(pp))

                # pylab.scatter([p[0] for p in pp], [p[1] for p in pp])

                # print(pp)

                lenArr = len(pp)

                for i in range(lenArr):
                    if (i == (lenArr - 1)):
                        # print(sum)
                        # print(pp[i][1])
                        # print(pp[i][0])
                        # print(pp[0][1])
                        # print(pp[0][0])
                        sum_all = sum_all + ((pp[i][1] + pp[0][1]) * (pp[0][0] - pp[i][0]))
                        # print(sum)
                    else:
                        # print('123')
                        sum_all = sum_all + ((pp[i][1] + pp[i + 1][1]) * (pp[i + 1][0] - pp[i][0]))
                        # print(pp[i+1][1])
                        # print(sum)

            sum_all = (sum_all / 2)

            # print(sum_all)

            vol = round(sum_all / (1000 * val_aver * val_aver * 10000), 4)

            return vol

        except Exception as ex:
            globalValues.writeLogData('Функция вычисления объёма по массиву точек', str(ex))

    def draw_predictions(self, pred_img, color_img, depth_image):  # <- Метод для отрисовки рамки
        for detection in pred_img[0, 0, :, :]:
            score = float(detection[2])
            # Рисуем рамку только при уверенности модели в обнаружении выше чем на 50%
            if score > 0.5:
                left = detection[3] * color_img.shape[1]
                top = detection[4] * color_img.shape[0]
                right = detection[5] * color_img.shape[1]
                bottom = detection[6] * color_img.shape[0]
                cv2.rectangle(color_img, (int(left), int(top)), (int(right), int(bottom)), (210, 230, 23), 2)

                # Измеряем расстояние до объекта
                depth = depth_image[int(left):int(right), int(top):int(bottom)].astype(float)
                global profile
                depth_scale = profile.get_device().first_depth_sensor().get_depth_scale()
                depth = depth * depth_scale
                dist, _, _, _ = cv2.mean(depth)
                dist = round(dist, 1)
                cv2.putText(color_img, "dist: " + str(dist) + "m", (int(left), int(top) - 5), cv2.FONT_HERSHEY_PLAIN, 1,
                           (0, 255, 0), 1)

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

            # print(listPath)

            for elPath in listPath:
                if (os.path.exists(elPath) == False):
                    try:
                        os.mkdir(elPath)
                    except Exception as ex:
                        globalValues.writeLogData('Функция проверки и создания папки хранилища', str(ex))

        except Exception as ex:
            globalValues.writeLogData('Функция проверки ссылки на папку хранилища', str(ex))

    def strCurDate(self):
        dateToday = datetime.date.today().strftime('%d.%m.%Y')
        str_date_today = str(dateToday)
        return str_date_today

    def strCurTime(self):
        str_cur_time = str(datetime.datetime.time(datetime.datetime.now()))
        len_cur_time = len(str_cur_time)
        str_cur_time = str_cur_time[0: (len_cur_time - 7)]
        str_cur_time = str_cur_time.replace(':', '.')
        return str_cur_time

if __name__ == '__main__':

    print ('Main run!')
    obMes = MeasureVol()
    obMes.runCam()
