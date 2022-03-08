if __name__ == "__main__":
    with open("day3.txt") as fileInput:
        file = list(fileInput)
    list = []
    for line in file:
        list.append(line.strip())
    print(list)
    hi = 0
    temp = ""
    gamma = ""
    epsilon = ""
    for charInt in range(len(list[0].strip()) - 1):
        temp = ""
        print("char int is " + str(charInt))
        x = 0
        y = 0

        for lineInt in range(len(list)):
            temp = temp + str(list[lineInt][charInt])
        if True:
            print("temp is " + temp)
            for i in temp:
                if i == "0":
                    x += 1
                elif i == "1":
                    y += 1
            # oxygen
            print("x is " + str(x) + " and y is " + str(y))

            if x > y:
                print("x > y")
                removalList = []
                print(list)
                for i in range(len(temp)):
                    if (list[i])[charInt] == "0":
                        removalList.append(i)
                print(removalList)
                print(len(list))

                for j in reversed(removalList):
                    list.pop(j)

                print(list)
                print(len(list))
            elif y >= x:
                print("y >= x")
                removalList = []
                print(list)
                for i in range(0, len(list), 1):
                    if (list[i])[charInt] == "1":
                        removalList.append(i)
                print(removalList)
                print(len(list) - 1)

                for j in reversed(removalList):
                    list.pop(j)

                print(list)
        print(list)
        '''print(max(x,y))

        if x > y:
            gamma += "1"
            epsilon += "0"
        elif y > x:
            gamma += "0"
            epsilon += "1"

        print(gamma, epsilon)'''
