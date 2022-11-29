# Imports
import sys

ON = 1  # ON do something OFF do nothing
OFF = 0


# My functions

def check_out_of_bounce(ivStartingPoint, ivIndex, ivData):  # returns True if the point is out of bounce.
    if ivStartingPoint.x + ivIndex.x < 0 or ivStartingPoint.y + ivIndex.y < 0:  # Check row and column >0
        return True
    if ivStartingPoint.y + ivIndex.y >= len(ivData):  # Check column max out of bounce
        return True
    if ivStartingPoint.x + ivIndex.x >= len(ivData[ivIndex.y]):  # Check row max out of bounce
        return True
    return False


def search_direction(ivRowIndex, ivDirection, ivData):
    lvStartPos = Vector2i(0, ivRowIndex)
    currentPosition = Vector2i(lvStartPos.y + ivDirection.y, lvStartPos.x + ivDirection.x)
    if check_out_of_bounce(lvStartPos, ivDirection, ivData):
        return 0
    if ivData[currentPosition.y][currentPosition.x] == '*':
        return 1
    else:
        return 0


def look_for_mines(ivData, ivCollum):
    lvMineString = ""
    for x in range(0, len(ivData[0])):
        lvMineCount = 0
        if ivData[ivCollum][x] == '*':
            lvMineCount = '*'
        else:
            for dirY in range(-1, 2):
                for dirX in range(-1, 2):
                    if dirX != 0 or dirY != 0:
                        lvDirection = Vector2i(dirY, dirX)
                        lvMineCount += search_direction(x, lvDirection, ivData)
        lvMineString += lvMineCount.__str__()
    return lvMineString


def append_line(ivLine, ivData):
    lvTempLine = []
    for x in range(len(ivLine)):
        lvTempLine.append(ivLine[x])
    ivData.append(lvTempLine)


# My class

class Vector2i:
    def __init__(self, y, x):
        self.y = y
        self.x = x


class MineField:
    def __init__(self, ivColumnCnt, ivRowCnt):
        self.rowCnt = ivRowCnt  # Row count
        self.collCnt = ivColumnCnt  # Column count
        self.matrix = []


# Main function
def main():
    # Initialize
    lvLoadTable, lvCalculating = ON, ON
    lvMineField = MineField(0, 0)
    lvFieldIndex = 1

    for tempInput in sys.stdin:
        # Creating variable
        if lvLoadTable == ON:  # Load the size of the array
            tempArray = tempInput.split()
            lvColumnCount = int(tempArray[0])
            lvRowCount = int(tempArray[1])
            if lvRowCount == 0 or lvColumnCount == 0:
                break
            else:
                print(f'Field #{lvFieldIndex}')
                lvFieldIndex += 1
                lvLoadTable = OFF
                lvMineField = MineField(lvColumnCount, lvRowCount)
                continue

        append_line(tempInput.strip(), lvMineField.matrix)
        if len(lvMineField.matrix) > 3:
            lvMineField.matrix.pop(0)

        if lvMineField.rowCnt == 1:
            print(look_for_mines(lvMineField.matrix, 1))
            lvMineField.matrix.pop(0)
            print(look_for_mines(lvMineField.matrix, 1))
            lvLoadTable = ON
            continue

        elif len(lvMineField.matrix) == 2:
            test = look_for_mines(lvMineField.matrix, 0)
            print(test)
        elif len(lvMineField.matrix) > 2:
            print(look_for_mines(lvMineField.matrix, 1))

        lvMineField.rowCnt -= 1


# Start of program
if __name__ == '__main__':
    main()
