def fractional_knapsack(values, weights, capacity):
    ratios = [values[i] / weights[i] for i in range(len(values))]
    result = 0

    while capacity:
        # find biggest ratio
        best_ratio_index = 0
        for i, ratio in enumerate(ratios):
            if ratios[i] > ratios[best_ratio_index]:
                best_ratio_index = i
        
        # if the best ratio is bigger than our capacity, take all of that
        if weights[best_ratio_index] >= capacity:
            result += ratios[best_ratio_index] * capacity
            capacity = 0
        else:
            result += weights[best_ratio_index] * ratios[best_ratio_index]
            capacity -= weights[best_ratio_index]
        

        # zero the used ratio, so its not used anymore
        ratios[best_ratio_index] = 0
    
    return result

# 240
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print( fractional_knapsack(values, weights, capacity) )