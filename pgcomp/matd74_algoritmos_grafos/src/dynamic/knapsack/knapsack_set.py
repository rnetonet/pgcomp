def knapsack(values, weights, capacity):
    values = [0] + values
    weights = [0] + weights

    grid_v = [ [0 for _ in range(capacity + 1)] for _ in range(len(values)) ]
    grid_s = [ [[] for _ in range(capacity + 1)] for _ in range(len(values)) ]

    for i in range(1, len(values)):
        for j in range(1, capacity + 1):
            if weights[i] <= j:
                grid_v[i][j] = max(
                    grid_v[i-1][j],
                    values[i] + grid_v[i-1][j - weights[i]]
                )

                if grid_v[i][j] != grid_v[i-1][j]:
                    grid_s[i][j] = [i] + grid_s[i-1][j - weights[i]].copy()
                else:
                    grid_s[i][j] = grid_s[i-1][j].copy()
            else:
                grid_v[i][j] =  grid_v[i-1][j]
                grid_s[i][j] = grid_s[i-1][j].copy()
    
    r = []
    for i in grid_s[len(values)-1][capacity]:
        r.append(weights[i])
    
    return r

# Test: geeksforgeeks.org/printing-items-01-knapsack/
# Output: 30 20
values = [ 60, 100, 120 ]
weights = [ 10, 20, 30 ]
capacity = 50

print( knapsack(values, weights, capacity) )
                    