import sys


# Function to find the smallest divisor
def smallestDivisor(n):
    # if divisible by 2
    if (n % 2 == 0):
        return 2;

    # iterate from 3 to sqrt(n)
    i = 3;
    while (i * i <= n):
        if (n % i == 0):
            return i;
        i += 2;

    return n;


for tempInput in sys.stdin:
    n = int(tempInput.split()[0])
    if n == 0:
        break
    print(countDividors(n))
