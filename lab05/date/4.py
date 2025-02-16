import datetime

date1 = datetime.datetime.now()
date2 = datetime.datetime(2024, 11, 3)
difference = date1 - date2
print(difference.total_seconds())