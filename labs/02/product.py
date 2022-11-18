import math


def get_max_prod(numbers):
    max_prod = 0
    for i in range(len(numbers)):
        for k in range(i, len(numbers)):
            prod = math.prod(numbers[i:k+1])
            max_prod = max(max_prod, prod)

    return max_prod


def main():
    run = True
    num_cases = 0
    while run:
        try:
            num = int(input())
            numbers = list(map(int, input().split(' ')))
            num_cases += 1
            print(
                f"Case #{num_cases}: The maximum product is {get_max_prod(numbers)}.")
            print("")

            if input() == '':
                continue

        except EOFError:
            break


if __name__ == "__main__":
    main()
