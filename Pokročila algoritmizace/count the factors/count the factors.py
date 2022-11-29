
if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            lvTempResult = 0
            if n>9:
                lvTempResult += (n%9)*81
                n -= n
            lvTempResult += (n%10)**2
            print(lvTempResult)
        except EOFError:
            break
