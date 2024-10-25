import datetime

x = datetime.datetime.now()
month = int(x.strftime("%m")) % 12
day = int(x.strftime("%d")) % 365
print("It has been " + str(month) + " months and " + str(day) + " days since your New Years resolution. How are you doing?")