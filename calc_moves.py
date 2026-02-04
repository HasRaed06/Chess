#evaluates all the possible moves of a piece (position of the piece)
def moves(self, board, piece_pos):
    #promotion
    possible_moves = []
    row, col = piece_pos
    if board[row][col] == "":
        raise ValueError(f"There is no piece in({row},{col})")
    color = board[row][col]['color']
    type = board[row][col]['type']
    if type == "queen" or type == "king":
        direction = [
                (1,0),
                (0,1),
                (-1,0),
                (0,-1),
                (1,1),
                (-1,1),
                (-1,-1),
                (1,-1)
        ]
    elif type == "rook":
        direction = [
                (1,0),
                (0,1),
                (-1,0),
                (0,-1)
        ]
    elif type == "bishop":
        direction = [
                (1,1),
                (-1,1),
                (-1,-1),
                (1,-1)
        ]
    elif type == "knight":
        direction = [
            (1,2),
            (-1,2),
            (-2,1),
            (-2,-1),
            (-1,-2),
            (1,-2),
            (2,-1),
            (2,1)
        ]
    elif type == "pawn":
        coff = 1 if color == "black" else -1
        if (color == "black" and row == 1 or color == "white" and row == 6) and board[row+2*coff][col]['type'] == "" and board[row+coff][col]['type'] == "":
            possible_moves.append((row+2*coff, col))


        if 0 <= row + coff < 8: 
            if board[row+coff][col]['type'] == "":
                possible_moves.append((row+coff,col))
            
            if 0 <= col + 1 < 8 and board[row+coff][col+1]['type'] != "" and board[row+coff][col+1]['color'] != color:
                possible_moves.append((row+coff, col+1))
            
            if 0<= col - 1 < 8 and board[row+coff][col-1]['type'] != "" and board[row+coff][col-1]['color'] != color:
                possible_moves.append((row+coff, col-1))

        if self.last_move:
            r,c = self.last_move[1].property("board_pos")
            if self.last_move[1].property("enpassant") and row == r and abs(col-c) == 1:
                possible_moves.append((row+coff,c))

    if type != "pawn":
        for dir in direction:
            rr,cc = dir
            i = 1
            r = row + rr*i
            c = col + cc*i
            if type == "queen" or type == "rook" or type == "bishop":
                while (0<=r<8 and 0<=c<8 and board[r][c]['type'] == ""):
                    possible_moves.append((r,c))
                    i += 1
                    r = row + rr*i
                    c = col + cc*i
                if 0<=r<8 and 0<=c<8 and board[r][c]['color'] != color:
                    possible_moves.append((r,c))
            elif type == "knight" or type == "king":
                if 0<=r<8 and 0<=c<8 and (board[r][c]['type'] == "" or board[r][c]['color'] != color):
                    possible_moves.append((r,c))
        if type == "king":
            if color == "white" and not(self.wking_moved) and row == 7 and col == 4:
                if not(self.wrq_moved):
                    i = 3
                    while i>0 and self.main_board[row][i]['type'] == '':
                        i -= 1
                    if i == 0:
                        possible_moves.append((row,col-2))
                if not(self.wrk_moved):
                    i = 5
                    while i<7 and self.main_board[row][i]['type'] == '':
                        i += 1
                    if i == 7:
                        possible_moves.append((row,col+2))
            elif color == "black" and not(self.bking_moved):
                if not(self.brq_moved):
                    i = 3
                    while i>0 and self.main_board[row][i]['type'] == '':
                        i -= 1
                    if i == 0:
                        possible_moves.append((row,col-2))
                if not(self.brk_moved):
                    i = 5
                    while i<7 and self.main_board[row][i]['type'] == '':
                        i += 1
                    if i == 7:
                        possible_moves.append((row,col+2))
    valid_moves = []

    return possible_moves