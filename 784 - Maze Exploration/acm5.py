#!/usr/bin/env python3.5
directions = (
    (1,0),
    (0,1),
    (1,1),
    (-1, 0),
    (0, -1),
    (-1,-1),
    (-1,1),
    (1,-1)
)
#((offsetx, offsety),(centerx, centery))
doorsOpenOffsets = (
    ((2,0),(4,0)),
    ((-2,0),(-4,0)),
    ((0,2),(0,4)),
    ((0,-2), (0, -4))
)

def find_star(puzzle):
    for y,line in enumerate(puzzle):
        for x,i in enumerate(line):
            if i == "*":
                return ((y,x),(x,y))

def paint_room(puzzle, center):
    puzzle[center[0]][center[1]] = "#"
    for direction in directions:
        if puzzle[center[0]+direction[0]][center[1]+direction[1]] == " ":
            puzzle[center[0]+direction[0]][center[1]+direction[1]] = "#"
        

def find_other_rooms(puzzle, center):
    rooms = []
    for door in doorsOpenOffsets:
        x = center[0] + door[0][0]
        y = center[1] + door[0][1]
        if x >= 0 and y >= 0 and x < len(puzzle):
            if y < len(puzzle[x]):
                place = puzzle[x][y]
                if place == " ":
                    puzzle[x][y] = "#"
                    rooms.append(((center[0] + door[1][0],center[1] + door[1][1]), (x,y)))
    return rooms

if __name__ == '__main__':
    puzzles_num = int(input())
    puzzles = []
    
    for i in range(puzzles_num):
        lineStr = input()
        operationMatrix = []
        while lineStr != "_____":
            operationMatrix.append([*lineStr])
            lineStr = input()
        puzzles.append(operationMatrix)
    
    for puzzle in puzzles:
        star = find_star(puzzle)
        centers = [star]
        while len(centers) > 0:
            room = centers[0]
            paint_room(puzzle, room[0])
            """puzzle[room[1][0]][room[1][1]] = "#"""
            centers += find_other_rooms(puzzle, room[0])
            centers.pop(0)
    
    for puzzle in puzzles:
        for i in puzzle:
            for j in i:
                print(j, end="")
            print()
        print("_____")
    