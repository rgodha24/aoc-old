def checkList(list):
    lineInt = 0
    accCurrent = 0
    visitedList = []
    visitedList.clear()
    for j in range(602):
        visitedList.append(False)
    while True:
        if len(list) > lineInt:
            line = list[lineInt]
            # print(str(lineInt) + ". Has it been visited? " + str(visitedList[lineInt]))
            if visitedList[lineInt]:
                return "False but the acc was " + str(accCurrent)
            elif lineInt == len(list):
                return "TRUE FINALLY FUCK YEAH" + str(accCurrent)
            x = line.split(" ")
            x[1].replace("\\n", "")
            # print(x)

            if x[0] == "acc":
                accCurrent = accCurrent + int(x[1])
                # print("found acc on line number " + str(lineInt) + " and added " + x[1])
                visitedList[lineInt] = True
                lineInt += 1

            elif x[0] == "jmp":
                visitedList[lineInt] = True
                # print(lineInt)
                lineInt = lineInt + int(x[1])
                # print(str(lineInt) + "\n \n")
            else:
                visitedList[lineInt] = True
                lineInt += 1
        else:
            print(accCurrent)


newList = []
# print("\\n")

with open("input.txt") as fileO:

    file = list(fileO)
    for i in range(len(file)):
        newList.clear()
        newList = file.copy()
        print(newList)
        # print(newList[i])
        x = newList[i].split(" ")
        print(x)
        if x[0] == "jmp":
            x[0] = "nop"
        elif x[0] == "nop":
            x[0] = "jmp"
        newList[i] = x[0] + " " + x[1]
        # print(newList)
        print(checkList(newList))
