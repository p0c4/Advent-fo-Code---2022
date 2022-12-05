with open("puzzle4_data.txt") as file:
    data = []
    for d in file.readlines():
        d = d.strip("\n")
        t = d.replace("-", ",")
        l1 = t.split(",")
        data.append(l1)

fully_contain = []
for d in data:
    if (int(d[0]) >= int(d[2]) and int(d[1]) <= int(d[3])) or (int(d[0]) <= int(d[2]) and int(d[1]) >= int(d[3])):
        fully_contain.append(d)

print(len(fully_contain))
