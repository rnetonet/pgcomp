def mincoins(coins, value):
    # coins in decreasing order
    coins = list(reversed(sorted(coins)))

    answer = []

    while value:
        for coin in coins:
            selected_coin = None

            if coin <= value:
                selected_coin = coin
                break
        
        value -= selected_coin
        answer.append(selected_coin)
    
    return answer

# 50  20  20  2  1
coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
value = 93
print( mincoins(coins, value) )