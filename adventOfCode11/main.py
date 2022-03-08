import math


# so basically X[0] is the first row, X[1] is the second row
# X[0][1] is the first column and the second row

def returnCount(column, row, list):
    count = 0
    ListOfCoordinates = [[-1, 1], [-1, 0], [-1, -1], [0, 1], [0, -1], [1, 1], [1, 0], [1, -1]]
    for i in range(8):  # this determines which of the 8 directions we are looking in
        run = 1
        k = 1
        while run == 1:
            if 0 <= column + k * ListOfCoordinates[i][0] < len(list[0]) and 0 <= row + k * ListOfCoordinates[i][
                1] < len(list):
                Seat = findValueOfSeat(column + k * ListOfCoordinates[i][0], row + k * ListOfCoordinates[i][1], list)
                if Seat == "#":
                    count += 1
                    run = 0
                elif Seat == "L":
                    run = 0
                else:
                    k += 1
            else:
                run = 0
    return count  # returns the amount of occupied seats someone can see


def checkSeat(line, lineBefore, lineAfter, letterInt, lineInt, file):
    occupiedNumber = 0
    loopVar = 0
    # checking if needs to be occupied
    # checking if top line exists
    if line[letterInt] == ".":
        return "."
    else:
        if lineInt != 0:
            # top left
            loopVar = min(lineInt, letterInt)
            while True:
                try:
                    if (file[lineInt - i])[letterInt - i] == "L":
                        break
                        i += 1
                    elif (file[lineInt - i])[letterInt - i] == "#":
                        i += 1
                        occupiedNumber += 1
                        break
                    else:
                        i += 1
                except:
                    break

            loopVar = lineInt
            while True:
                try:
                    if (file[lineInt - i])[letterInt] == "L":
                        break
                        i+=1
                    elif (file[lineInt - i])[letterInt] == "#":
                        occupiedNumber += 1
                        i +=1
                        break
                    else: i+= 1;
                except:
                    break

            loopVar = min(lineInt, len(line) - letterInt)
            while True:
                try:
                    if (file[lineInt - i])[letterInt + i] == "L":
                        i += 1
                        break
                    if (file[lineInt - i])[letterInt + i] == "#":
                        i += 1
                        occupiedNumber += 1
                        break
                    else: i += 1
                except:
                    break

        # middle line
        # left
        if letterInt != 0:
            loopVar = letterInt
            while True:
                try:
                    if (file[lineInt])[letterInt - i] == "L":
                        break
                    if (file[lineInt])[letterInt - i] == "#":
                        occupiedNumber += 1
                        break
                    i += 1
                except:
                    break
        # print("letterInt is " + str(letterInt) + " and the len of line is " + str(len(line)) + " and middle is " + line[letterInt])
        # right
        loopVar = len(line) - letterInt
        while True:
            try:
                if (file[lineInt])[letterInt + i] == "L":
                    break
                if (file[lineInt])[letterInt + i] == "#":
                    occupiedNumber += 1
                    break
                i += 1
            except:
                break

        # print("start " + lineAfter + " finished")

        # bottom line
        if line != lineAfter:
            # bottom left
            if letterInt != 0:
                loopVar = min(len(file) - lineInt, letterInt)
                while True:
                    try:
                        if (file[lineInt + i])[letterInt - i] == "L":
                            break
                        if (file[lineInt + i])[letterInt - i] == "#":
                            occupiedNumber += 1
                            break
                        i += 1
                    except:
                        break

            # bottom right
            if letterInt + 1 != len(line):
                loopVar = min(len(file) - lineInt, len(line) - letterInt)
                while True:
                    # print(i)
                    try:
                        j = file[lineInt + i]
                        if j[letterInt + i] == "L":
                            break
                        if j[letterInt + i] == "#":
                            occupiedNumber += 1
                            break
                        i += 1
                    except:
                        break

            # bottom
            loopVar = len(file) - lineInt
            while True:
                try:
                    if (file[lineInt + i])[letterInt] == "L":
                        break
                    if (file[lineInt + i])[letterInt] == "#":
                        occupiedNumber += 1
                        break
                    i += 1
                except:
                    break
        # occupiedNumber = returnCount(letterInt, lineInt, file)

        if occupiedNumber != returnCount(letterInt, lineInt, file):
            print("failed on line number " + str(lineInt) + " and letter number " + str(letterInt) + ". got " + str(
                occupiedNumber) + " and correct was " + str(returnCount(letterInt, lineInt, file)))

        if occupiedNumber == 0 and line[letterInt] == "L":
            return "#"

        elif 1 <= occupiedNumber < 5:
            return line[letterInt]


        elif line[letterInt] == "#" and occupiedNumber >= 5:
            return "L"

        else:
            return line[letterInt]


def findValueOfSeat(column, row, list):
    return list[row][column]


if __name__ == "__main__":
    with open("input.txt") as fileInput:
        file = list(fileInput)
        for line in range(len(file)):
            file[line] = file[line].strip()
        print(file)
        while True:
            lineBefore = " "
            newFile = file.copy()
            for lineInt in range(len(file)):
                # print(str(lineInt) + " is lineInt")
                if lineInt > 0:
                    lineBefore = file[lineInt - 1].strip()
                line = file[lineInt].strip()
                if lineInt + 1 != len(file):
                    lineAfter = file[lineInt + 1].strip()
                newLine = ""
                for letterInt in range(len(line)):
                    newLine = newLine + checkSeat(line, lineBefore, lineAfter, letterInt, lineInt, file)
                    # print(newLine)
                newFile[lineInt] = newLine
            # print(file)
            print(newFile)

            if newFile == file:
                # print(newFile)
                break

            file = newFile.copy()

        for line in newFile:
            print(line)

        count = 0
        for line in newFile:
            for char in line:
                if char == "#":
                    count += 1
        print(count)
