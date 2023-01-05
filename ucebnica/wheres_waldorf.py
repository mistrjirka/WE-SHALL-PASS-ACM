import sys

def find_word(r, c, word, idx, grid, row, column, word_len):
    dir1 = [-1, -1, -1, 0, 0, 1, 1, 1]
    dir2 = [-1, 0, 1, -1, 1, -1, 0, 1]

    is_word = False
    for i in range(8):
        if is_word == True:
            break
        tmp_row = r + dir1[i]
        tmp_col = c + dir2[i]
        while True:
            if word_len == 0:
                is_word = True       
                break
            if tmp_row >= 0 and tmp_col >= 0 and tmp_row < row and tmp_col < column:
                if grid[tmp_row][tmp_col] == word[idx]:
                    idx += 1
                    word_len -= 1
                    tmp_row = tmp_row + dir1[i]
                    tmp_col = tmp_col + dir2[i]
                else:
                    idx = 1
                    word_len = len(word) - 1
                    break
            else:
                idx = 1
                word_len = len(word) - 1
                break
    if is_word:
            return (r, c)
    else:
        return False

def main():
    number_of_test_cases = int(input())

    while number_of_test_cases > 0:
        empty_space = input()
        grid = []
        grid_size = input().split(" ")
        row = int(grid_size[0])
        column = int(grid_size[1])
        row_tmp = row
        while row_tmp > 0:
            grid.append(input().lower())
            row_tmp -= 1
        number_of_words = int(input())
        while number_of_words > 0:
            idx = 0
            word = input().lower()
            word_len = len(word)
            find = False
            for r in range(len(grid)):
                if find == True:
                    break
                for c in range(len(grid[r])):
                    if grid[r][c] == word[idx]:
                        idx += 1
                        word_len -= 1
                        if word_len <= 0:
                            idx = 0
                            print(str(r + 1) + " " + str(c + 1))
                            find = True
                            break
                        else:
                            coordinates = find_word(r, c, word, idx, grid, row, column, word_len)
                            idx = 0
                            if coordinates:
                                print(str(coordinates[0] + 1) + " " + str(coordinates[1] + 1))
                                find = True
                                break
                    else:
                        idx = 0
                        word_len = len(word)
            number_of_words -= 1
        number_of_test_cases -= 1
        #Space between each test case in output
        if number_of_test_cases > 0:
            print("")

if __name__ == "__main__":
    main()