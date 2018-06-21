def lcseq(a, b):
    # coluna zero
    a = '0' + a
    b = '1' + b

    grid = [ [0 for _ in range(len(b))] for _ in range(len(a)) ]

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                grid[i][j] = grid[i - 1][j - 1] + 1
            else:
                grid[i][j] = max(
                    grid[i-1][j],
                    grid[i][j - 1]
                )

    return grid[len(a) - 1][len(b) - 1]

# 3
X = 'fish'
Y = 'fosh'
print(lcseq(X, Y))

# 4
X = "AGGTAB"
Y = "GXTXAYB"
print(lcseq(X, Y))