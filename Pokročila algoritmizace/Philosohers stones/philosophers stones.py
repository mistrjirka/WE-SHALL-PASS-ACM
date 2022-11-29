import sys

# Defines
GO_LEFT = -1
GO_RIGHT = 1


# Functions
def check_direction(ivColum, ivRow, ivDirection, ivData):
    lvStartingRow = ivRow
    lvStartingColum = ivColum
    lvIndex = ivDirection
    while ivData[lvStartingColum][lvStartingRow + lvIndex] == 0 and lvStartingRow + lvIndex >= 0:
        ivData[lvStartingColum][lvStartingRow + lvIndex] = 1
        lvIndex += ivDirection


def line_size(ivColum, ivRow, ivData):
    check_direction(ivColum, ivRow, GO_LEFT, ivData)
    check_direction(ivColum, ivRow, GO_RIGHT, ivData)


def print_data(ivData):
    for x in ivData:
        print(x)

def generate_data(ivNumRows, ivNumCols):
    tempData = []
    for y in range(ivNumCols):
        tempRow = []
        for x in range(ivNumRows):
            tempRow.append(0)
        tempData.append(tempRow)
    return tempData

# Main function
def main():
    for tempInput in sys.stdin:
        # Creating variable
        tempArray = tempInput.split()
        data = []
        if len(tempArray) == 1:
            continue
        if len(tempArray) == 2:
            height = int(tempArray[0])
            width = int(tempArray[1])
            data = generate_data(width, height)
        else:
            ...


# Start of program
if __name__ == '__main__':
    main()
