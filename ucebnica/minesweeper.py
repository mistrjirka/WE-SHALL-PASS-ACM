import sys

def increase_values_in_matrix(row, col, board, number1, number2):
    dir1 = [-1, -1, -1, 0, 0, 1, 1, 1]
    dir2 = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(8):
        tmp_row = row + dir1[i]
        tmp_col = col + dir2[i]
        if tmp_row >= 0 and tmp_col >= 0 and tmp_row < number1 and tmp_col < number2:
            if board[tmp_row][tmp_col] != -1:
                board[tmp_row][tmp_col] = board[tmp_row][tmp_col] + 1
    return board

def main():
    count_line = 0
    count_board = 0
    board = []
    tmp_line = []
    for tempInput in sys.stdin:
        line = tempInput.split(" ")
        if line[0] == "0" and line[1] == "0":
            break
        if line[0] == "\n":
            continue
        if "." in line[0] or "*" in line[0]:
            if(count_line < number1):
                tmp_line = []
                for element in line[0]:
                    if(element == "."):
                        tmp_line.append(0)
                    elif(element == "*"):
                        tmp_line.append(-1)
                board.append(tmp_line)
                count_line += 1
        else:
            for r in range(len(board)):
                for c in range(len(board[r])):
                    if board[r][c] == -1:
                        board = increase_values_in_matrix(r, c, board, number1, number2)
            if count_board > 0:
                if count_board > 1:
                    print("")
                print("Field #{}:".format(count_board))
                for result_line in board:
                    tmp_string = ""
                    for i in range(len(result_line)):
                        if result_line[i] == -1:
                            tmp_string = tmp_string + "*"
                        else:
                            tmp_string = tmp_string + str(result_line[i])
                    print(tmp_string)
            board = []
            number1 = int(line[0])
            number2 = int(line[1])
            count_board += 1 
            count_line = 0

if __name__ == "__main__":
    main()