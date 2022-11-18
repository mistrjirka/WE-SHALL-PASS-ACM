
def rearrange_boxes(boxes):
    return sorted(boxes, key=lambda x: x[0][0])


def fits(box1, box2):
    return all([box1[0][i] < box2[0][i] for i in range(len(box1[0]))])


def find_nesting(boxes):
    maxBoxes = []
    maxBoxes.append(boxes[0])
    for i in range(len(boxes)):
        tempBoxes = []
        posStack = []
        i1, i2 = i, i+1
        while (i2 < len(boxes)):
            nests = fits(boxes[i1], boxes[i2])
            if nests:
                if tempBoxes == []:
                    tempBoxes.append(boxes[i1])
                    posStack.append(i1)
                tempBoxes.append(boxes[i2])
                posStack.append(i2)
                if len(tempBoxes) > len(maxBoxes):
                    maxBoxes = tempBoxes
                i1, i2 = i2, i2+1
            else:
                if i2 < len(boxes):
                    i2 += 1
                    if not (i2 < len(boxes)):
                        if len(posStack) < 2:
                            continue
                        i2 = posStack.pop() + 1
                        tempBoxes.pop()
                        i1 = posStack[len(posStack)-1]

    return maxBoxes


def print_nesting(nesting):
    print(len(nesting))
    nesting_str = str()
    i = 0
    for box in nesting:
        if i == 0:
            nesting_str += str(box[1])
        else:
            nesting_str += (" " + str(box[1]))
        i += 1
    print(nesting_str)


def main():
    run = True
    while run:
        boxes = []
        try:
            init_line = input().split(' ')
        except:
            break
        for i in range(int(init_line[0])):
            box = [int(x) for x in input().split(' ')]
            boxes.append((sorted(box), i+1))
        boxes = rearrange_boxes(boxes)
        nesting = find_nesting(boxes)
        print_nesting(nesting)


if __name__ == "__main__":
    main()
