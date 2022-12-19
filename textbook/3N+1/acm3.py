import sys
memoize = {}

def getNumberOfCycles_recursive(input_number):
    orig_number = int(input_number)
    cycles = 0
    if memoize.get(str(orig_number), None) is not None:
        return memoize[str(orig_number)]
    
    if input_number == 0 or input_number == 1:
        return 0
    else:
        cycles = getNumberOfCycles_recursive(3 * input_number + 1 if input_number%2 != 0 else input_number/2) + 1
    memoize[str(orig_number)] = cycles 
    return cycles

if __name__ == "__main__":
    series = []
    series_len = 0
    for n in sys.stdin:
        series = n.strip("\n").split()
        if len(series) == 2:
            series[0] = int(series[0])
            series[1] = int(series[1])
            numberOfCycles = 0
            for i in range(min(series[0], series[1]), max(series[0], series[1])+1):
                cycles = getNumberOfCycles_recursive(i)
                if cycles > numberOfCycles:
                    numberOfCycles = cycles

            result = numberOfCycles + 1
            print(series[0], series[1], result)
            series = []
