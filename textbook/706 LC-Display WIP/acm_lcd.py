numbers =[
    [
        ["-"],
        ["|", "|"],
        [" "],
        ["|", "|"],
        ["-"]
    ],
    [
        [" "],
        [" ", "|"],
        [" "],
        [" ", "|"],
        [" "]
    ],
    [
        ["-"],
        [" ", "|"],
        ["-"],
        ["|", " "],
        ["-"]
    ],
    [
        ["-"],
        [" ", "|"],
        ["-"],
        [" ", "|"],
        ["-"]
    ],
    [
        [" "],
        ["|", "|"],
        ["-"],
        [" ", "|"],
        [" "]
    ],
    [
        ["-"],
        ["|", " "],
        ["-"],
        [" ", "|"],
        ["-"]
    ],
    [
        ["-"],
        ["|", " "],
        ["-"],
        ["|", "|"],
        ["-"]
    ],
    [
        ["-"],
        [" ", "|"],
        [" "],
        [" ", "|"],
        [" "]
    ],
    [
        ["-"],
        ["|", "|"],
        ["-"],
        ["|", "|"],
        ["-"]
    ],
    [
        ["-"],
        ["|", "|"],
        ["-"],
        [" ", "|"],
        ["-"]
    ]
]
def getMultipleInputs(num_of_inputs):
    result = []
    valid = False
    while len(result) != num_of_inputs and not valid:
        try:
            #stolen from https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
            result = [x for x in input().split()]
        except:
            result = []
    return result

def render_integer(s, n):
    s = int(s)
    frame_buffer = [[" " for _ in range((s+3)*len(n))] for _ in range(2*s+3)]
    for index, num in enumerate(list(n)):
        working_offset = index*(s+2)
        num = int(num)
        template = numbers[num]
        vertical_index = 0
        horizontal_index = 0
        for j,line in enumerate(template):
            if j%2 == 0:
                y_offset = (vertical_index) * (s+1)
                for x in range(s):
                    x_offset = working_offset + x+1
                    frame_buffer[y_offset][x_offset] = template[j][0]
                vertical_index+=1
            else:
                for side, char in enumerate(line):
                    x_offset = working_offset + (s+1) * side
                    for x in range(s):
                        y_offset=(horizontal_index)*s+(horizontal_index+1)+x
                        frame_buffer[y_offset][x_offset] = char
                
                horizontal_index+=1
    return frame_buffer

def print_number(frame_buffer):
    for line in frame_buffer:
        for pixel in line:
            print(pixel, end=" ")
        print()

if __name__ == "__main__":
    s, n = getMultipleInputs(2)
    results = []
    while s != "0" and n != "0":
        print_number(render_integer(s, n))
        s, n = getMultipleInputs(2)
    
