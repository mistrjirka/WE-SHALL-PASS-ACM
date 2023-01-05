import sys

def insertion_sort(array):
    for i in range(1, len(array)):
        element = array[i]
        pos = i - 1
        while pos >= 0 and array[pos] > element:
            array[pos + 1] = array[pos]
            pos -= 1
        array[pos + 1] = element
    return array

def main():
    test_cases = int(input())
    for tmpInput in sys.stdin:
        line = tmpInput.split()
        line.pop(0)
        unsorted_arr = [eval(i) for i in line]
        sorted_arr = insertion_sort(unsorted_arr)
        if len(sorted_arr) % 2 == 0:
            middle = int(len(sorted_arr) / 2) - 1
        else:
            middle = int(len(sorted_arr) / 2)
        
        total = 0
        for element in sorted_arr:
            if element == sorted_arr[middle]:
                continue
            total += abs(element - sorted_arr[middle])
        print(total)

if __name__ == "__main__":
    main()