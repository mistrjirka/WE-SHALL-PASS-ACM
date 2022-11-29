import sys


# Calculating results of 3n+1 for num1

def calculateResult(start, end):
    maxLoopCount = 0
    for x in range(start, end + 1):
        loopCount = 1
        tempNum = x
        while tempNum != 1:
            if tempNum % 2 == 0:
                tempNum = int(tempNum / 2)
            else:
                tempNum = 3 * tempNum + 1
            loopCount += 1
        if loopCount > maxLoopCount:
            maxLoopCount = loopCount
    return maxLoopCount


# Main function
def main():
    for tempInput in sys.stdin:
        # Creating variable
        firstNum, secondNum = tempInput.split()
        firstNum = int(firstNum)
        secondNum = int(secondNum)

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


# Start of program
if __name__ == '__main__':
    main()
