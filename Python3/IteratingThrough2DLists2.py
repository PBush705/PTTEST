x = int(input("What is the first number?"))

y = int(input("What is the second number?"))

z = int(input("What is the third number?"))
rows = 4
cols = 3
my_list = [[0, 1, x], [10, 15, y], [100, 200, 300], [5, 6, z]]
largest = 0
cool = []

for i in range(rows):
    for j in range(cols):
        my_list[i][j] = cool.append(my_list[i][j])
largest = max(cool)
print(largest)