l_1 = ["N", "C", "R", "T", "M", "Z", "P"]
l_2 = ["D", "N", "T", "S", "B", "Z"]
l_3 = ["M", "H", "Q", "R", "F", "C", "T", "G"]
l_4 = ["G", "R", "Z"]
l_5 = ["Z", "N", "R", "H"]
l_6 = ["F", "H", "S", "W", "P", "Z", "L", "D"]
l_7 = ["W", "D", "Z", "R", "C", "G", "M"]
l_8 = ["S", "J", "F", "L", "H", "W", "Z", "Q"]
l_9 = ["S", "Q", "P", "W", "N"]

dict_l = {1: l_1, 2: l_2, 3: l_3, 4: l_4, 5: l_5, 6: l_6, 7: l_7, 8: l_8, 9: l_9}

with open("puzzle5_data1.txt") as file:
    data_list = [v.split(" ")[1::2] for v in file.readlines()]

for (x, y, z) in data_list:
    move_from = int(y)
    move_to = int(z)
    list_1 = dict_l[move_from]
    list_2 = dict_l[move_to]
    for i in range(int(x)):
        list_2.extend(list_1[-1])
        del list_1[-1]
    dict_l.update({move_from: list_1, move_to: list_2})

for i in range(9):
    print(dict_l[i+1][-1])

