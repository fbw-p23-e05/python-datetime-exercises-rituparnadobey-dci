# Write a Python program to add 5 seconds to the current time.


import datetime as dt
from datetime import timedelta

current_time = dt.datetime.now()

added_time = current_time + timedelta(seconds=5)

print(current_time)
print(added_time)

