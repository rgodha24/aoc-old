with open("day9.txt") as fileInput:
    file = list(fileInput)

list = []
x = []
for i in range(len(file[0].strip())+2):
    x.append(9)


list.append(x)
for line in file:
    temp = []
    temp.clear()
    temp.append(9)
    for char in line.strip():
        temp.append(int(char))
    temp.append(9)
    list.append(temp)
list.append(x)

print(list)

count = 0
for lineInt in range(1,len(list)-1):
    for charInt in range(1, len(list[0])-1):
        char = list[lineInt][charInt]
        print(char)
        bigger = 0
        if True:
            # checking above
            if list[lineInt-1][charInt] > char:
                bigger += 1

            # below
            if list[lineInt+1][charInt] > char:
                bigger += 1

            # left
            if list[lineInt][charInt-1] > char:
                bigger += 1

            # right
            if list[lineInt][charInt + 1] > char:
                bigger += 1

        if bigger == 4:
            count += char +1
            print("count is " + str(count) + " and char is " + str(char))

