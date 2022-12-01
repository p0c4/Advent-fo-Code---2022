from itertools import groupby

with open("data_puzzle1.txt") as data:
    lists = data.readlines()

result = [[string.rstrip() for string in group] for key, group in groupby(lists, lambda s: s != "\n") if key]

result_int = []
for _ in result:
    new_l = [int(x) for x in _]
    result_int.append(new_l)

sums_list = []
for ls in result_int:
    sums_list.append(sum(ls))

l_sorted = sorted(sums_list, reverse=True)

max_sum = l_sorted[0]
max_three_sum = l_sorted[0] + l_sorted[1] + l_sorted[2]

print(f"Max sum is: {max_sum}\nMax 3 sum is: {max_three_sum}")


