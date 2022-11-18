import math


def calculate_diameter(D, V):
    precomp = -6*(V - math.pi*((D/2)**2)*D + math.pi*D**3/12)/math.pi
    return math.pow(precomp, 1/3)


def main():
    run = True
    while run:
        input_seq = input().split(' ')
        if input_seq == ['0', '0']:
            run = False
            break
        D = int(input_seq[0])
        V = int(input_seq[1])
        print("{:.3f}".format(calculate_diameter(D, V)))


if __name__ == "__main__":
    main()
