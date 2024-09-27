flowers = [int(n) for n in input("How many blossoms are on each tree?").split()]

def orchard(flowers):
    if len(flowers) == 1:
        print(flowers[0] * 3)
    else: 
        mid = len(flowers) // 2
        first_half = flowers[:mid]
        second_half = flowers[mid:]
        orchard(first_half)
        orchard(second_half)

orchard(flowers)