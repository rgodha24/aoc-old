with open("input.txt") as fileInput:
    a = list(fileInput)
    print(a)
    list = [[[""]*(len(a[0].strip()))]*len(a)]*(6)
    print(list)
    for lineInt in range(len(a)):
        line = a[lineInt].strip()
        print('"' + line + '"')
        for charInt in range(len(line)):
            char = line[charInt]
            list[0][lineInt][charInt] = char
        print(list)
    for i in range(1, len(list)):
        list[i].clear()
    print(list)