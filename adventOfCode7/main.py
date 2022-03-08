# first we have to get the input into a useful format
import time
X = []
start = time.time()

def findBag(string, list):
    answer = []

    answerIndex = 0
    for lineInt in range(len(list)):
        line1 = list[lineInt]
        for inside in line1[1]:
            if inside == string:
                answer.append(0)
                answer[answerIndex] = lineInt
                answerIndex += 1

    return answer


with open("input.txt") as fileInput:
    file = list(fileInput)
    for line in file:
        firstSplit = line.split(" contain ")
        # print(firstSplit)
        secondSplit = firstSplit[1].split(", ")
        for i in range(len(secondSplit)):
            secondSplit[i] = (secondSplit[i])[2:]
            secondSplit[i] = secondSplit[i].strip(" \n.")
        firstSplit[1] = secondSplit
        X.append(firstSplit)

    print(X)
    checkedList = []
    for i in range(len(X)):
        checkedList.append(False)

    inputCheck = "shiny gold bag"
    foundIn = findBag(inputCheck, X)
    for i in foundIn:
        checkedList[(int(i))] = True

    print(checkedList)
    trueList = []
    newList = checkedList.copy()
    while True:
        print("new loop iteration")
        checkedList = newList.copy()
        trueList.clear()
        # we need to make an array of bags that we already know are allowed so we can check if it allows us to change any other bags
        trueListInt = 0
        for i in range(len(checkedList)):
            if checkedList[i]:  # == True
                trueList.append(0)
                trueList[trueListInt] = i
                trueListInt += 1

        # now we have a list of values that we already have a way to get to. now, we have to iterate on this list and check if those bags are in any others.

        for i in trueList:
            answer = findBag(X[i][0], X)  # i bc that is the line number of array. 0 bc that is the first thing in the array, which is the bag color.
            for j in answer:
                newList[j] = True

        # print(newList)
        if newList == checkedList:
            count = 0
            for i in newList:
                if i:
                    count += 1
            print(count)
            break

end = time.time()
print(end-start)