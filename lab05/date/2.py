import datetime



today = datetime.datetime.now()

yesterday = today - datetime.timedelta(days=1)

tomorrow = today + datetime.timedelta(days=1)

print(yesterday.strftime("%A"))
print(today.strftime("%A"))
print(tomorrow.strftime("%A"))
