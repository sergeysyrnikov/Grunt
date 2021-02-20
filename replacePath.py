import globalValues
pathFile = 'replacePath/setNetworkCam.txt'


f = open(pathFile, 'r')
data = f.read()
f.close()


data = data.replace('url(C:/img/', 'url(" + globalValues.pathStyleImgs + "')
data = data.replace('C:/img/', "globalValues.pathStyleImgs + '")

f = open(pathFile, 'w')
f.write(data)
f.close()


