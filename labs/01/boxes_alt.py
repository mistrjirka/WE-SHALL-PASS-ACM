# Program that solves the Stacking Boxes problem
# http://acm.uva.es/p/v1/103.html

boxes = []		# list of boxes
nBox = 0		# number of boxes
dim = 0			# dimensions of boxes

# sort boxes by their measurements using bubble sort


def sort_boxes():
	for i in range(nBox-1):
		for j in range(nBox-i-1):
			for k in range(dim):
				if boxes[j][k] < boxes[j+1][k]:
					break
				elif boxes[j][k] > boxes[j+1][k]:
					boxes[j], boxes[j+1] = boxes[j+1], boxes[j]
					break


file = open('input.txt')
while file:
	line = file.readline()								# read line from file
	if line == "":										# exit if end of file
		break
	vars = line.strip().split(' ')						# get input data from file
	nBox, dim = int(vars[0]), int(vars[1])

	boxes = []											# list of boxes
	for i in range(nBox):
		vars = file.readline().strip().split(' ')		# get input data from file
		mes = []										# measurements of a box
		for var in vars:
			mes.append(int(var))
		boxes.append(mes)								# add box to boxes
	for box in boxes:									# sort boxes' measurements
		box.sort()

	oldBoxes = []										# save previous arrangement of boxes
	for box in boxes:
		oldBoxes.append(box)

	sort_boxes()										# sort boxes by their measurements

	# Find the longest sring of boxes:
	maxBoxes = []										# list that holds the longest nesting string
	maxBoxes.append(boxes[0])							# make it the first box by default
	# find the longest string of boxes, try start with box[i]
	for i in range(nBox-1):
        tempBoxes = []
        posStack = []
        i1, i2 = i, i+1
        while (i2 < nBox):
            nests = True
            for j in range(dim):
                if boxes[i1][j] > boxes[i2][j]:
                    nests = False
                    break
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
                if i2 < nBox:
                    i2 += 1
                if not (i2 < nBox):
                    if len(posStack) < 2:
                        continue
                    i2 = posStack.pop() + 1
                    tempBoxes.pop()
                    i1 = posStack[len(posStack)-1]

	print len(maxBoxes)									# print output
	for box in maxBoxes:
		print oldBoxes.index(box)+1,
	print
file.close()[
