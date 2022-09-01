# CHECK LINE 45 or NP1-ReadMe >>> for introduction of app

import datetime
from khayyam import jalali_datetime, jalali_date

# khayyam ketabkhone hastesh ke module jalali_datetime ro dare
# az jalali_datetime bayad class JalaliDatetime ro seda konim
# function now ya today ro ham badesh seda mikonim

# date with hour
a = datetime.datetime
b = jalali_datetime.JalaliDatetime

# date without hour
aa = datetime.date
bb = jalali_date.JalaliDate

print("NP2-JalaliAndGregorianDate V1.0 running...\n")
print("the app will show today date in Jalali and Gregorian shape\n")

print('------------------------------------\ndate with hour :\n')
print(a.now())
print(b.now())
print('\n------------------------------------\ndate without hour :\n')
print(aa.today())
print(bb.today())
print('\n------------------------------------\ndate with name of month and day :\n')
print(aa.today().strftime('%A %d %B %Y'))
print(bb.today().strftime('%A %d %B %Y'))
# A = rozeNeveshtar;d = adadeRoze;B = maheNeveshtar;Y = adadeSal
