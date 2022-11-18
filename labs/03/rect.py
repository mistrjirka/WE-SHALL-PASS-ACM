def main():
    rect_perims = [[0, 0]]
    num_rects = int(input())
    prev_rect = []
    for i in range(num_rects):
        rect = list(map(int, input().split(' ')))
        curr_height, curr_width = rect[1], rect[0]
        if i == 0:
            # height 1
            # width 0
            rect_perims[i][0] = curr_width
            rect_perims[i][1] = curr_height
        else:
            prev_height, prev_width = prev_rect[1], prev_rect[0]
            case_0 = curr_width + max(rect_perims[i-1][0]+abs(curr_height-prev_height),
                                      rect_perims[i-1][1]+abs(curr_height-prev_width))
            case_1 = curr_height + max(rect_perims[i-1][0]+abs(curr_width-prev_height),
                                       rect_perims[i-1][1]+abs(curr_width-prev_width))

            rect_perims.append([case_0, case_1])
        prev_rect = rect.copy()

    print(max(rect_perims[i]))


if __name__ == "__main__":
    main()
