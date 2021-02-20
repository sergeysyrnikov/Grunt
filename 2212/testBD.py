import pymysql

con = pymysql.connect(host='127.0.0.1',
                                               port=3306,
                                               user='root',
                                               passwd='SiNaPs_281082',
                                               db='controlgruntsystemsinaps')

print(con.open)

cur = con.cursor()

sqlQ = "SELECT * FROM maindataorder"

# sqlQ = "SELECT * FROM maindataorder WHERE number_order like 1001"

# sqlQ = "SELECT * FROM maindataorder WHERE number_grz like 'N14%'"

# sqlQ = "SELECT * FROM maindataorder"

cur.execute(sqlQ)

rows = cur.fetchall()

print(len(rows))

i = 0
for row in rows:
    print(row)
    i += 1

# sqlID = 'SELECT id FROM maindataorder order by id desc limit 1'
#
# cur.execute(sqlID)
#
# rows_id = cur.fetchall()
#
# num_end_order = rows_id[0][0]
# print(num_end_order)
# num_start_order = str(num_end_order - 60)
#
# sqlCom = 'SELECT * FROM maindataorder LIMIT ' +num_start_order+ ', ' +str(num_end_order)+ ''
#
# cur.execute(sqlCom)
#
# rows = cur.fetchall()
#
# print(rows)

cur.close()
con.close()