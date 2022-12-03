with open("puzzle2_data.txt") as file:
    data = file.readlines()

for turn in range(len(data)):
    new_data = data[turn]
    data[turn] = new_data[0::2]
print(data)
score = 0
for choice in data:
    print(choice)
    if choice[0] == "A":
        if choice[1] == "X":
            score += 4
        elif choice[1] == "Y":
            score += 8
        elif choice[1] == "Z":
            score += 3
    elif choice[0] == "B":
        if choice[1] == "X":
            score += 1
        elif choice[1] == "Y":
            score += 5
        elif choice[1] == "Z":
            score += 9
    elif choice[0] == "C":
        if choice[1] == "X":
            score += 7
        elif choice[1] == "Y":
            score += 2
        elif choice[1] == "Z":
            score += 6

print(score)
