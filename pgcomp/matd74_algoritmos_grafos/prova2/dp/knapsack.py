def knapsack(values, weights, capacity):
    matrix = [ [0 for _ in range(capacity + 1)] for _ in range(len(values) + 1) ]
    
    for i in range(1, len(values)):
        for j in range(capacity + 1):
            if weights[i] <= j:
                matrix[i][j] = max(matrix[i][j], values[i] + matrix[i - 1][j - weights[i]])
            else:
                matrix[i][j] = max(matrix[i][j], matrix[i - 1][j])
    
    return matrix[len(values) - 1][capacity]

# 220
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print( knapsack(values, weights, capacity) )