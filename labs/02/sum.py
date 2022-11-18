sums = [[[-1 for i in range(2)] for j in range(180)]for k in range(20)]


def to_digits(x):
    digit = []
    while x:
        digit.append(x % 10)
        x //= 10
    return digit


def sum_of_digits(index, sumof, tight, digit):
    if index == -1:
        return sumof
    if sums[index][sumof][tight] != -1 and tight != 1:
        return sums[index][sumof][tight]
    ret = 0
    k = digit[index] if tight else 9
    for i in range(0, k+1):
        newTight = tight if digit[index] == i else 0
        ret += sum_of_digits(index-1, sumof+i, newTight, digit)
    if not tight:
        sums[index][sumof][tight] = ret
    return ret


def sum_of_range(a, b):
    a_digits = to_digits(int(a))
    b_digits = to_digits(int(b))
    ans1 = sum_of_digits(len(a_digits)-1, 0, 1, a_digits)
    ans2 = sum_of_digits(len(b_digits)-1, 0, 1, b_digits)
    return ans2-ans1+1


def main():
    while True:
        init_line = input().split(' ')
        a, b = init_line[0], init_line[1]
        if int(a) == -1 and int(b) == -1:
            break
        else:
            sum = sum_of_range(a, b)
            print(sum)


if __name__ == "__main__":
    main()
