class Fruit:

    def __init__(self, shape, kind, size):
        self.shape = shape
        self.kind = kind
        self.size = size

    p1 = Fruit("Tophat", "Red", "Leather")
    p2 = Fruit("Tophat", "Red", "Leather")
    p3 = Fruit("Tophat", "Red", "Leather")
    p4 = Fruit("Tophat", "Red", "Leather")

    print(p1.kind)
    print(p2.kind)
    print(p3.kind)
    print(p4.kind)