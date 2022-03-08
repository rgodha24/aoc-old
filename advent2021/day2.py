if __name__ == "__main__":
    with open("day2.txt") as fileInput:
        file = list(fileInput)


    list = []
    for line in file:
        list.append(line.split(" "))

    hCount = 0
    vCount = 0
    aim = 0
    for line in list:

        if "f" in line[0]:
            hCount += int(line[1])
            vCount += aim * int(line[1])
        elif "up" in line[0]:
            # vCount = vCount - int(line[1])
            aim = aim - int(line[1])
        elif "down" in line[0]:
            # vCount = vCount + int(line[1])
            aim = aim + int(line[1])

        print(vCount)
    print(hCount)
    print(vCount)
    print(hCount * vCount)