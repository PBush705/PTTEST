file = open("report.txt", "w")
answer = input("Give me an input")
file.write(answer)
print(file.read())
file.close()