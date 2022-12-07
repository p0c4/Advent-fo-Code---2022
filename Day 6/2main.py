with open("data.txt") as file:
    data = file.read()

print(data)

for i in range(len(data)):
    mylist = data[i:i + 14]
    myset = set(mylist)
    lenlist = len(myset)
    if lenlist == 14:
        print(mylist)
        print(i+14)
        break
