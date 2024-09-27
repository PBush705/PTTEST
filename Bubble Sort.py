arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]

num = int(input("Give a number"))

arr.append(num)


def bubbleSort(sort_list):
    n = len(sort_list)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if sort_list[j] > sort_list[j+1]:
                sort_list[j], sort_list[j+1] == sort_list[j+1], sort_list[j]

print(bubbleSort(arr))