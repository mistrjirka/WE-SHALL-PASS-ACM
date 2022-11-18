import math


def get_ops(n):
    num_ops = 0
    while n > 0:
        # print(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = find_smaller(n)
        num_ops += 1
    return num_ops


def find_smaller(n):
    if n == 3:
        return 2
    elif n-1 == 0:
        return n - 1
    a = n+1
    count_a = 1
    count_b = 1
    while a % 2 == 0:
        a //= 2
        count_a += 1
    b = n - 1
    while b % 2 == 0:
        b //= 2
        count_b += 1

    return n-1 if count_a < count_b else n+1


def main():
    run = True
    while run:
        try:
            ops = 0
            num = int(input())
            if num == 0:
                pass
            elif num == 1:
                ops = 1
            elif num == 2:
                ops = 2
            else:
                ops = get_ops(num)

            print(ops)

        except EOFError:
            run = False


if __name__ == "__main__":
    main()
