# CHECK LINE 18 or NP2-ReadMe >>> for introduction of app

import datetime
from khayyam import jalali_datetime, jalali_date

# khayyam ketabkhone hastesh ke module jalali_datetime ro dare
# az jalali_datetime bayad class JalaliDatetime ro seda konim
# function now ya today ro ham badesh seda mikonim

# date with hour
j_hour_date = jalali_datetime.JalaliDatetime
g_hour_date = datetime.datetime

# date without hour
j_date = jalali_date.JalaliDate
g_date = datetime.date

print("NP2-JalaliAndGregorianDate V1.1 running...")
print("the app will show today date in Jalali and Gregorian shape\n")

print('date with hour :')
print(j_hour_date.now())
print(g_hour_date.now())

print('\ndate without hour :')
print(j_date.today())
print(g_date.today())

print('\ndate with name of month and day :')
print(j_date.today().strftime('%A %d %B %Y'))
print(g_date.today().strftime('%A %d %B %Y'))

#   A = rozeNeveshtar   d = adadeRoze
#   B = maheNeveshtar   Y = adadeSal