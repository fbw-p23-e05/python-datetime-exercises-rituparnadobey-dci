# Write a Python program to convert Year/Month/Day to Day of Year using datetime module.



import datetime as dt


current_datetime = dt.datetime.now()

Day_of_year = current_datetime.strftime("%j")

print("Today's date:",current_datetime)
print("Day of year:",Day_of_year)