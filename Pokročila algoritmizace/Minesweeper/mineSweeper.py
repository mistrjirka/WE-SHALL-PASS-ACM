# Imports
import sys


def check_out_of_bounce(ivRow, ivCol, ivData):  # returns True if the point is out of bounce.
    if ivRow < 0 or ivCol < 0:  # Check row and column >0
        return True
    if ivCol >= len(ivData):  # Check column max out of bounce
        return True
    if ivRow >= len(ivData[ivCol]):  # Check row max out of bounce
        return True
    return False


def search_directions(ivRow, ivCol, ivData):
    lvMineCount = 0
    for dirY in range(-1, 2):
        for dirX in range(-1, 2):
            if dirX != 0 or dirY != 0:
                if check_out_of_bounce(dirX + ivRow, dirY + ivCol, ivData):
                    continue
                elif ivData[dirY + ivCol][dirX + ivRow] == '*':
                    lvMineCount += 1
    return lvMineCount.__str__()


def look_for_mines(ivCol, ivData):
    lvMineString = ""
    for lvRowIndex in range(0, len(ivData[ivCol])):
        if ivData[ivCol][lvRowIndex] == '*':
            lvMineString += '*'
        else:
            lvMineString += search_directions(lvRowIndex, ivCol, ivData)
    return lvMineString


if __name__ == '__main__':
    # Initialize
    lvLoadTable = True
    lvFieldIndex = 1
    lvRowsToPrint = 0
    lvMineField = []
    for tempInput in sys.stdin:
        # Load input
        if lvLoadTable:
            tempArray = tempInput.split()
            if len(tempArray) != 2:
                continue
            lvRowsToPrint = int(tempArray[0])
            lvColumnCount = int(tempArray[1])
            if lvRowsToPrint == 0 or lvColumnCount == 0:
                break
            else:
                print("Field #" + lvFieldIndex.__str__() + ":")
                lvMineField = []
                lvFieldIndex += 1
                lvLoadTable = False
                continue
        # Append input
        lvMineField.append([*tempInput.strip()])
        if len(lvMineField) > 3:
            lvMineField.pop(0)
        if len(lvMineField) == 2:
            print(look_for_mines(0, lvMineField))
        if len(lvMineField) == 3:
            print(look_for_mines(1, lvMineField))

        lvRowsToPrint -= 1
        if lvRowsToPrint == 0:
            lvMineField.pop(0)
            print(look_for_mines(1, lvMineField))
            print()
            lvLoadTable = True
