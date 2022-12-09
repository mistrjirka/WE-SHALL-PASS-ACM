def smallestDivisor(n):
    if (n % 2 == 0):
        return 2
 
    # iterate from 3 to sqrt(n)
    i = 3
    while(i * i <= n):
        if (n % i == 0):
            return i
        i += 2
 
    return n
         
 
# Driver program
 
 
 
# This code is contrib
if __name__ == "__main__":
    test_cases = []
    results =[]
    num = int(input())
    while num != 0:
        test_cases.append(num)
        num = int(input())

    
    for case in test_cases:
        print(smallestDivisor(case))


