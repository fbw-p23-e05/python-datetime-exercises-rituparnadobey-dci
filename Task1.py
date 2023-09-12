# Task 1:
# Write a Python script to display the various Date Time formats.

# Current date and time
# Current year
# Month of year
# Week number of the year
# Weekday of the week
# Day of year
# Day of the month
# Day of week


import datetime as dt


current_datetime = dt.datetime.now()
print(current_datetime)

current_year =  current_datetime.year
print("Current_year:",current_year)

Month_of_year = current_datetime.strftime("%B")
print("Month of year:", Month_of_year)

Weekday_of_the_week = current_datetime.strftime("%A")
print("Weekday of the week:",Weekday_of_the_week)

Day_of_year = current_datetime.strftime("%j")
print("Day of year:",Day_of_year)

Week_number_of_the_year = current_datetime.strftime("%U")
print("Week number of the year:",Week_number_of_the_year)

Day_of_the_month = current_datetime.day
print("Day of the month:",Day_of_the_month)

Day_of_week = current_datetime.strftime("%A")
print("Day of week:",Day_of_week)
