with open("day1.txt") as fileInput:
    file = list(fileInput)

list = []
for i in range(len(file)):
    line = int(file[i].strip())
    list.append(line)

print(list)
count = 0
for i in range(1,len(list)):
    line = list[i]
    lineBefore = list[i-1]
    print(line, lineBefore)
    if line > lineBefore:
        count += 1

print(count)