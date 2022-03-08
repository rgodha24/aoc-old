global correctCount
correctCount = 0
def verifyPassword(numbers, letters, password):
    letter = letters[0]
    low, high = numbers.split('-')
    highAnswer = 0
    lowAnswer = 0
    # print("low is " + str(low) + " high is " + str(high))
    count = 0

    if password[int(low)-1] == letter:
        lowAnswer = 1
    if password[int(high)-1] == letter:
        highAnswer = 1

    if lowAnswer + highAnswer == 1:
        answer = True
    else:
        answer = False

    return answer



with open('passwords.txt') as file:

    for line in file:

        numbers, letter, password = line.split()
        # print("numbers is " + numbers + " and letter is " + letter + " and password is " + password)

        if verifyPassword(numbers, letter, password) == True:
            correctCount += 1
            print(correctCount)

