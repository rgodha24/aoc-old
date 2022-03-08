passengerID = 0
x = [] * 300
iterateNumber = 0
dataPointCount = 0
correctCount = 0
entryNumber = 0
with open("passport.txt") as file:
    for line in file:
        for letterNumber in range(len(line)):
            letter1 = line[letterNumber]
            # finding if it is a new line and checking if there were enough data points
            if letter1 == "\n" and len(line) == 1:
                entryNumber += 1
                if dataPointCount >= 14:
                    correctCount += 1
                    print("entry number " + str(entryNumber) + " is correct. Correct number: " + str(correctCount))
                # else:
                    # print(dataPointCount)
                dataPointCount = 0
            # if it is not a new line, do this.
            else:
                # making sure that the index is in range
                if len(line) > letterNumber + 2:
                    letter2 = line[letterNumber + 1]
                    letter3 = line[letterNumber + 2]
                    combinedString = str(letter1) + str(letter2) + str(letter3)

                    # finding byr, iyr, eyr, hgt, hcl, ecl, or pid and counting if they were found. also the extra
                    # parts for part 2
                    if True:
                        # byr iyr eyr hgt hcl ecl pid

                        if str(combinedString) == "byr":

                            byrString = str(line[letterNumber + 4]) + str(line[letterNumber + 5]) + str(line[letterNumber + 6]) + str(line[letterNumber + 7])
                            byr = int(byrString)
                            # print("checking byr and byr string is " + byrString + " and byr times 2 is " + str(byr*2))

                            if 1920 <= byr <= 2002:
                                dataPointCount += 2
                                # print("found valid " + combinedString)

                        elif str(combinedString) == "iyr":

                            iyrString = str(line[letterNumber + 4]) + str(line[letterNumber + 5]) + str(line[letterNumber + 6]) + str(line[letterNumber + 7])
                            iyr = int(iyrString)
                            # print("checking iyr and iyr string is " + iyrString + " and iyr times 2 is " + str(iyr*2))

                            if 2010 <= iyr <= 2020:
                                dataPointCount += 2
                                # print("found valid " + combinedString)

                        elif str(combinedString) == "eyr":

                            eyrString = str(line[letterNumber + 4]) + str(line[letterNumber + 5]) + str(line[letterNumber + 6]) + str(line[letterNumber + 7])
                            eyr = int(eyrString)
                            # print("checking iyr and iyr string is " + iyrString + " and iyr times 2 is " + str(iyr*2))

                            if 2020 <= eyr <= 2030:
                                dataPointCount += 2
                                # print("found valid " + combinedString)

                        elif str(combinedString) == "hgt":

                            # print("found hgt")

                            if len(line) > letterNumber + 7:
                                # hgt:12in is format. 0-2 hgt, 3 is :, 4-5 numbers, 6-7 are in.
                                # must be between 59-76
                                # checks for in

                                if str(line[letterNumber + 6]) + (line[letterNumber + 7]) == "in":
                                    # gets height number into int.
                                    hgtString = str(line[letterNumber + 4]) + str(line[letterNumber + 5])
                                    hgt = int(hgtString)

                                    # checks if number is in the range
                                    if 59 <= hgt <= 76:
                                        dataPointCount += 2
                                        # print("found valid hgt in inches")

                                # hgt:123cm is format. 1 is g, 2 is t, 3 is :, 4-6 are numbers, 7-8 is cm
                                # must be between 150 - 193 inclusive
                                # checks for cm

                                elif len(line) > letterNumber + 8:
                                    if str(line[letterNumber + 7]) + (line[letterNumber + 8]) == "cm":
                                        # gets height number into int.
                                        hgtString = str(line[letterNumber + 4]) + str(line[letterNumber + 5]) + str(line[letterNumber + 6])
                                        hgt = int(hgtString)

                                        # checks if number is in the range
                                        if 150 <= hgt <= 193:
                                            dataPointCount += 2
                                            # print("found valid hgt in cm")

                        elif str(combinedString) == "hcl":
                            # hcl:#123abc
                            # 0-2 hcl, 3 :, 4 #, 5-11 abcdef 0123456789
                            hclNumber = 0
                            if len(line) > letterNumber + 10:

                                # print("checked line length")

                                if line[letterNumber+4] == "#":
                                    # checks each of the strings after the #
                                    for i in range(letterNumber + 5, letterNumber + 11, 1):
                                        z = line[i]
                                        if z in "abcdef0123456789":
                                            # print("number " + str(i) + " is correct. The letter is " + z)
                                            hclNumber += 1
                            # print("hcl number is " + str(hclNumber))

                            '''hclVar = ''
                            for i in range(5,10,1):
                                hclVar = hclVar + line[i]'''

                            if hclNumber == 6:
                                dataPointCount += 2
                                # print("found valid hcl")

                        elif str(combinedString) == "ecl":
                            # amb blu brn gry grn hzl oth

                            eclWord = line[letterNumber + 4] + line[letterNumber + 5] + line[letterNumber + 6]
                            if eclWord == "amb":
                                dataPointCount += 2
                                # print("found valid ecl. color: " + eclWord)
                            elif eclWord == "blu":
                                dataPointCount += 2
                                # print("found valid ecl. color: " + eclWord)
                            elif eclWord == "brn":
                                dataPointCount += 2
                                # print("found valid ecl. color: " + eclWord)
                            elif eclWord == "gry":
                                dataPointCount += 2
                                # print("found valid ecl. color: " + eclWord)
                            elif eclWord == "grn":
                                dataPointCount += 2
                                # print("found valid ecl. color: " + eclWord)
                            elif eclWord == "hzl":
                                dataPointCount += 2
                                # print("found valid ecl. color: " + eclWord)
                            elif eclWord == "oth":
                                dataPointCount += 2
                                # print("found valid ecl. color: " + eclWord)

                        elif str(combinedString) == "pid":
                            # 3 :, 456789
                            pidCount = 0
                            y = letterNumber + 4
                            temp = ""
                            while line[y] != " " and line[y] != "\n" and line[y] != "\t":
                                temp = temp + line[y]
                                y += 1
                                # print("y is " + str(y) + " and temp is " + temp)
                                if y > len(line):
                                    break
                                if line[y] == " " or line[y] == "\n" or line[y] == "\t":
                                    break
                            if len(temp) == 9:
                                pidCount = 0
                                for i in temp:
                                    if i in "0123456789":
                                        pidCount += 1
                            if pidCount == 9:
                                dataPointCount += 2
                                # print("found valid pid")

                        elif str(combinedString) == "cid":
                            dataPointCount += 1
                            # print("found " + combinedString)
