arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]

arr.append(int(input("Give a number")))


def InsertionSort(arr):
   for i in range(1, len(arr)):
       j = i
       while arr[j-1] > arr[j] and j > 0:
           arr[j - 1], arr[j] = arr[j], arr[j - 1]
           j -= 1


InsertionSort(arr)
print(arr)

