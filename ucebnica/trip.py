import sys
import math

def main():
    num_array = []
    n_array = []
    sum = 0

    for tempInput in sys.stdin:
        number = tempInput.split()[0]
        if number.find(".") == -1:
            n = int(number)
            if n == 0:
                break
            n_array.append(n)
        else:
            num_array.append(float(tempInput.split()[0]))
    for i in range(len(n_array)):
        average = 0
        sum = 0
        n = n_array[i]
        for k in range(n):
            sum = sum + num_array[k]
        average = sum / n
        max = 0.00
        min = 0.00
        for j in range(n):
            a = int((num_array[j] - average) * 100.0) / 100.0
            if a > 0:
                max = max + a
            else:
                min = min + a
        min *= -1

        if max > min:
            print('${0:.2f}'.format(abs(max)))
        else:
            print('${0:.2f}'.format(abs(min)))

        for _ in range(n):
            num_array.pop(0)

if __name__ == "__main__":
    main()