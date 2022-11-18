envs = {
    "A": [3, 2],
    "W": [-5, -10],
    "F": [-20, 5]
}

def get_max_time(case):
    h = case[0]
    a = case[1]
    last_move = str()
    l = 1
    while h > 0 and a > 0:
        if l % 2 == 0:
            if h > 5 and a > 10:
                last_move = "W"
            elif h > 20 and a <= 10:
                last_move = "F"
            else:
                break
        else:
            last_move = "A"
        h = h + envs[last_move][0]
        a = a + envs[last_move][1]
        l += 1

    return l-1


def main():
    num_cases = int(input())
    cases = []
    for _ in range(num_cases):
        try:
            input_line = input().split(" ")
            cases.append([int(input_line[0]), int(input_line[1])])
        except EOFError:
            break
    for case in cases:
        print(get_max_time(case))


if __name__ == "__main__":
    main()
