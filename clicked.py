from calc_moves import moves
#this works when you press on any square
def square_clicked(self,pos):
    row,col = pos
    board = self.main_board
    turn = self.turn()
    if self.possible_moves:
        if pos not in self.possible_moves:
            self.dehighlight()
            self.possible_moves = []
            if board[row][col]['type'] != "" and turn == board[row][col]['color']:
                self.possible_moves = moves(self, board, pos)
                self.highlight(self.possible_moves)

        else:
            prv_row, prv_col = self.prv_pos
            piece = board[prv_row][prv_col]
            if piece['type'] == 'king':
                if piece['color'] == 'black':
                    self.bking_moved = True
                else:
                    self.wking_moved = True
            elif piece['type'] == "rook":
                if piece['color'] == 'black':
                    if prv_col == 0:
                        self.brq_moved = True
                    elif prv_col == 7:
                        self.brk_moved = True
                else:
                    if prv_col == 0:
                        self.wrq_moved = True
                    elif prv_col == 7:
                        self.wrk_moved = True
            
            #en passant
            if board[prv_row][prv_col]['type'] == 'pawn' and col != prv_col and board[row][col]['type'] == '':
                if board[prv_row][prv_col]['color'] == 'black':
                    coff = 1
                else:
                    coff = -1

                board[row-coff][col] = {'type': '', 'color': '', 'image': ''}
                self.edit("",(row-coff,col))
            board[row][col] = board[prv_row][prv_col]
            board[prv_row][prv_col] = {'type': '', 'color': '', 'image': ''}
            image = board[row][col]['image']
            self.edit(image,(row,col))
            self.edit("",(prv_row,prv_col))
            #castling
            if board[row][col]['type'] == 'king':
                if col - prv_col == 2:
                    board[row][col-1] = board[row][col+1]
                    board[row][col+1] = {'type': '', 'color': '', 'image': ''}
                    image = board[row][col-1]["image"]
                    self.edit(image,(row,col-1))
                    self.edit("",(row,col+1))

                elif col - prv_col == -2:
                    board[row][col+1] = board[row][col-2]
                    board[row][col-2] = {'type': '', 'color': '', 'image': ''}
                    image = board[row][col+1]["image"]
                    self.edit(image,(row,col+1))
                    self.edit("",(row,col-2))


            if board[row][col]['type'] == 'pawn' and abs(row-prv_row) == 2:
                board[row][col]['enpassant'] = True
            if self.last_move:
                r,c = self.last_move
                try:
                    if board[r][c]['enpassant']:
                        board[r][c]['enpassant'] = False
                except:
                    pass

            #promotion
            if (row == 0 or row == 7) and board[row][col]['type'] == 'pawn':
                self.main_board[row][col] = {'type': 'queen', 'color': board[row][col]['color'], 'image': 'images/'+board[row][col]['color']+'queen.jpg'}
                image = self.main_board[row][col]["image"]
                self.edit(image,(row,col))
            self.last_move = pos
            self.dehighlight()
            self.possible_moves = []
    else:
        #highlight a piece
        if board[row][col]['type'] != "" and turn == board[row][col]['color']:
            self.possible_moves = moves(self, board, pos)
            self.highlight(self.possible_moves)
    self.prv_pos = pos