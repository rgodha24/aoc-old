x = input().split("\t")

print(x)
L = len(x[0])
count = [0, 0, 0, 0, 0]
finalCount = 1
#1/1
for i in range(len(x)):
    t = x[i]
    if t[1*i % len(x[0])] == "#":
        count[0] += 1
print(count[0])
#1/3
for i in range(len(x)):
    t = x[i]
    if t[3*i % len(x[0])] == "#":
        count[1] += 1
print(count[1])
#1/5
for i in range(len(x)):
    t = x[i]
    if t[5*i % len(x[0])] == "#":
        count[2] += 1
print(count[2])
#1/7
for i in range(len(x)):
    t = x[i]
    if t[7*i % len(x[0])] == "#":
        count[3] += 1
print(count[3])
#2/1
for i in range(int(len(x)/2)):
    t = x[2*i]
    if t[1*i % len(x[0])] == "#":
        count[4] += 1
print(count[4])

for i in range(5):
    if count[i] != 0:
        finalCount = finalCount * count[i]

print(finalCount)