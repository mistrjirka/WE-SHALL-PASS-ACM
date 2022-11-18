#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int sum_digits(int num, int factor, long *sums)
{
    int sum_of_digits = 0;
    for (int i = factor; i > -1; i--)
    {
        int curr_count = 0;
        while (num > pow(10, i))
        {
            num = num - pow(10, i);
            curr_count++;
        }
        sum_of_digits += curr_count;
    }
    return sum_of_digits;
}

int main(void)
{
    int a, b;
    long *sums = (long *)calloc(1000000, sizeof(long));

    while (scanf("%d %d", &a, &b) && (a != -1 && b != -1))
    {
        int sum_of_digits = 1;
        for (int i = a; i < b + 1; i++)
        {
            if (sums[i - 1] != 0)
            {
                sum_of_digits += sums[i - 1];
            }
            else
            {
                sum_of_digits += sum_digits(i, 9, sums);
            }
        }
        printf("%d\n", sum_of_digits);
    }

    free(sums);
}