def main():

    while True:
        try:
            num = int(input())
            if num == 0:
                print("1")
            else:
                a, b = 1, 1
                for i in range(num):
                    a, b = b, b+a
                print(b)
        except EOFError:
            break


if __name__ == "__main__":
    main()
