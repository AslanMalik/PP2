import datetime

today = datetime.datetime.now()

five_days_ago = today - datetime.timedelta(days=5)
print(today.strftime("%d-%m-%Y"))
print(five_days_ago.strftime("%d-%m-%Y"))