# lcseq.py
def lcseq(a, b):
    # "zero" column
    a = '-' + a
    b = '+' + b
    
    grid = [ [0 for _ in range(len(b))] for _ in range(len(a)) ]
    
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i] == b[j]:
                grid[i][j] = grid[i-1][j-1] + 1
            else:
                grid[i][j] = max(
                    grid[i-1][j],
                    grid[i][j-1]
                )
    return grid[len(a)-1][len(b)-1]

# 4
a = "AGGTAB"
b = "GXTXAYB"
print(lcseq(a, b))