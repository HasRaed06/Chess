#buttons properties: board_pos(row,col)/ square_color/ piece(brk)
import sys, os
import calc_moves
import clicked
import checks
import copy

def __init__(self,board):
    self.prv_btn = None
    self.last_move = None
    self.wking_moved = False
    self.bking_moved = False
    self.brq_moved = False
    self.brk_moved = False
    self.wrq_moved = False
    self.wrk_moved = False



#translate a piece postion in the board into chess code
def to_chess(self, row, col):
    return f"{chr(ord('a') + col)}{8 - row}"

#the result of a move
def result(self, board, prv_mov, ini_mov):
    new_board = copy.deepcopy(board)
    r, c = prv_mov
    row, col = ini_mov
    new_board[row][col] = new_board[r][c]
    new_board[r][c] = {'type': '', 'color': '', 'image': ''}
    return new_board



#print of the main_board(dictionaries)       
def print(self, board):
    for i in range(8):
        ch = ''
        for j in range(8):
            if board[i][j]["type"] == "":
                c = '    '
            else:
                c = board[i][j]["type"][:4]
            ch = ch + " " + c + " |"
        print(ch)

    
def turn(self):
    if self.last_move:
        color = self.last_move[1].property("piece")[0]
    else:
        return "white"
    return "black" if color == "w" else "white"

#checks if the color's king is on check or not
def check(self,board,color):
    return checks.check(self,board,color)


#checks if the game is over and return the winner(1/0/-1)
def terminal(self,board):
    pass

#evaluates all the possible moves of a piece (position of the piece)
def moves(self, board, piece_pos):
    return calc_moves.moves(self, board, piece_pos)



def main():
    pass

if __name__ == "__main__":
    main()