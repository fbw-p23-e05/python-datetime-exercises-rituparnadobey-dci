# Write a Python program to print the dates of yesterday, today, tomorrow.


import datetime as dt
from datetime import timedelta

today = dt.date.today()
print("Today's date:",today)

yesterday = today - timedelta(days=1)
print("Yesterday's date:",yesterday)

tomorrow = today + timedelta(days=1)
print("Tomorrow's date:",tomorrow)