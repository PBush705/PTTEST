rows = 4
cols = 3
my_list = [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]
yeah = int(input("multiply the list"))
for x in range(rows):
    for i in range(cols):
        my_list[x][i] = my_list[x][i] * yeah

print(my_list)