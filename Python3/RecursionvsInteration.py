list_of_nums = [int(n) for n in input().split()]
def add_list(my_list):
	if len(my_list) == 1:
		return my_list[0]
	else:
		return my_list[0] + add_list(my_list[1:])

print(add_list(list_of_nums))