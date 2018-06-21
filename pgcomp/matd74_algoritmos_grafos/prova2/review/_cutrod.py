# cutrod.py
def cutrod(prices, size):
    prices = [0] + prices
    _cutrod = prices.copy()

    result = 0
    for i in range(len(prices)):
        for j in range(i):
            _cutrod[i] = max(_cutrod[i], prices[j] + _cutrod[i - j])
            result = max(result, _cutrod[i])
    
    return result

# 22
prices = [1, 5, 8, 9, 10, 17, 17, 20]
size = 8
print(cutrod(prices, 8))