# cutrod_bottomup.py

sizes    = [0, 1, 2, 3, 4, 5,  6,  7,  8,  9,  10]
prices   = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

# hand calculated
optimals = [0, 1, 5, 8, 10, 13, 17, 18, 22, 25, 30]

table = dict(zip(sizes, prices))

def cutrod(n):
    best = table[n]

    for i in range(n + 1):
        for j in range(i + 1):
            best = max(best, table[j] + table[i - j])

    return best

for i in range(10 + 1):
    print(i, cutrod(i))