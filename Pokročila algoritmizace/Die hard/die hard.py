import sys


class Player:
    def __init__(self, HP, AC):
        self.HP = HP+3
        self.AC = AC+2
        self.LOC = "O"

    def pickPlace(self):
        if self.LOC == "W" or self.LOC == "F":
            self.LOC = "A"
            self.HP += 3
            self.AC += 2
        elif self.AC < 10 and self.HP > 20:
            self.LOC = "F"
            self.HP -= 20
            self.AC += 5
        elif self.AC > 10 and self.HP > 5:
            self.LOC = "W"
            self.HP -= 5
            self.AC -= 10
        elif self.HP>20:
            self.LOC = "F"
            self.HP -= 20
            self.AC += 5
        else:
            self.HP = 0
            self.AC = 0


# Main function
def main():
    for tempInput in sys.stdin:
        # Creating variable
        tempArray = tempInput.split()
        if len(tempArray) == 1:
            continue
        HP = int(tempArray[0])
        AC = int(tempArray[1])
        lvPlayer = Player(HP, AC)
        roundsSurvived = 0
        while lvPlayer.HP > 0:
            lvPlayer.pickPlace()
            roundsSurvived += 1
        print(roundsSurvived)


# Start of program
if __name__ == '__main__':
    main()
