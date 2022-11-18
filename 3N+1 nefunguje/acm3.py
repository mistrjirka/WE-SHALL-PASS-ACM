def getMultipleInputs(num_of_inputs):
    result = []
    valid = False
    while len(result) != num_of_inputs and not valid:
        try:
            #stolen from https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
            result = [int(x) for x in input("Enter " + str(num_of_inputs) + " values: ").split()]
            if result[0] < 10000 and result[0] > 0 and result[1] < 10000 and result[1] > 0:
                valid = True
        except:
            result = []
    return result


def getNumberOfCycles(input_number):
    cycles = 0
    while input_number != 1 and input_number != 0:
        cycles += 1
        if input_number%2:
            input_number = 3* input_number + 1
        else:
            input_number = input_number/2
    return cycles


if __name__ == "__main__":
    while True:
        series = getMultipleInputs(2)
        numberOfCycles = 0
        for i in range(series[0], series[1]+1):
            cycles = getNumberOfCycles(i)
            if cycles > numberOfCycles:
                numberOfCycles = cycles

        result = numberOfCycles + 1
        print(series[0], series[1], result)
