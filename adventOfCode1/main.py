x = str(input("input: "))

list = x.split()
print(list)

for i in list:
    var1 = int(i)
    for j in list:
        var2 = int(j)
        for k in list:
            var3 = int(k)
            if var1 + var2 + var3 == 2020:
                print(var1 * var2 * var3)
                break
