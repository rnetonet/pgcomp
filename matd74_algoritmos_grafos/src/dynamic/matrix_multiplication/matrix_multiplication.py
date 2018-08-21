# matrix_multiplication.py

a = [
    [1, 2, 3],
    [4, 5, 6]
]

b = [
    [7, 8],
    [9, 10],
    [11, 12]
]

def matrix_multiply(a, b):
    ai = len(a)
    aj = len(a[0])

    bi = len(b)
    bj = len(b[0])

    if aj != bi: raise Exception()
    
    result = [ [0] * ai for i in range(bj) ]

    for i in range(ai):
        for j in range(bj):
            result[i][j] = 0
            for k in range(aj):
                result[i][j] += a[i][k] * b[k][j]

    return result

print( matrix_multiply(a, b) )