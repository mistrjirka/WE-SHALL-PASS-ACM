directions = {
    "p":{
        "moves": (
            (1, 1),
            (1, -1),
        ),
        "range_limited": True
    },
    "P":{
        "moves": (
            (-1, 1),
            (-1, -1),
        ),
        "range_limited": True
    },
    "r":{
        "moves": (
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ),
        "range_limited": False
    },
    "R":{
        "moves": (
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ),
        "range_limited": False
    },
    "b":{
        "moves": (
            (-1, 1),
            (-1, -1),
            (1, 1),
            (1, -1),
        ),
        "range_limited":False
    },
    "B":{
        "moves": (
            (-1, 1),
            (-1, -1),
            (1, 1),
            (1, -1),
        ),
        "range_limited":False
    },
    "q":{
        "moves": (
            (-1, 1),
            (-1, -1),
            (1, 1),
            (1, -1),
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ),
        "range_limited":False
    },
    "Q":{
        "moves": (
            (-1, 1),
            (-1, -1),
            (1, 1),
            (1, -1),
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ),
        "range_limited":False
    },
    "n":{
        "moves": (
            (-1, 2),
            (2, -1),
            (1, 2),
            (2, 1),
            (-1, -2),
            (-2, -1),
            (1, -2),
            (-2, 1),
        ),
        "range_limited":True
    },
    "N":{
        "moves": (
            (-1, 2),
            (2, -1),
            (1, 2),
            (2, 1),
            (-1, -2),
            (-2, -1),
            (1, -2),
            (-2, 1),
        ),
        "range_limited":True
    },

}

def get_positions_under_attack(board, piece, position, attacked_positions_white, attacked_positions_black):

    for direction in directions[piece]["moves"]:
        ind = 0
        (x, y) = position
        x += direction[0]
        y += direction[1]
        while ind < (1 if directions[piece]["range_limited"] else 8) and x in range(8) and y in range(8):
            if board[x][y] != ".":
                if (piece.islower() and board[x][y].islower()):
                    break
                elif (piece.isupper() and board[x][y].isupper()):
                    break
                else:
                    if piece.isupper():
                        attacked_positions_white.add((x,y))
                    else:
                        attacked_positions_black.add((x,y))
                    break

            if piece.isupper():
                attacked_positions_white.add((x,y))
            else:
                attacked_positions_black.add((x,y))
            x += direction[0]
            y += direction[1]
            ind += 1
        
            



if __name__ == "__main__":    
    inputs = []
    not_empty = True
    game_num = 1
    while not_empty:
        chess_board = []
        empty_lines = 0
        for i in range(8):
            try:
                in_str = input()
            except EOFError:
                break

            if in_str == "........":
                empty_lines += 1

            if in_str and len(in_str):
                chess_board.append([*(in_str)])
        if empty_lines == 8:
            break

        attacked_positions_black = set()
        attacked_positions_white = set()
        black_king_position = (-1, -1)
        white_king_position = (-1, -1)
        for x, line in enumerate(chess_board):
            for y, piece in enumerate(line):
                if piece == "k":
                    black_king_position = (x, y)
                elif piece == "K":
                    white_king_position = (x, y)
                elif piece != ".":
                    get_positions_under_attack(chess_board, piece, (x,y), attacked_positions_white, attacked_positions_black)
        
        if black_king_position in attacked_positions_white:
            print("Game #"+str(game_num)+": black king is in check.")
        elif white_king_position in attacked_positions_black:
            print("Game #"+str(game_num)+": white king is in check.")
        else:
            print("Game #"+str(game_num)+": no king is in check.")

        game_num +=1
        try:
            input()
        except EOFError:
            break