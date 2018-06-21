# lcstr.py
def lcstr(a, b):
    a = '-' + a
    b = '+' + b

    grid = [ [0 for _ in range(len(b))] for _ in range(len(a)) ]

    result = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                grid[i][j] = grid[i-1][j-1] + 1
                result = max(result, grid[i][j])
    
    return result


# 10
X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'
 
print(lcstr(X, Y))