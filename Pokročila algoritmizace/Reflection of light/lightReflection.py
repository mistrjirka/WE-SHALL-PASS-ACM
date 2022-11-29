import sys


def calcFibonanci(ivNum):
    n1, n2 = 1, 1
    # first two terms
    count = 0
    while count < ivNum:
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
    return n2


# Main function
def main():
    for tempInput in sys.stdin:
        # Creating variable
        tempArray = tempInput.split()
        lvNum = int(tempArray[0])
        print(calcFibonanci(lvNum))


# Start of program
if __name__ == '__main__':
    main()
