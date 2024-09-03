def integer(smallest, largest):
    smallest = min(smallest, largest)
    print(smallest)


lowest = int(input("give me a number"))
highest = int(input("give me another number"))
integer(lowest, highest)