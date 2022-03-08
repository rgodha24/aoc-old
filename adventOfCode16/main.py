# first we want to analyze
with open("input.txt") as fileInput:
    file = list(fileInput)
    print(file)

lower = []
higher = []
x = 0
while file[x] != "\n":
    if file[x] == "\n":
        break

    line = file[x].strip("abcdefghijklmnopqrstuvwxyz: \n \t")
    # print(line)
    line = line.split()
    # print(line)
    x += 1

    for i in line:
        if i != "or":
            w = i.split("-")
            # print(w)

            lower.append(int(w[0]))
            higher.append(int(w[1]))

x += 5
print(lower)
print(higher)
# print(file[x])
wrongVar = 0
y = [[False]*(x-5)]*len(file[x].split(''))
print(y)
while x < len(file):
    line = file[x]
    line = line.strip()
    numbers = line.split(",")
    # print(numbers)
    z = 0
    for i in numbers:
        i = int(i)
        print("new loop")
        wrongCount = 0
        for j in range(len(lower)):
            print(str(j) + " " + str(int(j / 2)))
            if lower[j] <= i <= higher[j]:
                # print("i is correct. i is " + str(i))


            else:
                wrongCount += 1

        if wrongCount == len(lower):
            print("i is wrong. i is " + str(i))
            wrongVar += i

        z += 1

    x += 1

print(wrongVar)