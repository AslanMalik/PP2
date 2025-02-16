import datetime

day = datetime.datetime.now()
day_without = day.replace(microsecond=0)

print(day_without)