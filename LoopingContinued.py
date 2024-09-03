dictionary = { 7: "first", 3: "second", 4: "third", 8: "fourth", 9: "fifth" }

my_list = [int(n) for n in input().split()]

value1 = 0

for n in my_list:
    if n in dictionary:
        print("Yes")
        value1 == value1 + 1
    if n not in dictionary:
        print("No")
        value1 == value1 + 1
        
    