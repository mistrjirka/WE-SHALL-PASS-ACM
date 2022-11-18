def encode_combination(combination):
    colors = {0: "B", 1: "G", 2: "C"}
    return colors[combination[0]] + colors[combination[1]] + colors[combination[2]]


def main():
    run = True
    while run:
        combination_min = ()
        bins = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        all_bins = [0, 1, 2]
        try:
            in_line = input().split(' ')
        except EOFError:
            run = False
            break
        n_ints = 0
        curr_bin = 0
        for character in in_line:
            bins[curr_bin][n_ints] = int(character)
            n_ints += 1
            if n_ints == 3:
                n_ints = 0
                curr_bin += 1
        bin_counts = []
        for i in range(3):
            temp_bins = bins.copy()
            temp_bins.pop(i)
            count_bin = [0, 0, 0]
            for k in range(3):
                count_bin[k] = sum([other_bin[k] for other_bin in temp_bins])
            bin_counts.append(count_bin)

        for i in range(3):

            bins_to_search = all_bins.copy()
            bins_to_search.pop(i)

            for j in range(3):
                combination = [None, None, None]
                moves = 0
                submoves_a = 0
                submoves_b = 0
                comb_a = []
                comb_b = []
                combination[i] = j
                moves += bin_counts[i][j]
                colors_remaining = all_bins.copy()
                colors_remaining.pop(j)

                submoves_a = bin_counts[bins_to_search[0]][colors_remaining[0]
                                                           ] + bin_counts[bins_to_search[1]][colors_remaining[1]]
                submoves_b = bin_counts[bins_to_search[0]][colors_remaining[1]
                                                           ] + bin_counts[bins_to_search[1]][colors_remaining[0]]
                if submoves_a > submoves_b:
                    combination[bins_to_search[0]] = colors_remaining[1]
                    combination[bins_to_search[1]] = colors_remaining[0]
                    moves += submoves_b
                else:
                    combination[bins_to_search[0]] = colors_remaining[0]
                    combination[bins_to_search[1]] = colors_remaining[1]
                    moves += submoves_a

                if combination_min == ():
                    combination_min = (combination, moves)
                else:
                    if moves < combination_min[1]:
                        combination_min = (combination, moves)
                    elif moves == combination_min[1]:
                        text_comb = encode_combination(combination)
                        if text_comb == sorted([text_comb, encode_combination(combination_min[0])])[0]:
                            combination_min = (combination, moves)

        print(encode_combination(combination_min[0]), combination_min[1])


if __name__ == "__main__":
    main()
