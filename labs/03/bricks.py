def main():
    ones_count = [0]
    k_count = [0]
    ones_count.append(1)
    k_count.append(1)
    for i in range(2, 1001):
        ones_count.append(k_count[i-1])
        k_count.append(k_count[i-1] + ones_count[i-1])

    while True:
        try:
            num = int(input())
            if num == 0:
                print("1")
            else:
                print(k_count[num] + ones_count[num])

        except EOFError:
            break


if __name__ == "__main__":
    main()
