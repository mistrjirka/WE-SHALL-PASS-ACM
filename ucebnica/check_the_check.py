#white king = K
#black king = k

def find_black_king(board):
    king_found = False

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "k":
                king_found = True
                return (i, j)
        if king_found:
            break

def find_white_king(board):
    king_found = False

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "K":
                king_found = True
                return (i, j)
        if king_found:
            break

def is_bk_under_attack(board, bk_coordinates, counter):
    results = []
    results.append(check_pawn(board, bk_coordinates))
    if True in results:
        print("Game #" + str(counter) + ": black king is in check.")
        return True
    results.append(check_rook(board, bk_coordinates))
    if True in results:
        print("Game #" + str(counter) + ": black king is in check.")
        return True
    results.append(check_bishop(board, bk_coordinates))
    if True in results:
        print("Game #" + str(counter) + ": black king is in check.")
        return True
    results.append(check_queen(board, bk_coordinates))
    if True in results:
        print("Game #" + str(counter) + ": black king is in check.")
        return True
    results.append(check_knight(board, bk_coordinates))
    if True in results:
        print("Game #" + str(counter) + ": black king is in check.")
        return True

def is_wk_under_attack(board, wk_coordinates, counter):
    results = []
    results.append(check_pawn1(board, wk_coordinates))
    if True in results:
        print("Game #" + str(counter) + ": white king is in check.")
        return True
    results.append(check_rook1(board, wk_coordinates))
    if True in results:
        print("Game #" + str(counter) + ": white king is in check.")
        return True
    results.append(check_bishop1(board, wk_coordinates))
    if True in results:
        print("Game #" + str(counter) + ": white king is in check.")
        return True
    results.append(check_queen1(board, wk_coordinates))
    if True in results:
        print("Game #" + str(counter) + ": white king is in check.")
        return True
    results.append(check_knight1(board, wk_coordinates))
    if True in results:
        print("Game #" + str(counter) + ": white king is in check.")
        return True


def check_pawn(board, bk_coordinates):
    row = bk_coordinates[0] + 1 
    col = bk_coordinates[1] - 1
    if row < 8 and col >= 0:
        if board[row][col] == "P":
            return True
    row = bk_coordinates[0] + 1 
    col = bk_coordinates[1] + 1
    if row < 8 and col < 8:
        if board[row][col] == "P":
            return True

def check_rook(board, bk_coordinates):
    dir1 = [-1, 0, 0, 1]
    dir2 = [0, -1, 1, 0]

    for i in range(len(dir1)):
        row = bk_coordinates[0]
        col = bk_coordinates[1]
        while True:
            row += dir1[i]
            col += dir2[i]
            if row < 0 or col < 0 or row >= 8 or col >= 8:
                break
            if board[row][col] == "R":
                return True
            if board[row][col] != ".":
                break

def check_queen(board, bk_coordinates):
    dir1 = [-1, -1, -1, 0, 0, 1, 1, 1]
    dir2 = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(len(dir1)):
        row = bk_coordinates[0]
        col = bk_coordinates[1]
        while True:
            row += dir1[i]
            col += dir2[i]
            if row < 0 or col < 0 or row >= 8 or col >= 8:
                break
            if board[row][col] == "Q":
                return True
            if board[row][col] != ".":
                break

def check_bishop(board, bk_coordinates):
    dir1 = [-1, -1, 1, 1]
    dir2 = [-1, 1, -1, 1]

    for i in range(len(dir1)):
        row = bk_coordinates[0]
        col = bk_coordinates[1]
        while True:
            row += dir1[i]
            col += dir2[i]
            if row < 0 or col < 0 or row >= 8 or col >= 8:
                break
            if board[row][col] == "B":
                return True
            if board[row][col] != ".":
                break

def check_knight(board, bk_coordinates):
    dir1 = [-2, -2, -1, -1, 1, 1, 2, 2]
    dir2 = [-1, 1, -2, 2, -2, 2, -1, 1]

    for i in range(len(dir1)):
        row = bk_coordinates[0] + dir1[i]
        col = bk_coordinates[1] + dir2[i]
        if row >= 0 and col >= 0 and row < 8 and col < 8:
            if board[row][col] == "N":
                return True

#White king
def check_pawn1(board, bk_coordinates):
    row = bk_coordinates[0] - 1 
    col = bk_coordinates[1] + 1
    if row >= 0 and col < 8:
        if board[row][col] == "p":
            return True
    row = bk_coordinates[0] - 1 
    col = bk_coordinates[1] - 1
    if row >= 0 and col >= 0:
        if board[row][col] == "p":
            return True

def check_rook1(board, bk_coordinates):
    dir1 = [-1, 0, 0, 1]
    dir2 = [0, -1, 1, 0]

    for i in range(len(dir1)):
        row = bk_coordinates[0]
        col = bk_coordinates[1]
        while True:
            row += dir1[i]
            col += dir2[i]
            if row < 0 or col < 0 or row >= 8 or col >= 8:
                break
            if board[row][col] == "r":
                return True
            if board[row][col] != ".":
                break

def check_queen1(board, bk_coordinates):
    dir1 = [-1, -1, -1, 0, 0, 1, 1, 1]
    dir2 = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(len(dir1)):
        row = bk_coordinates[0]
        col = bk_coordinates[1]
        while True:
            row += dir1[i]
            col += dir2[i]
            if row < 0 or col < 0 or row >= 8 or col >= 8:
                break
            if board[row][col] == "q":
                return True
            if board[row][col] != ".":
                break

def check_bishop1(board, bk_coordinates):
    dir1 = [-1, -1, 1, 1]
    dir2 = [-1, 1, -1, 1]

    for i in range(len(dir1)):
        row = bk_coordinates[0]
        col = bk_coordinates[1]
        while True:
            row += dir1[i]
            col += dir2[i]
            if row < 0 or col < 0 or row >= 8 or col >= 8:
                break
            if board[row][col] == "b":
                return True
            if board[row][col] != ".":
                break

def check_knight1(board, bk_coordinates):
    dir1 = [-2, -2, -1, -1, 1, 1, 2, 2]
    dir2 = [-1, 1, -2, 2, -2, 2, -1, 1]

    for i in range(len(dir1)):
        row = bk_coordinates[0] + dir1[i]
        col = bk_coordinates[1] + dir2[i]
        if row >= 0 and col >= 0 and row < 8 and col < 8:
            if board[row][col] == "n":
                return True


def main():
    counter = 0 
    while True:
        bk_attack = False
        wk_attack = False
        end = ['........', '........', '........', '........', '........', '........', '........', '........']
        board = []
        for i in range(8):
            board.append(input())
        #End of file and terminate the program
        if board == end:
            break
        empty = input()
        
        counter += 1
        bk_coordinates = find_black_king(board)
        bk_attack = is_bk_under_attack(board, bk_coordinates, counter)
        if bk_attack != True:
            wk_coordinates = find_white_king(board)
            wk_attack = is_wk_under_attack(board, wk_coordinates, counter)
            if wk_attack != True:
                print("Game #" + str(counter) + ": no king is in check.")



if __name__ == "__main__":
    main()