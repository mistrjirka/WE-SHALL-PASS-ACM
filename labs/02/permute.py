def invert_permutation(perm):
    inverted_perm = [0 for _ in range(len(perm))]
    for i in range(len(perm)):
        inverted_perm[perm[i]-1] = i+1
    return inverted_perm


def main():
    run = True
    while run:
        num = int(input())
        if num == 0:
            break
        perm = [int(x) for x in input().split(" ")]
        inv_perm = invert_permutation(perm)
        if all([perm[i] == inv_perm[i] for i in range(num)]):
            print("ambiguous")
        else:
            print("not ambiguous")


if __name__ == "__main__":
    main()
