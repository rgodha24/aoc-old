with open("day5.txt") as fileInput:
    file = list(fileInput)

list1 = []
for line in file:
    list1.append(line.strip())

list = list1.copy()
print(list)
checkList = [["."]*10]*10

x = []
for line in list:
    x.clear()
    x = line.split("->")
    startA = 0
    startB = 0
    endA = 0
    endB = 0
    # print(line)
    # print(x[0], x[1])
    startA, startB = x[0].strip().split(",")
    endA, endB = x[1].strip().split(",")

    print(startA, startB, endA, endB)

    if startA == endA or startB == endB:
        # determining which equals which
        if startB == endB:
            for i in range(min(int(startA), int(endA)), max(int(startA), int(endA)) +1, 1 ):
                if checkList[int(startB)][i] == ".":
                    line = checkList[int(startB)].copy()
                    line[i] = 1
                    checkList[int(startB)] = line.copy()
                else:
                    line = checkList[int(startB)].copy()
                    line[i] += 1
                    checkList[int(startB)] = line.copy()
        elif startA == endA:
            for i in range(min(int(startB), int(endB)), max((int(startB), int(endB))) + 1, 1):
                if checkList[i][int(startA)] == ".":
                    line = checkList[i].copy()
                    line[int(startA)] = 1
                    checkList[i] = line.copy()
                else:
                    line = checkList[i].copy()
                    line[int(startA)] += 1
                    checkList[i] = line.copy()

        # diagonal :)
    else:
        if True:
            dLength = 0
            h = 0
            j = 0
            k = 0
            l = 0
            print("diagonal!! on line " + line)
            if int(startA) > int(endA):
                h = -1
                j = -1
                k = 1
                l = 0
            elif int(startA) < int(endA):
                h = 1
                j = 1
                k = 0
                l = 1

            for i in range(int(startA) + k, int(endA) + j, h):
                # checking if negative goes positive or negative
                sign = 0
                if int(startB) > int(endB):
                    sign = -1
                elif int(endB) > int(startB):
                    sign = 1

                iterationNumber = i - min(int(startA), int(endA))
                lineNumber = abs(int(startB) + iterationNumber * sign  - k * int(startA))
                print("changing line number " + str(lineNumber) + " and character number " + str(i))
                if checkList[lineNumber][i] == ".":
                    line = checkList[lineNumber].copy()
                    line[i] = 1
                    checkList[lineNumber] = line.copy()
                else:
                    line = checkList[lineNumber].copy()
                    line[i] += 1
                    checkList[lineNumber] = line.copy()


        print(checkList)

for line in checkList:
    temp = ""
    for char in line:
        temp += str(char)
    print(temp)

count = 0
for line in checkList:
    for char in line:
        if char != "." and int(char) >= 2:
            count += 1

print(count)