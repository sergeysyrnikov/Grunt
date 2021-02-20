import globalValues
from onvif import ONVIFCamera
import serial
import serial.tools.list_ports

def changeCamNightDayAuto(name, str_cur_time_st):
    # try:
        print('checkingName: ' + name)
        numCam = int(name)
        j = 2* numCam
        if (numCam > 1 and numCam < 4):
            dataLogin = 'admin'
            dataPassWd = 'qwE12345'
        else:
            dataLogin = 'admin'
            dataPassWd = 'admin'
        strIp = globalValues.listIp[numCam]
        print(strIp)
        strIp = '10.2.165.102'

        print(dataLogin)
        print(dataPassWd)
        print(strIp)

        cam = ONVIFCamera(strIp, 80, dataLogin, dataPassWd, '/home/sinaps/venv/lib/python3.6/site-packages/wsdl')

        print(cam.devicemgmt.GetDeviceInformation())
        check = True

        if check:
            dt = cam.devicemgmt.GetSystemDateAndTime()

            # media_service = cam.create_media_service()
            #
            # profiles = media_service.GetProfiles()
            #
            # video = media_service.GetVideoSources()
            #
            # image = cam.create_imaging_service()

            media_service = cam.create_media_service()

            # profiles = media_service.GetProfiles()

            # video = media_service.GetVideoSources()

            image = cam.create_imaging_service()

            request = cam.imaging.create_type('SetImagingSettings')
            video_sources = cam.media.GetVideoSources()  # get video source to fetch token

            request.VideoSourceToken = video_sources[0].token  # ptz.ContinuousMove(requestc)

            data = cam.imaging.create_type('GetImagingSettings')
            data.VideoSourceToken = video_sources[0].token

            dataInfo = cam.imaging.GetImagingSettings(data)
            dataInfo = str(dataInfo)
            print("GetImgSet: " + dataInfo)
            # strSearch = "IrCutFilter': 'OFF"
            # print(strSearch)
            # checkIs = strSearch in dataInfo
            #
            # print("dataCam:" + str(dataInfo))
            # print(checkIs)
            #
            # dataStCam = 'OFF'
            #
            # if checkIs:
            #     dataStCam = 'ON'

            request.ImagingSettings = {
                # 'Brightness': 50,
                # 'Contrast': 55,
                'IrCutFilter': str_cur_time_st
            }
            cam.imaging.SetImagingSettings(request)

            # data = cam.imaging.create_type('GetImagingSettings')
            # data.VideoSourceToken = video_sources[0].token
            # print(cam.imaging.GetImagingSettings(data))
    # except Exception as ex:
    #     globalValues.writeLogData('Функция работы с камерами по onvif', str(ex))
import sys
import glob
import serial


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux'):
        temp_list = glob.glob('/dev/tty[A-Za-z]*')

    result = []
    for a_port in temp_list:

        try:
                s = serial.Serial(a_port)
                s.close()
                result.append(a_port)
        except serial.SerialException:
                pass

    return result


if __name__ == '__main__':
    # changeCamNightDayAuto('2', 'OFF')


    list = serial.tools.list_ports.comports()
    for element in list:
        dataEl = str(element.device)
        print(dataEl)

    print(serial_ports())

