import sys
directions = (
    (1,0),
    (0,1),
    (1,1),
    (-1, 0),
    (0, -1),
    (-1,-1),
    (-1,1),
    (1,-1)
)

def count_mines_arround(x,y, field):
    mines_to_return = 0
    if x < len(field):
        if y < len(field[x]):
            if field[x][y] == "*":
                return "*"

    for direction in directions:
        x_test = x+direction[0]
        y_test = y+direction[1]
        if x_test < len(field) and x_test >= 0:
            if y_test < len(field[x_test]) and y_test >= 0:
                if field[x_test][y_test] == "*":
                    mines_to_return += 1
    return str(mines_to_return)


if __name__ == "__main__":    
    width, height = [eval(i) for i in input().split()]
    inputs = []
    while width != 0 or height != 0:
        lines = []
        for i in range(width):
            try:
                in_str = input()
            except EOFError:
                break

            if in_str and len(in_str):
                lines.append([*(in_str)])
        inputs.append(lines)
        try:
            in_str = input()
        except EOFError:
            break
        if len(in_str):
            width, height = [eval(i) for i in in_str.split()]

    
    for i, lines in enumerate(inputs):
        result = []
        for x,line in enumerate(lines):
            result.append([])
            for y,cell in enumerate(line):
                result[x].append(count_mines_arround(x, y, lines))
        print(f"Field #{i+1}:")
        for res in result:
            for cell in res:
                print(cell, end="")
            print()
        if i < len(inputs)-1:
            print()
    