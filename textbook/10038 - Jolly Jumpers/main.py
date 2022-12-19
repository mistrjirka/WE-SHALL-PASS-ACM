import sys

if __name__ == "__main__":
    for n in sys.stdin:
        series = n.strip("\n").split()
        sequence = [int(x) for x in series]
        n = sequence[0]
        sequence = sequence[1:]
        differences = set()
        jolly = True
        if n == 1:
            print("Jolly")
            continue
        for index, num in enumerate(sequence):
            if index + 1 >= n:
                break
            
            diff = abs(sequence[index] - sequence[index + 1])
            differences.add(diff)
        for i in range(1, n):
            if i not in differences:
                jolly = False
                break
        if jolly:
            print("Jolly")
        else:
            print("Not jolly")