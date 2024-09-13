file = open("yahoo!.txt", "r")
cough = int(input("How much should there be?"))
print(file.read(cough))
file.close()