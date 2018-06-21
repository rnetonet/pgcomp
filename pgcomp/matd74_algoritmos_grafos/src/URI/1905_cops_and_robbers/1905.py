# 1905_cops_and_robbers.py

#
# helpers
#
def mprint(m):
    for row in m:
        for col in row:
            print('{:4d}'.format(col), end='')
        print()
    print()


#
# cops_robbers()
#
def cops_robbers(matrix, i, j, visited):
    if i == 4 and j == 4: 
        return True

    if (i, j) in visited:
        return False

    visited.append((i, j))
    
    # options
    if i < 4 and not matrix[i + 1][j] and cops_robbers(matrix, i + 1, j, visited): return True
    if j < 4 and not matrix[i][j + 1] and cops_robbers(matrix, i, j + 1, visited): return True
    if i > 0 and not matrix[i - 1][j] and cops_robbers(matrix, i - 1, j, visited): return True
    if j > 0 and not matrix[i][j - 1] and cops_robbers(matrix, i, j - 1, visited): return True
    
    return False


#
# main
#
ncases = int(input())

while ncases:
    matrix = []
    visited = []

    while True:
        line = input().strip()
        if line:
            matrix.append( list(map(int, line.split(' '))) )
        if len(matrix) == 5: break

    # mprint(matrix)

    if cops_robbers(matrix, 0, 0, visited):
        print("COPS")
    else:
        print("ROBBERS")
    
    ncases -= 1
