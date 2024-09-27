books = [int(n) for n in input("Input a list of numbers").split()]

def reading(books):
    if len(books) == 2:
        print(books[0] + books[1])
    else: 
        mid = len(books) // 2
        first_half = books[:mid]
        second_half = books[mid:]
        reading(first_half)
        reading(second_half)

reading(books)