def min_coins(coins, value):
    result = []
    coins = list(reversed(sorted(coins)))

    while value > 0:
        selected_coin = None

        for coin in coins:
            if coin <= value:
                selected_coin = coin
                break
        
        value -= selected_coin
        result.append(selected_coin)
    
    return result


# 50  20  20  2  1
coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
value = 93
print( min_coins(coins, value) )