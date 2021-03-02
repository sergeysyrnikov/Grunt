import zeep
from onvif import ONVIFCamera
import globalValues

cam = ONVIFCamera('10.2.165.101', 80, 'admin', 'admin', globalValues.curDisk + '/wsdl/')

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


    request = cam.imaging.create_type('SetImagingSettings')
    video_sources = cam.media.GetVideoSources()  # get video source to fetch token

    request.VideoSourceToken = video_sources[0].token # ptz.ContinuousMove(requestc)

    data = cam.imaging.create_type('GetImagingSettings')
    data.VideoSourceToken = video_sources[0].token
    # print(cam.imaging.GetImagingSettings(data))

    request.ImagingSettings = {
        'Brightness': 50,
        'Contrast': 55,
        'IrCutFilter': 'OFF'
        }
    cam.imaging.SetImagingSettings(request)


    # data = cam.imaging.create_type('GetImagingSettings')
    # data.VideoSourceToken = video_sources[0].token
    # print(cam.imaging.GetImagingSettings(data))

