# Write a Python program to find the date of the first Monday of a given week.


import datetime as dt

usrYear = int(input('Please enter the year: '))

usrWeek = int(input('Please enter the week number: '))

year_start = dt.datetime(usrYear, 1, 1)

num_of_days = (usrWeek - 1) * 7

num_of_week = year_start + dt.timedelta(days=num_of_days)

while num_of_week.weekday() != 0:
    num_of_week += dt.timedelta(days=1)


day_of_week = num_of_week.strftime("%A")


print(day_of_week, "of week", usrWeek, "in", usrYear, "year is:", num_of_week.date())
num_of_week += dt.timedelta(days=7)













