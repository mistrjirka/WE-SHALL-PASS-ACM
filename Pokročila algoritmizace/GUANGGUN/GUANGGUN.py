import sys

ERASTIC_SIFTER = 1000000


def eratosthenovo_sito(do):
    do += 1
    sito = [True] * do

    for i in range(2, do):
        if sito[i]:
            for j in range(i ** 2, do, i):
                sito[j] = False

    prvocisla = []
    for i in range(2, do):
        if sito[i]:
            prvocisla.append(i)
    return prvocisla


primeArray = eratosthenovo_sito(ERASTIC_SIFTER)
for tempInput in sys.stdin:
    n = int(tempInput.split()[0])
    if n == 0:
        break
    lvCount = 0
    for x in primeArray:
        if n % x == 0:
            lvCount += 1
    print(n, ":", lvCount)
