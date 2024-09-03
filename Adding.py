shapes = {

"Triangle": 8,

"Circle": 15,

"Square": 10,

"Rectangle" : 12

}

shape = input("shape")

height = int(input("height"))

shapes[shape] = height

print(shapes)