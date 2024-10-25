import math

cool = int(input('People'))
bike = int(input('Bikes'))

print("In this town, for every bike that exists there are" + " " +  str(math.ceil(cool / bike)) + " " + "people.")