MAX = 20

# Criando buffer
data = []
while True:
    try:
        buffer = input().strip().split()
        for token in buffer:
            data.append(int(token))
    except: 
        break

# Define a funcao scanf
scanf_n = 0
def scanf():
    global scanf_n

    ret = data[scanf_n]
    scanf_n += 1

    return ret

t = scanf()

t -= 1
while t >= 0:
    n = scanf()
    k = scanf()

    d = [0] * MAX
    pesos = [0] * MAX
    dp = [0] * MAX

    for i in range(0, n):
        d[i] = scanf()

    aux = None

    for i in range(0, n):
        aux = scanf()
        pesos[d[i]] = max(pesos[d[i]], aux)

    max_current = pesos[0]
    
    for i in range(0, d[n-1] + 1):
        if i - k >= 0:
            max_current = max(max_current, pesos[i] + dp[i-k])
        else:
            max_current = max(max_current, pesos[i])
        
        dp[i] = max_current

    print('d = {}'.format(d))
    print('pesos = {}'.format(pesos))
    print('dp = {}'.format(dp))

    print(max_current)
    print('\n')

    t -= 1
