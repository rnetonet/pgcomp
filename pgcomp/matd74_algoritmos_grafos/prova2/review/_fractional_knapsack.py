def fractional_knapsack(values, weights, capacity):
    ratios = [values[i] / weights[i] for i in range(len(values))]

    result = 0
    while capacity:
        best_ratio = 0
        for i in range(len(ratios)):
            if ratios[i] > ratios[best_ratio]:
                best_ratio = i
        
        if weights[best_ratio] >= capacity:
            result += ratios[best_ratio] * capacity
            capacity = 0
        else:
            result += ratios[best_ratio] * weights[best_ratio]
            capacity -= weights[best_ratio]
        
        ratios[best_ratio] = 0
    
    return result

# 240
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print( fractional_knapsack(values, weights, capacity) )