from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.uic import loadUi
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize

#checks if the color's king is on check or not
def check(self,board,color):
    for btn in self.findChildren(QPushButton):
        if btn.property("piece") == color[0]+"k":
            row,col = btn.property("board_pos")
            color = board[row][col]['color']
            break
    #check for the pawn
    coff = 1 if color == "black" else -1
    print(row-coff)
    print(col+1)
    if 0<=row+coff<8:
        if 0<=col+1<8:
            piece1 = board[row+coff][col+1]
            if piece1['color'] != color and piece1['type'] == 'pawn':
                return True

        if 0<=col-1<8:
            piece2 = board[row+coff][col-1]
            if piece2['color'] != color and piece2['type'] == "pawn":
                return True

    direction1 = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
    ]
    direction2 = [
            (1,1),
            (-1,1),
            (-1,-1),
            (1,-1)
    ]
    direction3 = [
        (1,2),
        (-1,2),
        (-2,1),
        (-2,-1),
        (-1,-2),
        (1,-2),
        (2,-1),
        (2,1)
    ]
    #check diagnals
    for dir in direction1:
        rr,cc = dir
        i = 1
        r = row + rr*i
        c = col + cc*i
        while (0<=r<8 and 0<=c<8 and board[r][c]['type'] == ""):
            i += 1
            r = row + rr*i
            c = col + cc*i
        if 0<=r<8 and 0<=c<8:
            piece = board[r][c]
            if (piece['type'] == 'queen' or piece['type'] == 'rook') and piece['color'] != color:
                return True
    #check for straight lines
    for dir in direction2:
        rr,cc = dir
        i = 1
        r = row + rr*i
        c = col + cc*i
        while (0<=r<8 and 0<=c<8 and board[r][c]['type'] == ""):
            i += 1
            r = row + rr*i
            c = col + cc*i
        if 0<=r<8 and 0<=c<8:
            piece = board[r][c]
            if (piece['type'] == 'queen' or piece['type'] == 'bishop') and piece['color'] != color:
                return True
    #check for knight
    for dir in direction3:
        rr,cc = dir
        r = row + rr
        c = col + cc
        if 0<=r<8 and 0<=c<8:
            piece = board[r][c]
            if piece['type'] == 'knight' and piece['color'] != color:
                return True
    return False

