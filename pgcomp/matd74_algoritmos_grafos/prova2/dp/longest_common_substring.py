def lcstr(a, b):
    # coluna 0
    a = 'x' + a
    b = 'y' + b

    alen = len(a)
    blen = len(b)

    grid = [ [0 for _ in range(blen)] for _ in range(alen) ]

    result = 0
    for i in range(1, alen):
        for j in range(1, blen):
            if a[i] == b[j]:
                grid[i][j] = grid[i - 1][j - 1] + 1
                result = max(result, grid[i][j])
    
    return result

# 3
a = 'fish'
b = 'hish'
print(lcstr(a, b))

# 10
X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'
print(lcstr(X, Y))


