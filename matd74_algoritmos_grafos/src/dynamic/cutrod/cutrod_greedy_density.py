# cutrod_greedy_density.py

sizes    = [0, 1, 2, 3, 4, 5,  6,  7,  8,  9,  10]
prices   = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

# hand calculated
optimals = [0, 1, 5, 8, 10, 13, 17, 18, 22, 25, 30]

densities = [prices[i] / i for i in range(1, 10 + 1)]
densities.insert(0, 0)

def cutrod_greedy_density(n):
    if n == 0: return 0
    
    max_profit = 0

    while n:
        biggest_density_idx = 0

        for i in range(0, n + 1):
            if densities[i] > densities[biggest_density_idx]:
                biggest_density_idx = i
        
        max_profit += prices[biggest_density_idx]
        n -= biggest_density_idx
    
    return max_profit

print( cutrod_greedy_density(4) )