import sys


def solver(nums, counts):
    if int(nums[0]) < int(nums[1]):
        i, j = int(nums[0]), int(nums[1])
    else:
        j, i = int(nums[0]), int(nums[1])
    max_steps = 0
    if len(counts) < j:
        counts.extend([0 for _ in range(j-len(counts))])
    for k in range(i, j+1, 1):
        n_steps = 1
        num = k

        while (num != 1):
            if num % 2 == 0:
                num = num/2
            else:
                num = 3*num+1
            num = int(num)
            if num < k and counts[num-1] != 0:
                n_steps += counts[num-1]
                break
            n_steps += 1

        counts[k-1] = n_steps
        if n_steps > max_steps:
            max_steps = n_steps
    return max_steps, counts


def print_triplets(triplet):
    print(triplet[0], triplet[1], triplet[2])


def main():

    counts = []
    run = True
    while run:
        try:
            num_pair = input()
        except EOFError:
            break
        num_pair = num_pair.split(' ')
        cycle_length, counts = solver(num_pair, counts)
        print_triplets((num_pair[0], num_pair[1], cycle_length))


if __name__ == "__main__":
    main()
