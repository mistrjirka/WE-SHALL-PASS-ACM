import sys

def sort_lines(lines):
    return sorted(lines, key=len)

def determine_result(lines):
    sorted_lines = sort_lines(lines)
    dictionary = {}
    while len(sorted_lines) > 0:
        min_arr = []
        max_arr = []
        min_arr.append(min(sorted_lines, key=len))
        for element in min_arr:
            sorted_lines.remove(element)

        max_arr.append(max(sorted_lines, key=len))
        for element in max_arr:
            sorted_lines.remove(element)

        for max_element in max_arr:
            for min_element in min_arr:
                string1 = max_element + min_element
                string2 = min_element + max_element
        dictionary[string1] = dictionary.get(string1, 0) + 1
        dictionary[string2] = dictionary.get(string2, 0) + 1
    sorted_dic = sorted(dictionary.items(), key=lambda x:x[1])
    print(sorted_dic[len(sorted_dic) - 1][0])

def main():
    number_of_cases = int(input())
    empty_space = input()
    lines = []

    for tempInput in sys.stdin:
        if tempInput == "\n":
            determine_result(lines)
            print("")
            lines = []

        if tempInput != "\n":
            line = tempInput.replace("\n", "")
            lines.append(line)
    
    determine_result(lines)

if __name__ == "__main__":
    main()
