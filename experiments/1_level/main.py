import sys

def fib_dyn(n, memo):
    if memo[n] is not None:
        return memo[n]
    result = 0
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_dyn(n-1, memo) + fib_dyn(n-2, memo)
    memo[n] = result
    return result


"""
def fib(n):
    result = 0
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result
"""



def get_nth(n):
    arr = [None for _ in range(0, n+1)]
    return fib_dyn(n, arr)

if __name__ == '__main__':
    
    for n in sys.stdin:
        chnging = int(n)
        print(get_nth(chnging+2))
            
        
# print(fib(n))
