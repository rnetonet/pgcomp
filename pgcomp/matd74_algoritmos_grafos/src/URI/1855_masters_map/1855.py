width = int(input())
height = int(input())

matrix = []
visited = {}

counter = height
while counter:
    matrix.append(list(input()))
    counter -= 1

i = 0
j = 0
direction = ''

while True:
    if (i, j) in visited or i >= height or j >= width:
        print('!')
        break
    
    visited[(i, j)] = 1
    
    if matrix[i][j] == '*':
        print('*')
        break
    
    if matrix[i][j] != '.':
        direction = matrix[i][j]

    if direction == '>':
        j += 1
    if direction == '<':
        j -= 1
    if direction == '^':
        i -= 1
    if direction == 'v':
        i += 1