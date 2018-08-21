# cutrod_topdown.py

sizes    = [1, 2, 3, 4, 5,  6,  7,  8,  9,  10]
prices   = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

# hand calculated
optimals = [1, 5, 8,  10, 13, 17, 18, 22, 25, 30]

table = dict(zip(sizes, prices))

cache = {}

def cutrod(n):
    if n == 0: return 0
    
    best = table[n]

    for i in range(1, n):
        best = max(best, cutrod(i) + cutrod(n - i))

    cache[n] = best

    return best


for i in range(1, 11):
    print('{} -> {}'.format(i, cutrod(i)))
