with open("data.txt") as file:
    data = file.read()

print(data)

for i in range(len(data)):
    mylist = data[i:i + 4]
    myset = set(mylist)
    lenlist = len(myset)
    if lenlist == 4:
        print(mylist)
        print(i)
        break
