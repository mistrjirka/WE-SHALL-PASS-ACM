import sys

def fib_dyn(n):
    a = 0
    b = 1
    result = 0
    if n == 1 or n == 2:
        result = 1
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b



if __name__ == '__main__':
    n = int(input())
    results = []
    while n != 0:
        print(fib_dyn(n+2))
        n = int(input())
    """for result in results:
        print(result)"""

        