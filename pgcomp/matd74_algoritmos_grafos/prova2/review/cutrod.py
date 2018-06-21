# cutrod.py
def cutrod(prices, size):
    prices = [0] + prices
    _cutrod = [price for price in prices]
    
    for i in range(size + 1):
        for j in range(i):
            _cutrod[i] = max(_cutrod[i], prices[j] + _cutrod[i - j])

    return _cutrod[size]

# 22
prices = [1, 5, 8, 9, 10, 17, 17, 20]
size = 8
print(cutrod(prices, 8))