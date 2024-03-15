"""
import datetime as dt
current_date=dt.date.today()
print("current date : ",current_date)

new=dt.date(2024, 3, 6)
print(new)
print("year : ",new.year)
print("month : ",new.month)
print("day : ",new.day)

print("--------------------------------")

current_time=dt.datetime.now()
print(current_time)

print("--------------------------------")

newyear=dt.date(2025,1,1)
current_date=dt.date.today()
difference=newyear-current_date
print(difference)
"""
#spectifying the formate for the date

import datetime as dt
current = dt.datetime.now()
print(current)
words=current.strftime("%A %B %D %Y")
print(words)
