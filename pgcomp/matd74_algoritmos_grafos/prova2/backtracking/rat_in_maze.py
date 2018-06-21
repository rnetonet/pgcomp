def safe(maze, i, j):
        if i < len(maze) and j < len(maze[0]):
            if maze[i][j] > 0: return True
        
        return False

def rat_in_maze(maze, i, j):
    if i == len(maze) - 1 and j == len(maze[0]) - 1: 
        return True

    if safe(maze, i + 1, j):
        i = i + 1
        if rat_in_maze(maze, i, j): 
            maze[i][j] = 2
            return True
        else:
            maze[i][j] = 0
            i = i - 1
    
    if safe(maze, i, j + 1):
        j = j + 1
        if rat_in_maze(maze, i, j): 
            maze[i][j] = 2
            return True
        else:
            maze[i][j] = 0
            j = j - 1

    return False

maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

print( rat_in_maze(maze, 0, 0) )

for line in maze:
    print(line)