def find_empty_location(arr):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]==0):
                return row, col
    return -1, -1
 
def safe(arr,row,col,num):
    def used_in_row(arr,row,num):
        for i in range(9):
            if(arr[row][i] == num):
                return True
        return False
    
    def used_in_col(arr,col,num):
        for i in range(9):
            if(arr[i][col] == num):
                return True
        return False
    
    def used_in_box(arr,row,col,num):
        for i in range(3):
            for j in range(3):
                if(arr[i+row][j+col] == num):
                    return True
        return False
        
    return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row - row%3,col - col%3,num)


def sudoku(arr):
    row, col = find_empty_location(arr)
    if row == -1 and col == -1: return True # no empty space!
    
    for i in range(1, 10):
        if safe(arr, row, col, i):
            arr[row][col] = i
            if sudoku(arr):
                return True
            else:
                arr[row][col] = 0
    
    return False


grid=[[3,0,6,5,0,8,4,0,0],
        [5,2,0,0,0,0,0,0,0],
        [0,8,7,0,0,0,0,3,1],
        [0,0,3,0,1,0,0,8,0],
        [9,0,0,8,6,3,0,0,5],
        [0,5,0,0,9,0,6,0,0],
        [1,3,0,0,0,0,2,5,0],
        [0,0,0,0,0,0,0,7,4],
        [0,0,5,2,0,6,3,0,0]]

if sudoku(grid):
    for line in grid:
        print(line)
else:
    print('no solution!')