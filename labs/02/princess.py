
def get_max_profit(count, coins):
    if count == 0:
        return 0
    elif count == 1:
        return coins[0]
    elif count == 2:
        return max(coins)
    else:
        i = 2
        sum = [coins[0], coins[1]]
        while (i < count):
            sum.append(max(coins[i-1], coins[i]+sum[i-2]))
            i += 1
        return sum[-1]


def main():
    num_cases = int(input())
    for i in range(num_cases):
        try:
            monster_count = int(input())
            monster_coins = [int(x) for x in input().split(" ")]
            print(f"Case {i+1}:", get_max_profit(monster_count, monster_coins))

        except EOFError:
            break


if __name__ == "__main__":
    main()
