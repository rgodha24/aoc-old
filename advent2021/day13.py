with open("day13.txt") as fileInput:
    file = list(fileInput)


temp = ""
for line in file:
    temp += line

x = temp.split("\n\n")
n = x[1].strip().split("=")

print(x)

list = x[0].split()
checkList = []

temp = []
for i in range(11):
    temp.append(False)
for i in range(15):
    checkList.append(temp.copy())

print(checkList)

for line in list:
    temp = line.split(",")
    x = int(temp[0])
    y = int(temp[1])
    print(x, y)

    checkList[y][x] = True

count = 0
for line in checkList:
    temp = ""
    for char in line:
        if char:
            count += 1
            temp += "#"
        if not char:
            temp += "."

    print(temp)

if y in n[0]:
    checkList[int(n[1])
    for i in reversed(checkList[int(n[1]):]):



print(checkList)
print(count)