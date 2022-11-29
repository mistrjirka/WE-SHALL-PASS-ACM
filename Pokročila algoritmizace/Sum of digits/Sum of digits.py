import sys
import math


def get_digit(number, n):
    return number // 10 ** n % 10


def calcSum(ivNum1, ivNum2):
    array = [0] * 100000000
    index = 0
    for x in range(int(ivNum1), int(ivNum2) + 1):
        digits = int(math.log10(x)) + 1
        for y in range(0, digits):
            array[index] = get_digit(x, y)
            index += 1
    return sum(array)


# Main function
def main():
    for tempInput in sys.stdin:
        # Creating variable
        tempArray = tempInput.split()
        lvNum1 = tempArray[0]
        lvNum2 = tempArray[1]
        if lvNum1 == "-1" and lvNum2 == "-1" or lvNum1 == -1 and lvNum2 == -1:
            return 0
        print(calcSum(lvNum1, lvNum2))


# Start of program
if __name__ == '__main__':

    main()
