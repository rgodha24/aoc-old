def search(list, string):
    x = False
    for lineInt in range(len(list)):
        line = list[lineInt]
        for charInt in range(len(line)):
            char = line[charInt]
            if char == string:
                x = True
                return [lineInt, charInt, True]

    if not x:
        return[0,0,False]


if __name__ == "__main__":
    with open("day4.txt") as fileInput:
        file = list(fileInput)

    list = []
    for line in file:
        list.append(line.strip())

    # print(list)

    countingList = list[0].split(",")
    list.pop(0)
    list.pop(0)
    print(countingList)
    for i in range(len(countingList)):
        countingList[i] = int(countingList[i])

    print(countingList)
    # print(list)

    board = []
    temp = []
    for boardInt in range(0, len(list), 6):
        temp.clear()
        for lineInt in range(len(list[boardInt:boardInt + 5])):
            # print(list[lineInt+boardInt])
            temp.append(list[lineInt + boardInt].strip().split())
        # print(temp)
        board.append(temp.copy())

    print(board)

    # making board int
    for i in range(len(board)):
        for j in range(len(board[i])):
            for k in range(len(board[i][j])):
                board[i][j][k] = int(board[i][j][k])

    print(board)

    for string in countingList:
        # print("number we are searching for is " + str(string))
        # changing numbers for this count
        for i in range(len(board)):
            x = []
            x = search(board[i], string)
            if x[2]:
                board[i][x[0]][x[1]] = -1
            # print("changed i, x[0], x[1]", i, x[0], x[1])

        # checking for lines
        for n in range(len(board)):
            i = board[n]
            # print(i)
            # vertical line first
            correct = False
            # iterating on left -> right
            for j in range(5):
                temp = []
                for k in range(5):
                    temp.append(i[k][j])

                sum = 0
                for k in temp:
                    sum += k

                if sum == -5:
                    board.pop(n)
                    print(board)
                    correct = True
                    break

            # horizontal line
            for j in range(5):
                temp = i[j]

                sum = 0
                for k in temp:
                    sum += k

                if sum == -5:
                    board.pop(n)
                    print(board)
                    correct = True
                    break

            if correct:
                break

