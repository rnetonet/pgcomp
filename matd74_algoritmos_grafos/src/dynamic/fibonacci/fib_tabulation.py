cache = [0, 1]

def fib(n):
    if n <= 1: return n
    
    for i in range(2, n + 1):
        cache[-2], cache[-1] = cache[-1], cache[-1] + cache[-2]

    return cache[-1]

print( fib(30) )

