import checks
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
    if self.check(board,color) == False:
        if type == "pawn":
            #first move
            coff = 1 if color == "black" else -1
            if (color == "black" and row == 1 or color == "white" and row == 6) and board[row+2*coff][col]['type'] == "" and board[row+coff][col]['type'] == "" and self.check(self.result(board,(row,col),(row+2*coff, col)),color) == False:
                possible_moves.append((row+2*coff, col))


            if 0 <= row + coff < 8: 
                if board[row+coff][col]['type'] == "" and self.check(self.result(board,(row,col),(row+coff,col)),color) == False:
                    possible_moves.append((row+coff,col))
                
                if 0 <= col + 1 < 8 and board[row+coff][col+1]['type'] != "" and board[row+coff][col+1]['color'] != color and self.check(self.result(board,(row,col),(row+coff, col+1)),color) == False:
                    possible_moves.append((row+coff, col+1))
                
                if 0<= col - 1 < 8 and board[row+coff][col-1]['type'] != "" and board[row+coff][col-1]['color'] != color and self.check(self.result(board,(row,col),(row+coff, col-1)),color) == False:
                    possible_moves.append((row+coff, col-1))
            #en passant
            if self.last_move:
                r,c = self.last_move
                try:
                    if board[r][c]['enpassant']:

                        if row == r and abs(col-c) == 1 and self.check(self.result(board,(row,col),(row+coff,c)),color) == False:
                            possible_moves.append((row+coff,c))
                except:
                    pass 
                

        if type != "pawn":
            for dir in direction:
                rr,cc = dir
                i = 1
                r = row + rr*i
                c = col + cc*i
                if type == "queen" or type == "rook" or type == "bishop":
                    while (0<=r<8 and 0<=c<8 and board[r][c]['type'] == "" and self.check(self.result(board,(row,col),(r,c)),color) == False):
                        possible_moves.append((r,c))
                        i += 1
                        r = row + rr*i
                        c = col + cc*i
                    if 0<=r<8 and 0<=c<8 and board[r][c]['color'] != color and self.check(self.result(board,(row,col),(r,c)),color) == False:
                        possible_moves.append((r,c))
                elif type == "knight" or type == "king":
                    if 0<=r<8 and 0<=c<8 and (board[r][c]['type'] == "" or board[r][c]['color'] != color) and self.check(self.result(board,(row,col),(r,c)),color) == False:
                        possible_moves.append((r,c))
            if type == "king":
                if color == "white" and not(self.wking_moved) and row == 7 and col == 4:
                    if not(self.wrq_moved):
                        i = 3
                        while i>0 and self.main_board[row][i]['type'] == '':
                            i -= 1
                        if i == 0 and (row,col-1) in possible_moves and self.check(self.result(board,(row,col),(row,col-2)),color) == False:
                            possible_moves.append((row,col-2))
                    if not(self.wrk_moved):
                        i = 5
                        while i<7 and self.main_board[row][i]['type'] == '':
                            i += 1
                        if i == 7 and (row,col+1) in possible_moves and self.check(self.result(board,(row,col),(row,col+2)),color) == False:
                            possible_moves.append((row,col+2))
                elif color == "black" and not(self.bking_moved):
                    if not(self.brq_moved):
                        i = 3
                        while i>0 and self.main_board[row][i]['type'] == '':
                            i -= 1
                        if i == 0 and (row,col-1) in possible_moves and self.check(self.result(board,(row,col),(row,col-2)),color) == False:
                            possible_moves.append((row,col-2))
                    if not(self.brk_moved):
                        i = 5
                        while i<7 and self.main_board[row][i]['type'] == '':
                            i += 1
                        if i == 7 and (row,col+1) in possible_moves and self.check(self.result(board,(row,col),(row,col+2)),color) == False:
                            possible_moves.append((row,col+2))
    else:
        att = checks.attackers(self,board,color)
        for i in range(8):
            for j in range(8):
                if board[i][j]['type'] == 'king' and board[i][j]['color'] == color:
                    row_king,col_king = i,j
                    break
        if len(att) == 1:
            row_opp, col_opp = att[0]
            type_opp = board[row_opp][col_opp]['type']
            #blocks
            if type_opp != 'knight':
                #determine all the squares that can block the check
                block_squares = []
                r = row_opp-row_king
                c = col_opp-col_king
                row_sig = 1 if r>=0 else -1
                col_sig = 1 if c>=0 else -1
                if r != 0:
                    r = r-row_sig
                if c != 0:
                    c = c-col_sig
                while(r != 0 or c != 0):
                    block_squares.append((row_king+r, col_king+c))
                    if r != 0:
                        r -= row_sig
                    if c != 0:
                        c -= col_sig

                #check for pieces that can move to one of these squares
                if type == "pawn":
                    #first move
                    coff = 1 if color == "black" else -1
                    if (color == "black" and row == 1 or color == "white" and row == 6) and board[row+2*coff][col]['type'] == "" and board[row+coff][col]['type'] == "" and (row+2*coff,col) in block_squares :
                        possible_moves.append((row+2*coff, col))
                    if (row+coff,col) in block_squares:
                        possible_moves.append((row+coff,col))
                else:
                    for dir in direction:
                        rr,cc = dir
                        i = 1
                        r = row + rr*i
                        c = col + cc*i
                        if type == "queen" or type == "rook" or type == "bishop":
                            while (0<=r<8 and 0<=c<8 and board[r][c]['type'] == ""):
                                i += 1
                                if (r,c) in block_squares:
                                    possible_moves.append((r,c))
                                r = row + rr*i
                                c = col + cc*i
                        elif type == "knight" :
                            if 0<=r<8 and 0<=c<8 and board[r][c]['type'] == "" and (r,c) in block_squares:
                                possible_moves.append((r,c))


            #captures
            if type == "pawn":
                coff = 1 if color == "black" else -1
                if row_opp == row+coff and (col_opp == col+1 or col_opp == col-1):
                    possible_moves.append((row_opp,col_opp))
                elif self.last_move:
                    r,c = self.last_move
                    try:
                        if board[r][c]['enpassant'] and row_opp == row and (col_opp == col+1 or col_opp == col-1):
                            possible_moves.append((row+coff,col_opp))
                    except:
                        pass
            else:
                for dir in direction:
                    rr,cc = dir
                    i = 1
                    r = row + rr*i
                    c = col + cc*i
                    if type == "queen" or type == "rook" or type == "bishop":
                        while (0<=r<8 and 0<=c<8 and board[r][c]['type'] == ""):
                            i += 1
                            r = row + rr*i
                            c = col + cc*i
                        if row_opp == r and col_opp == c:
                            possible_moves.append((r,c))
                            break
                    elif type == "knight":
                        if row_opp == r and col_opp == c:
                            possible_moves.append((r,c))

        #king moves    
        if type == 'king':
            for dir in direction:
                rr,cc = dir
                r = row + rr
                c = col + cc
                if 0<=r<8 and 0<=c<8 and (board[r][c]['type'] == "" or board[r][c]['color'] != color) and self.check(self.result(board,(row,col),(r,c)),color) == False:
                    possible_moves.append((r,c))
            

    return possible_moves