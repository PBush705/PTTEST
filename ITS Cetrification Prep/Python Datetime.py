import datetime

x = datetime.datetime.now()

nice = int(x.strftime("%m"))

days = int(x.strftime("%d"))

months = int(input("Month"))

monthsleft = (months - nice) % 12 

if months == 4 or months == 6 or months == 9 or months == 11:
	daysleft = (30 - days)
elif months == 2:
    daysleft = (28 - days)
elif months == 1 or months == 3 or months == 5 or months == 6 or months == 7 or months == 8 or months == 10 or months == 12:
    daysleft = (31 - days)

print("You have" + " " + str(monthsleft) + " " + "months and" + " " + str(daysleft) + " " + "days until it's your birthday month!")

print(x)

print(x.strftime("%X"))

print(x.strftime("%m"))

print(x.strftime("%d"))

print(x.strftime("%Y"))