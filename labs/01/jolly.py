def check_jolly(n, seq):
    jolly = True
    ref = [i+1 for i in range(n-1)]
    checked = []
    for j in range(len(seq)-1):
        diff = abs(seq[j+1]-seq[j])
        if diff in ref:
            checked.append(diff)
            ref.remove(diff)
        elif diff in checked or diff not in ref:
            jolly = False
            break
    return jolly


def main():
    run = True
    while run:
        try:
            input_seq = input().split(' ')
        except EOFError:
            run = False
            break
        n_count = int(input_seq.pop(0))
        seq = [int(x) for x in input_seq]
        if check_jolly(n_count, seq):
            print("Jolly")
        else:
            print("Not jolly")


if __name__ == "__main__":
    main()
