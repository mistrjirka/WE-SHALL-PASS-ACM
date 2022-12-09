import math 
def getMultipleInputs(num_of_inputs, question):
    result = []
    valid = False
    while len(result) != num_of_inputs and not valid:
        #stolen from https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
        result = [int(x) for x in input(question).split()]
    return result

def factorial(top, end=2):
    if top == 0:
        return 1
    if top == 1 or top ==2:
        return top
    if top - end == 0:
        return 1
    for i in range(top-1,end ,-1):
        top*= i
    return top

def solve_combinations(n,m):
    start = m
    dividor = n-m
    result_top = n
    if(n-m == 0):
        result_top = 1
    else:
        result_top = start
        for i in range(start + 1, n+1):
            result_top *= i
    return int(result_top / math.factorial(dividor))
    

if __name__ == "__main__":
    x,y = getMultipleInputs(2, "")
    inputs = []
    while x != 0 and y != 0:
        inputs.append((x, y))
        x,y = getMultipleInputs(2, "")

    for inp in inputs:
        n = inp[0]
        m = inp[1]
        print(inp[0], "things taken", inp[1], "at a time is", int(factorial(n,m)/factorial(n-m)),"exactly.") 
    
