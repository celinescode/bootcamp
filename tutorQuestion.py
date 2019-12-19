

def method_one():
    user_input = input("Enter some number(separate with ,): ")

    stringList = user_input.split(",")

    print(stringList)

    intList = []

    for number in stringList:
        intList += [int(number)]

    pairList = []

    for i in range(0, len(intList)):
        for j in range(i + 1, len(intList)):
            pairList += [(intList[i], intList[j])]

    resultList = []

    for pair in pairList:
        if (pair[0] * pair[1]) % 2 == 0 and (pair[0] + pair[1]) % 2 != 0:
            resultList += [pair]

    for pair in resultList:
        print(pair)


def method_two():
    user_input = input("Enter some number(separate with ,): ")

    stringList = user_input.split(",")

    print(stringList)

    intList = []

    for number in stringList:
        intList += [int(number)]

    resultList = []

    for i in range(0, len(intList)):
        for j in range(i + 1, len(intList)):
            if (intList[i] + intList[j])% 2 == 1:
                resultList += [(intList[i], intList[j])]

    for pair in resultList:
        print(pair)


method_one()
method_two()
