# knapsack.py

def knapsack(values, weights, capacity, i):
    if capacity == 0: return 0
    if len(values) == i: return 0

    if weights[i] > capacity:
        return knapsack(values, weights, capacity, i + 1)
    else:
        return max(
            knapsack(values, weights, capacity, i + 1), 
            values[i] + knapsack(values, weights, capacity - weights[i], i + 1) 
        )

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

# Output: 220
print( knapsack(values, weights, capacity, i=0) )