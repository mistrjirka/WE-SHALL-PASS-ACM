import cProfile

# Calculating results of 3n+1 for num1
listOfLoopLength = [0 for _ in range(1000000)]


def calculateResult(start, end):
    maxLoopCount = 0
    for x in range(start, end+1):
        loopCount = 1
        tempNum = x
        while tempNum != 1:
            if tempNum % 2 == 0:
                tempNum = int(tempNum / 2)
            else:
                tempNum = 3 * tempNum + 1
            if tempNum < x and listOfLoopLength[tempNum - 1] != 0:
                loopCount += listOfLoopLength[tempNum - 1]
                break
            loopCount += 1
        listOfLoopLength[x - 1] = loopCount
        if loopCount > maxLoopCount:
            maxLoopCount = loopCount
    return maxLoopCount


# Main function
def main():

    file1 = open('data.txt', 'r')
    Lines = file1.readlines()

    for line in Lines:
        # Creating variables
        tempArray = line.split()
        firstNum = int(tempArray[0])
        secondNum = int(tempArray[1])

        # Second num is allways bigger
        if firstNum > secondNum:
            end = firstNum
            start = secondNum
        elif firstNum < secondNum:
            end = secondNum
            start = firstNum
        else:
            end = firstNum
            start = firstNum

        # Calculating max loop length
        loopCount = calculateResult(start, end)

        # Printing result
        print(firstNum, secondNum, loopCount)


if __name__ == '__main__':
    cProfile.run('main()')
    #main()