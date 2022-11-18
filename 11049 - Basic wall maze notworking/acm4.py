
"""
1 1
0 0 02


1 6
2 6
0 0 1 0
1 5 1 6
1 5 3 5
0 0
"""

def createXYArray(x, y, filler = 0):
    result = []
    for i in range(x):
        result.append([])
        for j in range(y):
            result[i].append(filler)
    return result

def getMultipleInputs(num_of_inputs, question):
    result = []
    valid = False
    while len(result) != num_of_inputs and not valid:
        #stolen from https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
        result = [int(x) for x in input(question).split()]
    return result

def print_data(data, walls):
    rows = createXYArray(len(data), len(data[0]))
    for ind1,x in enumerate(data):
        for ind2,y in enumerate(x):
            rows[ind2][ind1] = str(y if y < 0 else (" "+str(y)))

    for x in rows:
            
        print("", end='| ')
        for index1, y in enumerate(x):
            wallExist = False
            for index2,wall in enumerate(walls):
                if index1 in wall[0] and index2 in wall[1]:
                    wallExist = True
                    break
            if wallExist == True:
                print(y, end=' ! ')
            else: 
                print(y, end=' | ')
        print("")


def clamp(n, minn = -1, maxn = 1):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n

class pathFinder:
    def __init__(self, maze, start, end, firstWall, secondWall, thirdWall):
        self.counter = 1
        self.points=[]
        self.blind_points = []
        self.maze = maze
        self.maze[start[0]-1][start[1]-1] = -1
        self.maze[end[0]-1][end[1]-1] = -1
        self.start = [start[0]-1,start[1]-1]
        self.end = [end[0]-1,end[1]-1]
        self.walls = [self.getWall(firstWall), self.getWall(secondWall), self.getWall(thirdWall)]
        self.position = [start[0]-1,start[1]-1]
        
    def setWall(self, wall):
        if(wall[0] == 0 and wall[2] == 0) or (wall[0] == 6 and wall[2] == 6) or (wall[1] == 0 and wall[3] == 0) or (wall[1] == 6 and wall[3] == 6):
            return False

        
    def canGo(self, vector):
        markedWalls = []
        canGo = True
        if (self.position[0]+vector[0] 
            < 0 or self.position[1]+vector[1] 
            < 0 or self.position[0]+vector[0] 
            > len(self.maze)-1 or self.position[1]+vector[1] 
            > len(self.maze[0])-1
        ):
            return False
        elif (maze[self.position[0]+vector[0]][self.position[1]+vector[1]] != 0):
            return False

        for index, wall in enumerate(self.walls):
            for x in wall[0]:
                range_to_check = []
                if vector[0] == 0:
                    range_to_check = [self.position[0]]
                elif vector[0] > 0:
                    range_to_check = range(self.position[0], self.position[0]+vector[0]+1)
                else:
                    range_to_check = range(self.position[0]+vector[0]-1, self.position[0])
                if x in range_to_check:
                    for y in wall[1]: 
                        range_to_check = []
                        if vector[1] == 0:
                            range_to_check = [self.position[1]]
                        elif vector[1] > 0:
                            range_to_check = range(self.position[1], self.position[1]+vector[1]+1)
                        else:
                            range_to_check = range(self.position[1]+vector[1]-1, self.position[1])
                        
                        if y in range_to_check:
                            canGo = False
        print(canGo)        
        return canGo
    def go(self, vector): 
        if self.position[0]+vector[0] < 0 or self.position[1]+vector[1] < 0:
            return False
        
        self.position[0] += vector[0]
        self.position[1] += vector[1]
        self.maze[self.position[0]][self.position[1]] = self.counter
        self.points.append(vector)
        self.counter += 1

    def calculateImaginaryPositionDistance(self, vector):
        direction_x = self.end[0]-(self.position[0] + vector[0])
        direction_y = self.end[1]-(self.position[1] + vector[1])
        return (direction_x**2 + direction_y**2)**0.5

    def getBestDirection(self):
        direction_x = self.end[0]-self.position[0]
        direction_y = self.end[1]-self.position[1]
        vector = [0, 0]
        if abs(direction_x) >= abs(direction_y):
            vector = [clamp(direction_x), 0]
        else:
            vector = [0, clamp(direction_y)]
        
        if not self.canGo(vector):
            possible_vectors = (
                [0,1],
                [1,0],
                [-1,0],
                [0, -1]
            )
            lowest_distance = [-1, 9999]
            for ind, v in enumerate(possible_vectors):
                if self.canGo(v):
                    distance = self.calculateImaginaryPositionDistance(v)
                    if distance < lowest_distance[1]:
                        lowest_distance[0] = ind
                        lowest_distance[1] = distance
            vector = possible_vectors[lowest_distance[0]]
        return vector

    def start_finding(self):
        while self.position[0] != self.end[0] or self.position[1] != self.end[1]:
            vector = self.getBestDirection()
            self.go(vector)
            print_data(self.maze, self.walls)
            print(vector)
            print(self.position)
        
if __name__ == '__main__':
    maze = createXYArray(6,6, 0)
    
    startPoint = getMultipleInputs(2, "Enter Starting Point")
    endPoint = getMultipleInputs(2, "Enter End Point")
    firstWall = getMultipleInputs(4, "Enter first wall")
    secondWall = getMultipleInputs(4, "Enter second wall")
    thirdWall = getMultipleInputs(4, "Enter third wall")

    finder = pathFinder(maze, startPoint, endPoint, firstWall, secondWall, thirdWall)
    finder.start_finding()
    