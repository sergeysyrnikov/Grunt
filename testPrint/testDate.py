import datetime

dateToday = datetime.date.today().strftime('%d.%m.%Y')
str_date_today = str(dateToday)

lstDate = str_date_today.split('.')
        #
        # print(lstDate[0])
        # print(lstDate[1])

cur_time = datetime.datetime.time(datetime.datetime.now())
str_cur_time = str(cur_time)

# stTiming = str_cur_time.split(':')
# hour = lstTiming[0]
# min = lstTiming[1]
        # print(hour)
        # print(min)

# str_cur_time = hour + min

num_month = int(lstDate[1])
num_day = int(lstDate[0]) - 1

print(num_month)
print(num_day)