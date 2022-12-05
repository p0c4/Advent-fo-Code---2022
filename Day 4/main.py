with open("puzzle4_data.txt") as file:
    data = []
    for d in file.readlines():
        d = d.strip("\n")
        t = d.replace("-", ",")
        l1 = t.split(",")
        data.append(l1)

overlapping = []
for d in data:
    if int(d[1]) < int(d[2]) or int(d[3]) < int(d[0]):
        continue
    else:
        overlapping.append(d)

print(len(overlapping))
