# Write a Python program to print the next 5 days starting today.

import datetime as dt


Today = dt.datetime.today()

Date = Today.date()

print(Date)
print('__________')

for i in range(0,5):
    print(Date + dt.timedelta(days=i))
