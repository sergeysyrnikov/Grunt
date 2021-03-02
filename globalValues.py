import datetime
import os
import pymysql
import subprocess
import traceback
import sys

# curDisk = 'S'
curDisk = 'Data'

# diskForTimeFiles = 'F'
import tempfile

pathTemp = str(tempfile.gettempdir()).replace('\\', '/')
diskForTimeFiles = '/usr/local/Sinaps/Storage'

passwdLogin = '34ubitav'

valNumShowOeder = 60

timeClearCache = 30000

testSystem = True
# testSystem = False

checkEditMode = False

findingMainOrder = False
findingMainGRZ = False
findingMainDate = False
searchData = ''

# polygon = False
polygon = True

debug = False
# debug = True

debugCam = False
# debugCam = True

# debugPorts = False
debugPorts = True

# debugPortWeight = False
debugPortWeight = True

# debugCamScan = True
debugCamScan = False

# debugTestSystem = False
debugTestSystem = True

debugStrg = False
# debugStrg = True

debugSergey = True
# debugSergey = False
# debugAdmin = True
debugAdmin = False
# debugOperator = True
debugOperator = False

# debugLogin = True
debugLogin = False

debugOrder = True
# debugOrder = False

# debugClose = True
debugClose = False

# debugVolume = True
debugVolume = False

checkRestartExe = False

#################XLS File

# pathFileXls = str(os.getenv('APPDATA')) + r'\Sinaps\cryptoSSA.xlsx'
pathFileXls = '/usr/local/Sinaps/cryptoSSA.xlsx'

find_zakaz = False

lst_all_data = []

checkLoadData = False

#timeLoadSystemMenu
timeLoadSys = 10
delta_time= 20

#DisFindRec

disMeasure = 700

deltaDis = 50

maxDist = 5000

deltaFrame = 30

deltaFrameX = 120

numRepeat = 50

numRepeat_x = 50

height_obj = 33

width_obj = 39

# debug = False

numberFrameForDepth = 5

# nameModelNpz = 'grunt/modelGrunt.npz'
# nameImgGrunt = 'grunt/imgGrunt.png'
# nameImgGruntWithContur = 'grunt/imgAreaGrunt.png'
# nameModelGruntEmpty = 'grunt/modelAreaGruntEmpty.npz'
# nameModelGruntLoad = 'grunt/modelAreaGruntLoad.npz'

is_convex_hull = False
# is_convex_hull = True

#searchingEdgesMax

delta_find_edge = 20
delta_search = 50
delta_depth = 300

# is_empty = False
is_empty = True

is_read_depth = False

nameObject = 'Учаток #14'
namePolygon = 'Полигон #5'

defaultPathPr = curDisk + '/ACMK'
pathReports = defaultPathPr + '/Reports'
pathTalon = defaultPathPr + '/Тalons/'
pathWeightImg = defaultPathPr + '/imgs/'
pathScanImgs = defaultPathPr + '/imgs/'
pathNpArr = defaultPathPr + '/arrVolume/'
pathFileVideo = ''

pathStrg = ''
curTalon = ''
pathFileVideoKppIn = ''
pathFileVideoKppOut = ''
pathFileVideoWeightIn = ''
pathFileVideoWeightOut = ''

pathMainVideoStrg = ''

curNameChl = ''

refreshTblMain = False

value = 0
testVal = False

ipCam = ''
oneCheckCamEdit = False

#Coms
outComWeight = False
outComTraf = False

#valLimitDetect
valDetect = 0

if debugOrder:
    valDetect = -1
else:
    valDetect = -1

#VideoEvents

numTalonVideo = ''
numGRZVideo = ''
curChannelCam = ''

#ImgsForCr3D

pathImgs = curDisk + '/img3D'

#Login

curUserName = ''

rtspMainLink = ['','','','','','','','','','','','']

#PollTS

checkPoolTS = True

#ValVarWeight

if debugTestSystem:
    # valWeightMaxMeas = 90
    # valWeightToWriteVal = 40
    # deltaWeight = 50

    valWeightMaxMeas = 5000
    valWeightToWriteVal = 1000
    deltaWeight = 2000

else:
    valWeightMaxMeas = 5000
    valWeightToWriteVal = 1000
    deltaWeight = 2500

#checkConDB
checkConDbMySql = False
checkConDbPgSql = False


#MeasureWeight

stateScaner = False

#stateTS

listPoolTS = []
listWeightEmptyTS = []
listCurTsSt = []
timelistTs = []
# deltaTime = 18000
deltaTime = 60

listRtsp = ['','','','','','','','','','','','']
listIp = ['','','','','','']

#Storage

stateStorage = False

deltaWriting = 180

timeWriteEvent = 30

numberFolderDateSave = 3

curDate = ''

curPathFolderToWrite = ''

pathFileLog = curDisk + '/Sinaps/logGrunt.txt'

numEvent = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

listPathVideoCreate = []

numThreadVideo = 0

checkCamStrg = [False, False, False, False]

oldCheckCam = []

#Cams

lstGoodCams = [False, False, False, False, False, False]
lstIpCams = ['','','','','','']

#namesDB

dbMySqlName = 'controlgruntsystemsinaps'
dbPgSqlName = 'trassir3'

#varMainMeasureVals

str_grz_weight = ''
str_ready_weight = ''
startDeltaWeight = 0

#VarDBmySql

my_sql_localhost = 'localhost'
my_sql_name = ''
my_sql_password = ''
my_sql_db = "controlGruntSystem1"
my_sql_port = 3306

#TimingDayNightYear

lstTimingDayNight = []


#VarDBpgSql

my_pg_localhost = ''
my_pg_name = ''
my_pg_password = ''
my_pg_db = 'trassir3'
my_pg_port = 3306

#namesTblsMySqlBD

tblsDB = ['journal', 'maindataorder', 'orderdata', 'settingsvideocam', 'tracking', 'object', 'dataAboutTS']

#searchDataMainTbl

searchData = False
checkEditTbl = False
checkUpdate = True
is_edit_data = False

#varContextPanel

hideContext = False
defCon = 0

#colorForm

colorForm = 0

#pathFiles

# pathDefaultData = str(os.getenv('APPDATA'))

pathDefaultData = '/usr/local'

pathDefFldr = '/usr/local/Sinaps'

pathOnVif = pathDefFldr + '/wsdl'

print(pathDefFldr)
print('serhio123')

# pathStyleImgs = pathDefFldr + '\img\\'

pathStyleImgs = '/usr/local/Sinaps/img/'
# pathStyleImgs = '/home/sergey/123/imgStrg/'

# pathStyleImgs = pathStyleImgs.replace('\\', '/')
# pathStyleImgs = 'C:/Users/Admin/AppData/Roaming/Sinaps/img/'


pathFileTiming = ('/usr/local/Sinaps/timing.xlsx')
# pathFileTiming = 'C:/Users/Admin/AppData/Roaming/Sinaps/timing.xlsx'

print(pathStyleImgs)

pathImage = pathStyleImgs

pathImgGray = pathImage + 'icongreykrug3131.png'

print(pathImgGray)

sizeStrg = ''


# pathFileLog = 'E:/logGrunt.txt'
curPathFolderToWrite = ''

#boolStopThreading

stopThreadCams = False
stopSysPanel = False
stopUpdateTblJournal = False
stopThStHandWorking = False
stopCamInSet = False
stopAll = False
stopThreadSysMenu = False
stopEncryptedDecrypt = False
stopUpdateMainTbl = False
stopUpdateTblJournalTS = False
stopUpdateTblTS = False
stopStrg = False
stopComPortWeight = False
stopComPortTraffic = False
stopVideoScaner = False

#CamsVar

numCam = 0
refreshTblSetCam = False
isNextConCam = False
checkCamAfterAdd =False
checkUpdateTblJournal = False
checkUpdateTblMap = False
checkUpdateTblTS = False

camsSt = [False, False, False, False, False, False]
rtspCams = ['', '', '', '', '', '', '', '']
ipsCams = ['', '', '', '', '', '', '', '']

#Traffic

valTrafficSt = 0
startHandSt = False
trafWeightReady = False
trafMeasure = False
trafDefault = False
check_sema_1_out = 0
check_sema_1_in = 0
check_sema_2_out = 0
check_sema_2_in = 0

#encryptedAndDecrypted

encryptDecryptNum = [False, False, False, False, False, False, False, False]

boolCheckInsertPassword = [False, False, False, False, False, False, False, False]

boolCheckInsertTrueCamPassword = [False, False, False, False, False, False]

statusGoodLoginDev = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

loginDataList = ['','','','','','','','','','','','','','','','']

#FunctionWriteLogAndJournal

def writeEventToDBJournal(self, object_name, text_event):
    try:

        if (self.con.open == False):
            self.con = pymysql.connect(host=my_sql_localhost, port=my_sql_port,
                                       user=my_sql_name,
                                       passwd=my_sql_password, db=dbMySqlName)
        if True:
        # with self.con:

            cur = self.con.cursor()

            query = ("INSERT INTO " + tblsDB[0] + " (date , time, object, data) VALUES ( %s, %s, %s, %s)")
            # ( % s, \'B126PE777\', 5135, 9, \'выполняется\')'

            dateToday = datetime.date.today().strftime('%d.%m.%Y')
            str_date_today = str(dateToday)
            cur_time = datetime.datetime.time(datetime.datetime.now())
            str_cur_time = str(cur_time)
            len_cur_time = len(str_cur_time)
            str_cur_time = str_cur_time[0: (len_cur_time - 7)]
            # passwordCam = uiNetCam.leNewCamPass.text()

            # hash = hashlib.sha512(passwordCam.encode())
            # data = str(hash.hexdigest())
            #
            cur.execute(query, (str_date_today, str_cur_time, object_name, text_event))
            #
            self.con.commit()
            print('Data123123')
    except Exception as ex:
        writeLogData('Функция записи события в журнал системное меню', str(ex))

def writeEventToDBJournalMain(object_name, text_event):
    try:

        con = pymysql.connect(host=my_sql_localhost, port=my_sql_port,
                                   user=my_sql_name,
                                   passwd=my_sql_password, db=dbMySqlName)

        cur = con.cursor()
        if True:
        # with con:
            query = ("INSERT INTO " + tblsDB[0] + " (date , time, object, data) VALUES ( %s, %s, %s, %s)")

            dateToday = datetime.date.today().strftime('%d.%m.%Y')
            str_date_today = str(dateToday)
            cur_time = datetime.datetime.time(datetime.datetime.now())
            str_cur_time = str(cur_time)
            len_cur_time = len(str_cur_time)
            str_cur_time = str_cur_time[0: (len_cur_time - 7)]

            #hashKey

            # passwordCam = uiNetCam.leNewCamPass.text()

            # hash = hashlib.sha512(passwordCam.encode())
            # data = str(hash.hexdigest())
            #
            cur.execute(query, (str_date_today, str_cur_time, object_name, text_event))
            #
            con.commit()


        cur.close()
        con.close()
    except Exception as ex:
        writeLogData('Функция записи события в журнал', str(ex))

def writeLogData(strFunctionName, strSysError):
    try:

        print('Write to:', pathFileLog, strSysError)

        dateToday = datetime.date.today().strftime('%d.%m.%Y')
        str_date_today = str(dateToday)
        cur_time = datetime.datetime.time(datetime.datetime.now())
        str_cur_time = str(cur_time)
        len_cur_time = len(str_cur_time)
        str_cur_time = str_cur_time[0: (len_cur_time - 7)]
        # pathFileLog = globalValues.pathFileLog
        if (os.path.exists(pathFileLog) == False):
            fileLog = open(pathFileLog, 'w')
            fileLog.close()
        fileLog = open(pathFileLog, 'r')
        dataFile = fileLog.read()
        fileLog.close()
        strDataInfoErr = ''
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname, lineno, fn, text = frame
            strDataInfoErr = "Ошибка в %s строка: %d" % (fname, lineno)

        # print(strDataInfoErr)

        fileLog = open(pathFileLog, 'w')
        strDataToWrite = (str_cur_time + '  ' + str_date_today + '      ' + strFunctionName + '   :  ' + strSysError + '. ' + strDataInfoErr + '.' + '\r\n')
        newDataFile = strDataToWrite + dataFile
        fileLog.write(newDataFile)
        fileLog.close()

        print('Ending!')

    except Exception as ex:
        print(ex)

def checkFolderPath(pathFolder, isHide):
    try:

            if (os.path.exists(pathFolder) == False):
                try:
                    os.mkdir(pathFolder)
                    # globalValsSBV.curPathFolderToWrite = pathFolder
                    if (isHide):
                        subprocess.call(['attrib', '+H', pathFolder])
                    return False
                except Exception as ex:
                    print(ex)
            else:
                return True

    except Exception as ex:
        print(ex)

def writeLogDataTh(strFunctionName, strSysError, strIP):
    try:
        pathFolder = curDisk + '/SinapsLogs'
        checkFolderPath(pathFolder, True)
        dateToday = datetime.date.today().strftime('%d.%m.%Y')
        str_date_today = str(dateToday)
        cur_time = datetime.datetime.time(datetime.datetime.now())
        str_cur_time = str(cur_time)
        len_cur_time = len(str_cur_time)
        str_cur_time = str_cur_time[0: (len_cur_time - 7)]
        # pathFileLog = globalValues.pathFileLog
        pathFile = pathFolder + '/' + strIP + '.txt'
        if (os.path.exists(pathFile) == False):
            fileLog = open(pathFile, 'w')
            fileLog.close()
        fileLog = open(pathFile, 'r')
        dataFile = fileLog.read()
        fileLog.close()
        strDataInfoErr = ''
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname, lineno, fn, text = frame
            strDataInfoErr = "Ошибка в %s строка: %d" % (fname, lineno)

        fileLog = open(pathFile, 'w')
        strDataToWrite = (str_cur_time + '  ' + str_date_today + '      ' + strFunctionName + '   :  ' + strSysError + '. ' + strDataInfoErr + '.' + '\r\n')
        newDataFile = strDataToWrite + dataFile
        fileLog.write(newDataFile)
        fileLog.close()
    except Exception as ex:
        print(str(ex))

if (debug):
    # print('checkingIn!!!')
    my_sql_localhost = 'localhost'
    my_sql_name = 'sergey'
    my_sql_password = '34ubitav'
    my_sql_db = dbMySqlName
    my_sql_port = 3306