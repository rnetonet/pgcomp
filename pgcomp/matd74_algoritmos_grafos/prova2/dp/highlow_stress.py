def high_low(high, low):
    weeks = [0 for _ in high] + [0]
    high = [0] + high
    low = [0] + low

    weeks[1] = max(high[1], low[1])

    for i in range(2, len(weeks)):
        m_high = high[i] + weeks[i - 2]
        m_low = low[i] + weeks[i - 1]

        weeks[i] = max(m_high, m_low)
    
    return weeks[-1]

# 20
high = [3, 6, 8, 7, 6]
low = [1, 5, 4, 5, 3]
print( high_low(high, low) )
