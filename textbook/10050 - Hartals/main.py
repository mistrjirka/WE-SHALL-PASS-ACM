from math import floor

if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        days = int(input())
        parties = int(input())
        strikes = 0
        h_parties = []
        for j in range(parties):
            h_parties.append(int(input()))
        
        for day in range(1, days+1):
            if (day-6)%7 == 0 or day%7 == 0:
                continue
            
            for h in h_parties:
                if day%h==0:
                    strikes += 1
                    break

        print(int(strikes))
        
        
