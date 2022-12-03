import string

l_list = list(string.ascii_letters)

n_list = []
for n in range(len(l_list)):
    n_list.append(n + 1)
    
with open("puzzle3_data.txt") as data:
    dt = data.readlines()
new_data = []
for d in dt:
    d = d.strip('\n')
    new_data.append(d)

same_letters = []
for line in new_data:
    length = int(len(line)/2)
    list_1 = line[:length]
    list_2 = line[length:]
    for l in list_1:
        if l in list_2:
            same_letters.append(l)
            break

score = 0
for let in same_letters:
    index = l_list.index(let)
    score += n_list[index]

print(score)
