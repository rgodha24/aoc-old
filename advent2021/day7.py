import time
from datetime import timedelta

start = time.time()

with open("day7.txt") as fileInput:
    file = list(fileInput)


def findFuel(int):
    x = 0
    for i in range(int + 1):
        x += i

    return x


list = file[0].split(",")

for i in range(len(list)):
    list[i] = int(list[i])

print(list)
count = []
for i in range(1000):
    count.append(0)

for i in range(0, 1000):
    # print(i)
    for j in list:
        count[i] += findFuel(abs(j - i))

answer = 1000000000
for i in count:
    if i > 0:
        # print(answer)
        answer = min(i, answer)

print(answer)
print(answer == 100220525)

end = time.time()
print("time elapsed", timedelta(seconds=abs(start - end)))
