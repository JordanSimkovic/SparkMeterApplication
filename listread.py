list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def printList(numString, index, numList, increment):
    numString += str(numList[index]) + ", "

    try:
        numList[index + increment]
    except IndexError:
        return numString

    return printList(numString, index + increment, numList, increment)
print(printList("", 2, list1, 3))
