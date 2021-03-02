import globalValues
import pymysql
import datetime
import time

lstDataBD = [['127.0.0.1', 'sergey', '34ubitav', 'ssa2505', 3306], ['192.168.1.128', 'sergey', '34ubitav', 'ssamip', 3306]]

con = pymysql.connect(host='localhost',
                                   port=3306,
                                   user='sergey',
                                   passwd='34ubitav',
                                   db=globalValues.dbMySqlName)
cur = con.cursor()
sqlQ = ("SELECT reg_number FROM " + globalValues.tblsDB[6])
cur.execute(sqlQ)
rowsGRZPool = cur.fetchall()

for row in rowsGRZPool:
    globalValues.listPoolTS.append(str(row[0]))

cur.close()
con.close()

listGrz = globalValues.listPoolTS

def scanDataFromPoly(strGRZ, lstDataBD, list_grz_zakaz, name_st_order, debug):
    try:
        checkZN = False
        weight_obj = ''
        volume_obj = ''
        num_talon = 0
        time_entry = ''
        time_check_out = ''

        if (debug):
            print(lstDataBD[0][3])

            strGRZ = strGRZ.replace('(', '').replace(')', '').replace(',', '').replace('\'', '').replace(' ', '').upper()

            print(strGRZ)

            for str_db_grz in list_grz_zakaz:
                iter_s = 0
                check_good_grz = 0
                lenAr = min(len(str_db_grz), len(strGRZ))
                print(lenAr)
                countSymb = 0
                countVal = 0
                for i in range(lenAr):

                    if (0 < iter_s < 4):
                        if (strGRZ[iter_s] == str_db_grz[iter_s]):
                            countVal += 1
                    else:
                        if (strGRZ[iter_s] == str_db_grz[iter_s]):
                            countSymb += 1

                    if (countVal >= 2 and countSymb >= 1):
                        checkZN = True
                        strGRZ = str_db_grz
                        print('goooooooooooooooooood')
                        print(iter_s)
                        break
                    else:
                        checkZN = False

                    iter_s += 1

            print(checkZN)
            print(strGRZ)
            print(list_grz_zakaz)
        else:
            checkZN = True

        if (checkZN):

            iterL = 0
            checkOrder = False
            for rowData in lstDataBD:

                try:
                    con = pymysql.connect(host=lstDataBD[iterL][0],
                                          port=lstDataBD[iterL][4],
                                          user=lstDataBD[iterL][1],
                                          passwd=lstDataBD[iterL][2],
                                          db=lstDataBD[iterL][3])
                    # with con:
                    if True:
                        cur = con.cursor()

                        sqlQ = ("SELECT * FROM " + globalValues.tblsDB[1])
                        cur.execute(sqlQ)
                        rows = cur.fetchall()
                        for row in rows:
                            if (str(row[7]) == name_st_order):
                                print(str(row[1]))
                                if (str(row[2]) == strGRZ):
                                    checkOrder = True
                                    num_talon = row[1]
                                    weight_obj = row[5]
                                    volume_obj = row[6]
                                    time_entry = row[10]
                                    time_check_out = row[11]
                                    number_order = num_talon

                                    query = ("INSERT INTO " + globalValues.tblsDB[5] + " (num_talon, weight, volume, time_entry, time_out) VALUES ( %s, %s, %s, %s, %s)")
                                    cur.execute(query, (number_order, weight_obj, volume_obj, time_entry, time_check_out))
                                    con.commit()

                                    cur.execute("SELECT * FROM " + globalValues.tblsDB[6])
                                    rows = cur.fetchall()
                                    countRows = 0

                                    str_grz = ''
                                    car_name = ''
                                    date_work = ''
                                    name_company = ''
                                    car_model = ''

                                    dataSearch = strGRZ.lower()
                                    is_search = False

                                    for row in rows:
                                        is_search = dataSearch in str(row[4]).lower()
                                        if is_search:
                                            car_name = str(row[2])
                                            name_company = str(row[1])
                                            car_model = str(row[3])
                                            break

                                    print(number_order)
                                    print(strGRZ)
                                    print(car_name)
                                    print(name_company)
                                    print(car_model)
                                    dateToday = datetime.date.today().strftime('%d.%m.%Y')
                                    date_work = str(dateToday)
                                    print(date_work)
                                    str_cur_time = str(datetime.datetime.time(datetime.datetime.now()))
                                    len_cur_time = len(str_cur_time)
                                    str_cur_time = str_cur_time[0: (len_cur_time - 7)]
                                    str_cur_time = str_cur_time.replace(':', '.')
                                    str_time = str_cur_time

                                    print(str_time)

                                    query = ("INSERT INTO " + globalValues.tblsDB[1] + " (number_order, number_grz, date, time_entry, state_order) VALUES ( %s, %s, %s, %s, \'выполняется\')")
                                    cur.execute(query, (number_order, strGRZ, date_work, str_time))
                                    con.commit()

                                    query = ("INSERT INTO " + globalValues.tblsDB[2] + " (car_name, number_order, date_work, name_company, car_model, car_grz) VALUES (%s, %s, %s, %s, %s, %s)")
                                    cur.execute(query, (car_name, number_order, date_work, name_company, car_model, str_grz))
                                    con.commit()

                                    sqlMy = "INSERT INTO " + globalValues.tblsDB[4] + " (url) VALUES (%s)"
                                    cur.execute(sqlMy, ('http://'))
                                    con.commit()

                                    time.sleep(0.1)

                                    break



                    cur.close()
                    con.close()

                except Exception as ex:
                    globalValues.writeLogData('Функция подключения к выбранной бд', str(ex))

                iterL += 1

                if (checkOrder):
                    break

            print(weight_obj)
            print(volume_obj)
            print(num_talon)
            print(time_entry)
            print(time_check_out)

    except Exception as ex:
        globalValues.writeLogData('Функция поиска данных из БД по грз', str(ex))

scanDataFromPoly('K136LE69', lstDataBD, listGrz, 'выполняется', True)

