#checks if the color's king is on check or not
def check(self,board,color):
    for i in range(8):
        for j in range(8):
            if board[i][j]['type'] == 'king' and board[i][j]['color'] == color:
                row,col = i,j
                break
    #check for the pawn
    coff = 1 if color == "black" else -1
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
            if (piece['type'] == 'queen' or piece['type'] == 'rook') and piece['color'] != color or (piece['type'] == 'king' and i == 1):
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
            if (piece['type'] == 'queen' or piece['type'] == 'bishop') and piece['color'] != color or (piece['type'] == 'king' and i == 1):
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


def attackers(self,board,color):
    for i in range(8):
        for j in range(8):
            if board[i][j]['type'] == 'king' and board[i][j]['color'] == color:
                row,col = i,j
                break
    att = []
    #check for the pawn
    coff = 1 if color == "black" else -1
    if 0<=row+coff<8:
        if 0<=col+1<8:
            piece1 = board[row+coff][col+1]
            if piece1['color'] != color and piece1['type'] == 'pawn':
                att.append((row+coff,col+1))

        if 0<=col-1<8:
            piece2 = board[row+coff][col-1]
            if piece2['color'] != color and piece2['type'] == "pawn":
                att.append((row+coff,col-1))

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
    #check for straight lines
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
                att.append((r,c))
    #check for diagnals
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
                att.append((r,c))
    #check for knight
    for dir in direction3:
        rr,cc = dir
        r = row + rr
        c = col + cc
        if 0<=r<8 and 0<=c<8:
            piece = board[r][c]
            if piece['type'] == 'knight' and piece['color'] != color:
                att.append((r,c))
    
    return att