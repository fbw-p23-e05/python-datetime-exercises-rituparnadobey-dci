# Write a Python program to select all the Sundays in a specified year.


import datetime as dt

usrYear = int(input('Please enter the year: '))

current_date = dt.datetime(usrYear, 1, 1)

while current_date.year == usrYear:
        
    if current_date.weekday() == 6:
        print(current_date.strftime("%Y-%m-%d %A"))

    current_date += dt.timedelta(days=1)