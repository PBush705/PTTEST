arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]


cool = int(input("Input"))

arr.append(cool)

def selection_sort(sort_list):
    for i in range(len(sort_list)):
            smaller_index = i
            for j in range(i+1, len(sort_list)):
                if sort_list[smaller_index] > sort_list[j]:
                    smaller_index = j
            sort_list[i], sort_list[smaller_index] = sort_list[smaller_index], sort_list[i]
    return sort_list

print(selection_sort(arr))