work = {"Monday" : 1, "Tuesday" : 2, "Wednesday" : 3, "Thursday" : 4, "Friday" : 5}

work["Saturday"] = 6

work.pop("Wednesday")

print(len(work))
if "Friday" in work:
    print(work)