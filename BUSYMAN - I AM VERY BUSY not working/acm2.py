import itertools
numberOfTestCases = 0
testArray = []
results = []
#stolen from https://www.geeksforgeeks.org/python-intersection-two-lists/
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def getMultipleInputs(num_of_inputs):
    result = []
    valid = False
    while len(result) != num_of_inputs or not valid:
        try:
            #stolen from https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
            result = [int(x) for x in input("Enter " + str(num_of_inputs) + " values: ").split()]
            if result[1] > result[0]:
                valid = True
            else: 
                valid = False
        except:
            result = []
    return result

if __name__ == "__main__":
    numberOfTestCases = int(input())
    for i in range(1, numberOfTestCases+1):
        numberOfTasks = int(input())
        arrayOfTasks=[]
        for j in range(1, numberOfTasks+1):
            task = getMultipleInputs(2)
            arrayOfTasks.append(task)
        testArray.append(arrayOfTasks)

    for test in testArray:
        # trying to figure out test case
        tasks = test
        canBeTogetger = 0
        if len(tasks) == 1:
            canBeTogetger = 1
        for task1, task2 in itertools.combinations(tasks, 2):
            if len(intersection(task1, task2)) == 0:
                canBeTogetger += 1
        
        results.append(canBeTogetger)
    
    print("results")
    for i in results:
        print(i)
                    


