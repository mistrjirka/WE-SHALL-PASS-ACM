#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

void print_sum(int *current_sum)
{
    printf("%d", current_sum[0]);
    size_t k = 1;
    while (current_sum[k] != -1)
    {
        printf("+%d", current_sum[k]);
        k++;
    }
    putchar('\n');
}

void copy_arrs(int *source, int *dest, int *length)
{
    size_t i;
    for (i = 0; i < *length; i++)
    {
        dest[i] = source[i];
    }
}

bool compare_sums(int *sum1, int *sum2, int *max_length)
{
    size_t i = 0;
    bool ret = false;
    if (sum2[0] == 0)
        return true;
    while (i < *max_length && (sum1[i] != -1 && sum2[i] != -1))
    {
        if (sum1[i] != sum2[i])
        {
            ret = true;
            break;
        }
        else
            i++;
    }
    return ret;
}

void sum_digits(int *numbers, int *t, int *n)
{
    int prev_sum[*n];
    prev_sum[0] = 0;
    int found_sums = 0;
    printf("Sums of %d:\n", *t);
    size_t i;
    for (i = 0; i < *n; i++)
    {
        printf("Current main number is %d\n", numbers[i]);
        if (numbers[i] > *t)
            continue;

        else if (numbers[i] == *t)
        {
            printf("%d\n", numbers[i]);
            found_sums++;
        }
        else
        {
            size_t j;
            for (j = i + 1; j < *n; j++)
            {
                printf("Current secondary number is %d\n", numbers[j]);
                int curr_sum_value = numbers[i];
                int curr_sum[*n];
                curr_sum[0] = numbers[i];
                size_t k = j;
                size_t num_in_sum = 1;
                while (curr_sum_value < *t && k < *n)
                {
                    if (numbers[k] + curr_sum_value <= *t)
                    {
                        printf("Summing with number %d\n", numbers[k]);
                        curr_sum_value += numbers[k];
                        curr_sum[num_in_sum] = numbers[k];
                        num_in_sum++;
                    }
                    k++;
                }
                curr_sum[num_in_sum] = -1;
                if (curr_sum_value == *t && compare_sums(curr_sum, prev_sum, n))
                {
                    found_sums++;
                    print_sum(curr_sum);
                    copy_arrs(curr_sum, prev_sum, n);
                }
            }
        }
    }
    if (found_sums == 0)
        printf("NONE\n");
}

int main(void)
{
    int n, t;
    while (scanf("%d %d", &t, &n) && n != 0)
    {
        int *numbers = (int *)malloc(n * sizeof(int));
        size_t i;
        for (i = 0; i < n; i++)
        {
            scanf("%d", &numbers[i]);
        }
        sum_digits(numbers, &t, &n);
        free(numbers);
    }
    return 0;
}