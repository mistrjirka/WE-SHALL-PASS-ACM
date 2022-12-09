import math
if __name__ == "__main__":
    n = int(input())
    while n != 0:
        pole = []
        average = 0
        for i in range(n):
            cost = float(input())
            average += cost
            pole.append(cost)
        average /= n

        to_transfer = 0
        
        high = 0
        low = 0
        for el in pole:
            difference = round((el - average)*100)/100
            if difference > 0:
                high += difference
            else:
                low += difference
        low *= -1
        if low < high:
            to_transfer = low
        else:
            to_transfer = high
        
        print(f"${round(to_transfer*100)/100:.2f}")
        n = int(input())


