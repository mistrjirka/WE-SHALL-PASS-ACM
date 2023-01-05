def main():
    test_cases = int(input())
    protests = []
    total = set()
    while test_cases > 0:
        days = int(input())
        parties = int(input())
        for _ in range(parties):
            day = int(input())
            protests.append(day)
        for i in range(len(protests)):
            for j in range(days + 1):
                if j % 7 == 6 or j % 7 == 0:
                    continue
                if j % protests[i] == 0:
                    total.add(j)
        print(len(total))
        protests = [] 
        total = set()
        test_cases -= 1

if __name__ == "__main__":
    main()