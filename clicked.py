from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.uic import loadUi
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize

#this works when you press on any square
def square_clicked(self):
    btn = self.sender()
    row, col = btn.property("board_pos")
    board = self.main_board
    turn = self.turn()
    if self.highlighted():
        if btn.property("square_color") != self.theme[2]:
            self.dehighlight()
            if board[row][col]['type'] != "" and turn == board[row][col]['color']:
                self.highlight(row,col)
        else:
            name = self.prv_btn.property("piece")
            if name == "bk":
                self.bking_moved = True
            elif name == "wk":
                self.wking_moved = True
            elif name == "brq":
                self.brq_moved = True
            elif name == "brk":
                self.brk_moved = True 
            elif name == "wrq":
                self.wrq_moved = True 
            elif name == "wrk":
                self.wrk_moved = True
            
            #en passant
            r,c = self.prv_btn.property("board_pos")
            btn.setProperty("piece", name)
            if board[r][c]['type'] == 'pawn' and col != c and board[row][col]['type'] == '':
                if board[r][c]['color'] == 'black':
                    coff = 1
                else:
                    coff = -1

                board[row-coff][col] = {'type': '', 'color': '', 'image': ''}
                btn2 = self.findChild(QPushButton, "b"+str(row-coff)+str(col))
                btn2.setIcon(QIcon(""))
                btn2.setProperty("piece","")
            board[row][col] = board[r][c]
            board[r][c] = {'type': '', 'color': '', 'image': ''}
            image = board[row][col]["image"]
            btn.setIcon(QIcon(image))
            btn.setIconSize(QSize(86, 86))
            self.prv_btn.setProperty("piece","")
            self.prv_btn.setIcon(QIcon(""))
            self.dehighlight()
            #castling
            if board[row][col]['type'] == 'king':
                if col - c == 2:
                    btn2 = self.findChild(QPushButton, "b"+str(row)+str(col-1))
                    btn3 = self.findChild(QPushButton, "b"+str(row)+str(col+1))
                    board[row][col-1] = board[row][col+1]
                    board[row][col+1] = {'type': '', 'color': '', 'image': ''}
                    image = board[row][col-1]["image"]
                    btn2.setIcon(QIcon(image))
                    btn2.setIconSize(QSize(86, 86))
                    btn3.setIcon(QIcon(""))
                    btn2.setProperty("piece",btn3.property("piece"))
                    btn3.setProperty("piece", "")

                elif col - c == -2:
                    btn2 = self.findChild(QPushButton, "b"+str(row)+str(col+1))
                    btn3 = self.findChild(QPushButton, "b"+str(row)+str(col-2))
                    board[row][col+1] = board[row][col-2]
                    board[row][col-2] = {'type': '', 'color': '', 'image': ''}
                    image = board[row][col+1]["image"]
                    btn2.setIcon(QIcon(image))
                    btn2.setIconSize(QSize(86, 86))
                    btn3.setIcon(QIcon(""))
                    btn2.setProperty("piece",btn3.property("piece"))
                    btn3.setProperty("piece", "")

            if board[row][col]['type'] == 'pawn' and abs(row-r) == 2:
                btn.setProperty("enpassant", True)
            if self.last_move:
                if self.last_move[1].property("enpassant") == True :
                    self.last_move[1].setProperty("enpassant",None)

            #promotion
            if (row == 0 or row == 7) and board[row][col]['type'] == 'pawn':
                self.main_board[row][col] = {'type': 'queen', 'color': board[row][col]['color'], 'image': 'images/'+board[row][col]['color']+'queen.jpg'}
                image = self.main_board[row][col]["image"]
                btn.setIcon(QIcon(image))
                btn.setIconSize(QSize(86, 86))
                btn.setProperty("piece", board[row][col]['color'][0]+"q")
            self.last_move = (self.prv_btn,btn)
    else:
        #highlight a piece
        if board[row][col]['type'] != "" and turn == board[row][col]['color']:
            self.highlight(row,col)
    self.prv_btn = btn

def test(self):
    for i in range(8):
        ch = ''
        for j in range(8):
            btn = self.findChild(QPushButton, 'b'+str(i)+str(j))
            x = btn.property("piece")
            if not x:
                x = '   '
            elif len(x) == 2:
                x += ' '
            ch += " " + x + " |"
        print(ch)