ride = { "Tubathum" : 100, "Charles" : 300, "Martinet" : 60, "Barkley" : 705, "Peter" : 92 }

for x in ride.values():
    if x >= 100:
        print("This person is tall enough to ride.")
    else:
        print("This person is too short to ride.")
