with open("day6.txt") as fileInput:
    file = list(fileInput)

inputList = file[0].split(",")

for i in range(len(inputList)):
    inputList[i] = int(inputList[i])

print(inputList)
countingList = []
for i in range(9):
    countingList.append(0)

# counting numbers in input list
for i in inputList:
    countingList[i] += 1

print(countingList)

def switchList(list):
    temp = []
    for i in range(9):
        temp.append(0)
    for i in range(8):
        temp[i] = int(list[i+1]/1)

    # now we have to deal with all of the 0s
    temp[6] += int(list[0])
    temp[8] += int(list[0])

    return temp

temp = []
for i in range(256):
    temp.clear()
    temp = switchList(countingList).copy()
    countingList = temp.copy()
    print(countingList)

count = 0
for i in countingList:
    count += i

print(count)