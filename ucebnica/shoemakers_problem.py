def main():
    num_of_cases = int(input())

    while num_of_cases > 0:
        dic_arr = []
        lines_counter = 0
        empty = input()
        num_of_jobs = int(input())
        while num_of_jobs > 0:
            dictionary = {
                "line_num": 0,
                "ratio": 0
            }
            lines_counter += 1
            line = input().split()
            dictionary["line_num"] = lines_counter
            dictionary["ratio"] = int(line[1]) / int(line[0])
            dic_arr.append(dictionary)
            num_of_jobs -= 1

        newlist = sorted(dic_arr, key=lambda d: d['ratio'], reverse=True)
        for idx, element in enumerate(newlist):
            if idx == 0:
                print(element["line_num"], end="")
            else:
                print(" " + str(element["line_num"]), end="")
        print("")
        if num_of_cases != 1:
            print("") 
        num_of_cases -= 1

if __name__ == "__main__":
    main()