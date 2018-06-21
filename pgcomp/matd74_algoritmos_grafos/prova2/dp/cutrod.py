def cutrod(prices):
    _cutrod = prices.copy()

    for i in range(len(prices)):
        best = -1
        for j in range(i):
            best = max(best, prices[j] + _cutrod[i - j])
        _cutrod[i] = best
    
    return _cutrod[-1]

# 22
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
print(cutrod(prices))
