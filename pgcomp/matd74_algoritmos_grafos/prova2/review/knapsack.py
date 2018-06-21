def knapsack(values, weights, capacity):
    values = [0] + values
    weights = [0] + weights

    grid = [ [0 for _ in range(capacity + 1)] for _ in range(len(values)) ]

    for i in range(1, len(values)):
        for j in range(1, capacity + 1):
            if weights[i] > j:
                grid[i][j] = grid[i - 1][j]
            else:
                grid[i][j] = max(
                    grid[i-1][j],
                    values[i] + grid[i-1][j - weights[i]]
                )
    
    return grid[len(values) - 1][capacity]

# 220
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print(knapsack(values, weights, capacity))