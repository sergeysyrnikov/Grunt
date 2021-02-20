import hashlib
import pymysql

# login_new = 'operator'
# password = 'sinaps2020'

login_new = 'admin'
password = 'sinaps'

hash = hashlib.sha512(password.encode())
data = str(hash.hexdigest())

con = pymysql.connect('localhost', 'sergey',
                      '34ubitav', 'cars')




# with con:
if True:
    cur = con.cursor()
    query = (
            'INSERT INTO datalogin (login, account_passwords) VALUES ( %s, %s)')
        # ( % s, \'B126PE777\', 5135, 9, \'выполняется\')'
    cur.execute(query, (login_new, data))

    con.commit()

