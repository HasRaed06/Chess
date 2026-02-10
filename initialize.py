def initialize(self,board):
        self.prv_pos = None
        self.possible_moves = []
        self.last_move = None
        self.wking_moved = False
        self.bking_moved = False
        self.brq_moved = False
        self.brk_moved = False
        self.wrq_moved = False
        self.wrk_moved = False
        new_board = []
        #initializing the board with dictionaries (type,color,image)
        for line in range(8):
            new_line = []
            for piece in board[line]:
                if piece:
                    color = "black" if piece[0] == "b" else "white"
                    type = piece[1]
                    if type == "q":
                        type = "queen"
                    elif type == "k":
                        type = "king"
                    elif type == "b":
                        type = "bishop"
                    elif type == "n":
                        type = "knight"
                    elif type == "r":
                        type = "rook"
                    elif type == "p":
                        type = "pawn"
                    new_line.append({'type': type, 'color': color, 'image': 'images/'+color+type+'.jpg'})
                else:
                    new_line.append({'type': '', 'color': '', 'image': ''})
            new_board.append(new_line)
        
        self.main_board = new_board