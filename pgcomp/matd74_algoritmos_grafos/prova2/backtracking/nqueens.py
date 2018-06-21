def safe(board, row, col):
    N = len(board[0])

    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
 
    # Check upper diagonal on left side
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False
 
    # Check lower diagonal on left side
    for i,j in zip(range(row,N,1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False
 
    return True

def nqueens(board, col):
    if col >= len(board[0]): return True
    
    for row in range(len(board)):
        if safe(board, row, col):
            board[row][col] = 1
            if nqueens(board, col + 1):
                return True
            else:
                board[row][col] = 0
    
    return False

board = [
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0]
]

print( nqueens(board, 0) )

for line in board:
    print(line)