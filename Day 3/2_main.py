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

rng = 0
group_letters = []
for _ in range(100):
    for lit in new_data[rng]:
        if lit in new_data[rng + 1] and lit in new_data[rng + 2]:
            group_letters.append(lit)
            rng += 3
            break

score = 0
for let in group_letters:
    index = l_list.index(let)
    score += n_list[index]

print(score)
