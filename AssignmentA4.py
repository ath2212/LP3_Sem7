def check(board, row, col):
    for i in range(len(board)):
        if board[row][i]==1 or board[i][col]==1:
            return False
    
    r = row
    c = col

    while r>=0 and c <len(board):
        if board[r][c]==1:
            return False
        r -= 1
        c += 1
    
    r = row
    c = col

    while r<len(board) and c >=0:
        if board[r][c]==1:
            return False
        r += 1
        c -= 1
    
    r = row
    c = col

    while r>=0 and c >=0:
        if board[r][c]==1:
            return False
        r -= 1
        c -= 1
    
    r = row
    c = col

    while r<len(board) and c<len(board):
        if board[r][c]==1:
            return False
        r += 1
        c += 1

    return True

def solve(board, ctr, col):
    if ctr>=len(board):
        return True
    
    for i in range(len(board)):
        if check(board, i, col):
            board[i][col] = 1
            print(i, col)
            if solve(board, ctr+1, (col+1)%len(board)):
                return True
            board[i][col] = 0
    return False

n = 8
board = [[0 for i in range(n)] for j in range(n)]
row = int(input("Row: "))-1
column = int(input("Col: "))-1

board[row][column] = 1

print(solve(board, 1, (column+1)%len(board)))

for i in board:
    print(i)
