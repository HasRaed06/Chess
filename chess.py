#buttons properties: board_pos(row,col)/ square_color/ piece(brk)
import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.uic import loadUi
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
import calc_moves
import clicked
import checks
import copy
import initialize

class ChessWindow(QMainWindow):
    def __init__(self,board):
        super().__init__()
        self.initialize(board)
        self.theme = ('green','tan','purple')
        loadUi("chess.ui", self)
        self.reset.clicked.connect(self.reset_game)
        self.display(board)
    
    def initialize(self, board):
        initialize.initialize(self, board)
    
    
    def display(self,board):
        #displaying the board in the UI
        for row in range(8):
            for col in range(8):
                btn = self.findChild(QPushButton, f"b{row}{col}")
                name = btn.objectName()
                if not (len(name) == 3 and name.startswith("b")):
                    continue
                btn.setProperty("piece", board[row][col])
                image = self.main_board[row][col]["image"]
                btn.setIcon(QIcon(image))
                btn.setIconSize(QSize(86, 86))
                btn.setProperty("board_pos", (row, col))
                self.btn = btn
                btn.clicked.connect(self.square_clicked)
                square = self.theme[0] if (row+col)%2 == 0 else self.theme[1]
                btn.setProperty("square_color", square)
                btn.setStyleSheet(f"background-color: {square};")
 
                
    def reset_game(self):
        self.initialize(ini_board)
        self.display(ini_board)

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


    #checks if theres highlited square(you selected a piece)
    def highlighted(self):
        for row in range(8):
            for col in range(8):
                btn = self.findChild(QPushButton, f"b{row}{col}")
                if btn.property("square_color") == self.theme[2]:
                    return True
        return False
    
    def edit(self,image,pos):
        row, col = pos
        btn = self.findChild(QPushButton,f"b{row}{col}")
        btn.setIcon(QIcon(image))
        btn.setIconSize(QSize(86, 86))

    #highlightes the moves of a piece
    def highlight(self,list):
        for row,col in list:
                btn = self.findChild(QPushButton, f"b{row}{col}")
                btn.setProperty("square_color",self.theme[2])
                btn.setStyleSheet(f"background-color : {self.theme[2]};")
       
    #remove the highlighted squares
    def dehighlight(self):
        for row in range(8):
            for col in range(8):
                btn = self.findChild(QPushButton, f"b{row}{col}")
                square = self.theme[0] if (row+col)%2 == 0 else self.theme[1]
                btn.setProperty("square_color",square)
                btn.setStyleSheet(f"background-color: {square};")


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
    
    #remove the piece from the UI
    def remove(pos):
        pass

    #this works when you press on any square
    def square_clicked(self):
        btn = self.sender()
        clicked.square_clicked(self,btn.property("board_pos"))
    
    def turn(self):
        if self.last_move:
            row, col = self.last_move
            return 'black' if self.main_board[row][col]["color"] == 'white' else 'white'
        else:
            return "white"
    
    #checks if the color's king is on check or not
    def check(self,board,color):
        return checks.check(self,board,color)

    
    #checks if the game is over and return the winner(1/0/-1)
    def terminal(self,board):
        pass

    #evaluates all the possible moves of a piece (position of the piece)
    def moves(self, board, piece_pos):
        return calc_moves.moves(self, board, piece_pos)


ini_board = [
    ["brq", "bnq", "bbq", "bq", "bk", "bbk", "bnk", "brk"],
    ["bpa", "bpb", "bpc", "bpd", "bpe", "bpf", "bpg", "bph"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["wpa", "wpb", "wpc", "wpd", "wpe", "wpf", "wpg", "wph"],
    ["wrq", "wnq", "wbq", "wq", "wk", "wbk", "wnk", "wrk"]
]

def main():
    app = QApplication(sys.argv)
    window = ChessWindow(ini_board)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()