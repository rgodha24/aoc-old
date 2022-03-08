def simplify(string):
    openParentheses = False
    startInt = 0
    endInt = len(string)
    w = ""
    for charInt in range(len(string)):
        char = string[charInt]
        if char == "(":
            startInt = charInt
        elif char == ")":
            endInt = charInt
    # if there are parentheses
    print(startInt)
    print(endInt)
    if startInt != 0:
        print(string[startInt+1:endInt-1])
        w = simplify(string[startInt+1:endInt-1])

    elif startInt == 0:
        if string[1] == "*":
            w = int(string[0]) * int(string[2])
        elif string[1] == "+":
            w = int(string[0]) + int(string[2])
        else:
            w = "FAILED L LL LL L L"
    print("w is " + str(w))
    answer1 = ""
    if startInt != 0:
        answer1 = string[startInt:]
    answer2 = str(w)
    answer3 = ""
    if endInt != len(string):
        answer3 = string[endInt:]
    print("answer1 is " + answer1 + " answer2 is " + answer2 + " answer 3 is " + answer3)
    answer = answer1 + answer2 + answer3
    print(answer)
    return answer

with open("input.txt") as fileInput:
    file = []
    file2 = list(fileInput)
    for lineInt in range(len(file2)):
        line = ""
        # print(lineInt)
        line2 = file2[lineInt]
        for char in line2:
            # print(char)
            if char != " ":
                line = line + char

        # print(line)
        file.append(line)
    print(file)

    for line in file:
        simplify(line)
