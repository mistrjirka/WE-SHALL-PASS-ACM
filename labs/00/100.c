#include <stdio.h>
#include <stdlib.h>

int incrementer(long i, long j, long *counts, int result_index)
{
    int max_steps = 0;
    long start, stop;
    if (i > j)
    {
        start = j;
        stop = i;
    }
    else
    {
        start = i;
        stop = j;
    }
    /*start = i;
    stop = j;*/
    long k = 0;
    for (k = start; k <= stop; k++)
    {
        int n_steps = 1;
        long n = k;
        while (n != 1)
        {

            if (n % 2 == 0)
            {
                n = n / 2;
            }
            else
            {
                n = 3 * n + 1;
            }

            if (n < k && counts[n] != 0)
            {
                n_steps += counts[n];
                break;
            }
            n_steps++;
        }
        counts[k] = n_steps;
        if (n_steps > max_steps)
        {
            max_steps = n_steps;
        }
    }
    return max_steps;
}

int main(void)
{
    long *counts = (long *)calloc(1000000, sizeof(long));
    /* int *results = (int *)calloc(3000000, sizeof(int));*/
    long num1, num2;
    int r, steps = 0, result_index = 0;
    while ((r = scanf("%ld %ld", &num1, &num2)) == 2 && r != EOF)
    {
        steps = incrementer(num1, num2, counts, result_index);
        printf("%ld %ld %d\n", num1, num2, steps);
        result_index++;
    }
    /* int i = 0;
      for (i = 0; i < result_index; i++)
    {
          printf("%d %d %d\n", results[3 * i], results[3 * i + 1], results[3 * i + 2]);
      }*/
    free(counts);
    /* free(results);*/

    return 0;
}