import  os
import shutil

pathCamFolderImgWrt = '/usr/local/Sinaps/Storage/172.22.2.49'

listPathElFrm = os.listdir(pathCamFolderImgWrt)

# os.rmdir(pathCamFolderImgWrt)
shutil.rmtree(pathCamFolderImgWrt)

# for el in listPathElFrm:
#     os.system('rm -r ' + pathCamFolderImgWrt + '/' + str(el))