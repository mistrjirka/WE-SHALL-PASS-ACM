import sys

def main():
    input_arr = []
    standard_sol_num = int(input())
    run = 1
    while standard_sol_num != 0:
        input_arr.append(standard_sol_num)
        result = 0
        standard_sol = ""
        solutions = ""
        standard_sol_arr = []
        solutions_arr = []
        while standard_sol_num > 0:
            input1 = input()
            standard_sol_arr.append(input1)
            standard_sol = standard_sol + input1
            standard_sol_num -= 1
        solutions_num = int(input())
        input_arr.append(solutions_num)
        while solutions_num > 0:
            input2 = input()
            solutions_arr.append(input2)
            solutions = solutions + input2
            solutions_num -= 1

        standard_sol_dic = {}
        solution_dic = {}
        if standard_sol_arr == solutions_arr:
            result = 1
        else:
            for k in range(len(standard_sol)):
                if standard_sol[k] >= "0" and standard_sol[k] <= "9":
                    standard_sol_dic[standard_sol[k]] = standard_sol_dic.get(standard_sol[k], 0) + 1
            for k in range(len(solutions)):
                if solutions[k] >= "0" and solutions[k] <= "9":
                    solution_dic[solutions[k]] = solution_dic.get(solutions[k], 0) + 1
            if solution_dic != standard_sol_dic:
                result = 2
        if result == 1:
            print("Run #" + str(run) + ": Accepted")
        elif result == 2:
            print("Run #" + str(run) + ": Wrong Answer")
        else:
            print("Run #" + str(run) + ": Presentation Error")

        run += 1
        input_arr = []
        standard_sol_num = int(input())



if __name__ == "__main__":
    main()