import sys

def sort_flapjacks(line, position, arr_len):
    new_line = []
    for i in range(arr_len):
        new_line.append(0)
    for i in range(arr_len):
        if i > (arr_len - position):
            new_line[i] = line[i]
        else:
            new_line[arr_len - position - i] = line[i]
    return new_line

def main():
    for tempInput in sys.stdin:
        line = tempInput.split(" ")
        arr_len = len(line)
        length = len(line) - 1
        line[length] = line[length].replace("\n", "")
        sorted_line = sorted(line, key=int)
        position = 0
        for i in range(length):
            print(line[i], end=" ")
        print(line[length])
        while True:
            if line == sorted_line:
                print("0")
                break
            elif line[0] == sorted_line[length]:
                length -= 1
                position += 1
                line = sort_flapjacks(line, position, arr_len)
                print(position, end=" ")
            elif line[arr_len - position - 1] == sorted_line[arr_len - position - 1]:
                length -= 1
                position += 1
            else:
                for i in range(arr_len):
                    if line[i] == sorted_line[length]:
                        print(arr_len - i, end=" ")
                        line = sort_flapjacks(line, (arr_len - i), arr_len)
                        break

if __name__ == "__main__":
    main()