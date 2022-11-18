#include <stdio.h>
#include <stdlib.h>
#include <math.h>

long max(long *num1, long *num2)
{
    if (*num1 > *num2)
        return *num1;
    else
        return *num2;
}

long find_max_sum(int *num_monsters, long *coins)
{
    long coin_sum[*num_monsters + 1];
    coin_sum[0] = coins[0];
    coin_sum[1] = max(&coins[1], &coin_sum[0]);
    int i = 2;
    while (i < *num_monsters)
    {
        long prev_coins = coin_sum[i - 1];
        long curr_coin_sum = coins[i] + coin_sum[i - 2];
        coin_sum[i] = max(&prev_coins, &curr_coin_sum);
        i++;
    }
    return coin_sum[*num_monsters - 1];
}

void solve_case(int num_case)
{
    int num_monsters;
    scanf("%d", &num_monsters);
    long coins[num_monsters + 1];
    long final_sum = 0;
    for (size_t i = 0; i < num_monsters; i++)
    {
        scanf("%ld", &coins[i]);
    }
    switch (num_monsters)
    {
    case 0:
        final_sum = 0;
        break;
    case 1:
        final_sum = coins[0];
        break;
    case 2:
        final_sum = max(&coins[0], &coins[1]);
        break;
    default:
        final_sum = find_max_sum(&num_monsters, coins);
        break;
    }
    printf("Case %d: %ld\n", num_case, final_sum);
}

int main(void)
{

    int cases;
    scanf("%d", &cases);
    for (size_t i = 0; i < cases; i++)
    {
        solve_case(i + 1);
    }

    return 0;
}