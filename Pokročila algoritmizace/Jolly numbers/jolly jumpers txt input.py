def calculateTemporaryResults(ivArrayCalc, ivArraySafe):
    for index, item in enumerate(ivArrayCalc):
        if index > len(ivArrayCalc) - 2:
            break
        item = int(item)
        tempResult = item - int(ivArrayCalc[index + 1])
        tempResult = abs(tempResult)
        ivArraySafe.append(tempResult)


def isJollySequence(array, n):
    arrayOfResults = []
    if n == 1:
        return "Jolly"
    calculateTemporaryResults(array, arrayOfResults)
    missing_value = set(range(1, n)) - set(arrayOfResults)
    if missing_value:
        return "Not jolly"
    else:
        return "Jolly"


# Main function
def main():
    fileOpen = open("data.txt", "r")
    lines = fileOpen.readlines()
    for line in lines:
        # Creating variable
        tempArray = line.split()
        n = int(tempArray[0])
        tempArray.pop(0)
        isJolly = isJollySequence(tempArray, n)
        # Printing result
        print(isJolly)


# Start of program
if __name__ == '__main__':
    main()
