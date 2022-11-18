import math


def getMultipleInputs(num_of_inputs, question):
    result = []
    valid = False
    while len(result) != num_of_inputs and not valid:
        # stolen from https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
        result = [int(x) for x in input(question).split()]
    return result


def fit_array_reversed(length, hash_val, node, memoize):
    if length == 0 and hash_val == 0:
        return 1
    elif length <= 0 or hash_val <= 0 or node > 26:
        """basically: if length is smaller or equal to zero but it is not a solution it means it is a dead end
        if hashval is smaller or equal to zero it means we run out of hash space and this is a dead end
        if node is bigger than 26 it means we run out of characters and this is a dead end"""
        return 0

    if memoize[length][hash_val][node] is not None:
        return memoize[length][hash_val][node]

    result = 0
    for i in range(26, node - 1, -1):
        result += fit_array_reversed(length-1, hash_val-i, i+1, memoize)
    memoize[length][hash_val][node] = result
    return result


def clamp(n, minn=-1, maxn=1):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n


if __name__ == '__main__':
    cases = []

    while (tmp_case := getMultipleInputs(2, "")) != [0, 0]:
        cases.append(tmp_case)
    results = []
    max_length = clamp(max(cases, key=lambda l: l[0])[0], 1, 28)+1
    max_hash = clamp(max(cases, key=lambda l: l[1])[1], 1, 366)+1
    memoize_arr = [[[None for _ in range(28)]for _ in range(
        max_hash)] for _ in range(max_length)]
    for case in cases:
        length = case[0]
        hash_val = case[1]
        if length > 26 or hash_val > 351:
            results.append(0)
        else:
            results.append(fit_array_reversed(
                length, hash_val, 1, memoize=memoize_arr))

    for ind, result in enumerate(results):
        print(f"Case {ind+1}: {result}")
